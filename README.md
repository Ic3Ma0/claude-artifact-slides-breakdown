# Claude Artifact 动画演示拆解 · The Last Boring Slide

一个白底标题页，怎样变成一场可以走进图表、拖动两种未来、最后又回到白底标题页的演讲？这里收录了 @fluxxrider 的 Claude Artifact《The Last Boring Slide》的中文制作拆解，包含场景取样、检测结果和逐拍记录。

## 体验成品

从开场的白底幻灯片，到高塔折成纸船、骨牌依次倒下，再到结尾的提问。下面这段约 71 秒的无声预览按演讲顺序串起全部 13 个场景。

[![13 场动画精选，从开场标题页到最后一个问题](evidence/presentation-highlights.webp)](https://claude.ai/artifact/Cy2d8Vn63CnzCtonA1LSah)

[播放或下载预览 MP4](evidence/presentation-highlights.mp4)　·　**[打开完整交互演示 ↗](https://claude.ai/artifact/Cy2d8Vn63CnzCtonA1LSah)**　·　[下载离线 HTML](https://raw.githubusercontent.com/Ic3Ma0/claude-artifact-slides-breakdown/main/demo/the-last-boring-slide.zip)

点击上方动图可打开原作。在演示中点击画面或按 **→** 推进，按 **A** 自动播放，按 **O** 挑选场景。离线体验请解压 ZIP，用浏览器打开里面的 `index.html`。

## 给 Agent 的阅读入口

1. **理解某一场怎么做**。从逐场手册选主题。每场都写了可见对象、实现线索、时序和复现检查，并给每一拍配上起、中、末三帧。[13 份逐场手册](scenes/README.md)
2. **按结构读取全部 43 拍**。JSON 将原作节拍、配置时长、中文摘要、逐拍图和对应笔记关联起来。[场景地图](evidence/deck-map.json)
3. **理解全局实现**。看按键与回退逻辑、10 种转场、手势分派、事件声音和画质调节。[播放器技术拆解](technical-notes.md)
4. **复核实际运动与声音**。对照五段动作取样、结尾音轨、工具检测结果与复跑方法。[实验记录](experiments.md)

## 从图表走进高塔

![第二场：柱形图延伸成一座塔，红线沿塔身上升](evidence/scenes/tower.jpg)

**第二场 · The real chart**　原本挤在图表底部的数值，被放到一座塔的垂直尺度上。讲者继续推进时，视点随之升高，观众能直观看到数据之间的距离。

[逐场看完整演示画面：13 张大图与中文解读](gallery.md)

## 制作资料

- **演讲结构与叙事**。逐场查看 13 个场景的论点、画面和入场方式。纸船与锚链解释认知锚定，靶心把一度偏差放大成可见的落点距离，结尾再用一次按键改变观众对标题页的理解。[中文拆解](breakdown.md)
- **43 个演讲节拍**。CSV 每行对应一次可独立推进的状态，列出场景、入场方式、启动延迟、动画时长、自动播放停留时长和屏显页码。时间单位为秒，来自公开演示程序的配置；现场讲者可自行停顿。[逐拍数据](evidence/beats.csv)
- **画面取样与工具输出**。从本地实际渲染的每个场景取第二个节拍的一帧，按原顺序各停留一秒，得到 13 秒无声索引片。rea-video 检出 13 段。JSON 摘录了工具的切点、分数与像素分类；其中的静帧判断描述的是索引片。[分析输入 MP4](evidence/scene-samples.mp4) · [检测结果 JSON](evidence/shot-results.json) · [原始检测分镜图](evidence/storyboard.jpg)

## 怎样复查

在原作中按 O 打开场景总览，选中场景后用方向键推进，按 N 对照讲者备注。渲染引擎、转场和音效触发来自公开作品代码。声音部分核对了事件绑定，未做整场听审。复跑取样片的检测可使用 [rea-video](https://github.com/JuneYaooo/rea-video)：

```sh
rea-video decompose evidence/scene-samples.mp4 -o out/samples --no-vlm --no-asr --no-packaging --no-ocr --no-stems --no-moments --lang zh
```
