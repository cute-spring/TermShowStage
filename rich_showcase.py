#!/usr/bin/env python3
"""
Rich Library Showcase - Terminal Interaction Capabilities Demo
A comprehensive demonstration of Python's Rich library features for terminal beautification.
"""

import time
import json
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn, SpinnerColumn, TaskProgressColumn, TransferSpeedColumn, DownloadColumn
from rich.tree import Tree
from rich.logging import RichHandler
from rich.status import Status
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.layout import Layout
from rich.columns import Columns
from rich.live import Live
from rich import box, inspect
import time
import random
import argparse

# Initialize console
console = Console()

def show_basic_text_styling():
    """Show Case 1: Basic text styling with colors and formatting"""
    console.rule("[bold blue]Show Case 1: Basic Text Styling")
    
    # Create text with multiple styles
    warning_text = Text("警告", style="bold red")
    hint_text = Text("提示", style="italic blue")
    notice_text = Text("注意", style="black on yellow")
    link_text = Text("链接", style="underline")
    success_text = Text("成功信息", style="green")
    
    # Combine all text elements
    combined_text = Text()
    combined_text.append(warning_text)
    combined_text.append(" ")
    combined_text.append(hint_text)
    combined_text.append(" ")
    combined_text.append(notice_text)
    combined_text.append(" ")
    combined_text.append(link_text)
    combined_text.append(" ")
    combined_text.append(success_text)
    
    console.print(combined_text)
    console.print()

def show_dynamic_text():
    """Show Case 2: Dynamic text with typewriter effect"""
    console.rule("[bold blue]Show Case 2: Dynamic Text (Typewriter Effect)")
    
    message = "欢迎来到Rich库展示舞台！这里将展示终端交互的各种炫酷功能。"
    
    # Create gradient colors from light blue to dark blue
    colors = [f"color({i})" for i in range(20, 231, 10)]
    
    console.print("准备开始打字机效果演示...")
    time.sleep(1)
    
    # Typewriter effect with gradient
    for i, char in enumerate(message):
        color_index = min(i, len(colors) - 1)
        console.print(char, style=colors[color_index], end="")
        time.sleep(0.05)
    
    console.print("\n")

def show_data_table():
    """Show Case 3: Data statistics table with highlighting"""
    console.rule("[bold blue]Show Case 3: Data Statistics Table")
    
    # Create table
    table = Table(title="期中考试成绩", box=box.ROUNDED)
    
    # Add columns
    table.add_column("姓名", justify="center")
    table.add_column("数学", justify="right")
    table.add_column("语文", justify="right")
    table.add_column("总分", justify="right", style="bold")
    
    # Add data
    data = [
        ("张三", 90, 85, 175),
        ("李四", 88, 92, 180),
        ("王五", 95, 88, 183)
    ]
    
    # Find highest total score
    max_total = max(row[3] for row in data)
    
    for row in data:
        name, math, chinese, total = row
        style = "green" if total == max_total else None
        table.add_row(name, str(math), str(chinese), str(total), style=style)
    
    console.print(table)
    console.print()

def show_nested_tables():
    """Show Case 4: Nested tables for complex data"""
    console.rule("[bold blue]Show Case 4: Nested Tables")
    
    # Main table
    main_table = Table(title="班级信息表")
    main_table.add_column("班级", justify="center")
    main_table.add_column("人数", justify="right")
    main_table.add_column("学科成绩", justify="center")
    
    # Create nested tables for each class
    class_data = [
        ("高一(1)班", 45, [("数学", 85), ("语文", 88), ("英语", 92)]),
        ("高一(2)班", 42, [("数学", 78), ("语文", 85), ("英语", 89)])
    ]
    
    for class_name, student_count, subjects in class_data:
        # Create nested table
        nested_table = Table(box=None)
        nested_table.add_column("科目", justify="left")
        nested_table.add_column("分数", justify="right")
        
        for subject, score in subjects:
            nested_table.add_row(subject, str(score))
        
        main_table.add_row(class_name, str(student_count), nested_table)
    
    console.print(main_table)
    console.print()

def show_single_progress_bar():
    """Show Case 5: Single task progress bar with details"""
    console.rule("[bold blue]Show Case 5: Single Task Progress Bar")
    
    total_size = 100  # MB
    
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("{task.completed}MB/{task.total}MB"),
        TimeRemainingColumn(),
    ) as progress:
        
        task = progress.add_task("[cyan]下载文件中...", total=total_size)
        
        while not progress.finished:
            progress.update(task, advance=5)  # Simulate download progress
            time.sleep(0.1)
    
    console.print("[green]下载完成！")
    console.print()

def show_multi_progress_bars():
    """Show Case 6: Multi-task parallel progress bars"""
    console.rule("[bold blue]Show Case 6: Multi-Task Progress Bars")
    
    tasks = [
        ("处理文件A", 100, "red"),
        ("处理文件B", 150, "green"),
        ("处理文件C", 200, "blue")
    ]
    
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=30),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        
        progress_tasks = []
        for desc, total, color in tasks:
            task = progress.add_task(f"[{color}]{desc}", total=total)
            progress_tasks.append(task)
        
        while not progress.finished:
            for task in progress_tasks:
                progress.update(task, advance=2)  # Simulate progress
            time.sleep(0.05)
    
    console.print("[bold]所有任务完成！")
    console.print()

def show_file_tree():
    """Show Case 7: File directory tree with icons"""
    console.rule("[bold blue]Show Case 7: File Directory Tree")
    
    tree = Tree("📁 my_project/", guide_style="bold bright_blue")
    
    src_branch = tree.add("📁 src/")
    src_branch.add("🐍 main.py")
    utils_branch = src_branch.add("📁 utils/")
    utils_branch.add("🐍 __init__.py")
    utils_branch.add("🐍 helpers.py")
    
    docs_branch = tree.add("📁 docs/")
    docs_branch.add("📄 README.md")
    
    tree.add("📄 requirements.txt")
    tree.add("📄 .gitignore")
    
    console.print(tree)
    console.print("[italic]提示: 在实际终端中可以使用方向键展开/折叠节点")
    console.print()

def show_json_tree():
    """Show Case 8: JSON data tree visualization"""
    console.rule("[bold blue]Show Case 8: JSON Data Tree")
    
    user_data = {
        "name": "Alice",
        "age": 30,
        "hobbies": ["reading", "coding", "hiking"],
        "address": {
            "street": "123 Main St",
            "city": "Techville",
            "zip": "12345"
        },
        "active": True
    }
    
    def build_tree_from_dict(data, parent_tree):
        if isinstance(data, dict):
            for key, value in data.items():
                key_text = Text(f"{key}:", style="blue")
                if isinstance(value, (dict, list)):
                    branch = parent_tree.add(key_text)
                    build_tree_from_dict(value, branch)
                else:
                    value_style = "green" if isinstance(value, str) else "yellow" if isinstance(value, (int, float)) else "cyan"
                    value_text = Text(str(value), style=value_style)
                    parent_tree.add(Text.assemble(key_text, " ", value_text))
        elif isinstance(data, list):
            for i, item in enumerate(data):
                item_style = "green" if isinstance(item, str) else "yellow" if isinstance(item, (int, float)) else "cyan"
                item_text = Text(str(item), style=item_style)
                parent_tree.add(item_text)
    
    tree = Tree("📋 User Data")
    build_tree_from_dict(user_data, tree)
    
    console.print(tree)
    console.print()

def show_graded_logging():
    """Show Case 9: Graded logging with timestamps"""
    console.rule("[bold blue]Show Case 9: Graded Logging")
    
    from datetime import datetime
    
    current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    
    # Simulate different log levels
    console.print(f"{current_time} [gray]DEBUG: 初始化配置文件")
    console.print(f"{current_time} [blue]INFO: 服务启动成功")
    console.print(f"{current_time} [yellow]WARNING: 内存使用率超过 80%")
    console.print(f"{current_time} [bold red]ERROR: 连接数据库失败")
    
    console.print()

def show_real_time_status():
    """Show Case 10: Real-time status updates"""
    console.rule("[bold blue]Show Case 10: Real-Time Status Updates")
    
    total_items = 100
    spinner_chars = ["↻", "→", "↺", "←"]
    
    with Live(console=console, refresh_per_second=10) as live:
        for i in range(total_items + 1):
            if i == total_items:
                live.update("[green]同步完成！耗时 5.2s")
                break
            
            spinner = spinner_chars[i % len(spinner_chars)]
            percentage = (i / total_items) * 100
            status_text = f"{spinner} 同步中... {percentage:.1f}%（已同步 {i}/{total_items} 条）"
            live.update(status_text)
            time.sleep(0.02)
    
    console.print()

def show_markdown_rendering():
    """Show Case 11: Markdown rendering in terminal"""
    console.rule("[bold blue]Show Case 11: Markdown Rendering")
    
    markdown_content = """
## 使用说明

- **安装**: `pip install rich`
- **导入**: `from rich import print`

### 功能特性

* 彩色文本和背景
* 精美的表格
* 进度条显示
* 树状结构展示
* Markdown 支持

注意：支持大部分 Markdown 语法

官方文档：https://rich.readthedocs.io
    """
    
    console.print(Markdown(markdown_content))
    console.print()

def show_code_syntax_highlighting():
    """Show Case 12: Code syntax highlighting"""
    console.rule("[bold blue]Show Case 12: Code Syntax Highlighting")
    
    python_code = '''def calculate_total(items):
    """计算商品总价"""
    total = 0
    for item in items:
        if item['quantity'] > 0:  # 检查库存
            total += item['price'] * item['quantity']
    return total

# 示例用法
items = [
    {'name': '苹果', 'price': 5.0, 'quantity': 3},
    {'name': '香蕉', 'price': 3.0, 'quantity': 2}
]
result = calculate_total(items)
print(f"总价: ${result:.2f}")'''
    
    syntax = Syntax(python_code, "python", theme="monokai", line_numbers=True)
    console.print(syntax)
    console.print()

def show_terminal_operations():
    """Show Case 13: Terminal dimensions and clear animation"""
    console.rule("[bold blue]Show Case 13: Terminal Operations")
    
    # Get terminal size
    width, height = console.size
    console.print(f"终端尺寸: {width} × {height}")
    
    console.print("\n准备演示清屏动画...")
    time.sleep(2)
    
    # Simulate clear animation (this is a simplified version)
    console.clear()
    
    # Display centered message
    message = "Hello, Rich!"
    padding = (width - len(message)) // 2
    console.print(" " * padding + "[bold blue]" + message)
    
    console.print()

def show_emoji_icons():
    """Show Case 14: Emoji and icon integration"""
    console.rule("[bold blue]Show Case 14: Emoji & Icons")
    
    console.print("✅ 任务状态: 完成")
    console.print("☀️  天气: 晴朗")
    console.print("⚠️  警告: 即将超时")
    console.print("📊 统计: 数据加载中")
    console.print("🎯 目标: 达成")
    console.print("🔔 通知: 新消息")
    
    console.print()

def show_layout_system():
    """Show Case 15: Layout system with panels"""
    console.rule("[bold blue]Show Case 15: Layout System")
    
    # Create a layout
    layout = Layout()
    
    # Split into main sections
    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=2),
        Layout(name="footer", size=2)
    )
    
    # Split main section into columns
    layout["main"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="center", ratio=2),
        Layout(name="right", ratio=1)
    )
    
    # Add content to each section
    layout["header"].update(Panel("[bold]Rich Layout System Demo[/bold]", style="blue"))
    layout["left"].update(Panel("[green]左侧面板\n这里可以放置菜单\n或导航内容[/green]", title="菜单"))
    layout["center"].update(Panel("[yellow]中央内容区域\n这是主要的显示区域\n可以展示各种信息[/yellow]", title="内容"))
    layout["right"].update(Panel("[cyan]右侧面板\n状态信息\n或辅助内容[/cyan]", title="状态"))
    layout["footer"].update(Panel("[dim]底部状态栏\n© 2024 Rich Showcase[/dim]", style="dim"))
    
    console.print(layout)
    console.print()

def show_columns_display():
    """Show case 16: Multi-column content display"""
    console.rule("[bold blue]Show Case 16: Columns Display")
    
    # Create multiple panels for columns
    panels = [
        Panel("[bold red]项目 A[/bold red]\n状态: 进行中\n进度: 75%", title="面板 1"),
        Panel("[bold green]项目 B[/bold green]\n状态: 已完成\n进度: 100%", title="面板 2"),
        Panel("[bold blue]项目 C[/bold blue]\n状态: 待开始\n进度: 0%", title="面板 3"),
        Panel("[bold yellow]项目 D[/bold yellow]\n状态: 暂停\n进度: 50%", title="面板 4")
    ]
    
    # Display in columns
    console.print(Columns(panels, equal=True, expand=True))
    console.print()

def show_repl_integration():
    """Show case 17: REPL integration and pretty printing"""
    console.rule("[bold blue]Show Case 17: REPL Integration")
    
    # Demonstrate pretty printing in REPL
    sample_data = {
        "users": [
            {"id": 1, "name": "张三", "email": "zhangsan@example.com", "active": True},
            {"id": 2, "name": "李四", "email": "lisi@example.com", "active": False},
            {"id": 3, "name": "王五", "email": "wangwu@example.com", "active": True}
        ],
        "metadata": {
            "version": "1.2.3",
            "timestamp": "2024-01-15T10:30:00Z",
            "settings": {"theme": "dark", "language": "zh-CN"}
        }
    }
    
    console.print("[bold]Python 数据结构美化输出:[/bold]")
    console.print(sample_data)
    console.print()

def show_inspect_function():
    """Show case 18: Rich inspect function for debugging"""
    console.rule("[bold blue]Show Case 18: Inspect Function")
    
    # Create a sample class for inspection
    class SampleClass:
        """一个示例类用于演示 inspect 功能"""
        
        def __init__(self, name):
            self.name = name
            self._private_data = "secret"
            self.public_data = [1, 2, 3]
        
        def public_method(self):
            """公共方法"""
            return f"Hello {self.name}"
        
        def _private_method(self):
            """私有方法"""
            return "This is private"
    
    # Create instance
    obj = SampleClass("测试对象")
    
    console.print("[bold]Rich inspect() 函数演示:[/bold]")
    console.print("可以详细检查任何Python对象的属性和方法")
    console.print()
    
    # Use inspect
    inspect(obj, methods=True, help=True)
    console.print()

def show_advanced_progress():
    """Show case 19: Advanced progress tracking with custom columns"""
    console.rule("[bold blue]Show Case 19: Advanced Progress")
    
    # Custom progress columns
    progress_columns = [
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        TransferSpeedColumn(),
        DownloadColumn()
    ]
    
    console.print("[bold]高级进度条 - 自定义列:[/bold]")
    
    with Progress(*progress_columns, console=console) as progress:
        tasks = [
            progress.add_task("[red]下载文件...", total=1000),
            progress.add_task("[green]处理数据...", total=800),
            progress.add_task("[blue]上传结果...", total=600)
        ]
        
        while not progress.finished:
            for task_id in tasks:
                progress.update(task_id, advance=2.5)
            time.sleep(0.02)
    
    console.print()

def show_live_display():
    """Show case 20: Live display for real-time updates"""
    console.rule("[bold blue]Show Case 20: Live Display")
    
    console.print("[bold]实时数据显示演示:[/bold]")
    console.print("模拟实时数据更新（每秒更新一次）...")
    console.print()
    
    # Simulate live data updates
    from rich.live import Live
    from rich.table import Table
    
    def generate_table() -> Table:
        """生成实时数据表格"""
        table = Table()
        table.add_column("时间")
        table.add_column("CPU使用率")
        table.add_column("内存使用")
        table.add_column("网络流量")
        
        # Generate random data
        import random
        current_time = time.strftime("%H:%M:%S")
        cpu_usage = f"{random.randint(10, 90)}%"
        memory_usage = f"{random.randint(512, 2048)} MB"
        network_traffic = f"{random.randint(100, 1000)} KB/s"
        
        table.add_row(current_time, cpu_usage, memory_usage, network_traffic)
        return table
    
    # Display live updates
    with Live(generate_table(), refresh_per_second=1, console=console) as live:
        for _ in range(5):
            time.sleep(1)
            live.update(generate_table())
    
    console.print()

def show_rules_separators():
    """Show case 21: Rules and separators for visual organization"""
    console.rule("[bold blue]Show Case 21: Rules & Separators")
    
    console.print("[bold]使用规则线进行视觉分隔:[/bold]")
    console.print()
    
    # Different types of rules
    console.rule("普通规则线")
    console.print("这是普通规则线上方的内容")
    console.print("这是普通规则线下方的内容")
    console.print()
    
    console.rule("[bold green]带样式的规则线[/bold green]")
    console.print("这是带样式规则线上方的内容")
    console.print("这是带样式规则线下方的内容")
    console.print()
    
    console.rule("章节标题", style="bold red")
    console.print("重要章节内容...")
    console.print()
    
    # Horizontal separator
    console.print("─" * console.width)
    console.print("这是水平分隔线")
    console.print()

def show_prompt_input():
    """Show case 22: Interactive prompts and input handling"""
    console.rule("[bold blue]Show Case 22: Prompt & Input")
    
    console.print("[bold]交互式提示和输入演示:[/bold]")
    console.print()
    
    # Simulate different types of prompts
    from rich.prompt import Prompt, Confirm, IntPrompt
    
    console.print("1. 文本输入提示:")
    console.print("   示例: 请输入你的名字 [默认: 张三]")
    console.print("   → 张三")
    console.print()
    
    console.print("2. 确认提示:")
    console.print("   示例: 确定要继续吗? (y/n) [默认: y]")
    console.print("   → y")
    console.print()
    
    console.print("3. 数字输入提示:")
    console.print("   示例: 请输入年龄 [默认: 18]")
    console.print("   → 25")
    console.print()
    
    console.print("4. 选择提示:")
    console.print("   示例: 请选择操作:")
    console.print("       1. 创建")
    console.print("       2. 编辑") 
    console.print("       3. 删除")
    console.print("   → 1")
    console.print()

def show_traceback_handling():
    """Show case 23: Beautiful traceback formatting"""
    console.rule("[bold blue]Show Case 23: Traceback Handling")
    
    console.print("[bold]美观的异常追踪信息格式化:[/bold]")
    console.print()
    
    # Demonstrate rich traceback
    try:
        # Create a deliberate error
        def problematic_function():
            another_function()
            
        def another_function():
            raise ValueError("这是一个模拟的错误信息")
            
        problematic_function()
        
    except Exception:
        from rich.traceback import install
        install(show_locals=True)
        
        console.print("标准Python traceback:")
        console.print_exception()
        console.print()
        
        console.print("Rich美化后的traceback:")
        console.print("(包含语法高亮和更好的格式)")
    
    console.print()

def show_theme_customization():
    """Show case 24: Theme customization and styling"""
    console.rule("[bold blue]Show Case 24: Theme Customization")
    
    console.print("[bold]主题定制和样式配置:[/bold]")
    console.print()
    
    # Demonstrate different themes and styles
    from rich.theme import Theme
    
    # Custom theme
    custom_theme = Theme({
        "info": "dim cyan",
        "warning": "magenta",
        "error": "bold red",
        "success": "green",
        "highlight": "reverse"
    })
    
    themed_console = Console(theme=custom_theme)
    
    themed_console.print("这是信息样式", style="info")
    themed_console.print("这是警告样式", style="warning") 
    themed_console.print("这是错误样式", style="error")
    themed_console.print("这是成功样式", style="success")
    themed_console.print("这是高亮样式", style="highlight")
    
    console.print()
    console.print("还可以创建完整的主题配置文件:")
    console.print("• 定义颜色方案")
    console.print("• 设置默认样式") 
    console.print("• 创建一致的品牌视觉")
    console.print()

def parse_arguments():
    """Parse command line arguments"""
    import argparse
    parser = argparse.ArgumentParser(description="Rich Library Showcase")
    parser.add_argument("--skip-pause", action="store_true", help="跳过展示间的暂停")
    parser.add_argument("--fast", action="store_true", help="快速模式（减少动画时间）")
    parser.add_argument("--list", action="store_true", help="列出所有展示项目")
    parser.add_argument("--show", type=str, help="运行特定展示项目（编号或名称）")
    return parser.parse_args()

def list_showcases():
    """List all available showcases"""
    console = Console()
    console.print("[bold green]📋 可用展示项目:[/bold green]\n")
    
    showcases = [
        ("1", "Basic Text Styling", "基础文本样式和颜色"),
        ("2", "Dynamic Text", "动态文本效果（打字机效果）"),
        ("3", "Data Table", "数据表格展示"),
        ("4", "Nested Tables", "嵌套表格"),
        ("5", "Single Progress Bar", "单任务进度条"),
        ("6", "Multi Progress Bars", "多任务并行进度条"),
        ("7", "File Tree", "文件目录树"),
        ("8", "JSON Tree", "JSON数据树"),
        ("9", "Graded Logging", "分级日志"),
        ("10", "Real-time Status", "实时状态更新"),
        ("11", "Markdown Rendering", "Markdown文档渲染"),
        ("12", "Code Syntax Highlighting", "代码语法高亮"),
        ("13", "Terminal Operations", "终端操作"),
        ("14", "Emoji & Icons", "Emoji和图标"),
        ("15", "Layout System", "布局系统与面板"),
        ("16", "Columns Display", "多列内容展示"),
        ("17", "REPL Integration", "REPL集成与美化输出"),
        ("18", "Inspect Function", "对象检查调试功能"),
        ("19", "Advanced Progress", "高级进度条跟踪"),
        ("20", "Live Display", "实时数据显示"),
        ("21", "Rules & Separators", "规则线和分隔符"),
        ("22", "Prompt & Input", "交互式提示和输入"),
        ("23", "Traceback Handling", "异常追踪美化"),
        ("24", "Theme Customization", "主题定制"),
    ]
    
    for num, name, desc in showcases:
        console.print(f"  [{num}] [bold]{name}[/bold] - {desc}")

def main():
    """Main function to run all showcase demonstrations"""
    args = parse_arguments()
    
    if args.list:
        list_showcases()
        return
    
    console.print(Panel.fit("[bold blue]Rich Library 终端交互展示舞台[/bold blue]", subtitle="Python终端美化瑞士军刀"))
    console.print()
    
    # Define all showcase functions
    showcases = [
        ("1", "Basic Text Styling", show_basic_text_styling),
        ("2", "Dynamic Text", show_dynamic_text),
        ("3", "Data Table", show_data_table),
        ("4", "Nested Tables", show_nested_tables),
        ("5", "Single Progress Bar", show_single_progress_bar),
        ("6", "Multi Progress Bars", show_multi_progress_bars),
        ("7", "File Tree", show_file_tree),
        ("8", "JSON Tree", show_json_tree),
        ("9", "Graded Logging", show_graded_logging),
        ("10", "Real-time Status", show_real_time_status),
        ("11", "Markdown Rendering", show_markdown_rendering),
        ("12", "Code Syntax Highlighting", show_code_syntax_highlighting),
        ("13", "Terminal Operations", show_terminal_operations),
        ("14", "Emoji & Icons", show_emoji_icons),
        ("15", "Layout System", show_layout_system),
        ("16", "Columns Display", show_columns_display),
        ("17", "REPL Integration", show_repl_integration),
        ("18", "Inspect Function", show_inspect_function),
        ("19", "Advanced Progress", show_advanced_progress),
        ("20", "Live Display", show_live_display),
        ("21", "Rules & Separators", show_rules_separators),
        ("22", "Prompt & Input", show_prompt_input),
        ("23", "Traceback Handling", show_traceback_handling),
        ("24", "Theme Customization", show_theme_customization)
    ]
    
    # Run specific showcase if requested
    if args.show:
        found = False
        for num, name, func in showcases:
            if args.show == num or args.show.lower() in name.lower():
                console.print(f"[bold blue]───────────────────────────────────────────────────────────── Show Case {num}: {name.replace('_', ' ').title()} ─────────────────────────────────────────────────────────────[/bold blue]")
                func()
                found = True
                break
        
        if not found:
            console.print(f"[red]❌ 未找到展示项目: {args.show}[/red]")
            list_showcases()
        return
    
    # Run all showcases
    for i, (num, name, showcase_func) in enumerate(showcases, 1):
        console.print(f"[bold blue]───────────────────────────────────────────────────────────── Show Case {num}: {name.replace('_', ' ').title()} ─────────────────────────────────────────────────────────────[/bold blue]")
        showcase_func()
        if i < len(showcases) and not args.skip_pause:
            console.input("[dim]按回车键继续下一个展示...")
            if not args.fast:
                console.clear()
    
    console.print(Panel.fit("[green]🎉 所有展示完成！[/green]", subtitle="感谢观看Rich库功能演示"))

if __name__ == "__main__":
    main()