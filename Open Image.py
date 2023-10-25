from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root=Tk()
root.title("Open Image")
root.geometry("600x600")
root.configure(background="light blue")

label2 = Label(root, text="Created by: Anwesha Das", highlightthickness = "2", bg = "teal")
label2.place(relx=0.5,rely=1,anchor=CENTER)

label1 = Label(root, highlightthickness = "2", bg = "white")
label1.place(relx=0.5,rely=0.4,anchor=CENTER)

img_path =""

def Open_Image():
    global img_path
    img_path = filedialog.askopenfilename(title="Open Images",filetypes=[("Image Files", "*.jpg;","*.gif;" ,"*.png;", "*.jpeg;")])
    print(img_path)
    img2 = ImageTk.PhotoImage(file = img_path)
    label1["image"]=img
    img.close()
    
def Rotate_Image():
    global img_path
    im=Image.open(img_path)
    rotated_img = im.rotate(180)
    img=ImageTk.PhotoImage(rotated_img)
    img.close()
    
btn = Button(root, text="Open Image", command=Open_Image, font=("Bell MT",10,"bold"), borderwidth=1, relief=SOLID, bg="white")
btn.place(relx=0.5,rely=0.1,anchor=CENTER)

btn1 = Button(root, text="Rotate Image", command=Rotate_Image, font=("Bell MT",10,"bold"), borderwidth=1, relief=SOLID, bg="white")
btn1.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()