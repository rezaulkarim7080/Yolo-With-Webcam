from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model("images/1.jpg",show=True)