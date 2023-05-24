import tkinter as tk

url = 'https://alexismonroy.com/data/'

jpg = 'alexis.jpg'

pic_url = url + '/' + jpg

print(pic_url)

# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title('Greeting')

# Create a label to display the prompt message
prompt_label = tk.Label(window, text='What is your name?')
prompt_label.pack()

# Create an entry field for the user to enter their name
name_entry = tk.Entry(window)
name_entry.pack()

# Create a function to handle the button click event
def greet():
    name = name_entry.get()
    greeting_label.config(text='Hello, ' + name + '!')

# Create a button to submit the user's name
submit_button = tk.Button(window, text='Submit', command=greet)
submit_button.pack()

# Create a label to display the greeting message
greeting_label = tk.Label(window, text='')
greeting_label.pack()

# Start the Tkinter event loop
window.mainloop()