from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
    
    # Make a new window variable, window = Tk()
window = Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw(
    # 1. Ask the user if they know how to write code.
code = simpledialog.askstring(title='Question', prompt='Can you write code? (yes or no)')
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
if code == 'yes':
    messagebox.showinfo(title='YAY!', message='Then you will rule the world!')
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
else:
    messagebox.showerror(title='ERROR', message='Then you should sign up for classes at the League!')

    # Run the window's .mainloop() method
