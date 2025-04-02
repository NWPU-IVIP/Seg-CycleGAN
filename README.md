# Seg-CycleGAN:SAR-to-optical image translation  guided by a downstream task

Paper link: [Seg-CycleGAN : SAR-to-optical image translation  guided by a downstream task](https://ieeexplore.ieee.org/abstract/document/10872937)

## Introduction
Optical remote sensing and synthetic aperture radar (SAR) remote sensing are crucial for earth observation, offering complementary capabilities. While optical sensors provide high-quality images, they are limited by weather and lighting conditions. In contrast, SAR sensors can operate effectively under adverse conditions. This letter proposes a generative adversarial network (GAN)-based SAR-to-optical image translation method named Seg-CycleGAN, designed to enhance the accuracy of ship target translation by leveraging semantic information from a pretrained semantic segmentation model. Our method utilizes the downstream task of ship target semantic segmentation to guide the training of the image translation network, improving the quality of output optical-styled images. The potential of foundation-model-annotated datasets in SAR-to-optical translation tasks is revealed. This work suggests broader research and applications for downstream-task-guided frameworks.

![image](https://github.com/NWPU-IVIP/Seg-CycleGAN-and-HRSID-DIOR/blob/main/figures/fig1.png)

This repository provides:

1. the official code implementation of Seg-CycleGAN.
2. the HRSID-DIOR dataset used in our research. 

## Dataset Download

The HRSID-DIOR Dataset is used to support SAR-to-Optical image translation for ship targets.

This dataset is composed of 2 parts:
1) DIOR-ship : 3202 samples containing ship targets from DIOR dataset further augmented and labeled with SAM.
2) HRSID subset: 1031 inshore images and corresponding ship segmentation labels are selected and cropped.

Download the dataset through [GoogleDrive](https://drive.google.com/drive/folders/1_1F_A7iUUEgOSgQ7qLMPFT32z6_GCxO4?usp=drive_link).

## Usage

### Dependencies
```
pip install -r requirements.txt
```
### Build Environment
```
conda env create -f environment.yml -n Seg-CycleGAN
```
### Evaluation
```
python sar2opt_eval.py
```
### Training
```
python train.py
```

## Citation

If you use our dataset, please cite our paper below.

```BibTeX
@ARTICLE{10872937,
  author={Zhang, Hannuo and Li, Huihui and Lin, Jiarui and Zhang, Yujie and Fan, Jianghua and Liu, Hang and Liu, Kun},
  journal={IEEE Geoscience and Remote Sensing Letters}, 
  title={Seg-CycleGAN: SAR-to-Optical Image Translation Guided by a Downstream Task}, 
  year={2025},
  volume={22},
  number={},
  pages={1-5},
  keywords={Marine vehicles;Translation;Optical imaging;Optical sensors;Semantic segmentation;Training;Generators;Adaptive optics;Optical fiber networks;Radar polarimetry;Cycle-consistency;downstream-task-guided framework;semantic segmentation synthetic aperture radar (SAR)-to-optical image translation},
  doi={10.1109/LGRS.2025.3538868}}
```
