# License_plate_detection
## RFB_Net object detection: [Github](https://github.com/ruinmessi/RFBNet)
## Models
* License_plate_detection weights [RFB_Net300] (https://drive.google.com/file/d/1-cBiSRdfEH4_-pJ7FU4nCajRhSARFZEO/view?usp=sharing)
## Datasets
* Dataset+target: (https://drive.google.com/drive/folders/1mkFeNGTMMDoullEbgbtle1nk-ft7PQLW?usp=sharing)
## Installation
- Install [PyTorch-0.4.0](http://pytorch.org/) by selecting your environment on the website and running the appropriate command.
- Clone this repository. This repository is mainly based on [ssd.pytorch](https://github.com/amdegroot/ssd.pytorch) and [Chainer-ssd](https://github.com/Hakuyume/chainer-ssd), a huge thank to them.
  * Note: We currently only support PyTorch-0.4.0 and Python 3+.
- Compile the nms and coco tools:
```Shell
./make.sh
```
*Note*: Check you GPU architecture support in utils/build.py, line 131. Default is:
``` 
'nvcc': ['-arch=sm_52',
```
- Then download the dataset by following the [instructions](#download-voc2007-trainval--test) below and install opencv. 
```Shell
conda install opencv
```
## Training 
- First download the fc-reduced [VGG-16](https://arxiv.org/abs/1409.1556) PyTorch base network weights at:    https://s3.amazonaws.com/amdegroot-models/vgg16_reducedfc.pth
or from our [BaiduYun Driver](https://pan.baidu.com/s/1jIP86jW) 
- MobileNet pre-trained basenet is ported from [MobileNet-Caffe](https://github.com/shicai/MobileNet-Caffe), which achieves slightly better accuracy rates than the original one reported in the [paper](https://arxiv.org/abs/1704.04861), weight file is available at: https://drive.google.com/open?id=13aZSApybBDjzfGIdqN1INBlPsddxCK14 or [BaiduYun Driver](https://pan.baidu.com/s/1dFKZhdv).

- By default, we assume you have downloaded the file in the `RFBNet/weights` dir:
```Shell
mkdir weights
cd weights
wget https://s3.amazonaws.com/amdegroot-models/vgg16_reducedfc.pth
```

- To train RFBNet using the train script simply specify the parameters listed in `train_RFB.py` as a flag or manually change them.
```Shell
python train_RFB.py -d ANPR -v RFB_vgg -s 300 
```
- Note:
  * -d: choose datasets, VOC, ANPR or COCO
  * -v: choose backbone version, RFB_VGG, RFB_E_VGG or RFB_mobile.
  * -s: image size, 300 or 512.
  * You can pick-up training from a checkpoint by specifying the path as one of the training parameters (again, see `train_RFB.py` for options)
  * If you want to reproduce the results in the paper, the VOC model should be trained about 240 epoches while the COCO version need 130 epoches.
