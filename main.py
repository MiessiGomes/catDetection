from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch


# Use the model
model.train(data="config.yaml", epochs=10, patience = 100, batch = 16, device = 0, verbose = False)  # train the model
