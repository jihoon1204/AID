import tkinter as tk
from tkinter import Tk
import cv2
from PIL import Image, ImageTk
import torch
import time
import threading

root = Tk()
root.bind("<Escape>", lambda e: root.quit())
root.geometry('1500x900')
root.title('YOLOv5 Object detection')

model = torch.hub.load('ultralytics/yolov5', 'custom', path = 'C:/yolov5-master/yolov5-master/runs/train/fallenperson_yolov5s_results2/weights/best.pt')

a1 = 0
start1 = 0
end1 = 0

a2 = 0
start2 = 0
end2 = 0

def main_page1():

    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('http://172.17.135.92:8080/video')

    def video_play():

        global a1
        global start1
        global end1
        global video_frame1

        ret, frame = cap.read()
        if not ret :
            cap.release()
            return

        results = model(frame)

        class_name = ''
        for *xyxy, conf, cls in results.xyxy[0]:
            if conf>0.7:
                label = f'{results.names[int(cls)]} {conf:.2f}'
                cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (255,0,0), 2)
                cv2.putText(frame, label, (int(xyxy[0]), int(xyxy[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
                if results.names[int(cls)] == 'Fall':
                    class_name = results.names[int(cls)]

        if len(results.xyxy[0]) == 0 :
            a1=0
            start1=0
            end1=0
            video_frame1.config(bg='white')
        else :
            if class_name =='Fall':
                if a1 == 0:
                    start1 = time.time()
                    a1 = 1
                else :
                    end1 = time.time()
                    
                if 10<=end1-start1 :
                    video_frame1.config(bg='red')
            else :
                a1=0
                start1=0
                end1=0
                video_frame1.config(bg='white')

        video = frame
        cv2img = cv2.cvtColor(video, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2img)
        imgtk = ImageTk.PhotoImage(image=img)

        video_label1.imgtk = imgtk
        video_label1.configure(image=imgtk)

        video_label1.after(1, video_play)

    video_play()
def main_page2():

    cap = cv2.VideoCapture('http://172.17.239.46:8080/video')
    #cap = cv2.VideoCapture('http://172.17.135.92:8080/video')

    def video_play():

        global a2
        global start2
        global end2
        global video_frame2

        ret, frame = cap.read()
        if not ret :
            cap.release()
            return

        results = model(frame)

        class_name = ''
        for *xyxy, conf, cls in results.xyxy[0]:
            if conf>0.7:
                label = f'{results.names[int(cls)]} {conf:.2f}'
                cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (255,0,0), 2)
                cv2.putText(frame, label, (int(xyxy[0]), int(xyxy[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
                if results.names[int(cls)] == 'Fall':
                    class_name = results.names[int(cls)]

        if len(results.xyxy[0]) == 0 :
            a2=0
            start2=0
            end2=0
            video_frame2.config(bg='white')
        else :
            if class_name =='Fall':
                if a2 == 0:
                    start2 = time.time()
                    a2 = 1
                else :
                    end2 = time.time()
                    
                if 10<=end2-start2 :
                    video_frame2.config(bg='red')
            else :
                a2=0
                start2=0
                end2=0
                video_frame2.config(bg='white')

        video = frame
        cv2img = cv2.cvtColor(video, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2img)
        imgtk = ImageTk.PhotoImage(image=img)

        video_label2.imgtk = imgtk
        video_label2.configure(image=imgtk)

        video_label2.after(1, video_play)

    video_play()

Title_label = tk.Label(root, text = '실시간 CCTV')
Title_label.place(x=470, y=10)

video_frame1 = tk.Frame(root, bg='white', width=500, height=400)
video_frame1.place(x=10, y=40)

video_frame2 = tk.Frame(root, bg='white', width=500, height=400)
video_frame2.place(x=510, y=40)

video_frame3 = tk.Frame(root, bg='pink', width=500, height=400)
video_frame3.place(x=10, y=440)

video_frame4 = tk.Frame(root, bg='skyblue', width=500, height=400)
video_frame4.place(x=510, y=440)

video_label1 = tk.Label(video_frame1, bg='white', width=480, height=380)
video_label1.place(x=8,y=10)
video_label2 = tk.Label(video_frame2, bg='white', width=480, height=380)
video_label2.place(x=8,y=10)
video_label3 = tk.Label(video_frame3, bg='white', width=68, height=25)
video_label3.place(x=8,y=10)
video_label4 = tk.Label(video_frame4, bg='white', width=68, height=25)
video_label4.place(x=8,y=10)

th1 = threading.Thread(target=main_page1)
#th2 = threading.Thread(target=main_page2)

th1.start()
#th2.start()

txt_frame = tk.Frame(root, bg='white', width=400, height=800)
txt_frame.place(x=1020, y=40)

root.mainloop()