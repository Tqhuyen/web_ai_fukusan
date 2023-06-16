from ultralytics import YOLO

def predict(file_dir):
    # Load a pretrained YOLO model (recommended for training)
    model = YOLO('yolov8n.pt')
    # Perform object detection on an image using the model
    results = model.predict(file_dir, save=True, imgsz=320, conf=0.5, device="cpu")
    return results
# res = predict("E:\Learn\web_ai\static\data\WIN_20230307_00_02_48_Pro.jpg")
# print(res)
