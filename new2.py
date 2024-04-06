from tkinter import*  
screen = Tk()  
screen.geometry('500x500')  
screen.title("Registration Form") 
screen["background"]="#96DED1"

  
lable = Label(screen, text="Registration form", bg ="#96DED1",width=20,font=("bold", 20)) .pack(padx=90 , pady= 50) 
  
  
lable1 = Label(screen, text="Name", bg ="#96DED1", width=20,font=("bold", 10)) .pack(anchor=W) 
entry1 = Entry(screen).place(x=180 , y=140)

lable2 = Label(screen, text="Moblie no", bg ="#96DED1", width=20,font=("bold", 10)) .pack(anchor=W , padx=10, pady=19) 
entry2 = Entry(screen).place(x=180 , y=180)

lable3 = Label(screen, text="Address", bg ="#96DED1", width=20,font=("bold", 10)) .pack(anchor=W , padx=6, pady=1) 
entry3 = Entry(screen).place(x=180 , y=220)

lable4 = Label(screen, text="Email", bg ="#96DED1", width=20,font=("bold", 10)) .pack(anchor=W , padx=1 , pady=14) 
entry4 = Entry(screen).place(x=180 , y=260)

lable5 = Label(screen, text="Gender", bg ="#96DED1" ,width=20,font=("bold", 10)) .pack(anchor=W , padx=3 , pady=4) 
Radiobutton(screen, text="Male",  value=1).place(x=180,y=300)  
Radiobutton(screen, text="Female", value=2).place(x=250,y=300)  

Button(screen, text='Submit',width=20,bg='black',fg='white').place(x=160,y=380)  
  

screen.mainloop()  
























  
# labl_2 = Label(screen, text="Email",width=20,font=("bold", 10))  
# labl_2.place(x=68,y=180)  
  
# entry_02 = Entry(screen)  
# entry_02.place(x=240,y=180)  
  
# labl_3 = Label(screen, text="Gender",width=20,font=("bold", 10))  
# labl_3.place(x=70,y=230)  
# # varblbl = IntVarblbl()  
# Radiobutton(screen, text="Male",padx = 5,  value=1).place(x=235,y=230)  
# Radiobutton(screen, text="Female",padx = 20,  value=2).place(x=290,y=230)  
  
# labl_4 = Label(screen, text="Age:",width=20,font=("bold", 10))  
# labl_4.place(x=70,y=280)  
  
  
# entry_02 = Entry(screen)  
# entry_02.place(x=240,y=280)  
  
# Button(screen, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)  
# # it will be used for displaying the registration form onto the window  
# screen.mainloop()  
# print("Registration form is created seccussfully...")