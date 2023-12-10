import tkinter as tk
from tkinter import Tk
from object_detect import *
from board import BoardApp
import webbrowser

source = "http://172.17.156.226:8080/video"

root = Tk()
root.geometry('1400x900')
root.title('YOLOv5 Object detection')

main_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

Title_label = tk.Label(main_frame, text = '실시간 CCTV')
Title_label.place(x=470, y=10)

video_frame1 = tk.Frame(main_frame, bg='white', width=1000, height=800, bd=1, relief=tk.SOLID)
video_frame1.place(x=10, y=40)

video_label1 = tk.Label(video_frame1, bg='white', width=960, height=720)
video_label1.place(x=16,y=20)

txt_frame = tk.Frame(main_frame, bg='white', width=400, height=800, bd=1, relief=tk.SOLID)
txt_frame.place(x=1020, y=40)

board = BoardApp(frame=txt_frame, width=40, height=60)

vb1 = VideoBox(address='경남 진주시 진주대로 501 경상국립대학교 공과대학 407동 202호', frame=video_frame1, label=video_label1, source=source, board=board)
video_label1.bind("<Button-1>", lambda e: webbrowser.open(vb1.get_source()))

vb1.main_page()

root.mainloop()