"""
Textual Library Showcase

This module demonstrates various features of the Textual library for building
rich terminal user interfaces (TUIs). Textual provides a modern framework
for creating interactive applications with widgets, layouts, and events.
"""

from textual.app import App, ComposeResult
from textual.widgets import (
    Button, 
    Static, 
    Input, 
    Label, 
    DataTable,
    ListView,
    ListItem,
    Select,
    Checkbox,
    RadioButton,
    RadioSet,
    ProgressBar,
    Switch,
    TabbedContent,
    TabPane,
    Markdown,
    Log
)
from textual.containers import Container, Horizontal, Vertical, Grid
from textual.reactive import reactive
from textual import events, on
from textual.screen import Screen, ModalScreen
from textual.binding import Binding
from textual.message import Message
from textual.css.query import NoMatches
from textual.timer import Timer
import asyncio
from datetime import datetime
from typing import List, Dict, Any


class WelcomeScreen(Screen):
    """Welcome screen with introductory message and navigation."""
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("🎯 Textual Library Showcase", id="title"),
            Static("\nExplore the powerful features of Textual for building rich terminal applications", id="subtitle"),
            Static("\n" + "="*60, id="separator"),
            Static("\nSelect a demo to explore:", id="prompt"),
            Button("1. Basic Widgets Demo", id="basic-widgets", variant="primary"),
            Button("2. Layout & Containers Demo", id="layout-demo"),
            Button("3. Interactive Forms Demo", id="forms-demo"),
            Button("4. Data Display Demo", id="data-demo"),
            Button("5. Real-time Updates Demo", id="realtime-demo"),
            Button("6. Custom Components Demo", id="custom-demo"),
            Button("7. Multi-screen Navigation", id="navigation-demo"),
            Static("\n" + "="*60, id="separator2"),
            Static("Press 'q' to quit | 'h' for help", id="footer"),
            id="welcome-container"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks to navigate to different demos."""
        demo_id = event.button.id
        if demo_id == "basic-widgets":
            self.app.push_screen(BasicWidgetsScreen())
        elif demo_id == "layout-demo":
            self.app.push_screen(LayoutDemoScreen())
        elif demo_id == "forms-demo":
            self.app.push_screen(FormsDemoScreen())
        elif demo_id == "data-demo":
            self.app.push_screen(DataDisplayScreen())
        elif demo_id == "realtime-demo":
            self.app.push_screen(RealTimeScreen())
        elif demo_id == "custom-demo":
            self.app.push_screen(CustomComponentsScreen())
        elif demo_id == "navigation-demo":
            self.app.push_screen(NavigationDemoScreen())


class BasicWidgetsScreen(Screen):
    """Demo showcasing basic Textual widgets."""
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("📦 Basic Widgets Demo", id="title"),
            Static("\nExplore fundamental Textual widgets:", id="subtitle"),
            
            Horizontal(
                Vertical(
                    Static("Buttons:", classes="section-title"),
                    Button("Primary Button", variant="primary"),
                    Button("Success Button", variant="success"),
                    Button("Warning Button", variant="warning"),
                    Button("Error Button", variant="error"),
                    classes="widget-group"
                ),
                Vertical(
                    Static("Inputs:", classes="section-title"),
                    Input(placeholder="Enter text here..."),
                    Input(placeholder="Password...", password=True),
                    Input(placeholder="Number...", type="number"),
                    classes="widget-group"
                ),
                classes="widget-row"
            ),
            
            Horizontal(
                Vertical(
                    Static("Selection:", classes="section-title"),
                    Checkbox("Checkbox Option 1"),
                    Checkbox("Checkbox Option 2", value=True),
                    RadioSet(
                        RadioButton("Radio Option 1"),
                        RadioButton("Radio Option 2"),
                        RadioButton("Radio Option 3")
                    ),
                    classes="widget-group"
                ),
                Vertical(
                    Static("Switches & Select:", classes="section-title"),
                    Switch("Toggle Switch"),
                    Select(
                        [("Option 1", "opt1"), ("Option 2", "opt2"), ("Option 3", "opt3")],
                        prompt="Select an option..."
                    ),
                    ProgressBar(total=100),
                    classes="widget-group"
                ),
                classes="widget-row"
            ),
            
            Button("← Back to Main Menu", variant="default", id="back-btn"),
            id="basic-widgets-container"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            self.app.pop_screen()


class LayoutDemoScreen(Screen):
    """Demo showcasing Textual layout capabilities."""
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("🎨 Layout & Containers Demo", id="title"),
            Static("\nExplore Textual's powerful layout system:", id="subtitle"),
            
            TabbedContent(
                TabPane("Horizontal Layout", id="horizontal-tab"),
                TabPane("Vertical Layout", id="vertical-tab"),
                TabPane("Grid Layout", id="grid-tab"),
                TabPane("Mixed Layout", id="mixed-tab"),
            ),
            
            Button("← Back to Main Menu", variant="default", id="back-btn"),
            id="layout-demo-container"
        )

    def on_mount(self) -> None:
        """Set up the tab content after mount."""
        try:
            # Horizontal layout tab
            horizontal_tab = self.query_one("#horizontal-tab")
            horizontal_tab.mount(
                Horizontal(
                    Button("Left", variant="primary"),
                    Button("Center", variant="success"),
                    Button("Right", variant="warning"),
                    Button("Extra", variant="error"),
                    id="horizontal-demo"
                )
            )
            
            # Vertical layout tab
            vertical_tab = self.query_one("#vertical-tab")
            vertical_tab.mount(
                Vertical(
                    Button("Top", variant="primary"),
                    Button("Middle", variant="success"),
                    Button("Bottom", variant="warning"),
                    id="vertical-demo"
                )
            )
            
            # Grid layout tab
            grid_tab = self.query_one("#grid-tab")
            grid_tab.mount(
                Grid(
                    Button("1,1", variant="primary"),
                    Button("1,2", variant="success"),
                    Button("2,1", variant="warning"),
                    Button("2,2", variant="error"),
                    grid_columns="1fr 1fr",
                    grid_rows="1fr 1fr",
                    id="grid-demo"
                )
            )
            
            # Mixed layout tab
            mixed_tab = self.query_one("#mixed-tab")
            mixed_tab.mount(
                Vertical(
                    Horizontal(
                        Button("H1", variant="primary"),
                        Button("H2", variant="success"),
                    ),
                    Horizontal(
                        Button("H3", variant="warning"),
                        Button("H4", variant="error"),
                    ),
                    id="mixed-demo"
                )
            )
            
        except NoMatches:
            pass

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            self.app.pop_screen()


class FormsDemoScreen(Screen):
    """Demo showcasing form handling and validation."""
    
    form_data = reactive({})
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("📝 Interactive Forms Demo", id="title"),
            Static("\nExperience form handling with validation:", id="subtitle"),
            
            Vertical(
                Static("User Registration Form:", classes="form-title"),
                Input(placeholder="Username", id="username"),
                Input(placeholder="Email", id="email", type="email"),
                Input(placeholder="Password", id="password", password=True),
                Input(placeholder="Age", id="age", type="number"),
                
                Horizontal(
                    Static("Gender:"),
                    RadioSet(
                        RadioButton("Male", id="gender-male"),
                        RadioButton("Female", id="gender-female"),
                        RadioButton("Other", id="gender-other"),
                        id="gender"
                    ),
                    classes="form-row"
                ),
                
                Horizontal(
                    Checkbox("Subscribe to newsletter", id="newsletter"),
                    Switch("Accept terms", id="terms"),
                    classes="form-row"
                ),
                
                Select(
                    [("Beginner", "beginner"), ("Intermediate", "intermediate"), ("Advanced", "advanced")],
                    prompt="Select experience level",
                    id="experience"
                ),
                
                Horizontal(
                    Button("Submit Form", variant="success", id="submit-btn"),
                    Button("Clear Form", variant="default", id="clear-btn"),
                    classes="form-buttons"
                ),
                
                Static("Form Data:", classes="data-title"),
                Log(id="form-log", max_lines=10),
                
                classes="form-container"
            ),
            
            Button("← Back to Main Menu", variant="default", id="back-btn"),
            id="forms-demo-container"
        )

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle input changes and update form data."""
        self.form_data[event.input.id] = event.value
        self.update_form_log()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            self.app.pop_screen()
        elif event.button.id == "submit-btn":
            self.submit_form()
        elif event.button.id == "clear-btn":
            self.clear_form()

    def submit_form(self) -> None:
        """Submit the form and show validation."""
        log = self.query_one("#form-log")
        log.write_line("✅ Form submitted successfully!")
        log.write_line(f"📋 Data: {self.form_data}")

    def clear_form(self) -> None:
        """Clear all form fields."""
        self.form_data = {}
        # Clear all inputs
        for widget in self.query(Input):
            widget.value = ""
        for widget in self.query(Checkbox):
            widget.value = False
        for widget in self.query(Switch):
            widget.value = False
        for widget in self.query(Select):
            widget.value = None
        for widget in self.query(RadioSet):
            widget.value = None
        
        log = self.query_one("#form-log")
        log.clear()
        log.write_line("🧹 Form cleared!")

    def update_form_log(self) -> None:
        """Update the form data log."""
        log = self.query_one("#form-log")
        log.clear()
        for key, value in self.form_data.items():
            if value:
                log.write_line(f"{key}: {value}")


class DataDisplayScreen(Screen):
    """Demo showcasing data display widgets."""
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("📊 Data Display Demo", id="title"),
            Static("\nExplore data visualization widgets:", id="subtitle"),
            
            TabbedContent(
                TabPane("Data Table", id="table-tab"),
                TabPane("List View", id="list-tab"),
                TabPane("Markdown", id="markdown-tab"),
            ),
            
            Button("← Back to Main Menu", variant="default", id="back-btn"),
            id="data-display-container"
        )

    def on_mount(self) -> None:
        """Set up data display widgets."""
        try:
            # Data table
            table_tab = self.query_one("#table-tab")
            table = DataTable()
            table.add_columns("ID", "Name", "Age", "City", "Status")
            table.add_rows([
                ("1", "Alice", "25", "New York", "Active"),
                ("2", "Bob", "30", "London", "Inactive"),
                ("3", "Charlie", "28", "Tokyo", "Active"),
                ("4", "Diana", "35", "Paris", "Pending"),
                ("5", "Eve", "22", "Berlin", "Active"),
            ])
            table_tab.mount(table)
            
            # List view
            list_tab = self.query_one("#list-tab")
            list_view = ListView(
                ListItem(Label("Item 1")),
                ListItem(Label("Item 2")),
                ListItem(Label("Item 3")),
                ListItem(Label("Item 4")),
                ListItem(Label("Item 5")),
            )
            list_tab.mount(list_view)
            
            # Markdown content
            markdown_tab = self.query_one("#markdown-tab")
            markdown_content = """
# Sample Markdown

## Features
- **Bold** and *italic* text
- Code blocks: `print('Hello')`
- Lists and tables

## Code Example
```python
def hello():
    print("Hello, Textual!")
```

> This is a blockquote
            """
            markdown = Markdown(markdown_content)
            markdown_tab.mount(markdown)
            
        except NoMatches:
            pass

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            self.app.pop_screen()


class RealTimeScreen(Screen):
    """Demo showcasing real-time updates and timers."""
    
    counter = reactive(0)
    current_time = reactive("")
    progress_value = reactive(0)
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("⏰ Real-time Updates Demo", id="title"),
            Static("\nExperience real-time data updates:", id="subtitle"),
            
            Vertical(
                Static("Counter: 0", id="counter-display"),
                Horizontal(
                    Button("Increment", variant="primary", id="increment-btn"),
                    Button("Decrement", variant="default", id="decrement-btn"),
                    Button("Reset", variant="warning", id="reset-btn"),
                    classes="counter-buttons"
                ),
                
                Static("Current Time: ", id="time-label"),
                Static("", id="time-display"),
                
                Static("Progress Bar:", classes="progress-label"),
                ProgressBar(total=100, id="progress-bar"),
                Horizontal(
                    Button("Start Progress", variant="success", id="start-progress"),
                    Button("Stop Progress", variant="error", id="stop-progress"),
                    classes="progress-buttons"
                ),
                
                Log(id="event-log", max_lines=8),
                
                classes="realtime-container"
            ),
            
            Button("← Back to Main Menu", variant="default", id="back-btn"),
            id="realtime-container"
        )

    def on_mount(self) -> None:
        """Start timers for real-time updates."""
        self.set_interval(1.0, self.update_time)
        self.progress_timer = None

    def watch_counter(self, counter: int) -> None:
        """Update counter display when counter changes."""
        self.query_one("#counter-display").update(f"Counter: {self.counter}")
        self.query_one("#event-log").write_line(f"Counter updated: {self.counter}")

    def watch_current_time(self, time: str) -> None:
        """Update time display when time changes."""
        self.query_one("#time-display").update(self.current_time)

    def watch_progress_value(self, value: int) -> None:
        """Update progress bar when value changes."""
        progress_bar = self.query_one("#progress-bar")
        progress_bar.progress = value

    def update_time(self) -> None:
        """Update current time."""
        self.current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            if self.progress_timer:
                self.progress_timer.stop()
            self.app.pop_screen()
        elif event.button.id == "increment-btn":
            self.counter += 1
        elif event.button.id == "decrement-btn":
            self.counter -= 1
        elif event.button.id == "reset-btn":
            self.counter = 0
        elif event.button.id == "start-progress":
            self.start_progress()
        elif event.button.id == "stop-progress":
            self.stop_progress()

    def start_progress(self) -> None:
        """Start progress bar animation."""
        if self.progress_timer:
            self.progress_timer.stop()
        
        self.progress_value = 0
        self.progress_timer = self.set_interval(0.1, self.update_progress)
        self.query_one("#event-log").write_line("Progress started")

    def stop_progress(self) -> None:
        """Stop progress bar animation."""
        if self.progress_timer:
            self.progress_timer.stop()
            self.progress_timer = None
            self.query_one("#event-log").write_line("Progress stopped")

    def update_progress(self) -> None:
        """Update progress bar value."""
        if self.progress_value < 100:
            self.progress_value += 1
        else:
            self.stop_progress()


class CustomComponentsScreen(Screen):
    """Demo showcasing custom components and messages."""
    
    class CustomMessage(Message):
        """Custom message for component communication."""
        def __init__(self, message: str) -> None:
            self.message = message
            super().__init__()

    class CustomButton(Static):
        """A custom button component."""
        
        def __init__(self, label: str, **kwargs) -> None:
            super().__init__(**kwargs)
            self.label = label
            self.pressed = False
        
        def compose(self) -> ComposeResult:
            yield Static(self.label, classes="custom-button-label")
        
        def on_click(self) -> None:
            self.pressed = not self.pressed
            self.add_class("pressed" if self.pressed else "")
            self.remove_class("pressed" if not self.pressed else "")
            self.post_message(self.CustomMessage(f"Custom button '{self.label}' clicked!"))

    def compose(self) -> ComposeResult:
        yield Container(
            Static("🔧 Custom Components Demo", id="title"),
            Static("\nExplore custom components and messaging:", id="subtitle"),
            
            Vertical(
                Static("Custom Buttons:", classes="section-title"),
                Horizontal(
                    self.CustomButton("Custom 1", id="custom-btn-1"),
                    self.CustomButton("Custom 2", id="custom-btn-2"),
                    self.CustomButton("Custom 3", id="custom-btn-3"),
                    classes="custom-buttons-row"
                ),
                
                Static("Message Log:", classes="log-title"),
                Log(id="message-log", max_lines=6),
                
                classes="custom-components-container"
            ),
            
            Button("← Back to Main Menu", variant="default", id="back-btn"),
            id="custom-components-container"
        )

    def on_custom_components_screen_custom_message(self, message: CustomMessage) -> None:
        """Handle custom messages from components."""
        self.query_one("#message-log").write_line(f"📨 {message.message}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            self.app.pop_screen()


class NavigationDemoScreen(Screen):
    """Demo showcasing multi-screen navigation."""
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("🧭 Multi-screen Navigation Demo", id="title"),
            Static("\nExperience screen navigation patterns:", id="subtitle"),
            
            Vertical(
                Static("Navigation Options:", classes="section-title"),
                Button("Push Modal Screen", variant="primary", id="modal-btn"),
                Button("Replace Current Screen", variant="success", id="replace-btn"),
                Button("Show Alert Dialog", variant="warning", id="alert-btn"),
                Button("Show Confirmation", variant="error", id="confirm-btn"),
                
                Static("Navigation History:", classes="history-title"),
                Log(id="nav-log", max_lines=5),
                
                classes="navigation-container"
            ),
            
            Button("← Back to Main Menu", variant="default", id="back-btn"),
            id="navigation-container"
        )

    def on_mount(self) -> None:
        """Log initial navigation."""
        self.query_one("#nav-log").write_line("📱 NavigationDemoScreen mounted")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back-btn":
            self.app.pop_screen()
        elif event.button.id == "modal-btn":
            self.push_modal()
        elif event.button.id == "replace-btn":
            self.replace_screen()
        elif event.button.id == "alert-btn":
            self.show_alert()
        elif event.button.id == "confirm-btn":
            self.show_confirmation()

    def push_modal(self) -> None:
        """Push a modal screen."""
        class ModalDemoScreen(ModalScreen):
            def compose(self) -> ComposeResult:
                yield Container(
                    Static("🔘 Modal Screen", id="modal-title"),
                    Static("This is a modal dialog!", id="modal-content"),
                    Button("Close", variant="primary", id="close-btn"),
                    id="modal-container"
                )
            
            def on_button_pressed(self, event: Button.Pressed) -> None:
                if event.button.id == "close-btn":
                    self.dismiss()
        
        self.app.push_screen(ModalDemoScreen())
        self.query_one("#nav-log").write_line("📤 Modal screen pushed")

    def replace_screen(self) -> None:
        """Replace current screen."""
        class ReplacementScreen(Screen):
            def compose(self) -> ComposeResult:
                yield Container(
                    Static("🔄 Replacement Screen", id="replace-title"),
                    Static("This screen replaced the previous one!", id="replace-content"),
                    Button("Go Back", variant="default", id="back-btn"),
                    id="replace-container"
                )
            
            def on_button_pressed(self, event: Button.Pressed) -> None:
                if event.button.id == "back-btn":
                    self.app.pop_screen()
        
        self.app.push_screen(ReplacementScreen())
        self.query_one("#nav-log").write_line("🔄 Screen replaced")

    def show_alert(self) -> None:
        """Show an alert dialog."""
        self.app.bell()
        self.query_one("#nav-log").write_line("⚠️  Alert triggered")

    def show_confirmation(self) -> None:
        """Show a confirmation dialog."""
        # This would typically use a proper dialog component
        self.query_one("#nav-log").write_line("❓ Confirmation requested")


class TextualShowcaseApp(App):
    """Main Textual showcase application."""
    
    CSS = """
    #title {
        text-align: center;
        text-style: bold;
        color: #FF6B6B;
        margin: 1;
    }
    
    #subtitle {
        text-align: center;
        color: #4ECDC4;
        margin: 1 0 2 0;
    }
    
    .section-title {
        text-style: bold underline;
        color: #45B7D1;
        margin: 1 0;
    }
    
    .widget-group {
        border: solid #FFE66D;
        padding: 1;
        margin: 1;
        width: 1fr;
    }
    
    .widget-row {
        height: auto;
        margin: 1 0;
    }
    
    .form-container {
        border: solid #4ECDC4;
        padding: 2;
        margin: 1 0;
    }
    
    .form-title {
        text-style: bold;
        color: #FF6B6B;
        margin: 0 0 1 0;
    }
    
    .form-row {
        height: auto;
        margin: 1 0;
    }
    
    .form-buttons {
        margin: 2 0 1 0;
    }
    
    .data-title {
        text-style: bold;
        color: #FF6B6B;
        margin: 2 0 1 0;
    }
    
    .realtime-container {
        border: solid #FF6B6B;
        padding: 2;
        margin: 1 0;
    }
    
    .counter-buttons {
        margin: 1 0;
    }
    
    .progress-label {
        margin: 2 0 1 0;
        color: #4ECDC4;
    }
    
    .progress-buttons {
        margin: 1 0;
    }
    
    .custom-components-container {
        border: solid #45B7D1;
        padding: 2;
        margin: 1 0;
    }
    
    .custom-buttons-row {
        margin: 1 0;
    }
    
    .log-title {
        margin: 2 0 1 0;
        color: #FF6B6B;
    }
    
    .navigation-container {
        border: solid #FFE66D;
        padding: 2;
        margin: 1 0;
    }
    
    .history-title {
        margin: 2 0 1 0;
        color: #4ECDC4;
    }
    
    #footer {
        text-align: center;
        color: #666;
        margin: 2 0 0 0;
    }
    
    .custom-button-label {
        background: #45B7D1;
        color: white;
        padding: 1 2;
        border: solid #2C8AA6;
    }
    
    .custom-button-label.pressed {
        background: #2C8AA6;
        border: solid #1A5C6F;
    }
    
    #separator, #separator2 {
        color: #666;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("h", "help", "Help"),
        Binding("escape", "back", "Back"),
    ]
    
    def on_mount(self) -> None:
        """Start the application with the welcome screen."""
        self.push_screen(WelcomeScreen())
    
    def action_back(self) -> None:
        """Go back to previous screen."""
        if len(self.screen_stack) > 1:
            self.pop_screen()
    
    def action_help(self) -> None:
        """Show help information."""
        self.bell()
        # Would typically show a help dialog


def main():
    """Run the Textual showcase application."""
    app = TextualShowcaseApp()
    app.run()


if __name__ == "__main__":
    main()