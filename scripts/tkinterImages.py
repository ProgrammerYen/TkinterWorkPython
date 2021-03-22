from tkinter import *
from PIL import ImageTk, Image

# Creating root widget.
root = Tk()
root.title("Image Viewer")
root.iconbitmap("logos/picture_photo_image_icon_131252.ico")
root.configure(bg="#000")
root.resizable(False, False)

img1 = ImageTk.PhotoImage(Image.open("images/038.jpg").resize((600,850)))
img2 = ImageTk.PhotoImage(Image.open("images/066.jpg").resize((600,850)))
img3 = ImageTk.PhotoImage(Image.open("images/136.jpg").resize((600,850)))
img4 = ImageTk.PhotoImage(Image.open("images/204.jpg").resize((600,850)))
img5 = ImageTk.PhotoImage(Image.open("images/342.jpg").resize((600,850)))
img6 = ImageTk.PhotoImage(Image.open("images/462.jpg").resize((700,500)))
img7 = ImageTk.PhotoImage(Image.open("images/TriptoSriLana2011Jan 114.jpg").resize((700,500)))

imgs = [img1, img2, img3, img4, img5, img6, img7]

status = Label(root, text="Image 1 of " + str(len(imgs)), bg="#000", fg="#FFF", font=(None, 18))

labelImg = Label(root, image=img1)
labelImg.grid(row=0, column=0, columnspan=3)

def Forward(image):
    global labelImg
    global buttonBack
    global buttonForward
    
    labelImg.grid_forget()
    labelImg = Label(root, image=imgs[image-1])
    labelImg.grid(row=0, column=0, columnspan=3)
    status = Label(root, text="Image " + str(image) + " of " + str(len(imgs)), bg="#000", fg="#FFF", font=(None, 18))
    
    buttonForward = Button(root, text=">", command=lambda: Forward(image+1), font=(None,25), bd=0, bg="#000", fg="#fff", activebackground="#000", activeforeground="#fff")
    buttonBack = Button(root, text="<", command=lambda: Backward(image), font=(None,25), bd=0, bg="#000", fg="#fff", activebackground="#000", activeforeground="#fff")
    
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3)
    
    if image == len(imgs):
        buttonForward = Button(root, text=">", font=(None,25), bd=0, bg="#000", fg="#fff", activebackground="#000", activeforeground="#fff")
        buttonForward.grid(row=1, column=2)
        
def Backward(image):
    global labelImg
    global buttonBack
    global buttonForward
    
    labelImg.grid_forget()
    labelImg = Label(root, image=imgs[image-1])
    labelImg.grid(row=0, column=0, columnspan=3)
    
    buttonForward = Button(root, text=">", command=lambda: Forward(image), font=(None,25), bd=0, bg="#000", fg="#fff", activebackground="#000", activeforeground="#fff")
    buttonBack = Button(root, text="<", command=lambda: Backward(image-1), font=(None,25), bd=0, bg="#000", fg="#fff", activebackground="#000", activeforeground="#fff")
    status = Label(root, text="Image " + str(image) + " of " + str(len(imgs)), bg="#000", fg="#FFF", font=(None, 18))
    
    buttonBack.grid(row=1, column=0)
    buttonForward.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3)
    
    if image == 1:
        status = Label(root, text="Image " + str(image) + " of " + str(len(imgs)), bg="#000", fg="#FFF", font=(None, 18))
        buttonBackward = Button(root, text="<", font=(None,25), bd=0, bg="#000", fg="#fff", activebackground="#000", activeforeground="#fff")
        buttonBackward.grid(row=1, column=0)
        status.grid(row=2, column=0, columnspan=3)
    
buttonBack = Button(root, text="<", command=lambda: Backward(1), font=(None,25), bd=0, bg="#000", fg="#fff", activebackground="#000", activeforeground="#fff")
buttonExit = Button(root, text="Click Here to Exit Image Viewer", command=root.quit, font=(None,20), bd=0, bg="#000", fg="#fff", activebackground="#000", activeforeground="#fff")
buttonForward = Button(root, text=">", command=lambda: Forward(2), font=(None,25), bd=0, bg="#000", fg="#fff", activebackground="#000", activeforeground="#fff")

buttonBack.grid(row=1, column=0)
buttonExit.grid(row=1, column=1, pady=10)
buttonForward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3)

root.mainloop()
