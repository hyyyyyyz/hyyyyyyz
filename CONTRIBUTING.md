# 维护 Jason 的 GitHub 主页

仓库根目录的 `README.md` 就是 GitHub 个人主页。修改正文和 SVG 后，在 GitHub 的分支预览里即可查看效果。主页使用 GitHub 原生 Markdown、HTML 链接和折叠面板。

## 文件放在哪里

| 位置 | 内容 |
| --- | --- |
| `README.md` | 自我介绍、兴趣卡带、教育经历与贡献日历 |
| `assets/studio.webp` | 为这个主页生成的像素工作室封面 |
| `assets/cartridges/` | 篮球、沙盒和电竞卡带的可编辑 SVG 源文件 |
| `assets/education/` | 教育经历卡片中的城市插画 |
| `assets/activity/` | 3D 贡献日历的亮色和暗色主题，由 Actions 更新 |
| `scripts/check_profile.py` | 检查 README 的本地资源引用、HTML 图片替代文本与 SVG 格式 |
| `.github/workflows/` | 提交检查和贡献图更新 |

## 修改兴趣卡带

在 `README.md` 对应的表格单元格中修改卡面链接、折叠标题和内容。卡面和折叠标题是两个独立的操作入口。卡面 SVG 可以直接在浏览器中打开，配色和动画都在文件里。系统启用减少动态效果后，卡面使用静态画面。

从仓库根目录运行检查，使用 Python 3 标准库即可。

```sh
python3 scripts/check_profile.py
```

提交前可在窄屏上点开三个标题，确认卡片内容可读。修改日历时也请在亮色和暗色主题中打开 3D 折叠面板。

## 贡献图怎样更新

- **Contribution snake** 每 12 小时用 [Platane/snk](https://github.com/Platane/snk) 生成一次动画，发布到 `output` 分支。原有图片地址保持可用。
- **3D contribution calendar** 每天用 [github-profile-3d-contrib](https://github.com/yoshi389111/github-profile-3d-contrib) 生成主题。工作流只暂存主页引用的两张 SVG，有变化时由 GitHub Actions 机器人提交。仓库内的版本也供本地预览。
- 两项任务都支持在 Actions 页选择默认分支后手动运行。使用仓库自带的 `GITHUB_TOKEN`。发布蛇形图需要写入 `output`，更新 3D 日历需要写入默认分支。
- **Check profile** 在推送和拉取请求时运行本地检查。工作流依赖固定到提交，Dependabot 每月检查版本。

## 设计参考与许可

游戏房首屏参考了 [MishManners 的主页](https://github.com/mishmanners/MishManners)，卡面入口参考了 [BrunnerLivio 的复古导航](https://github.com/BrunnerLivio/brunnerlivio)。封面使用 ImageGen 为 Jason 绘制，三张卡带在仓库中以 SVG 维护。仓库保留原有 [MIT 许可证](./LICENSE)和版权声明。
