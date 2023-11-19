import cv2
import threading
import subprocess
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

running = False
yolo_process = None  # YOLO 감지 프로세스 변수

def run():
    global running
    cap = cv2.VideoCapture(0)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    label.resize(width, height)
    while running:
        ret, img = cap.read()
        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, c = img.shape
            qImg = QtGui.QImage(img.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(qImg)
            label.setPixmap(pixmap)
        else:
            QtWidgets.QMessageBox.about(win, "Error", "Cannot read frame.")
            print("cannot read frame.")
            break
    cap.release()
    print("Thread end.")

def stop():
    global running, yolo_process
    running = False
    if yolo_process:
        yolo_process.kill()
        yolo_process = None
    print("stopped..")

def start():
    global running, yolo_process
    running = True
    th = threading.Thread(target=run)
    th.start()
    
    # YOLO 감지 스크립트 실행
    yolo_script_path = 'C:/yolov5-master/yolov5-master/detect.py'  # YOLO 감지 스크립트의 경로
    yolo_process = subprocess.Popen(['python', yolo_script_path, '--weights', 'C:\yolov5-master\yolov5-master\runs\train\fallenperson_yolov5s_results2\weights\best.pt', '--img', '640', '--conf', ' 0.5','--source', '0'])
    
    print("started..")

def onExit():
    print("exit")
    stop()

app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel()
btn_start = QtWidgets.QPushButton("Camera On")
btn_stop = QtWidgets.QPushButton("Camera Off")
vbox.addWidget(label)
vbox.addWidget(btn_start)
vbox.addWidget(btn_stop)
win.setLayout(vbox)
win.show()

btn_start.clicked.connect(start)
btn_stop.clicked.connect(stop)
app.aboutToQuit.connect(onExit)

sys.exit(app.exec_())