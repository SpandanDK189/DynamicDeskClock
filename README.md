
# Windows 11 Desktop Clock Overlay

A draggable and transparent desktop clock styled like the Windows 11 lock screen. Displays the current time, day, and date in a sleek, customizable design.

---

## Features

- **Clean UI:** Displays time, day, and date in a clean, minimalist format.
- **Draggable:** Move the clock anywhere on the desktop.
- **Customizable Fonts:** Default font is `Segoe UI`, but you can modify it.
- **Transparent Background:** Seamlessly blends into the desktop.
- **Real-time Sync:** Updates every minute to ensure accurate time.

---

## Prerequisites

1. **Python Installation**
   - Ensure Python (version 3.10 or higher) is installed. [Download Python here](https://www.python.org/downloads/).
   - Add Python to your system PATH during installation.

2. **NirCmd**
   - Download and extract NirCmd from [NirCmd Official Website](https://www.nirsoft.net/utils/nircmd.html).
   - Place `nircmd.exe` in the project directory.

---

## Installation and Setup

### Step 1: Clone or Download the Repository
Clone this repository or download the ZIP and extract it to your desired folder.

```bash
git clone https://github.com/your-username/desktop-clock-overlay.git
cd desktop-clock-overlay
```

### Step 2: Folder Structure
Ensure the following folder structure is in place:

```
project-folder/
│
├── CustomizableClockTemplate.py    # Main Python script
├── LaunchClock.bat                 # Batch file to run the clock
├── nircmd.exe                      # NirCmd executable for minimizing CMD
├── nircmd.chm                      # Optional help file
└── nircmdc.exe                     # Command-line version of NirCmd
```

### Step 3: Create the Python Script
Create a file named `CustomizableClockTemplate.py` in the `project-folder` directory and paste the following code:

```python
import tkinter as tk
import time

# Function to update the clock
def update_time():
    current_time = time.strftime('%H:%M')  # Display hours and minutes only
    day_and_date = time.strftime('%A, %B %d')  # Day of the week, month name, day of the month
    time_label.config(text=current_time)
    date_label.config(text=day_and_date)
    root.after(60000, update_time)

# Function to drag the clock window
def start_drag(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

def do_drag(event):
    delta_x = event.x - x_offset
    delta_y = event.y - y_offset
    new_x = root.winfo_x() + delta_x
    new_y = root.winfo_y() + delta_y
    root.geometry(f"+{new_x}+{new_y}")

# Create the main window
root = tk.Tk()
root.title("Desktop Clock Overlay")

root.overrideredirect(True)  # Remove window decorations
root.attributes('-alpha', 1)  # Full opacity
root.config(bg='black')
root.attributes('-transparentcolor', 'black')

time_font_size = 128
date_font_size = 36

time_label = tk.Label(root, font=('Segoe UI', time_font_size), fg='white', bg='black')
time_label.pack(fill='both', expand=True, pady=(0, 5))

date_label = tk.Label(root, font=('Segoe UI', date_font_size), fg='white', bg='black')
date_label.pack(fill='both', expand=True, pady=(5, 0))

window_width = time_font_size * 4
window_height = time_font_size * 2 + date_font_size + 12

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = screen_height // 2 - window_height // 2

root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

update_time()

root.bind('<Button-1>', start_drag)
root.bind('<B1-Motion>', do_drag)

root.mainloop()
```

### Step 4: Create the Batch File
Create a file named `LaunchClock.bat` in the `project-folder` directory with the following content:

```bat
@echo off
cd /d "C:\path\to\project-folder"
start "" nircmd.exe exec hide "C:\path\to\python.exe" "C:\path\to\project-folder\CustomizableClockTemplate.py"
exit
```

- Replace `C:\path\to\python.exe` with the actual path of your Python executable. Use `where python` to find it.
- Replace `C:\path\to\project-folder` with the actual path of your project folder.

---

## Usage

1. Double-click the `LaunchClock.bat` file to run the clock.
2. To auto-start on system boot:
   - Press `Win + R`, type `shell:startup`, and press Enter.
   - Copy `LaunchClock.bat` into the startup folder.

---

## Notes

- You can adjust the fonts and dimensions by modifying the `time_font_size` and `date_font_size` variables in `CustomizableClockTemplate.py`.
- Ensure NirCmd is in the same folder as the script for minimizing CMD windows.

---

## Contributing

Feel free to submit issues or pull requests to improve this project.