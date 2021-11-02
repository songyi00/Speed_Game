import tkinter.font as tkFont
import pandas as pd
import os
import random
from PIL import Image, ImageTk

try:
    import Tkinter as tk
except:
    import tkinter as tk

import pygame

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        startBtnFont = tkFont.Font(family="Consolas", size=20)
        tk.Label(self, text="Speed Game", font=labelFont).pack(fill="x", pady=100)
        tk.Button(self, text="Start", foreground="red",
                  background="white", padx="100", font=startBtnFont, relief="ridge",
                  command=lambda: master.switch_frame(PageOne)).pack(pady=20)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #ImagePath = 'halloween.gif'
        #background_img = ImageTk.PhotoImage(Image.open(ImagePath).resize((600, 500), Image.ANTIALIAS))
        #canvas = tk.Canvas(self)
        #canvas.create_image(0, 0, image=background_img, anchor="nw")
        #canvas.place(x=0, y=0, relwidth=1, relheight=1)
        #canvas.create_text(300, 200, fill="white", text="TITLE")

        # 배경 img 넣기
        # ImagePath = 'halloween.png'
        # background_img = ImageTk.PhotoImage(Image.open(ImagePath).resize((5, 5), Image.ANTIALIAS))
        # background_label = tk.Label(self, image=background_img)
        # background_label.pack()
        # background_label.place(x=-50, y=-2)
        # frame = tk.Frame(self)
        # frame.place(anchor="center", relx=0.5, rely=0.5)

        labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        tk.Label(self, text="MENU", font=labelFont).pack(side="top", fill="x", pady=5)
        BtnFont = tkFont.Font(family="Consolas", size=20)
        tk.Button(self, text="Country", foreground="yellow",
                  width=15, height=1,
                  background="black", font=BtnFont, relief="ridge",
                  command=lambda: master.switch_frame(PageCountry)).pack(pady=20)
        tk.Button(self, text="preve page", foreground="yellow",
                  width=15, height=1,
                  background="black", font=BtnFont, relief="ridge",
                  command=lambda: master.switch_frame(StartPage)).pack(side="bottom")


class PageCountry(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        tk.Label(self, text="Country", font=labelFont).pack(side="top", fill="x", pady=5)
        filename = random.choice(os.listdir("./images"))
        code = filename.split(".")[0]
        path = "./images/"+filename
        ref = Image.open(path)
        photo = ImageTk.PhotoImage(file=path)
        image = tk.PhotoImage(file=path)
        tk.Label(self, image=photo).pack(pady=10)
        print(filename)


if __name__ == "__main__":
    pygame.init()
    mySound = pygame.mixer.Sound("SpeedGameBgm.mp3")
    mySound.play(-1)

    df = pd.read_excel("./CountryCodeData.xlsx", index_col=0, names=["code", "country"])
    print(df["country"]["KR"])

    app = SampleApp()
    # winsound.PlaySound("SpeedGameBgm.mp3", winsound.SND_NOSTOP)
    app.title("Speed Game")

    app.geometry('600x500+100+100')
    app.mainloop()

