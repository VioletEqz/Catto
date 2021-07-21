
  

  

# Catto

  

**Just a smol model to detect kawaii catto <3**

  

This repository contains mostly the hyperparameters and configurations which was tinkered to train a Catto model on YoloV5. We also included an modified version of `detect.py` to implements [image segmentation](https://arxiv.org/abs/1805.09512) before detection.

  

  

## Methodology

  

### Data source

  

Most of the data was crawled using **[petfinder API](https://www.petfinder.com/developers/v2/docs/)**, which are grouped then by **IDs**. We filtered only cats with more than 2 images and labelled them by hand.

  

**ID** | 52332561 | 52419810 | 51939580|
-------|------------|------------|----------|
**Example**|![52332561](./docs/52332561.png)|![52419810](./docs/52419810.png)|![51939580](./docs/51939580.png)|

  

  

We also crawled data from the **COCO 2017 Dataset** using their provided [API](https://cocodataset.org/#download), filtering only cat images. But since the label was in a different format, we had converted them back to Yolo format.

|**Example 1**| **Example 2** | **Example 3**|
|---------|-----------|-----------|
|![Example1](./docs/Example1.jpg)|![Example2](./docs/Example2.jpg)|![Example3](./docs/Example3.jpg)|

  

A total of 4114 cat images were extracted from **COCO 2017 Dataset** for training process.

  

### YoloV5 architecture

  

The model's architecture details can be found here: [Doc](https://docs.google.com/document/d/1hW2rTwayBT0Nyr-hxEWSqHnjyVp5n6dZHW2cMy9vjmE/edit)

  

*(Note: as **YoloV5** are still in-development, there might be some changes in the future involving the architecture. The document is only accurate as of the publish date)*

  

### Future improvement

  

From what we observed, here are some factors that can be improved for better results:

  

-  **Data**: More data is always good for training the model, but we must also take note that the data used is of good quality and accurate.

  

-  **Model**: For our case, we chose YoloV5s as our base model to train on because speed and movability are of greater priority. Should one want better accuracy, deeper model is recommended.

  

-  **Hyperparameters**: While we have found a rather good hyperparameters on YoloV5s, there are still rooms for improvement, especially on future model or bigger model.

  

  

## Usage

  

### Training

  

A detailed guide on training can be found here:

  

[Guide](https://colab.research.google.com/drive/1vdv23_4YaU5YVBhJFYoMnGe_7fMaOyGo?usp=sharing)

  

### Inference

  

To perform inference, it is recommended to use `detect.py` included in the YoloV5 repository. However, if that does not suite you, **Pytorch Hub** is a good alternative.

  

[Guide](https://colab.research.google.com/drive/1YQD-P_Q62utkuD-blboejuqKrehXLKEG?usp=sharing)

  
## Result
Running detection on validation set returned very promising results after training **Catto** model for 200 epochs:
![Val1](./docs/Val1.jpg)
![Val2](./docs/Val2.jpg)
With more data, the result can definitely improve even further. One can further expand the dataset simply by crawling from the ever-expanding Petfinder source, or extract from other datasets like **VOC**,...
## Pretrained models

  

| Model | mAP<sup>val<br>0.5:0.95| mAP<sup>val<br>0.5 | mAP<sup>test<br>0.5:0.95| mAP<sup>test<br>0.5| Download |
|:---------------------:|:------:|:-------:|:--------:|:--------: |:------: |
| **Catto** | 0.704 | 0.953 | 0.703 | 0.954 | [Link](https://github.com/VioletEqz/Catto/releases/download/1.0/Catto.pt) |
| CocoCat | 0.677 | 0.922 | 0.674 | 0.931 | [Link](https://github.com/VioletEqz/Catto/releases/download/1.0/CocoCat.pt) |


