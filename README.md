# Seg-CycleGAN
Paper link: [Seg-CycleGAN : SAR-to-optical image translation  guided by a downstream task](https://ieeexplore.ieee.org/abstract/document/10872937)

This repository provides:

1. the official code implementation of Seg-CycleGAN.
2. the HRSID-DIOR dataset used in our research. 

- Use `train.py` to start training. 

- The Seg-CycleGAN model is located in the `models/cycle_gan_model.py`.

## HRSID-DIOR Dataset

The HRSID-DIOR Dataset is used to support SAR-to-Optical image translation for ship targets.

This dataset is composed of 2 parts:
1) DIOR-ship : 3202 samples containing ship targets from DIOR dataset further augmented and labeled with SAM.
2) HRSID subset: 1031 inshore images and corresponding ship segmentation labels are selected and cropped.

## Download 

Download the dataset through [GoogleDrive](https://drive.google.com/drive/folders/1_1F_A7iUUEgOSgQ7qLMPFT32z6_GCxO4?usp=drive_link).



## Citation

If you use our dataset, please cite our paper below.

```BibTeX
@misc{zhang2024segcyclegansartoopticalimage,
      title={Seg-CycleGAN : SAR-to-optical image translation guided by a downstream task}, 
      author={Hannuo Zhang and Huihui Li and Jiarui Lin and Yujie Zhang and Jianghua Fan and Hang Liu},
      year={2024},
      eprint={2408.05777},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2408.05777}, 
}
```
