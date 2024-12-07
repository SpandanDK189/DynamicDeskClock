import tkinter as tk
import time

# Function to update the clock
def update_time():
    current_time = time.strftime('%H:%M')  # Display hours and minutes only
    day_and_date = time.strftime('%A, %B %d')  # Day of the week, month name, day of the month
    time_label.config(text=current_time)
    date_label.config(text=day_and_date)
    root.after(1000, update_time)  # Update every second for perfect synchronization

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
root.title("Customizable Clock")

# Remove the window border and title bar
root.overrideredirect(True)

# Set window transparency and make the background color transparent
root.attributes('-alpha', 1)  # Fully opaque
root.config(bg='black')
root.attributes('-transparentcolor', 'black')

# Set the font size for time and day/date
time_font_size = 128  # Customize font size here
date_font_size = 36   # Customize date font size here

# Create label for time
time_label = tk.Label(root, font=('Segoe UI', time_font_size), fg='white', bg='black')
time_label.pack(fill='both', expand=True, pady=(0, 5))

# Create label for day and date
date_label = tk.Label(root, font=('Segoe UI', date_font_size), fg='white', bg='black')
date_label.pack(fill='both', expand=True, pady=(5, 0))

# Dynamically set the window size based on font size
window_width = time_font_size * 4
window_height = time_font_size * 2 + date_font_size + 12

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the initial position to center the clock
x_position = (screen_width - window_width) // 2
y_position = screen_height // 2 - window_height // 2

# Set the window size and position
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')

# Call the update_time function to start updating the clock
update_time()

# Bind mouse events to make the window draggable
root.bind('<Button-1>', start_drag)
root.bind('<B1-Motion>', do_drag)

# Start the Tkinter event loop
root.mainloop()
