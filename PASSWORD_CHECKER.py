from tkinter import *
from tkinter import messagebox


def password_check():
    s = str(key.get("1.0", "end-1c"))
    if(s == ""):
        messagebox.showerror("Error", "PLEASE ENTER A PASSWORD")
        exit()

    if(len(s)<12):
        messagebox.showerror("Error", "PASSWORD MUST HAVE AT LEAST 12 CHARACTERS LONG")
    elif any(i.isspace() for i in s):
        messagebox.showerror("Error", "PASSWORD MUST NOT CONTAIN A SPACE")
    elif any(i=="\n" for i in s):
        messagebox.showerror("Error", "PASSWORD MUST NOT CONTAIN A NEWLINE")
    elif not any(i.isdigit() for i in s):
        messagebox.showerror("Error", "PASSWORD MUST CONTAIN A DIGIT")
    elif not any(i.isupper() for i in s):
        messagebox.showerror("Error", "PASSWORD MUST CONTAIN AN UPPERCASE LETTER")
    elif not any(i.islower() for i in s):
        messagebox.showerror("Error", "PASSWORD MUST CONTAIN A LOWERCASE LETTER")
    elif not any(i in "!+%^@#$_&*" for i in s):
        messagebox.showerror("Error", "PASSWORD MUST CONTAIN A SPECIAL CHARACTER")
    else:
        messagebox.showinfo("SUCCESS", "STRONG PASSWORD")
        exit()



windows = Tk()
windows.title("PASSWORD COMPLEXITY ANALYSER")
windows.geometry("600x600")
windows.config(bg="#C45FFF")


frame = Frame(windows, bg="#2ac04f", highlightbackground="gray", relief="solid", bd=2)
frame.pack(padx=50, pady=50,expand=True)
Label(frame, text="🔑PASSWORD CHECKER", font=("Times New Roman", 24, "bold"),fg="#000000", bg="#f0f0f0", relief="ridge").pack(side="top")
Label(frame, text="ENTER A PASSWORD FOR CHECKING", font=("Times New Roman", 16),fg="#000000", bg="#f0f0f0",relief="ridge").pack(pady=(15,5))


key = Text(frame, height=5, width=20, font=("Times New Roman", 14),bd=2, relief="sunken")
key.pack(padx=30,pady=30,side="top",expand=True)

Check = Button(frame,text="Check",command=password_check,font=("Times New Roman", 14, "bold"),bd=2,relief="raised")
Check.pack(pady=12,padx=12,side="bottom",expand=True)

windows.mainloop()