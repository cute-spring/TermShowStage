#!/usr/bin/env python3
"""
高级交互式示例展示
展示 Rich 库的高级用户交互功能
"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, Confirm, FloatPrompt
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.progress import Progress
from rich import box
import time
from typing import List, Dict, Any, Optional
import random

console = Console()

class InteractiveDemo:
    """高级交互式示例类"""
    
    def __init__(self):
        self.user_data = {}
    
    def clear_screen(self):
        """清屏"""
        console.clear()
    
    def show_welcome(self):
        """显示欢迎界面"""
        self.clear_screen()
        welcome_text = Text("🎯 高级交互式示例展示", style="bold green")
        welcome_text.append("\n\n探索 Rich 库的强大交互功能", style="blue")
        
        console.print(Panel(
            welcome_text,
            title="欢迎使用",
            border_style="green",
            padding=(2, 4)
        ))
        
        console.print("\n📋 本演示将展示:")
        console.print("  • 智能菜单选择系统")
        console.print("  • 动态表单输入界面") 
        console.print("  • 实时搜索过滤功能")
        console.print("  • 分步向导体验")
        console.print("  • 实时数据仪表盘")
        
        console.input("\n🎮 按回车键开始体验...")
    
    def smart_menu_system(self):
        """智能菜单选择系统"""
        self.clear_screen()
        
        console.print(Panel(
            "📊 智能菜单选择系统",
            title="功能演示",
            border_style="yellow"
        ))
        
        # 定义菜单选项
        menu_options = [
            {"id": 1, "name": "查看系统状态", "description": "显示当前系统信息和资源使用情况"},
            {"id": 2, "name": "用户管理", "description": "管理用户账户和权限设置"},
            {"id": 3, "name": "数据分析", "description": "运行数据分析和生成报告"},
            {"id": 4, "name": "系统设置", "description": "配置系统参数和偏好"},
            {"id": 5, "name": "帮助文档", "description": "查看使用说明和帮助信息"},
            {"id": 0, "name": "退出系统", "description": "安全退出应用程序"}
        ]
        
        while True:
            # 显示菜单表格
            table = Table(title="🔧 主菜单", box=box.ROUNDED)
            table.add_column("ID", style="cyan", justify="center")
            table.add_column("功能名称", style="green")
            table.add_column("描述", style="white")
            
            for option in menu_options:
                table.add_row(
                    str(option["id"]),
                    option["name"],
                    option["description"]
                )
            
            console.print(table)
            
            # 获取用户选择
            try:
                choice = IntPrompt.ask(
                    "\n🎯 请输入选项编号",
                    choices=[str(opt["id"]) for opt in menu_options],
                    show_choices=False
                )
                
                if choice == 0:
                    console.print("👋 感谢使用，再见！", style="bold green")
                    break
                
                # 处理选择
                selected = next((opt for opt in menu_options if opt["id"] == choice), None)
                if selected:
                    self.handle_menu_selection(selected)
                else:
                    console.print("❌ 无效的选择，请重新输入", style="bold red")
                    
            except KeyboardInterrupt:
                console.print("\n👋 用户中断操作", style="yellow")
                break
            except Exception as e:
                console.print(f"❌ 发生错误: {e}", style="bold red")
    
    def handle_menu_selection(self, option: Dict[str, Any]):
        """处理菜单选择"""
        self.clear_screen()
        
        console.print(Panel(
            f"📋 您选择了: {option['name']}",
            title="选项详情",
            border_style="blue"
        ))
        
        console.print(f"📝 描述: {option['description']}")
        
        # 模拟不同选项的处理
        if option["id"] == 1:
            self.show_system_status()
        elif option["id"] == 2:
            self.user_management()
        elif option["id"] == 3:
            self.data_analysis()
        elif option["id"] == 4:
            self.system_settings()
        elif option["id"] == 5:
            self.show_help()
        
        console.input("\n↵ 按回车键返回主菜单...")
    
    def user_management(self):
        """用户管理功能"""
        console.print("\n👥 用户管理功能:")
        console.print("• 查看用户列表")
        console.print("• 添加新用户")
        console.print("• 编辑用户权限")
        console.print("• 删除用户账户")
        console.print("\n📊 当前用户数量: 15")
        console.print("🔐 权限组: 管理员(3), 普通用户(12)")
    
    def data_analysis(self):
        """数据分析功能"""
        console.print("\n📈 数据分析功能:")
        console.print("• 生成销售报告")
        console.print("• 用户行为分析")
        console.print("• 系统性能统计")
        console.print("• 数据可视化图表")
        console.print("\n📅 最近分析: 今日销售数据")
        console.print("📊 数据总量: 1,250 条记录")
    
    def system_settings(self):
        """系统设置功能"""
        console.print("\n⚙️ 系统设置功能:")
        console.print("• 网络配置")
        console.print("• 安全设置")
        console.print("• 外观主题")
        console.print("• 通知偏好")
        console.print("• 备份与恢复")
        console.print("\n🌐 当前设置:")
        console.print("• 语言: 中文")
        console.print("• 时区: Asia/Shanghai")
        console.print("• 主题: 深色模式")
    
    def show_help(self):
        """显示帮助文档"""
        console.print("\n📚 帮助文档:")
        console.print("• 系统状态: 查看CPU、内存、磁盘等实时信息")
        console.print("• 用户管理: 管理用户账户和权限设置")
        console.print("• 数据分析: 生成各种统计报告和分析")
        console.print("• 系统设置: 配置系统参数和外观主题")
        console.print("\n🎯 使用技巧:")
        console.print("• 使用数字键快速选择菜单选项")
        console.print("• 按 Ctrl+C 可随时退出当前操作")
        console.print("• 查看详细帮助请访问官方文档")
        console.print("\n📞 技术支持: support@example.com")
    
    def show_system_status(self):
        """显示系统状态"""
        console.print("\n📊 系统状态信息:")
        
        # 模拟实时数据
        status_data = [
            {"指标": "CPU 使用率", "值": f"{random.randint(10, 80)}%", "状态": "正常"},
            {"指标": "内存使用", "值": f"{random.randint(2, 6)}GB / 8GB", "状态": "良好"},
            {"指标": "磁盘空间", "值": f"{random.randint(50, 200)}GB 空闲", "状态": "充足"},
            {"指标": "网络延迟", "值": f"{random.randint(20, 100)}ms", "状态": "稳定"},
            {"指标": "运行时间", "值": f"{random.randint(1, 72)} 小时", "状态": "正常"}
        ]
        
        table = Table(box=box.SIMPLE)
        table.add_column("指标", style="cyan")
        table.add_column("值", style="green")
        table.add_column("状态", style="yellow")
        
        for data in status_data:
            status_style = "green" if data["状态"] in ["正常", "良好", "充足"] else "red"
            table.add_row(
                data["指标"],
                data["值"],
                Text(data["状态"], style=status_style)
            )
        
        console.print(table)
    
    def dynamic_form_input(self):
        """动态表单输入示例"""
        self.clear_screen()
        
        console.print(Panel(
            "📝 动态表单输入界面",
            title="用户注册",
            border_style="magenta"
        ))
        
        form_data = {}
        
        # 用户名输入
        while True:
            username = Prompt.ask("👤 请输入用户名")
            if len(username) >= 3:
                form_data["username"] = username
                break
            console.print("❌ 用户名至少需要3个字符", style="red")
        
        # 邮箱输入验证
        while True:
            email = Prompt.ask("📧 请输入邮箱地址")
            if "@" in email and "." in email:
                form_data["email"] = email
                break
            console.print("❌ 请输入有效的邮箱地址", style="red")
        
        # 年龄输入
        age = IntPrompt.ask("🎂 请输入年龄", default=18)
        form_data["age"] = age
        
        # 偏好选择
        preferences = ["技术", "音乐", "运动", "阅读", "旅行", "美食"]
        console.print("\n🎯 请选择您的兴趣偏好 (可多选，用逗号分隔):")
        for i, pref in enumerate(preferences, 1):
            console.print(f"  {i}. {pref}")
        
        selected_prefs = []
        while True:
            choices = Prompt.ask("📋 请输入偏好编号 (如: 1,3,5)")
            try:
                selected_indices = [int(x.strip()) for x in choices.split(",") if x.strip()]
                selected_prefs = [preferences[i-1] for i in selected_indices if 1 <= i <= len(preferences)]
                if selected_prefs:
                    form_data["preferences"] = selected_prefs
                    break
                console.print("❌ 请至少选择一个有效的偏好", style="red")
            except ValueError:
                console.print("❌ 请输入有效的数字", style="red")
        
        # 确认信息
        console.print("\n✅ 表单填写完成！")
        console.print(Panel(
            f"👤 用户名: {form_data['username']}\n"
            f"📧 邮箱: {form_data['email']}\n"
            f"🎂 年龄: {form_data['age']}\n"
            f"🎯 偏好: {', '.join(form_data['preferences'])}",
            title="确认信息",
            border_style="green"
        ))
        
        if Confirm.ask("\n✅ 确认提交信息吗？"):
            console.print("🎉 表单提交成功！", style="bold green")
            self.user_data.update(form_data)
        else:
            console.print("❌ 表单已取消", style="yellow")
    
    def real_time_search(self):
        """实时搜索过滤功能"""
        self.clear_screen()
        
        console.print(Panel(
            "🔍 实时搜索过滤演示",
            title="搜索功能",
            border_style="cyan"
        ))
        
        # 模拟数据
        items = [
            "Python 编程语言", "JavaScript 前端开发", "Java 企业应用",
            "C++ 系统编程", "Go 并发编程", "Rust 系统级编程",
            "TypeScript 类型安全", "Swift iOS 开发", "Kotlin Android 开发",
            "PHP Web 开发", "Ruby 脚本语言", "SQL 数据库查询",
            "HTML 网页结构", "CSS 样式设计", "Docker 容器化",
            "Kubernetes 容器编排", "AWS 云服务", "Azure 微软云",
            "Git 版本控制", "Linux 操作系统"
        ]
        
        console.print(f"📚 总共有 {len(items)} 个技术项目可供搜索")
        console.print("💡 尝试输入关键词如: 'python', 'web', '云', '开发'")
        
        search_term = Prompt.ask("\n🔎 请输入搜索关键词")
        
        # 实时过滤
        filtered_items = [
            item for item in items 
            if search_term.lower() in item.lower()
        ]
        
        if filtered_items:
            console.print(f"\n✅ 找到 {len(filtered_items)} 个匹配结果:")
            
            table = Table(box=box.SIMPLE)
            table.add_column("序号", style="cyan", justify="right")
            table.add_column("项目名称", style="green")
            
            for i, item in enumerate(filtered_items, 1):
                # 高亮搜索关键词
                highlighted = item.replace(search_term, f"[bold yellow]{search_term}[/bold yellow]")
                table.add_row(str(i), highlighted)
            
            console.print(table)
            
            # 选择详细查看
            if len(filtered_items) > 1:
                try:
                    choice = IntPrompt.ask(
                        "\n📖 请输入序号查看详情 (0 返回)",
                        choices=[str(i) for i in range(len(filtered_items) + 1)],
                        show_choices=False
                    )
                    
                    if choice > 0:
                        selected = filtered_items[choice - 1]
                        console.print(f"\n📋 项目详情: {selected}")
                        console.print(f"📏 长度: {len(selected)} 字符")
                        console.print(f"🔤 包含关键词: {search_term}")
                        
                except (ValueError, IndexError):
                    console.print("❌ 无效的选择", style="red")
        else:
            console.print("❌ 没有找到匹配的结果", style="red")
    
    def step_by_step_wizard(self):
        """分步向导体验"""
        self.clear_screen()
        
        console.print(Panel(
            "🧙‍♂️ 分步配置向导",
            title="系统设置",
            border_style="blue"
        ))
        
        steps = [
            "欢迎和介绍",
            "基本配置", 
            "网络设置",
            "安全选项",
            "确认配置",
            "完成安装"
        ]
        
        config = {}
        
        with Progress() as progress:
            task = progress.add_task("🚀 配置进度", total=len(steps))
            
            # 步骤 1: 欢迎
            progress.update(task, advance=1, description=steps[0])
            console.print("\n🎯 欢迎使用系统配置向导!")
            console.print("📝 我们将引导您完成系统的基本配置")
            time.sleep(1)
            
            # 步骤 2: 基本配置
            progress.update(task, advance=1, description=steps[1])
            config["hostname"] = Prompt.ask("🏷️ 请输入系统主机名", default="myserver")
            config["timezone"] = Prompt.ask("⏰ 请输入时区", default="Asia/Shanghai")
            
            # 步骤 3: 网络设置
            progress.update(task, advance=1, description=steps[2])
            config["ip_address"] = Prompt.ask("🌐 请输入IP地址", default="192.168.1.100")
            config["netmask"] = Prompt.ask("🔗 请输入子网掩码", default="255.255.255.0")
            
            # 步骤 4: 安全选项
            progress.update(task, advance=1, description=steps[3])
            config["enable_firewall"] = Confirm.ask("🛡️ 是否启用防火墙")
            if config["enable_firewall"]:
                config["firewall_rules"] = Prompt.ask("📋 请输入防火墙规则", default="default")
            
            # 步骤 5: 确认
            progress.update(task, advance=1, description=steps[4])
            console.print("\n✅ 配置完成!")
            console.print(Panel(
                f"🏷️ 主机名: {config['hostname']}\n"
                f"⏰ 时区: {config['timezone']}\n"
                f"🌐 IP地址: {config['ip_address']}\n"
                f"🔗 子网掩码: {config['netmask']}\n"
                f"🛡️ 防火墙: {'启用' if config['enable_firewall'] else '禁用'}",
                title="配置摘要",
                border_style="green"
            ))
            
            if not Confirm.ask("\n✅ 确认应用这些配置吗？"):
                console.print("❌ 配置已取消", style="yellow")
                return
            
            # 步骤 6: 完成
            progress.update(task, advance=1, description=steps[5])
            console.print("\n🎉 配置应用成功!", style="bold green")
            
            # 模拟应用过程
            with Progress() as apply_progress:
                apply_task = apply_progress.add_task("⚙️ 应用配置", total=100)
                for i in range(10):
                    time.sleep(0.1)
                    apply_progress.update(apply_task, advance=10)
    
    def real_time_dashboard(self):
        """实时数据仪表盘"""
        self.clear_screen()
        
        console.print(Panel(
            "📊 实时监控仪表盘",
            title="系统监控",
            border_style="red"
        ))
        
        console.print("🔄 仪表盘正在实时更新中... (Ctrl+C 停止)")
        
        try:
            with Live(refresh_per_second=4) as live:
                for _ in range(20):  # 显示20次更新
                    # 生成实时数据
                    cpu_usage = random.randint(5, 95)
                    memory_usage = random.randint(20, 90)
                    disk_io = random.randint(10, 200)
                    network_traffic = random.randint(1, 100)
                    
                    # 创建仪表盘布局
                    layout = Layout()
                    layout.split_column(
                        Layout(name="header", size=3),
                        Layout(name="main", ratio=2),
                        Layout(name="footer", size=3)
                    )
                    
                    # 头部信息
                    header_text = Text("🖥️ 系统实时监控", style="bold blue")
                    layout["header"].update(Panel(header_text, style="blue"))
                    
                    # 主内容 - 指标表格
                    metrics_table = Table(show_header=False, box=box.SIMPLE)
                    metrics_table.add_column("指标", style="cyan", ratio=1)
                    metrics_table.add_column("值", style="green", ratio=1)
                    metrics_table.add_column("状态", style="yellow", ratio=1)
                    
                    metrics_table.add_row(
                        "CPU 使用率", 
                        f"{cpu_usage}%",
                        "⚠️ 警告" if cpu_usage > 80 else "✅ 正常"
                    )
                    metrics_table.add_row(
                        "内存使用", 
                        f"{memory_usage}%", 
                        "🔴 危险" if memory_usage > 85 else "🟡 注意" if memory_usage > 70 else "✅ 正常"
                    )
                    metrics_table.add_row(
                        "磁盘 I/O", 
                        f"{disk_io} MB/s", 
                        "⚡ 高速" if disk_io > 150 else "📊 正常"
                    )
                    metrics_table.add_row(
                        "网络流量", 
                        f"{network_traffic} Mbps", 
                        "🌊 高负载" if network_traffic > 80 else "📡 正常"
                    )
                    
                    layout["main"].update(Panel(metrics_table, title="📈 实时指标"))
                    
                    # 底部状态
                    status = "🟢 系统正常" if cpu_usage < 70 and memory_usage < 75 else "🟡 系统繁忙" if cpu_usage < 85 else "🔴 系统过载"
                    footer_text = Text(f"📊 当前状态: {status} | ⏰ 更新时间: {time.strftime('%H:%M:%S')}")
                    layout["footer"].update(Panel(footer_text))
                    
                    live.update(layout)
                    time.sleep(1)
                    
        except KeyboardInterrupt:
            console.print("\n👋 监控已停止", style="yellow")
    
    def run_all_demos(self):
        """运行所有演示"""
        self.show_welcome()
        
        demos = [
            ("智能菜单系统", self.smart_menu_system),
            ("动态表单输入", self.dynamic_form_input), 
            ("实时搜索过滤", self.real_time_search),
            ("分步配置向导", self.step_by_step_wizard),
            ("实时数据仪表盘", self.real_time_dashboard)
        ]
        
        while True:
            self.clear_screen()
            
            console.print(Panel(
                "🎮 交互式演示选择",
                title="主菜单",
                border_style="green"
            ))
            
            # 显示演示选项
            table = Table(box=box.ROUNDED)
            table.add_column("ID", style="cyan", justify="center")
            table.add_column("演示名称", style="green")
            table.add_column("描述", style="white")
            
            for i, (name, func) in enumerate(demos, 1):
                desc = {
                    "智能菜单系统": "多级菜单选择和导航系统",
                    "动态表单输入": "带验证的用户注册表单界面",
                    "实时搜索过滤": "即时搜索和高亮显示功能", 
                    "分步配置向导": "进度引导的系统设置流程",
                    "实时数据仪表盘": "动态更新的系统监控界面"
                }
                table.add_row(str(i), name, desc[name])
            
            table.add_row("0", "退出演示", "结束交互式演示")
            
            console.print(table)
            
            try:
                choice = IntPrompt.ask(
                    "\n🎯 请选择要运行的演示",
                    choices=[str(i) for i in range(len(demos) + 1)],
                    show_choices=False
                )
                
                if choice == 0:
                    console.print("👋 感谢体验交互式演示!", style="bold green")
                    break
                
                if 1 <= choice <= len(demos):
                    demos[choice - 1][1]()
                    console.input("\n↵ 按回车键继续...")
                else:
                    console.print("❌ 无效的选择", style="red")
                    
            except KeyboardInterrupt:
                console.print("\n👋 用户中断", style="yellow")
                break
            except Exception as e:
                console.print(f"❌ 发生错误: {e}", style="red")

def main():
    """主函数"""
    demo = InteractiveDemo()
    demo.run_all_demos()

if __name__ == "__main__":
    main()