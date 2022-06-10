from tkinter import messagebox, simpledialog, Tk

    # Create an if-main code block, *hint, type main then ctrl+space to auto-complete

    # Make a new window variable, window = Tk()
window = Tk()
    # Hide the window using the window's .withdraw() method
window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
question = simpledialog.askstring(title='Question', prompt="What is 5*5?")
    #      // 3.  Use an if statement to check if their answer is correct
if question=='25':
    messagebox.showinfo(title='Good Job', message='Your not a total moron!')
    score += 1
    #      // 4.  if the user's answer was correct, add one to their score
else:
    messagebox.showinfo(title='STUPID!', message='HOW ARE YOU SO DUMB! GO BACK TO KINDERGARTEN!!')
    score -= 0
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
question = simpledialog.askstring(title='Question', prompt="What is 2+2")

if question=='4':
    messagebox.showinfo(title='Good Job', message='You are maybe kinda not dumb!')
    score += 1
    #      // Option: Subtract a point from their score for a wrong answer
else:
    messagebox.showinfo(title='STUPID!', message='I fail to understand your stupidity!')
    score -= 0

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
question = simpledialog.askstring(title='Question', prompt="What is the pi, writen in full. NO SIMPLIFYING!")

if question=='no':
    messagebox.showinfo(title='Good Job', message='You got lucky. But I am counting it.')
    score += 1
else:
    messagebox.showinfo(title='STUPID!', message='You are stupid. But that was impossible, there is an answer though.')
    score -= 0
    # Run the window's .mainloop() method
messagebox.showinfo(title='your score', message='your very low score is ' + str(score))
