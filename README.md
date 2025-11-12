# Rich Library Showcase Stage 🎭

一个全面的 Python Rich 库功能展示项目，演示了终端交互和美化功能的所有核心特性。

## ✨ 功能特性

### 基础展示功能
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

### 高级交互式演示

本项目还包含高级交互式演示功能：

1. **智能菜单选择系统** - 动态菜单导航和选择
2. **动态表单输入** - 实时表单验证和输入处理
3. **实时搜索过滤** - 动态数据搜索和过滤
4. **分步配置向导** - 交互式配置流程
5. **实时数据仪表盘** - 动态数据可视化

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行基础展示

```bash
# 运行所有基础展示
python run_showcase.py

# 使用独立运行器（推荐）
python run_basic_showcase.py

# 快速模式（跳过暂停）
python run_showcase.py --skip-pause

# 仅检查依赖
python run_showcase.py --check-only
```

### 运行交互式演示

```bash
# 运行高级交互式演示
python run_interactive_demo.py

# 仅检查依赖
python run_interactive_demo.py --check-only
```

### 运行 Click 命令行展示

```bash
# 运行完整的 Click 展示
python run_click_showcase.py

# 运行特定命令示例
python run_click_showcase.py --command hello --name Alice --count 3
python run_click_showcase.py --command calculate 10 20 30 --operation avg
python run_click_showcase.py --command register

# 仅检查依赖
python run_click_showcase.py --check-only

# 直接运行 Click 程序
python click_showcase.py --help
```

### 直接运行主程序

```bash
python rich_showcase.py
```

## 🎮 如何玩转展示案例

### 基础 Rich 库展示玩法

1. **文本样式探索**：
   ```bash
   python rich_showcase.py --show 1
   ```
   观察不同的文本格式化效果：颜色、粗体、斜体、下划线等

2. **表格功能测试**：
   ```bash
   python rich_showcase.py --show 3
   python rich_showcase.py --show 4
   ```
   查看简单表格和嵌套表格的展示效果

3. **进度条体验**：
   ```bash
   python rich_showcase.py --show 5
   python rich_showcase.py --show 6
   ```
   观察单任务和多任务进度条的动画效果

4. **数据可视化**：
   ```bash
   python rich_showcase.py --show 7
   python rich_showcase.py --show 8
   ```
   探索文件目录树和 JSON 数据树的结构展示

5. **Markdown 和代码高亮**：
   ```bash
   python rich_showcase.py --show 11
   python rich_showcase.py --show 12
   ```
   查看 Markdown 文档渲染和代码语法高亮效果

### 交互式演示玩法

1. **菜单导航体验**：
   ```bash
   python run_interactive_demo.py
   ```
   使用数字键选择不同的功能模块，体验完整的交互流程

2. **实时数据监控**：
   - 选择 "实时数据监控" 菜单
   - 观察 CPU、内存、磁盘使用率的实时更新
   - 注意状态栏的动态变化

3. **用户管理操作**：
   - 选择 "用户管理" 菜单
   - 尝试添加、删除、搜索用户
   - 观察表格的实时更新效果

4. **表单输入测试**：
   - 选择 "数据分析" 菜单
   - 测试各种输入验证（必填字段、数字范围、邮箱格式等）
   - 观察错误提示和成功反馈

5. **搜索过滤功能**：
   - 在用户管理或数据分析中
   - 使用搜索功能过滤数据
   - 测试实时搜索的响应速度

### Click 命令行展示玩法

#### 基础命令体验

1. **打招呼命令**：
   ```bash
   python run_click_showcase.py --command hello --name World --count 5 --uppercase
   ```
   尝试不同的名称、次数和大小写选项

2. **数学计算器**：
   ```bash
   python run_click_showcase.py --command calculate 1 2 3 4 5 --operation sum
   python run_click_showcase.py --command calculate 10 20 30 --operation avg
   python run_click_showcase.py --command calculate 5 10 15 --operation min
   ```
   测试不同的数学运算

3. **文件处理**：
   ```bash
   python run_click_showcase.py --command file-processor --input-file README.md --output-file test.txt --verbose
   ```
   观察文件操作和详细模式输出

#### 交互式功能体验

4. **用户注册**：
   ```bash
   python run_click_showcase.py --command register
   ```
   按照提示输入用户名、邮箱、密码，体验交互式输入

5. **数据库操作**：
   ```bash
   python run_click_showcase.py --command db-create --name mydb --user admin
   python run_click_showcase.py --command db-delete --name mydb --backup
   ```
   体验子命令系统和确认对话框

#### 高级功能探索

6. **环境变量支持**：
   ```bash
   API_KEY=secret123 python run_click_showcase.py --command config-demo
   DEBUG=true python run_click_showcase.py --command config-demo --api-key testkey
   ```
   测试环境变量和命令行参数的优先级

7. **多值选项**：
   ```bash
   python run_click_showcase.py --command tagging-demo --tags python --tags cli --tags demo --categories dev --categories test
   ```
   体验多个标签和分类的处理

8. **参数验证**：
   ```bash
   python run_click_showcase.py --command validate-range --min-value 0 --max-value 100 --value 50
   python run_click_showcase.py --command validate-range --min-value 0 --max-value 100 --value 150
   ```
   测试验证通过和验证失败的情况

9. **自定义类型**：
   ```bash
   python run_click_showcase.py --command apply-discount --price 200 --discount 25
   python run_click_showcase.py --command apply-discount --price 100 --discount 150
   ```
   测试自定义百分比类型的验证

10. **文件输出**：
    ```bash
    python run_click_showcase.py --command file-output-demo --output test.txt
    python run_click_showcase.py --command file-output-demo --output test.txt --append
    ```
    体验文件写入和追加模式

### 趣味挑战任务

1. **创建完整的用户流程**：
   - 使用注册命令创建用户
   - 使用数据库命令创建相关数据库
   - 使用文件处理器处理用户数据

2. **配置服务器环境**：
   - 设置服务器配置
   - 配置日志级别
   - 设置主题样式

3. **批量处理任务**：
   - 使用多值选项处理多个文件
   - 批量应用折扣计算
   - 处理多个数据验证任务

### 调试和学习技巧

1. **使用帮助系统**：
   ```bash
   python click_showcase.py --help
   python click_showcase.py hello --help
   python click_showcase.py calculate --help
   ```

2. **查看错误信息**：
   - 故意输入错误参数观察错误提示
   - 测试边界情况和异常处理

3. **学习代码结构**：
   - 查看 `click_showcase.py` 中的装饰器用法
   - 学习参数验证和类型处理
   - 研究交互式输入的实现

4. **性能测试**：
   - 测试大量数据时的性能表现
   - 观察实时更新的流畅度
   - 检查内存使用情况

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
├── rich_showcase.py        # 主展示程序（基础功能）
├── run_showcase.py         # 基础展示启动器
├── run_basic_showcase.py   # 独立基础展示运行器
├── interactive_demo.py     # 高级交互式演示程序
├── run_interactive_demo.py # 交互式演示启动器
├── click_showcase.py       # Click 库功能展示程序
├── run_click_showcase.py   # Click 展示启动器
├── requirements.txt        # 依赖配置
└── README.md              # 项目文档
```

### 文件功能说明

- **rich_showcase.py** - 核心展示程序，包含 Rich 库 14 个基础功能模块的演示
- **run_showcase.py** - 基础展示启动器，提供依赖检查和命令行参数支持
- **run_basic_showcase.py** - 独立的基础展示运行器，专注于基础功能演示
- **interactive_demo.py** - 高级交互式演示程序，包含 5 个交互式功能模块
- **run_interactive_demo.py** - 交互式演示启动器，独立运行高级交互功能
- **click_showcase.py** - Click 库功能展示程序，演示命令行接口开发
- **run_click_showcase.py** - Click 展示启动器，提供依赖检查和运行支持
- **requirements.txt** - 项目依赖配置，包含 rich 和 click 库
- **README.md** - 项目文档和使用说明

## 🎯 Click 库功能展示

### 关于 Click 库

Python 的 Click 库是一个优雅的命令行接口（CLI）开发工具，基于装饰器语法，让开发者能快速构建功能完善、交互友好的命令行程序。它自动处理参数解析、帮助信息生成、错误提示等底层工作，支持子命令、参数验证、交互式输入等高级功能。

### 运行 Click 展示

```bash
# 运行完整的 Click 展示
python run_click_showcase.py

# 运行特定命令示例
python run_click_showcase.py --command hello --name Alice --count 3
python run_click_showcase.py --command calculate 10 20 30 --operation avg
python run_click_showcase.py --command register

# 仅检查依赖
python run_click_showcase.py --check-only

# 直接运行 Click 程序
python click_showcase.py --help
```

### Click 功能特性

1. **基础命令** - 简单的打招呼命令，演示选项和参数
2. **数学计算器** - 支持多种计算操作和参数验证
3. **文件处理器** - 文件操作和路径验证
4. **用户注册** - 交互式输入和确认提示
5. **服务器配置** - 复杂选项和默认值设置
6. **数据库操作** - 子命令组和互斥选项
7. **主题设置** - 选择器和互斥选项演示
8. **日期时间** - 高级类型处理和格式化

### 核心功能演示

- **装饰器语法** - 使用 `@click.command()` 和 `@click.option()` 快速构建 CLI
- **参数验证** - 类型检查、路径存在性验证、选择器限制
- **交互式输入** - 密码隐藏输入、确认提示、交互式选项
- **子命令系统** - 命令分组和嵌套命令结构
- **帮助系统** - 自动生成的帮助信息和文档
- **错误处理** - 友好的错误提示和异常处理

## 🔍 案例审查指南

### 基础展示案例审查

基础展示案例位于 `rich_showcase.py` 文件中，包含 14 个核心功能模块：

1. **审查方法**：
   ```bash
   # 运行完整的基础展示
   python run_showcase.py
   
   # 或者直接运行主程序
   python rich_showcase.py
   ```

2. **重点审查内容**：
   - 文本样式格式化（颜色、粗体、斜体等）
   - 表格结构的正确性和美观性
   - 进度条的动画效果和实时更新
   - 文件目录树和 JSON 数据树的层次结构展示
   - Markdown 渲染和代码语法高亮效果
   - 终端操作功能的完整性

3. **命令行参数测试**：
   ```bash
   # 测试特定功能
   python rich_showcase.py --show 3          # 审查表格功能
   python rich_showcase.py --show "progress"  # 审查进度条功能
   
   # 快速模式审查
   python rich_showcase.py --fast
   ```

### 交互式演示案例审查

交互式演示案例位于 `interactive_demo.py` 文件中，包含 5 个高级功能模块：

1. **审查方法**：
   ```bash
   # 运行完整的交互式演示
   python run_interactive_demo.py
   ```

2. **重点审查内容**：
   - **智能菜单系统**：测试菜单导航、选项选择和返回功能
   - **动态表单输入**：验证表单字段的实时验证和错误提示
   - **实时搜索过滤**：测试搜索功能的响应速度和过滤准确性
   - **分步配置向导**：审查向导流程的完整性和用户引导
   - **实时数据仪表盘**：测试数据更新的实时性和可视化效果

3. **交互测试要点**：
   - 所有用户输入都应该得到即时反馈
   - 错误输入应该有清晰的错误提示
   - 菜单导航应该流畅且逻辑清晰
   - 表单验证应该准确且用户友好
   - 搜索功能应该快速且结果准确

### 代码审查要点

1. **架构设计**：
   - 基础展示和交互演示完全分离，架构清晰
   - 每个功能模块独立封装，便于维护
   - 错误处理机制完善

2. **代码质量**：
   - 遵循 PEP 8 代码规范
   - 函数和变量命名清晰有意义
   - 注释充分，便于理解
   - 异常处理完善

3. **用户体验**：
   - 输出信息美观且易读
   - 交互流程自然流畅
   - 错误提示友好明确
   - 性能响应快速

### 测试建议

1. **功能测试**：逐个运行所有展示模块，确保功能正常
2. **边界测试**：测试极端输入情况（空输入、超长输入等）
3. **性能测试**：确保响应速度满足交互需求
4. **兼容性测试**：在不同终端环境中测试显示效果
5. **用户体验测试**：从用户角度评估交互流程的顺畅性

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