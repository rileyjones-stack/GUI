from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

# ------------------- FUNCTION CODE ---------------------#

# Greet me function, run when button is clicked and says greeting with name e.g. Hello Bob!
def greet_me():
    greeting_message.set("{} {}".format(greeting.get(), name.get()))


# -------------------- USER INTERFACE CODE --------------#
# Create the main window with title
root = Tk()
root.title("My Python GUI Demo")

# Create an outer label frame - puts a labeled border around its child widgets, can help to organise UI
container = ttk.LabelFrame(root, text="Greeting Program")
container.grid(column=0, row=0)

# ---------------------- GREETING CHOICES --------------#
# Adding a combo box - dropdown with text entry, can disable free text entry (read only)
greeting_box_label = ttk.Label(container, text="Choose/enter a greeting:").grid(column=0, row=0)
greeting = StringVar()

greeting_box = ttk.Combobox(container, textvariable=greeting)
greeting_box['values'] = ["Hello", "Goodbye", "Good Morning", "Good Afternoon", "Good Night"]
greeting_box.grid(column=0, row=1)
greeting_box.current(0)

# -----------------------NAME ENTRY --------------------#
#Adding a Label - Text labels that can go anywhere
name_label = ttk.Label(container, text="Enter a name: ")
name_label.grid(column=1, row=0)

#Adding a textbox entry widget - just a basic 1 line input you can set the width of
#Can assign it a textvariable which it will automatically change to if that variable is changed
name = StringVar()
name_entered = ttk.Entry(container, textvariable=name)
name_entered.grid(column=1, row=1)
name_entered.focus()

# ------------------- GREETING OUTPUT AND BUTTON --------#
# Label to put text into
greeting_message = StringVar()
greeting_label = ttk.Label(container, textvariable=greeting_message).grid(column=2, row=0)

#Adding a Button - just a button, with text, can run a function when clicked
action_button = ttk.Button(container, text="Greet me!", command=greet_me)
action_button.grid(column=2, row=1)

# Adding checkboxes in different states
use_name = IntVar()
check_box = Checkbutton(container, text="Use my name", variable=use_name, state='disabled')
check_box.select()
check_box.grid(column=0, row=2, sticky=W)

# ------------------- STYLES/PADDING --------------------#
container.grid_configure(padx=10, pady=10)

for child in container.winfo_children():
    child.grid_configure(padx=10, pady=10, sticky=W)

# Up to page 41 with tabbed widgets up next
root.mainloop()
