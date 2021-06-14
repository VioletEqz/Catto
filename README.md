
  

# My little Catto can't be this cute !!!

  

Just a smol model to detect kawaii catto <3

  

## Requirements

  

**Python >= 3.8**

  

**Pytorch >= 1.8**

  

**YOLOv5**

  

Using a GPU is not required but is highly recommended.

  

*(Incase you use GPU, get CUDA 11.1 for maximum compatibility with Pytorch 1.8)*

## How to train ?

  

Start by cloning **YOLOv5** and installing the requirements.

```py
pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt
```

  

Get the **YoloV5s model** from here and put it in the same directory.

```
https://github.com/ultralytics/yolov5/releases
```

*(Any model works, but we recommend using YoloV5s)*

  

You can get the dataset we labelled here manually, or just let the code do it automatically.

```
https://github.com/VioletEqz/Catto/releases/download/Dataset/catset.zip
```

  

Then run the following to start training.

```py
#python train.py --img 320 --batch 15 --epochs 32 --data catset.yaml --worker 0 --weights yolov5s.pt
```

## Catto Model
Using transfer learning with YoloV5s model in our dataset, we have trained our model with the sole purpose of cat tracking. Both the model and the dataset can be found in the /release of the repository.
## That's it for nowi owo

Training line:

```py

python train.py --img 320  --batch 32  --epochs 100  --data catset.yaml --worker 0  --weights yolov5s.pt

```

Freezing line (replace in train.py):

```py

freeze =  ['model.%s.'  % x for x in  range(10)]

```

Test line:

```py

#Using Yolov5s model to test

python detect.py --weights yolov5s.pt --img 640  --conf 0.25  --source catset/images

#Using Catto model to test

python detect.py --weights yolov5s_cat.pt --img 320  --source catset/images

```
