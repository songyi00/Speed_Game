from tkinter import *
import tkinter.font as tkFont

root = Tk()

root.title("Speed Game")
root.geometry("600x400+100+100")
root.resizable

labelFont = tkFont.Font(family="Arial", size=40, weight="bold", slant="italic")
startBtnFont = tkFont.Font(family="Consolas", size=20)

# 레이블 생성 + 옵션 추가
label = Label(root, text="Speed Game")
label.configure(font=labelFont)
label.configure(background="white")
# 레이블을 화면에 배치
label.pack()

# start 버튼 추가 + 옵션 추가
startBtn = Button(root, text="start")   # 버튼 text
startBtn.configure(foreground="red")    # 버튼 문자열 색상
startBtn.configure(background="white")  # 버튼 background 색상
startBtn.configure(padx="100")          # 버튼 가로 padding
startBtn.configure(font=startBtnFont)   # 버튼 폰트
startBtn.configure(relief="ridge")

startBtn.pack()  # 화면에 배치

root.configure(background="white")
root.mainloop()
