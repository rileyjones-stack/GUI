####################  IMPORTS  #######################
from tkinter import *
from tkinter import ttk
import random


##################  CLASS CODE  ######################
# Create the Comic class
class Comic:
  """The Comic class stores the details of each comic and has methods to restock, sell and calculate progress towards the daily average sold"""
  def __init__(self, name, stock, average):
    self.name = name
    self.stock = stock
    self.average = average
    comic_list.append(self)

  # restock method adds comic to stock
  def restock(self, amount):
    if amount > 0:
      self.stock += amount
      return True
    else:
      return False

  # Sell method subtracts comics from total stock
  def sell(self, amount):
    if amount > 0 and amount <= self.stock:
      self.stock -= amount
      return True
    else:
      return False

  # Get progress method calculates average progress
  def get_progress(self):
      progress = (self.stock / self.average) * 100
      return progress


##############  FUNCTIONS AND SETUP ###############
# Create a function to read data from the file



# Create a function to get comic names list
def create_name_list():
  name_list = []
  for comic in comic_list:
    name_list.append(comic.name) 
  return name_list

# Create a function that will update the stock.
def update_stock():
  global total_comic
  stock_string = ""

  # Append each comics stock, progress and average to the label
  for comic in comic_list:
    progress = comic.get_progress()
    stock_string += "{}: {:.0f} - {:.0f}% of {:.0f} daily average sold\n".format(comic.name, comic.stock, progress, comic.average)

  stock_string += "\nTotal sold: {:.0f}".format(total_comic)
  comic_details.set(stock_string)

# Create the restock function
def restock_comics(comic):
  if comic.restock(amount.get()):
    message = random.choice(restock_messages)
    message_text.set(message)
    action_feedback.set("Success! Total of {:.0f} restocked into {}".format(amount.get(), comic.name))
    
  else:
    action_feedback.set("Please enter a positive number")

# Create the sell function
def sell_comics(comic):
  global total_comic
  if comic.sell(amount.get()):
    message = random.choice(sell_messages)
    message_text.set(message)
    # in this case, action means the process of either restocking or selling comics 
    action_feedback.set("Success! Total of {:.0f} sold from {}".format(amount.get(), comic.name))
    total_comic += amount.get()
    
  else:
    action_feedback.set("Not enough comics in {} or not a valid amount".format(comic.name))

# Create the manage action(restock and sell) function
def manage_action():
  try:
    for comic in comic_list:
      if chosen_comic.get() == comic.name:
        if chosen_action.get() == "Restock":
            restock_comics(comic)
        else:
            sell_comics(comic)

    # Update the GUI
    update_stock()
    amount.set("")

  # Add an exception for text input
  except ValueError:
    action_feedback.set("Please enter a valid number")


# Set up Lists
comic_list = []
total_comic = 0
restock_messages = ["Well done, remember to always restock comics when we don't have enough to sell!", "Keep those comics coming!","Awesome! Make sure that you have more than or just the right amount of average daily comics sold so we don't run out."]
sell_messages = ["Think about how many comics we have left to sell, so that we can restock if needed.","Good job, it is a busy day!","Tomorrow is another day for selling comics and making more money!"]


# Create instances of the class
super_dude = Comic("Super Dude", 8, 100)
lizard_man = Comic("Lizard Man", 12, 100)
water_woman = Comic("Water Woman", 3, 100)
comic_names = create_name_list()

##################  GUI CODE  ######################
root = Tk()
root.title("Riley's Comics")

# Create the top frame
top_frame = ttk.LabelFrame(root, text="Stock Levels and Other Information")
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the message text variable
message_text = StringVar()
message_text.set("Welcome! You can sell comics to customers or use the restock tool to make sure we have enough comics to sell.")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250)
message_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create and set the comic details variable
comic_details = StringVar()

# Create the details label and pack it into the GUI
details_label = ttk.Label(top_frame, textvariable=comic_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the bottom frame
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create a label for the comic combobox
comic_label = ttk.Label(bottom_frame, text="Comic:")
comic_label.grid(row=3, column=0, padx=10, pady=3)

# Set up a variable and option list for the comic Combobox
chosen_comic = StringVar()
chosen_comic.set(comic_names[0])

# Create a Combobox to select the comic
comic_box = ttk.Combobox(bottom_frame, textvariable=chosen_comic, state="readonly")
comic_box['values'] = comic_names
comic_box.grid(row=3, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the action(restock and sell) Combobox
action_label = ttk.Label(bottom_frame, text="Restock or Sell:")
action_label.grid(row=4, column=0)

# Set up a variable and option list for the action Combobox
action_list = ["Restock", "Sell"]
chosen_action = StringVar()
chosen_action.set(action_list[0])

# Create the Combobox to select the action(restock or sell)
action_box = ttk.Combobox(bottom_frame, textvariable=chosen_action, state="readonly")
action_box['values'] = action_list
action_box.grid(row=4, column=1, padx=10, pady=3, sticky="WE")

# Create a label for the amount field and pack it into the GUI
amount_label = ttk.Label(bottom_frame, text="Amount:")
amount_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the amount
amount = DoubleVar()
amount.set("")

# Create an entry to type in amount
amount_entry = ttk.Entry(bottom_frame, textvariable=amount)
amount_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = ttk.Button(bottom_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create an action(restock or sell) feedback label
action_feedback = StringVar()
action_feedback_label = ttk.Label(bottom_frame, textvariable=action_feedback)
action_feedback_label.grid(row=7, column=0, columnspan=2)

# Run the mainloop
update_stock()
root.mainloop()
