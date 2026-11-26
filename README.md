# Claude Artifact 动画演示拆解 · The Last Boring Slide

一个白底标题页，怎样变成一场可以走进图表、拖动两种未来、最后又回到白底标题页的演讲？这里收录了 @fluxxrider 的 Claude Artifact《The Last Boring Slide》的中文制作拆解，以及一个能把同样的设计方法用在新主题上的 Agent Skill。[观看原作](https://claude.ai/artifact/Cy2d8Vn63CnzCtonA1LSah)

![rea-video 从 13 个场景样帧得到的分镜索引](evidence/storyboard.jpg)

## 把资料交给 Agent

下载压缩包并解压，把其中的文件夹交给支持 Skill 的 Agent。Codex 用户可以把整个文件夹放进个人技能目录，再开一个新会话。[下载 Claude Artifact Slides Skill](./claude-artifact-slides.zip)

> 使用 $claude-artifact-slides，为普通听众做一场三分钟的交互演示，讲清“为什么前面没有事故，高速公路也会堵车”。先让车流稳定行驶，再让我让一辆车轻踩刹车，看减速波怎样向后传播。交付可离线打开的 HTML，支持逐步推进，带讲者备注。

也可以把仓库交给 Agent，让它先读中文拆解，再按自己的主题改编。想先看看成品，可以下载包后打开里面的唱片示例。[Skill 入口](claude-artifact-slides/SKILL.md) · [原创 HTML 示例](claude-artifact-slides/assets/vinyl.html)

## 制作资料

- **演讲结构与叙事**。逐场查看 13 个场景的论点、画面和入场方式。纸船与锚链解释认知锚定，靶心把一度偏差放大成可见的落点距离，结尾再用一次按键改变观众对标题页的理解。[中文拆解](claude-artifact-slides/references/case-study.md)
- **43 个演讲节拍**。CSV 每行对应一次可独立推进的状态，列出场景、入场方式、启动延迟、动画时长、自动播放停留时长和屏显页码。时间单位为秒，来自公开演示程序的配置；现场讲者可自行停顿。[逐拍数据](evidence/beats.csv)
- **画面取样与工具输出**。从本地实际渲染的每个场景取第二个节拍的一帧，按原顺序各停留一秒，得到 13 秒无声索引片。rea-video 检出 13 段。JSON 摘录了工具的切点、分数与像素分类；其中的静帧判断描述的是索引片。[分析输入 MP4](evidence/scene-samples.mp4) · [检测结果 JSON](evidence/shot-results.json)

## 怎样复查

在原作中按 O 打开场景总览，选中场景后用方向键推进，按 N 对照讲者备注。渲染引擎、转场和音效触发来自公开作品代码。声音部分核对了事件绑定，未做整场听审。复跑取样片的检测可使用 [rea-video](https://github.com/JuneYaooo/rea-video)：

```sh
rea-video decompose evidence/scene-samples.mp4 -o out/samples --no-vlm --no-asr --no-packaging --no-ocr --no-stems --no-moments --lang zh
```
