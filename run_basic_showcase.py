#!/usr/bin/env python3
"""
基础 Rich 库展示运行器
仅运行基础的 Rich 库功能展示
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

def run_showcase(skip_pause=False, fast_mode=False):
    """运行展示程序"""
    try:
        cmd = [sys.executable, "rich_showcase.py"]
        if skip_pause:
            cmd.append("--skip-pause")
        if fast_mode:
            cmd.append("--fast")
        
        subprocess.check_call(cmd)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 展示程序运行失败: {e}")
        return False
    except KeyboardInterrupt:
        print("\n👋 用户中断程序")
        return False

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="基础 Rich 库展示运行器")
    parser.add_argument("--skip-pause", action="store_true", help="跳过展示间的暂停")
    parser.add_argument("--fast", action="store_true", help="快速模式（减少动画时间）")
    parser.add_argument("--check-only", action="store_true", help="仅检查依赖，不运行展示")
    
    args = parser.parse_args()
    
    print("🚀 Rich 库基础展示启动器")
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

    # 运行展示
    print("\n🎭 启动基础展示程序...")
    time.sleep(1)
    
    if not run_showcase(args.skip_pause, args.fast):
        sys.exit(1)
    
    print("\n✨ 基础展示完成！")

if __name__ == "__main__":
    main()