import tkinter.font as tkFont

try:
    import Tkinter as tk
except:
    import tkinter as tk


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
        tk.Label(self, text="Speed Game", font=labelFont).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Start",foreground="red",
                  background="white",padx="100",font=startBtnFont,relief="ridge",
                  command=lambda: master.switch_frame(PageOne)).pack()
        

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
        tk.Label(self, text="MENU", font=labelFont).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.geometry('600x500+100+100')
    app.mainloop()