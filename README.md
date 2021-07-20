
# Catto
Just a smol model to detect kawaii catto <3
This repository contains mostly the hyperparameters and configurations which was tinkered to train a Catto model on YoloV5. We also included an modified version of `detect.py` to implements [image segmentation](https://arxiv.org/abs/1805.09512) before detection.

## Methodology
### Data source
Most of the data was crawled using [petfinder API](https://www.petfinder.com/developers/v2/docs/), which are grouped then by IDs. We filtered only cats with more than 2 images and labelled them by hand.

ID818   | ID5481 |ID
------------|------------|----------
||

We also crawled data from the COCO 2017 Dataset using their provided [API](https://cocodataset.org/#download), filtering only cat images. But since the label was in a different format, we had to convert them back to Yolo format.
### YoloV5 architecture 
The model's architecture details can be found here: [Link](https://docs.google.com/document/d/1hW2rTwayBT0Nyr-hxEWSqHnjyVp5n6dZHW2cMy9vjmE/edit)\
*(Note: as YoloV5 are still in-development, there might be some changes in the future involving the architecture. The document is only accurate as of the publish date)* 
### Future improvement
From what we observed, here are some factors that can be improved for better results:
- **Data**: More data is always good for training the model, but we must also take note that the data used is of good quality and accurate.
- **Model**: For our case, we chose YoloV5s as our base model to train on because speed and movability are of greater priority. Should one want better accuracy, deeper model is recommended.
- **Hyperparameters**: While we have found a rather good hyperparameters on YoloV5s, there are still rooms for improvement, especially on future model or bigger model.

## Usage
### Training
A detailed guide on training can be found here:
[Guide](https://colab.research.google.com/drive/1vdv23_4YaU5YVBhJFYoMnGe_7fMaOyGo?usp=sharing)

### Inference
To perform inference, it is recommended to use `detect.py` included in the YoloV5 repository. However, if that does not suite you, Pytorch Hub is a good alternative.
[Guide](https://colab.research.google.com/drive/1YQD-P_Q62utkuD-blboejuqKrehXLKEG?usp=sharing)

## Pretrained models
|          Model        | mAP_val| mAP_test| Download |
|:---------------------:|:------:|:-------:|:--------:|
|  Catto			    |        |         |          |
| CocoCat			    |        |         |          |
