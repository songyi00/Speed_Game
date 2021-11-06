import tkinter.font as tkFont
from tkinter import messagebox
import pandas as pd
import os
import random
from PIL import Image, ImageTk
import threading


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

        ImagePath = 'halloween.png'
        canv = tk.Canvas(self, width=600, height=500, bg='white')
        canv.pack(side='bottom')
        self.img = ImageTk.PhotoImage(Image.open(ImagePath).resize((600, 500), Image.ANTIALIAS))
        canv.create_image(0, 0, anchor="nw", image=self.img)

        labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        canv.create_text((600//2), (500//2)-40, fill = "white", text="Speed Game", font=labelFont)

        startBtnFont = tkFont.Font(family="Consolas", size=20)
        startBtn = tk.Button(canv, text="START", font=startBtnFont, foreground="yellow", background="black",
                             relief="ridge", borderwidth=5, highlightbackground="yellow",
                             activebackground="yellow", activeforeground="black",
                             command=lambda: master.switch_frame(CategoryPage))
        canv.create_window((600//2), (500//2) + 100, window=startBtn)

class CategoryPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        ImagePath = 'halloween.png'
        canv = tk.Canvas(self, width=600, height=500, bg='white')
        canv.pack(side='bottom')
        self.img = ImageTk.PhotoImage(Image.open(ImagePath).resize((600, 500), Image.ANTIALIAS))
        canv.create_image(0, 0, anchor="nw", image=self.img)

        labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        canv.create_text((600 // 2), (500 // 2) - 190, fill="white", text="Speed Game", font=labelFont)

        btnFont = tkFont.Font(family="Consolas", size=20)
        countryBtn = tk.Button(self, text="country", foreground="yellow",
                  width=15, height=1,
                  background="black", font=btnFont, relief="ridge",
                  borderwidth=5, highlightbackground="yellow",
                  activebackground="yellow", activeforeground="black",
                  command=lambda: master.switch_frame(CountryPage))
        canv.create_window((600 // 2), (500 // 2) - 100, window=countryBtn)

        prevBtn = tk.Button(self, text="preve page", foreground="yellow",
                  width=15, height=1,
                  background="black", font=btnFont, relief="ridge",
                  borderwidth=5, highlightbackground="yellow",
                  activebackground="yellow", activeforeground="black",
                  command=lambda: master.switch_frame(StartPage))
        canv.create_window((600 // 2), (500 // 2) - 10, window=prevBtn)

def passBtn_click(master):
    global pass_count
    pass_count = pass_count - 1
    if(pass_count < 0):
        print("패스 그만")
    master.switch_frame(CountryPage)

def checkBtn_click(master):
    master.switch_frame(CountryPage)

class CountryPage(tk.Frame):
    def __init__(self, master):
        global pass_count
        global df
        tk.Frame.__init__(self, master)

        labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        tk.Label(self, text="Country", font=labelFont).pack(side="top", fill="x")
        filename = random.choice(os.listdir("./images"))
        code = filename.split(".")[0]

        # 엑셀에 없는 이미지일 경우 예외처리
        while code.upper() not in df.index:
            filename = random.choice(os.listdir("./images"))
            code = filename.split(".")[0]

        countryPath = "./images/"+filename

        print(countryPath)
        print(df["country"][code.upper()])
        print(filename)

        canv = tk.Canvas(self, width=180, height=160, bg='white')
        canv.pack()
        self.img = ImageTk.PhotoImage(Image.open(countryPath))
        canv.create_image(30, 30, anchor="nw", image=self.img)

        labelFont = tkFont.Font(family="Arial", size=20, slant="italic")
        BtnFont = tkFont.Font(family="Consolas", size=15)

        tk.Label(self, text="answer",font=labelFont).pack()
        input_text = tk.Entry(self, width=30)
        input_text.pack(pady=10)

        check_btn = tk.Button(self, text="check",
                  width=10, height=1, font=BtnFont, foreground="yellow",
                  background="black", relief="ridge",
                  command=lambda: checkBtn_click(master))
        check_btn.pack(side="left", pady=20)
        pass_btn = tk.Button(self, text="pass: " +str(pass_count)+"/3",
                  width=10, height=1, font=BtnFont, foreground="yellow",
                  background="black", relief="ridge",
                  command=lambda : passBtn_click(master))
        pass_btn.pack(side="right", padx=5, pady=20)

        self.num = 180
        mins, secs = divmod(self.num, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        TimerFont = tkFont.Font(family="Arial", size=30, weight="bold", slant="italic")
        self.timer = tk.Label(self, text=timeformat, font=TimerFont)
        self.timer.pack(pady=20)
        self.threadctl = threading.Timer(interval=1, function=self.countdown, args=(1,))
        self.threadctl.start()

    def countdown(self, task):
        self.timer.pack_forget()
        self.num = self.num - 1
        mins, secs = divmod(self.num, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        TimerFont = tkFont.Font(family="Arial", size=30, weight="bold", slant="italic")
        self.timer = tk.Label(self, text=timeformat, font=TimerFont)
        self.timer.pack(pady=20)
        if (self.num >= 0):
            self.threadctl = threading.Timer(interval=1, function=self.countdown, args=(1,))
            self.threadctl.start()





class FinishPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ImagePath = 'halloween.png'
        canv = tk.Canvas(self, width=600, height=500, bg='white')
        canv.pack(side='bottom')
        self.img = ImageTk.PhotoImage(Image.open(ImagePath).resize((600, 500), Image.ANTIALIAS))
        canv.create_image(0, 0, anchor="nw", image=self.img)

        labelFont = tkFont.Font(family="Arial", size=40, weight="bold")
        canv.create_text((600 // 2), (500 // 2) - 100, fill="white", text="총점수", font=labelFont)
        canv.create_text((600 // 2), (500 // 2) - 70, fill="white", text="수고하셨습니다.", font=labelFont)


if __name__ == "__main__":
    pygame.init()
    mySound = pygame.mixer.Sound("SpeedGameBgm.mp3")
    mySound.play(-1)
    pass_count = 3

    df = pd.read_excel("./CountryCodeData.xlsx", index_col=0, names=["code", "country"])
    print(df["country"]["KR"])

    app = SampleApp()
    app.title("Speed Game")

    app.geometry('600x500+100+100')
    app.mainloop()
