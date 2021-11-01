from tkinter import *
import tkinter.font as tkFont

root = Tk()

root.title("Game")
root.geometry("600x300+100+100")
root.resizable

labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
startBtnFont = tkFont.Font()

# 레이블 생성 + 옵션 추가
label = Label(root, text="Speed Game")
label.configure(font=labelFont)
label.configure(background="white")
# 레이블을 화면에 배치
label.pack()

# start 버튼 추가 + 옵션 추가
startBtn = Button(root, text="start")
startBtn.configure(foreground="red")
startBtn.configure(background="white")
startBtn.configure(padx="50")
startBtn.configure(font=startBtnFont)
startBtn.pack()  # 화면에 배치

root.configure(background="white")
root.mainloop()
