"""Render beat contact sheets from a local copy of The Last Boring Slide."""
import argparse
import json
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="Original standalone presentation HTML")
    parser.add_argument("output", type=Path, help="New or empty destination directory")
    parser.add_argument("--chrome", help="Optional Chromium or Google Chrome executable")
    args = parser.parse_args()
    if args.output.exists() and any(args.output.iterdir()):
        parser.error("Choose an empty output directory")
    source = args.html.resolve(strict=True).as_uri() + "?headless"
    args.output.mkdir(parents=True, exist_ok=True)
    manifest = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            executable_path=args.chrome,
            args=["--enable-unsafe-swiftshader", "--use-angle=swiftshader"],
        )
        index = browser.new_page()
        index.goto(source)
        index.wait_for_function("window.ready === true")
        scenes = index.evaluate("""() => window.__deck.scenes.map(s => ({
            id:s.id, beats:s.beats.map(b => ({delay:b.delay || 0, duration:b.dur}))
        }))""")
        index.close()
        for scene in scenes:
            page = browser.new_page(viewport={"width": 640, "height": 360})
            page.goto(source)
            page.wait_for_function("window.ready === true")
            for beat, spec in enumerate(scene["beats"], 1):
                sheet = Image.new("RGB", (1440, 300), "#202328")
                labels = ImageDraw.Draw(sheet)
                times = [spec["delay"] + f * spec["duration"] for f in (0, 0.5, 1)]
                for col, seconds in enumerate(times):
                    page.evaluate("""async ([scene, beat, t]) => {
                        await window.__deck.test.seek(scene, beat - 1, t);
                        await new Promise(resolve => requestAnimationFrame(resolve));
                    }""", [scene["id"], beat, seconds])
                    frame = Image.open(BytesIO(page.screenshot(type="jpeg", quality=93)))
                    sheet.paste(frame.resize((480, 270), Image.Resampling.LANCZOS), (col * 480, 0))
                    labels.text((col * 480 + 8, 278), f'{scene["id"]} / beat {beat}   {seconds:.2f} s', fill="white")
                name = f'{scene["id"]}-{beat}.jpg'
                sheet.save(args.output / name, quality=91)
                manifest.append(dict(scene=scene["id"], beat=beat, seconds=times, image=name))
            page.close()
        browser.close()
    (args.output / "samples.json").write_text(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
