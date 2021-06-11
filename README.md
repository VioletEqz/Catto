
# My little Catto can't be this cute !!!

Just a smol model to detect kawaii catto <3

## Requirements

**Python >= 3.8**

**Pytorch >= 1.8**

**YOLOv5**

Using a GPU is not required but is highly recommended.

*(Incase you use GPU, get CUDA 11.1 for maximum compatibility with Pytorch 1.8)*
## Getting Started

Start by cloning **YOLOv5** and installing the requirements.\
```pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt```

Get the **YoloV5s model** from here and put it in the same directory. \
```https://github.com/ultralytics/yolov5/releases```
*(Any model works, but we recommend using YoloV5s)*\

You can get the dataset we labelled here manually, or just let the code do it automatically.\
```https://github.com/VioletEqz/Catto/releases/download/Dataset/catset.zip```

Then run the following to start training.\
```#python train.py --img 320 --batch 15 --epochs 6 --data catset.yaml --worker 0 --weights yolov5s.pt```
## That's it for nowi owo
