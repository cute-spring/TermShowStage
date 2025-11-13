#!/usr/bin/env python3
"""
Runner script for Prompt Toolkit Showcase

This script provides an easy way to run the Prompt Toolkit showcase examples.
"""

import sys
import os
import argparse

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from prompt_toolkit_showcase import PromptToolkitShowcase
    
    def main():
        """Main function to run the showcase."""
        parser = argparse.ArgumentParser(description="Prompt Toolkit Showcase Runner")
        parser.add_argument("--self-test-all", action="store_true", help="Run non-interactive self-tests for all demos")
        args = parser.parse_args()

        print("🚀 Starting Prompt Toolkit Showcase...")
        print("=" * 50)

        showcase = PromptToolkitShowcase()
        if args.self_test_all:
            showcase.self_test_all()
        else:
            showcase.run()
        
    if __name__ == "__main__":
        main()
        
except ImportError as e:
    print(f"❌ Error: {e}")
    print("\n📋 Please make sure you have installed the required dependencies:")
    print("   pip install prompt-toolkit pygments")
    print("\n💡 Or run: pip install -r requirements.txt")
    sys.exit(1)

except Exception as e:
    print(f"❌ Unexpected error: {e}")
    sys.exit(1)