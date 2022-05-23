from tkinter import*
from PIL import ImageTk , Image
root=Tk()
root.title("")
root.geometry("800x800") #width x height
root.configure(bg = "white")
root.resizable(True, True)

frame1 = Frame(root,bg="white")
frame1.pack(pady=20)


canvas = Canvas(frame1, width= 265, height= 125)
img = Image.open(r"C:\Users\naiti\Desktop\a.jpg")
resized_image = img.resize((250,110), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

canvas.create_image(10,10, anchor=NW, image=new_image)
canvas.grid(row=8, column =0)

label_0=Label(frame1, text="Test our sentiment analyzer, below:", width=80, font=("bold",26),bg="white", fg='#0000FF')
label_0.grid(row=2, column=0,padx=10,pady=10)

label_1=Label(frame1, text="Test with your own text", width=26, font=("bold",20),bg="white", fg='black')
label_1.grid(row=3, column=0,padx=20,pady=20)

you_selected_textbox = Text(frame1,height = 20,width = 70)
you_selected_textbox["bg"] = "white"
you_selected_textbox.grid(row=4, column=0,padx=10,pady=10)

rock_button = Button(frame1, text = " Classify Text ",height = 3, width = 17)
rock_button.grid(row=6, column=0,padx=10,pady=10)
rock_button["bg"] = "#0000FF"

label_3=Label(frame1, text="Results", width=70, font=("bold",25),bg="white", fg='black')
label_3.grid(row=7, column=0,padx=10,pady=10)

root.mainloop()