#!/usr/bin/env python3
"""
Runner script for Textual Showcase

This script provides an easy way to run the Textual showcase application.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from textual_showcase import TextualShowcaseApp

    def main():
        """Main function to run the Textual showcase."""
        print("🚀 Starting Textual Showcase...")
        print("=" * 50)

        app = TextualShowcaseApp()
        app.run()

    if __name__ == "__main__":
        main()

except ImportError as e:
    print(f"❌ Error: {e}")
    print("\n📋 请确保已安装所需依赖：")
    print("   pip install textual")
    print("\n💡 或运行: pip install -r requirements.txt")
    sys.exit(1)

except Exception as e:
    print(f"❌ Unexpected error: {e}")
    sys.exit(1)