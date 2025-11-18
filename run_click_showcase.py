#!/usr/bin/env python3
"""
Click 库展示运行器
运行 Click 库的各种功能展示
"""

import subprocess
import sys
import os

def run_click_cli(arg_list):
    try:
        from click_showcase import cli
        click_args = ['click_showcase.py'] + arg_list
        sys.argv = click_args
        cli()
    except SystemExit:
        pass
    except Exception as e:
        print(f"❌ 运行命令时出错: {e}")
        return False
    return True

MENU_ITEMS = {
    '1': ['hello', '--name', 'World', '--count', '1'],
    '2': ['calculate', '10', '20', '30', '--operation', 'avg'],
    '3': ['register'],
    '4': ['server', '--host', 'localhost', '--port', '8080'],
    '5': ['db', 'create', '--name', 'test_db', '--user', 'admin'],
    '6': ['theme', '--style', 'fancy', '--color'],
    '7': ['show-date', '--format', '%Y-%m-%d %H:%M:%S'],
    '8': ['apply-discount', '--price', '199', '--discount', '20'],
    '9': ['config-demo'],
    '10': ['log-demo', '--verbose', '--verbose'],
    '11': ['tagging-demo', '--tags', 'foo', '--tags', 'bar', '--categories', 'demo'],
    '12': ['validate-range', '--min-value', '0', '--max-value', '100', '--value', '42'],
    '13': ['file-output-demo']
}

def interactive_menu():
    print("\n🎯 Click 展示菜单")
    print("  1. hello - 打招呼命令")
    print("  2. calculate - 数学计算器")
    print("  3. register - 用户注册")
    print("  4. server - 服务器配置")
    print("  5. db create - 数据库创建")
    print("  6. theme - 主题设置")
    print("  7. show-date - 日期时间演示")
    print("  8. apply-discount - 折扣计算")
    print("  9. config-demo - 配置演示")
    print("  10. log-demo - 日志级别")
    print("  11. tagging-demo - 标签系统")
    print("  12. validate-range - 范围验证")
    print("  13. file-output-demo - 文件输出")
    choice = input("\n请输入编号选择要运行的示例 (1-13): ").strip()
    if choice in MENU_ITEMS:
        print(f"\n🚀 正在运行示例 [{choice}] ...\n")
        return run_click_cli(MENU_ITEMS[choice])
    else:
        print("❌ 无效的选择")
        return False

def install_dependencies():
    """安装必要的依赖"""
    try:
        import click
        print("✅ Click 库已安装")
        return True
    except ImportError:
        print("📦 正在安装 Click 库...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "click"])
            print("✅ Click 库安装成功")
            return True
        except subprocess.CalledProcessError:
            print("❌ 安装 Click 库失败")
            return False

def show_help():
    """显示帮助信息"""
    print("""
🎯 Click 库功能展示运行器

使用方法:
  python run_click_showcase.py [选项]

选项:
  --help, -h     显示帮助信息
  --check-only   仅检查依赖，不运行展示
  --command      运行特定命令示例

示例:
  python run_click_showcase.py --command hello --name Alice --count 3
  python run_click_showcase.py --command calculate 10 20 30 --operation avg
  python run_click_showcase.py --command register
""")

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Click 库展示运行器")
    parser.add_argument('--check-only', action='store_true', help='仅检查依赖')
    parser.add_argument('--command', nargs=argparse.REMAINDER, help='运行特定命令或编号')
    
    args = parser.parse_args()
    
    if args.check_only:
        return install_dependencies()
    
    if not install_dependencies():
        print("❌ 依赖安装失败，无法运行展示")
        return False
    
    if args.command:
        first = args.command[0] if len(args.command) > 0 else ''
        if first.isdigit() and first in MENU_ITEMS and len(args.command) == 1:
            return run_click_cli(MENU_ITEMS[first])
        else:
            return run_click_cli(args.command)
    else:
        show_help()
        print("\n现在可以直接选择要运行的示例编号")
        print("💡 也可使用: python run_click_showcase.py --command 1")
        return interactive_menu()

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)