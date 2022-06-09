from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method

    # Ask the user for their name and save it to a variable
    # name = simple dialog.askstring(title='Greeter', prompt="What is your name?")
    name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo(title='Greeter', message='hello '+name+'!')
    messagebox.showinfo(title='Greeter', message='how has your day been?')
    name = simpledialog.askstring(title='Greeter', prompt="how has your day been?")
    messagebox.showinfo(title='Greeter', message='mine has also been '+name+'!')
    # Print your message to the console using the print() function
    print('good morning')
    # Show an error message using messagebox.showerror()
    messagebox.showerror(title='Greeter', message='HeY! YOu arE reAlLy RaD!')
    name = simpledialog.askstring(title='Greeter', prompt="YoU aRe ReALLY raD!?")
    messagebox.showinfo(title='Greeter', message='I AgrEe!')
    messagebox.showerror(title='Greeter', message='w0uLd yoU Like tO l1vE?')
    name = simpledialog.askstring(title='Greeter', prompt="w0uLd yoU Like tO l1vE?")
    messagebox.showerror(title='Greeter', message='mE t0!1!')
    messagebox.showerror(title='Greeter', message='Go0byE!')
    # Run the window's .mainloop() method

    pass
