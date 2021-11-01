import tkinter.font as tkFont
import pandas as pd

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
