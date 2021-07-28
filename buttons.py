from tkinter import *
from PIL import Image,ImageTk
import social
from detect_mask_video import mask

class button:
    def __init__(self):

        self.rt=Tk()
        self.rt.title("COVID-19 E-Surveillance")
        self.rt.config(background="#ccffcc")    #FFFFCC       #94b8b8
        self.rt.geometry("1145x500+160+100")

        self.l1=Label(self.rt)
        self.l1.place(relx=0.25, rely=0.0, height=81, width=604)
        img1=ImageTk.PhotoImage(Image.open("bank_images/hebutton.png"))
        self.l1.configure(image=img1)
        self.l1.configure(background="#ccffcc")

        self.l2=Label(self.rt)
        self.l2.place(relx=0.22, rely=0.32, height=200, width=250)
        limg=ImageTk.PhotoImage(Image.open("bank_images/2.png"))
        self.l2.configure(image=limg)

        self.l21 = Label(self.rt)
        self.l21.place(relx=0.580, rely=0.32, height=200, width=250)
        limg1 = ImageTk.PhotoImage(Image.open("bank_images/Face Mask.png"))
        self.l21.configure(image=limg1)

        self.but=Button(self.rt,command=self.click)
        self.but.place(relx=0.24, rely=0.75, height=73, width=200)
        img2 = ImageTk.PhotoImage(Image.open("bank_images/wm.gif"))
        self.but.configure(image=img2)

        self.but2 = Button(self.rt, command=mask)
        self.but2.place(relx=0.60, rely=0.75, height=73, width=200)
        img3 = ImageTk.PhotoImage(Image.open("bank_images/wm.gif"))
        self.but2.configure(image=img3)
        self.rt.mainloop()

    def click(self):
        self.rt.destroy()
        lo=social.sociall()
        
#     def clicked(self):
#         self.rt.destroy()
#         mask()