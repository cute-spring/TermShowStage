#!/usr/bin/env python3
"""
交互式演示运行器
仅运行高级交互式演示功能
"""

import subprocess
import sys
import argparse
import time

def install_requirements():
    """安装依赖包"""
    try:
        print("📦 正在安装依赖包...")
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ 依赖安装完成!")
            return True
        else:
            print(f"❌ 依赖安装失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 安装过程中出错: {e}")
        return False

def run_interactive_demo():
    """运行交互式演示"""
    try:
        # 直接导入并运行交互式演示
        from interactive_demo import main
        main()
        return True
    except ImportError as e:
        print(f"❌ 无法导入交互式演示模块: {e}")
        return False
    except Exception as e:
        print(f"❌ 交互式演示运行失败: {e}")
        return False

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="交互式演示运行器")
    parser.add_argument("--check-only", action="store_true", help="仅检查依赖，不运行演示")
    
    args = parser.parse_args()
    
    print("🚀 Rich 库交互式演示启动器")
    print("-" * 50)
    
    # 检查是否安装 rich
    try:
        import rich
        print("✅ Rich 库已安装")
        if args.check_only:
            return
    except ImportError:
        print("📦 检测到未安装 Rich 库")
        if not install_requirements():
            print("\n💡 请手动运行: pip install -r requirements.txt")
            return
    
    if args.check_only:
        return

    # 运行交互式演示
    print("\n🎮 启动交互式演示...")
    time.sleep(1)
    
    if not run_interactive_demo():
        sys.exit(1)
    
    print("\n✨ 交互式演示完成！")

if __name__ == "__main__":
    main()