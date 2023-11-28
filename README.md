# AID
wlgns1204@gmail.com / 0221dmstn@naver.com / wdk6936@gnu.ac.kr / gimsh8887@gnu.ac.kr

python train.py --img 640 --batch 16 --epochs 200 --data fallenperson\data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name fall

python .\detect.py --weight .\runs\train\fall\weights\best.pt --img 640 --confpython train.py --img 640 --conf 0.9 --source 0 
