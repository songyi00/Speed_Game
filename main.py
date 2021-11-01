from tkinter import *
import tkinter.font as tkFont

root = Tk()

root.title("Game")
root.geometry("600x300+100+100")
root.resizable

fontExample = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
# 레이블 생성
label = Label(root, text="Speed Game")

# 레이블을 화면에 배치
label.pack()

label.configure(font=fontExample)
root.mainloop()