# Rich Library Showcase Stage 🎭

一个全面的 Python Rich 库功能展示项目，演示了终端交互和美化功能的所有核心特性。

## ✨ 功能特性

本项目展示了 Rich 库的 14 个核心功能模块：

1. **基础文本样式** - 颜色、粗体、斜体、下划线等文本格式化
2. **动态文本效果** - 打字机动画效果
3. **数据表格** - 结构化数据展示
4. **嵌套表格** - 复杂表格结构
5. **单任务进度条** - 带详细信息的进度跟踪
6. **多任务进度条** - 并行任务进度监控
7. **文件目录树** - 文件系统结构可视化
8. **JSON 数据树** - JSON 数据结构展示
9. **分级日志** - 不同级别的日志输出
10. **实时状态更新** - 动态状态信息
11. **Markdown 渲染** - Markdown 文档预览
12. **代码语法高亮** - 编程语言语法高亮
13. **终端操作** - 终端尺寸获取和清屏
14. **Emoji 和图标** - 表情符号和图标集成

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行展示

```bash
# 运行所有展示
python run_showcase.py

# 快速模式（跳过暂停）
python run_showcase.py --skip-pause

# 仅检查依赖
python run_showcase.py --check-only
```

### 直接运行主程序

```bash
python rich_showcase.py
```

## 🎯 高级用法

### 命令行参数

主程序支持多种命令行参数：

```bash
# 列出所有展示项目
python rich_showcase.py --list

# 运行特定展示
python rich_showcase.py --show 3          # 按编号
python rich_showcase.py --show "table"     # 按名称搜索

# 跳过暂停
python rich_showcase.py --skip-pause

# 快速模式（减少动画时间）
python rich_showcase.py --fast
```

### 启动器功能

`run_showcase.py` 提供增强功能：
- 自动依赖检查安装
- 更好的错误处理
- 命令行参数支持
- 用户友好的输出

## 📁 项目结构

```
TermShowStage/
├── rich_showcase.py    # 主展示程序
├── run_showcase.py     # 增强启动器
├── requirements.txt    # 依赖配置
└── README.md          # 项目文档
```

## 🛠️ 技术栈

- **Python 3.6+** - 编程语言
- **Rich >=13.0.0** - 终端美化库
- **argparse** - 命令行参数解析
- **subprocess** - 进程管理

## 🔧 开发说明

### 添加新展示

1. 在 `rich_showcase.py` 中创建新的展示函数
2. 函数名格式：`show_*_feature()`
3. 在 `main()` 函数的 `showcases` 列表中添加
4. 在 `list_showcases()` 中添加描述信息

### 代码规范

- 使用有意义的函数名和变量名
- 添加适当的注释
- 遵循 PEP 8 代码风格
- 包含错误处理

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [Rich](https://github.com/Textualize/rich) - 优秀的终端美化库
- Python 社区 - 强大的生态系统

---

⭐ 如果这个项目对你有帮助，请给它一个 Star！