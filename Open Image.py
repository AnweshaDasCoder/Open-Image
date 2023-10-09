from tkinter import *
from tkinter import filedialog

root=Tk()
root.title("Open Image")
root.geometry("600x600")
root.configure(background="light blue")

label1 = Label(root, highlightthickness = "2", bg = "white")
label1.place(relx=0.05,rely=0.03,anchor=CENTER)

img_path =""

def Open_Image():
    global img_path
    img_path = filedialog.askopenfilename(title=" Open Images",filetypes=[("Image Files", "*.jpg;","*.gif;" ,"*.png;", "*.jpeg;")])
    print(img_path)
    img2 = ImageTk.PhotoImage(file = img_path)
    label1["image"]=img
    img.close()
    
btn = Button(root, text="Open Image", command=Open_Image, font=("Bell MT",10,"bold"), borderwidth=2, relief=SOLID, bordercolor="black", bg="white")
btn.place(relx=0.05,rely=0.09,anchor=CENTER)

root.mainloop()