# 动画、声音与定位渲染实验

## 为 43 拍取 129 个状态

每场新开一个本地浏览器页面，在 640×360 舞台上调用原作发布包自带的定位接口。不依赖鼠标手速。若该拍延迟为 d、动画时长为 T，就在 d、d + T/2、d + T 秒渲染。每格保留画面和时间标签。三帧可用来辨认构图、移动方向和文字状态；需要判断是否弹跳、何时切换或运动是否均匀时，再看连续样片。每次单独进场，涉及历史快照的高墙可能使用作者内置缩略图。[逐场图解](scenes/README.md)

可用 Python、Pillow、Playwright 和本地 Chromium 重跑。下方两个路径分别替换为本地原作的独立 HTML 和一个空输出目录；仓库不包含原作发布包。脚本从本地作品运行时读取节拍配置，并输出 JPG 与名为 samples.json 的时间索引。已有 Chrome 时可用 --chrome 指定浏览器可执行文件。[取样脚本](analysis/sample_beats.py)

```sh
python analysis/sample_beats.py "/path/to/The Last Boring Slide/index.html" ./beat-samples
```

## 五段动态样片说明了什么

|动作|样片覆盖范围|画面与工具输出如何对应|
|---|---|---|
|[议程出现](evidence/office-agenda.mp4)|第 1 场第 2 拍，12 fps，51 帧|同一白底上相继出现文字与图表，工具检出 1 段，最高分类是代码渲染。|
|[塔面折成纸船](evidence/tower-to-boat.mp4)|场间折纸，12 fps，42 帧，包含终点|约 0.583 秒时画面变化足以触发检测切点；原程序仍在推进同一个折纸合成器。|
|[比例图形展开](evidence/loop-motion.mp4)|第 4 场第 2 拍，10 fps，41 帧|这个样本覆盖比例变化，工具检出 1 段，最高分类为三维渲染。该场实际组织了着色平面、嵌套范围和字形图集。要研究末拍的持续递归，另看该拍三帧取样。|
|[骨牌穿过多个尺度](evidence/dominoes-motion.mp4)|第 6 场第 2 拍，6 fps，85 帧|覆盖完整 14 秒动画及末帧；工具检出 1 段，最高分类为 AI 视频。公开包中可以定位到实例化骨牌、实例序号和逐牌事件。复刻时优先保留相邻尺寸比和尺度参照物。|
|[最后一个问题](evidence/questions-motion.mp4)|第 13 场第 3 拍的前 5 秒，10 fps，51 帧|留白占比高，工具给出 mostly_static 和代码渲染；逐帧仍可见删字、换句和光标。整页倾斜发生在后段，请看该拍终点图。|

各样片都是原作定位接口计算的定步长近似，便于比较同一动作。6 fps 的骨牌样片适合读动作顺序，运动流畅度应回原作检验。视频都没有音轨。容器时长包含末帧的显示时间。机器可读记录中有文件哈希、实际帧数、每个检测区间与全部类别得分。[五段检测结果](evidence/motion-analysis.json)

复跑某段时将路径换成上表对应的 MP4；这里沿用初次分析的低依赖设置，未启用 VLM。

```sh
rea-video decompose evidence/dominoes-motion.mp4 -o out/dominoes --no-vlm --no-asr --no-packaging --no-ocr --no-stems --no-moments --lang zh
```

## 结尾声音实际输出

另开普通播放页面，从结尾场进入第 2 拍，解锁 AudioContext 后开始录制，再用键盘右方向键推进到第 3 拍。录制点是连接到网页音频输出端的信号，设备麦克风与其他程序的声音均不参与。得到约 7.2 秒双声道片段。它是独立的一次播放，起始操作、帧率和计时与上表无声视频各自独立。[播放或下载音频](evidence/questions-audio.mp3)

将发布的 MP3 解码为 48 kHz 双声道，再按每 0.2 秒计算 RMS 与峰值。整段平均电平约 −31.1 dBFS，峰值约 −16.1 dBFS；这些数值只适用于此文件。能量变化能验证有声输出与响度起伏，无法单独识别某次峰值对应哪个事件。打字、选择与整页倾斜的触发条件可在结尾场的代码笔记中对照。[电平数据](evidence/questions-audio-levels.csv) · [结尾场逐拍笔记](scenes/questions.md)
