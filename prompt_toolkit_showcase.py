"""
Prompt Toolkit Library Showcase

This module demonstrates various features of the Prompt Toolkit library for
building interactive command-line applications with advanced input handling,
auto-completion, syntax highlighting, and more.
"""

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import (
    WordCompleter, 
    PathCompleter, 
    NestedCompleter,
    FuzzyCompleter,
    Completer,
    Completion
)
from prompt_toolkit.history import FileHistory, InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML, ANSI
from prompt_toolkit.layout import Layout
from prompt_toolkit.widgets import (
    TextArea, 
    Button, 
    Frame, 
    RadioList, 
    CheckboxList,
    Box,
    HorizontalLine
)
from prompt_toolkit.shortcuts import (
    input_dialog, 
    message_dialog, 
    yes_no_dialog,
    button_dialog,
    ProgressBar,
    clear,
    print_formatted_text
)
from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.document import Document
from prompt_toolkit.filters import has_focus
from prompt_toolkit.layout.containers import (
    HSplit, 
    VSplit, 
    Window, 
    FloatContainer, 
    Float
)
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.validation import Validator, ValidationError
from pygments.lexers import PythonLexer, JsonLexer, XmlLexer
from pygments import highlight
from pygments.formatters import TerminalFormatter

import os
import time
import random
from typing import List, Dict, Any, Callable
from datetime import datetime
from pathlib import Path


class PromptToolkitShowcase:
    """Main class demonstrating Prompt Toolkit features."""
    
    def __init__(self):
        self.history = FileHistory(".prompt_toolkit_history")
        self.session = PromptSession(history=self.history)
        self.setup_key_bindings()
        self.setup_styles()
        
    def setup_key_bindings(self):
        """Setup custom key bindings."""
        self.kb = KeyBindings()
        
        @self.kb.add('c-c')
        def _(event):
            """Exit on Ctrl+C."""
            event.app.exit()
            
        @self.kb.add('c-d')
        def _(event):
            """Exit on Ctrl+D."""
            event.app.exit()
    
    def setup_styles(self):
        """Setup custom styles for the application."""
        self.style = Style.from_dict({
            'completion-menu.completion': 'bg:#008888 #ffffff',
            'completion-menu.completion.current': 'bg:#00aaaa #000000',
            'scrollbar.background': 'bg:#88aaaa',
            'scrollbar.button': 'bg:#222222',
            'prompt': 'ansigreen bold',
            'input': 'ansicyan',
            'output': 'ansiyellow',
            'error': 'ansired bold',
            'success': 'ansigreen bold',
            'warning': 'ansiyellow bold',
            'info': 'ansiblue',
            'title': 'ansiwhite bold',
            'highlight': 'bg:#444444 #ffffff',
        })
    
    def demo_basic_prompt(self):
        """Demo basic prompt functionality."""
        print_formatted_text(HTML('<title>🔹 Basic Prompt Demo</title>'))
        print_formatted_text(HTML('<info>This demonstrates basic prompt input with history and styling</info>'))
        
        try:
            result = self.session.prompt(
                HTML('<prompt>❯ </prompt>'),
                style=self.style,
                key_bindings=self.kb
            )
            print_formatted_text(HTML(f'<output>You entered: {result}</output>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
        except EOFError:
            print_formatted_text(HTML('<error>\nEnd of input</error>'))
    
    def demo_auto_completion(self):
        print_formatted_text(HTML('<title>🔹 Auto-Completion Demo</title>'))
        print_formatted_text(HTML('<info>1) Command completion  2) Path completion  3) Nested completion</info>'))
        
        command_completer = WordCompleter([
            'git', 'docker', 'python', 'node', 'npm',
            'list', 'show', 'create', 'delete', 'update',
            'start', 'stop', 'restart', 'status', 'help'
        ], ignore_case=True)
        
        path_completer = PathCompleter()
        
        nested_completer = NestedCompleter.from_nested_dict({
            'git': {
                'status': None,
                'add': None,
                'commit': None,
                'push': None,
                'pull': None,
            },
            'docker': {
                'build': None,
                'run': None,
                'ps': None,
                'images': None,
                'logs': None,
            }
        })
        
        try:
            cmd = self.session.prompt(
                HTML('<prompt>❯ Command: </prompt>'),
                completer=command_completer,
                complete_while_typing=True,
                style=self.style
            )
            print_formatted_text(HTML(f'<output>Command: {cmd}</output>'))
            
            p = self.session.prompt(
                HTML('<prompt>❯ Path: </prompt>'),
                completer=path_completer,
                complete_while_typing=True,
                style=self.style
            )
            print_formatted_text(HTML(f'<output>Path: {p}</output>'))
            
            nested = self.session.prompt(
                HTML('<prompt>❯ Nested: </prompt>'),
                completer=nested_completer,
                complete_while_typing=True,
                style=self.style
            )
            print_formatted_text(HTML(f'<output>Nested: {nested}</output>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
    
    def demo_syntax_highlighting(self):
        """Demo syntax highlighting with Pygments."""
        print_formatted_text(HTML('<title>🔹 Syntax Highlighting Demo</title>'))
        print_formatted_text(HTML('<info>Try Python code with syntax highlighting</info>'))
        
        try:
            result = self.session.prompt(
                HTML('<prompt>🐍 </prompt>'),
                lexer=PygmentsLexer(PythonLexer),
                style=self.style,
                multiline=True,
                prompt_continuation=lambda width, line_number, is_soft_wrap: '... '
            )
            print_formatted_text(HTML(f'<output>Code entered:\n{result}</output>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
    
    def demo_input_validation(self):
        """Demo input validation."""
        print_formatted_text(HTML('<title>🔹 Input Validation Demo</title>'))
        print_formatted_text(HTML('<info>Try entering invalid email addresses</info>'))
        
        class EmailValidator(Validator):
            def validate(self, document):
                text = document.text
                if '@' not in text or '.' not in text.split('@')[-1]:
                    raise ValidationError(
                        message='Please enter a valid email address',
                        cursor_position=len(text)
                    )
        
        class NumberValidator(Validator):
            def validate(self, document):
                text = document.text
                if text and not text.isdigit():
                    raise ValidationError(
                        message='Please enter a number',
                        cursor_position=len(text)
                    )
        
        try:
            # Email validation
            email = self.session.prompt(
                HTML('<prompt>📧 Email: </prompt>'),
                validator=EmailValidator(),
                style=self.style
            )
            
            # Number validation
            number = self.session.prompt(
                HTML('<prompt>🔢 Age: </prompt>'),
                validator=NumberValidator(),
                style=self.style
            )
            
            print_formatted_text(HTML(f'<success>✅ Valid email: {email}</success>'))
            print_formatted_text(HTML(f'<success>✅ Valid age: {number}</success>'))
            
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
    
    def demo_dialogs(self):
        """Demo various dialog boxes."""
        print_formatted_text(HTML('<title>🔹 Dialog Boxes Demo</title>'))
        
        # Message dialog
        message_dialog(
            title="Information",
            text="This is an information message dialog!"
        ).run()
        
        # Yes/No dialog
        result = yes_no_dialog(
            title="Confirmation",
            text="Do you want to continue?"
        ).run()
        
        print_formatted_text(HTML(f'<info>Confirmation result: {result}</info>'))
        
        # Button dialog
        button_result = button_dialog(
            title="Options",
            text="Choose an option:",
            buttons=[
                ("Option 1", "opt1"),
                ("Option 2", "opt2"),
                ("Option 3", "opt3"),
            ]
        ).run()
        
        print_formatted_text(HTML(f'<info>Button result: {button_result}</info>'))
        
        # Input dialog
        input_result = input_dialog(
            title="User Input",
            text="Please enter your name:"
        ).run()
        
        print_formatted_text(HTML(f'<success>Hello, {input_result}!</success>'))
    
    def demo_progress_bar(self):
        """Demo progress bar functionality."""
        print_formatted_text(HTML('<title>🔹 Progress Bar Demo</title>'))
        
        with ProgressBar() as pb:
            for i in pb(range(100), label="Processing..."):
                time.sleep(0.02)  # Simulate work
        
        print_formatted_text(HTML('<success>✅ Progress completed!</success>'))
    
    def demo_custom_layout(self):
        """Demo custom layout with widgets."""
        print_formatted_text(HTML('<title>🔹 Custom Layout Demo</title>'))
        
        # Create widgets
        text_area = TextArea(
            text="Type some text here...\nYou can use multiple lines!",
            multiline=True,
            height=10
        )
        
        def on_button_click():
            text_area.buffer.text = text_area.buffer.text + "\n[Button clicked]"
        button = Button("Click Me!", handler=on_button_click)
        
        radio_list = RadioList(
            values=[
                ("option1", "Option 1"),
                ("option2", "Option 2"),
                ("option3", "Option 3"),
            ]
        )
        
        checkbox_list = CheckboxList(
            values=[
                ("check1", "Checkbox 1"),
                ("check2", "Checkbox 2"),
                ("check3", "Checkbox 3"),
            ]
        )
        
        # Create layout
        layout = Layout(
            HSplit([
                Frame(
                    title="Text Editor",
                    body=text_area,
                    height=12
                ),
                HorizontalLine(),
                Frame(
                    title="Options",
                    body=HSplit([
                        radio_list,
                        checkbox_list,
                        button
                    ])
                )
            ])
        )
        
        # Create application
        app = Application(
            layout=layout,
            key_bindings=self.kb,
            style=self.style,
            full_screen=True
        )
        
        print_formatted_text(HTML('<info>Press any key to continue...</info>'))
        app.run()
    
    def demo_history_search(self):
        """Demo history search functionality."""
        print_formatted_text(HTML('<title>🔹 History Search Demo</title>'))
        print_formatted_text(HTML('<info>Use up/down arrows to navigate history</info>'))
        self.history.append_string("git status")
        self.history.append_string("docker run -it alpine")
        self.history.append_string("python app.py")
        
        # Create session with history
        session_with_history = PromptSession(history=self.history)
        
        try:
            result = session_with_history.prompt(
                HTML('<prompt>🔍 </prompt>'),
                style=self.style,
                enable_history_search=True,
                complete_while_typing=True
            )
            print_formatted_text(HTML(f'<output>Search result: {result}</output>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
    
    def demo_fuzzy_matching(self):
        """Demo fuzzy matching completion."""
        print_formatted_text(HTML('<title>🔹 Fuzzy Matching Demo</title>'))
        print_formatted_text(HTML('<info>Try typing partial matches like: py, git, doc</info>'))
        
        words = [
            'python', 'javascript', 'typescript', 'java', 'c++',
            'git', 'github', 'docker', 'kubernetes', 'aws',
            'database', 'mysql', 'postgresql', 'mongodb', 'redis',
            'framework', 'django', 'flask', 'react', 'vue', 'angular'
        ]
        
        fuzzy_completer = FuzzyCompleter(WordCompleter(words))
        
        try:
            result = self.session.prompt(
                HTML('<prompt>🔎 </prompt>'),
                completer=fuzzy_completer,
                complete_while_typing=True,
                style=self.style
            )
            print_formatted_text(HTML(f'<output>Fuzzy matched: {result}</output>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
    
    def demo_multi_line_input(self):
        """Demo multi-line input."""
        print_formatted_text(HTML('<title>🔹 Multi-line Input Demo</title>'))
        print_formatted_text(HTML('<info>Press Enter for new line, Ctrl+D to finish</info>'))
        
        try:
            result = self.session.prompt(
                HTML('<prompt>📝 </prompt>'),
                multiline=True,
                style=self.style,
                prompt_continuation=lambda width, line_number, is_soft_wrap: '... ',
                key_bindings=self.kb
            )
            print_formatted_text(HTML(f'<output>Multi-line input:\n{result}</output>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
    
    def demo_auto_suggest(self):
        """Demo auto-suggest from history."""
        print_formatted_text(HTML('<title>🔹 Auto-Suggest Demo</title>'))
        print_formatted_text(HTML('<info>Type something, then use right arrow to accept suggestions</info>'))
        
        # Add some history first
        self.history.append_string("git status")
        self.history.append_string("docker ps")
        self.history.append_string("python main.py")
        
        try:
            result = self.session.prompt(
                HTML('<prompt>💡 </prompt>'),
                auto_suggest=AutoSuggestFromHistory(),
                style=self.style
            )
            print_formatted_text(HTML(f'<output>Auto-suggested: {result}</output>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
    
    def demo_password_input(self):
        """Demo password input with masking."""
        print_formatted_text(HTML('<title>🔹 Password Input Demo</title>'))
        
        try:
            password = self.session.prompt(
                HTML('<prompt>🔒 Password: </prompt>'),
                is_password=True,
                style=self.style
            )
            print_formatted_text(HTML('<success>✅ Password accepted!</success>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
    
    def demo_custom_completer(self):
        """Demo custom completer with context-aware completion."""
        print_formatted_text(HTML('<title>🔹 Custom Completer Demo</title>'))
        
        class ContextAwareCompleter(Completer):
            def get_completions(self, document, complete_event):
                text = document.text_before_cursor
                
                # Context-aware completion
                if text.startswith('git '):
                    git_commands = ['status', 'add', 'commit', 'push', 'pull', 'log', 'branch']
                    for cmd in git_commands:
                        if cmd.startswith(document.get_word_before_cursor()):
                            yield Completion(cmd, start_position=-len(document.get_word_before_cursor()))
                
                elif text.startswith('docker '):
                    docker_commands = ['ps', 'images', 'build', 'run', 'stop', 'logs', 'exec']
                    for cmd in docker_commands:
                        if cmd.startswith(document.get_word_before_cursor()):
                            yield Completion(cmd, start_position=-len(document.get_word_before_cursor()))
                
                else:
                    # Default completion
                    commands = ['git', 'docker', 'python', 'exit', 'help', 'clear']
                    for cmd in commands:
                        if cmd.startswith(document.get_word_before_cursor()):
                            yield Completion(cmd, start_position=-len(document.get_word_before_cursor()))
        
        try:
            result = self.session.prompt(
                HTML('<prompt>🚀 </prompt>'),
                completer=ContextAwareCompleter(),
                complete_while_typing=True,
                style=self.style
            )
            print_formatted_text(HTML(f'<output>Context-aware: {result}</output>'))
        except KeyboardInterrupt:
            print_formatted_text(HTML('<error>\nOperation cancelled</error>'))
    
    def show_menu(self):
        """Show main menu and handle user selection."""
        while True:
            clear()
            print_formatted_text(HTML('<title>🎯 Prompt Toolkit Showcase</title>'))
            print_formatted_text(HTML('<info>Explore various features of Prompt Toolkit library</info>'))
            print_formatted_text(HTML('=' * 60))
            
            menu_options = [
                ("0", "Quick Tour", "快速导览所有功能"),
                ("1", "Basic Prompt", "基础输入与历史"),
                ("2", "Auto-Completion", "词/路径/嵌套补全"),
                ("3", "Syntax Highlighting", "Pygments 语法高亮"),
                ("4", "Input Validation", "邮箱与数字校验"),
                ("5", "Dialog Boxes", "信息/确认/按钮/输入"),
                ("6", "Progress Bar", "进度条演示"),
                ("7", "Custom Layout", "文本区/控件布局"),
                ("8", "History Search", "历史搜索与导航"),
                ("9", "Fuzzy Matching", "模糊匹配补全"),
                ("10", "Multi-line Input", "多行输入与续行"),
                ("11", "Auto-Suggest", "历史智能建议"),
                ("12", "Password Input", "密码输入遮罩"),
                ("13", "Custom Completer", "上下文敏感补全"),
                ("q", "Quit", "退出"),
            ]
            
            for key, title, desc in menu_options:
                print_formatted_text(HTML(f'<prompt>{key}</prompt>. {title} - {desc}'))
            
            print_formatted_text(HTML('=' * 60))
            
            try:
                choice_text = self.session.prompt(
                    HTML('<prompt>❯ Select option: </prompt>'),
                    style=self.style
                )
                choice = (choice_text or '').strip().lower()
            
                if choice == 'q':
                    break
                elif choice == '0':
                    self.quick_tour()
                elif choice == '1':
                    self.demo_basic_prompt()
                elif choice == '2':
                    self.demo_auto_completion()
                elif choice == '3':
                    self.demo_syntax_highlighting()
                elif choice == '4':
                    self.demo_input_validation()
                elif choice == '5':
                    self.demo_dialogs()
                elif choice == '6':
                    self.demo_progress_bar()
                elif choice == '7':
                    self.demo_custom_layout()
                elif choice == '8':
                    self.demo_history_search()
                elif choice == '9':
                    self.demo_fuzzy_matching()
                elif choice == '10':
                    self.demo_multi_line_input()
                elif choice == '11':
                    self.demo_auto_suggest()
                elif choice == '12':
                    self.demo_password_input()
                elif choice == '13':
                    self.demo_custom_completer()
                else:
                    print_formatted_text(HTML('<error>Invalid option. Please try again.</error>'))
                
                print_formatted_text(HTML('\n<info>Press Enter to continue...</info>'))
                input()
                
            except KeyboardInterrupt:
                print_formatted_text(HTML('\n<error>Operation cancelled</error>'))
                break
            except EOFError:
                print_formatted_text(HTML('\n<error>End of input</error>'))
                break
    
    def run(self):
        """Run the showcase."""
        try:
            self.show_menu()
            print_formatted_text(HTML('<success>\n🎉 Thank you for exploring Prompt Toolkit!</success>'))
        except Exception as e:
            print_formatted_text(HTML(f'<error>Error: {e}</error>'))

    def quick_tour(self):
        print_formatted_text(HTML('<title>🚀 Prompt Toolkit 快速导览</title>'))
        print_formatted_text(HTML('=' * 60))
        
        print_formatted_text(HTML('<info>基础输入与历史</info>'))
        print_formatted_text(HTML('<output>示例: 支持历史记录与样式化提示</output>'))
        
        print_formatted_text(HTML('<info>词/路径/嵌套补全</info>'))
        wc = WordCompleter(['git','docker','status','run','build'], ignore_case=True)
        pc = PathCompleter()
        nc = NestedCompleter.from_nested_dict({'git': {'status': None, 'add': None}})
        wcs = [c.text for c in wc.get_completions(Document('st', cursor_position=2), None)]
        pcs = [c.text for c in pc.get_completions(Document('~', cursor_position=1), None)][:5]
        ncs = [c.text for c in nc.get_completions(Document('git ', cursor_position=4), None)]
        print_formatted_text(HTML(f'<output>词补全: {", ".join(wcs) or "(无)"}</output>'))
        print_formatted_text(HTML(f'<output>路径补全: {", ".join(pcs) or "(无)"}</output>'))
        print_formatted_text(HTML(f'<output>嵌套补全: {", ".join(ncs) or "(无)"}</output>'))
        
        print_formatted_text(HTML('<info>Pygments 语法高亮</info>'))
        code = 'def add(a, b):\n    return a + b\n'
        ansi = highlight(code, PythonLexer(), TerminalFormatter())
        print_formatted_text(ANSI(ansi))
        
        print_formatted_text(HTML('<info>输入校验</info>'))
        class _EmailV(Validator):
            def validate(self, d):
                t = d.text
                if '@' not in t or '.' not in t.split('@')[-1]:
                    raise ValidationError(message='邮箱不合法', cursor_position=len(t))
        try:
            _EmailV().validate(Document('user@invalid'))
        except ValidationError:
            print_formatted_text(HTML('<error>⛔ 错误邮箱: user@invalid</error>'))
        _EmailV().validate(Document('user@example.com'))
        print_formatted_text(HTML('<success>✅ 正确邮箱: user@example.com</success>'))
        
        print_formatted_text(HTML('<info>对话框</info>'))
        _ = message_dialog(title='信息', text='示例')
        _ = yes_no_dialog(title='确认', text='示例')
        _ = button_dialog(title='按钮', text='示例', buttons=[('OK','ok')])
        print_formatted_text(HTML('<output>已创建: 信息/确认/按钮 对话框</output>'))
        
        print_formatted_text(HTML('<info>进度条</info>'))
        with ProgressBar() as pb:
            for _ in pb(range(20), label='Tour'):
                time.sleep(0.005)
        
        print_formatted_text(HTML('<info>自定义布局</info>'))
        ta = TextArea(text='示例', multiline=True, height=3)
        lay = Layout(HSplit([Frame(title='编辑器', body=ta, height=4)]))
        _ = Application(layout=lay, key_bindings=self.kb, style=self.style, full_screen=False)
        print_formatted_text(HTML('<output>布局构建完成</output>'))
        
        print_formatted_text(HTML('<info>历史搜索与导航</info>'))
        self.history.append_string('git status')
        self.history.append_string('docker ps')
        self.history.append_string('python main.py')
        print_formatted_text(HTML('<output>历史已预置: git status, docker ps, python main.py</output>'))
        
        print_formatted_text(HTML('<info>模糊匹配补全</info>'))
        fz = FuzzyCompleter(WordCompleter(['python','docker','status','start']))
        fzs = [c.text for c in fz.get_completions(Document('st', cursor_position=2), None)]
        print_formatted_text(HTML(f'<output>模糊匹配: {", ".join(fzs) or "(无)"}</output>'))
        
        print_formatted_text(HTML('<info>多行输入与续行</info>'))
        ml = 'line1\nline2\nline3'
        print_formatted_text(HTML(f'<output>示例:\n{ml}</output>'))
        
        print_formatted_text(HTML('<info>历史智能建议</info>'))
        mem_hist = InMemoryHistory()
        mem_hist.append_string('print("hello")')
        sug = AutoSuggestFromHistory()
        buf = Buffer(history=mem_hist)
        s = sug.get_suggestion(buf, Document('pri', cursor_position=3))
        print_formatted_text(HTML(f'<output>建议: {(s.text if s else "(无)")}</output>'))
        
        print_formatted_text(HTML('<info>密码输入遮罩</info>'))
        print_formatted_text(HTML('<output>示例: ******</output>'))
        
        print_formatted_text(HTML('<info>上下文敏感补全</info>'))
        class _Ctx(Completer):
            def get_completions(self, document, ce):
                t = document.text_before_cursor
                if t.startswith('git '):
                    for c in ['status','add','commit']:
                        yield Completion(c, start_position=0)
        ctx = _Ctx()
        ctxs = [c.text for c in ctx.get_completions(Document('git ', cursor_position=4), None)]
        print_formatted_text(HTML(f'<output>上下文补全: {", ".join(ctxs) or "(无)"}</output>'))
        
        print_formatted_text(HTML('<success>🎉 快速导览完成</success>'))

    def self_test_all(self):
        """Run non-interactive self-tests to verify APIs without blocking input."""
        print_formatted_text(HTML('<title>🔧 Running Prompt Toolkit Self-Tests</title>'))
        errors = []

        # Auto-completion constructs
        try:
            command_completer = WordCompleter([
                'git', 'docker', 'python', 'list', 'show', 'create', 'delete'
            ], ignore_case=True)
            path_completer = PathCompleter()
            nested_completer = NestedCompleter.from_nested_dict({
                'git': {
                    'status': None,
                    'add': None,
                    'commit': None,
                    'push': None,
                    'pull': None,
                },
                'docker': {
                    'build': None,
                    'run': None,
                    'ps': None,
                    'images': None,
                    'logs': None,
                }
            })
            fuzzy = FuzzyCompleter(command_completer)
            # Probe completions programmatically
            _ = list(fuzzy.get_completions(Document('gi', cursor_position=2), None))
            _ = list(path_completer.get_completions(Document('~', cursor_position=1), None))
            _ = list(nested_completer.get_completions(Document('git ', cursor_position=4), None))
            print_formatted_text(HTML('<success>✅ Auto-completion APIs OK</success>'))
        except Exception as e:
            errors.append(f'Auto-completion: {e}')

        # Syntax highlighting (lexer instantiation)
        try:
            _ = PygmentsLexer(PythonLexer)
            print_formatted_text(HTML('<success>✅ Syntax highlighting lexer OK</success>'))
        except Exception as e:
            errors.append(f'Syntax highlighting: {e}')

        # Validators
        try:
            class _EmailValidator(Validator):
                def validate(self, document):
                    text = document.text
                    if '@' not in text or '.' not in text.split('@')[-1]:
                        raise ValidationError(message='invalid', cursor_position=len(text))
            v = _EmailValidator()
            try:
                v.validate(Document('user@example.com'))
            except ValidationError:
                pass
            print_formatted_text(HTML('<success>✅ Validators OK</success>'))
        except Exception as e:
            errors.append(f'Validators: {e}')

        # Dialogs (instantiate but do not run)
        try:
            _ = message_dialog(title='Info', text='Self-test')
            _ = yes_no_dialog(title='Confirm', text='Self-test')
            _ = button_dialog(title='Buttons', text='Self-test', buttons=[('OK','ok')])
            print_formatted_text(HTML('<success>✅ Dialog creation OK</success>'))
        except Exception as e:
            errors.append(f'Dialogs: {e}')

        # Progress bar (short run)
        try:
            with ProgressBar() as pb:
                for _ in pb(range(10), label='Self-test'):
                    time.sleep(0.001)
            print_formatted_text(HTML('<success>✅ Progress bar OK</success>'))
        except Exception as e:
            errors.append(f'Progress bar: {e}')

        # Custom layout (create Application without running)
        try:
            text_area = TextArea(text='Self-test', multiline=True, height=3)
            layout = Layout(HSplit([Frame(title='Test', body=text_area, height=4)]))
            _ = Application(layout=layout, key_bindings=self.kb, style=self.style, full_screen=False)
            print_formatted_text(HTML('<success>✅ Layout and Application creation OK</success>'))
        except Exception as e:
            errors.append(f'Layout: {e}')

        # History & auto-suggest
        try:
            mem_hist = InMemoryHistory()
            mem_hist.append_string('print("hello")')
            suggester = AutoSuggestFromHistory()
            buf = Buffer(history=mem_hist)
            _ = suggester.get_suggestion(buf, Document('pri', cursor_position=3))
            print_formatted_text(HTML('<success>✅ History and Auto-suggest OK</success>'))
        except Exception as e:
            errors.append(f'History/Auto-suggest: {e}')

        # Fuzzy matching (verify completions)
        try:
            fuzzy = FuzzyCompleter(WordCompleter(['start','stop','status']))
            comps = list(fuzzy.get_completions(Document('st', cursor_position=2), None))
            assert len(comps) >= 1
            print_formatted_text(HTML('<success>✅ Fuzzy matching OK</success>'))
        except Exception as e:
            errors.append(f'Fuzzy matching: {e}')

        # Custom completer
        try:
            class _SimpleCompleter(Completer):
                def get_completions(self, document, complete_event):
                    words = ['alpha','beta','gamma']
                    text = document.text
                    for w in words:
                        if w.startswith(text):
                            yield Completion(w, start_position=-len(text))
            c = _SimpleCompleter()
            _ = list(c.get_completions(Document('a', cursor_position=1), None))
            print_formatted_text(HTML('<success>✅ Custom completer OK</success>'))
        except Exception as e:
            errors.append(f'Custom completer: {e}')

        if errors:
            print_formatted_text(HTML('<error>❌ Self-tests found issues:</error>'))
            for err in errors:
                print_formatted_text(HTML(f'<error>- {err}</error>'))
            raise Exception('Prompt Toolkit self-tests failed')
        else:
            print_formatted_text(HTML('<success>🎉 All Prompt Toolkit self-tests passed</success>'))


def main():
    """Main function to run the Prompt Toolkit showcase."""
    showcase = PromptToolkitShowcase()
    # Allow a non-interactive self-test mode via environment variable
    if os.environ.get('PTK_SELF_TEST_ALL') == '1':
        showcase.self_test_all()
    else:
        showcase.run()


if __name__ == "__main__":
    main()