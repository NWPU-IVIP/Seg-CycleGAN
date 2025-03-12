import os
from data.base_dataset import BaseDataset, get_transform
from data.image_folder import make_dataset
from PIL import Image
import random
import cv2 as cv
import torch


class EvaluationDataset(BaseDataset):
    """
    用于转换模型效果测试
    """
    def __init__(self, opt):
        """Initialize this dataset class.

        Parameters:
            opt (Option class) -- stores all the experiment flags; needs to be a subclass of BaseOptions
        """
        BaseDataset.__init__(self, opt)
        self.eval_image_folder = "/speed-scratch/z_hannuo/sar2opt/whu_opt_sar/testA" #"/speed-scratch/z_hannuo/sar2opt/HRSID-DIOR-512/trainA"
        self.eval_samples = os.listdir(self.eval_image_folder)
        btoA = self.opt.direction == 'BtoA'
        input_nc = self.opt.output_nc if btoA else self.opt.input_nc
        self.transform_A = get_transform(self.opt, grayscale=(input_nc == 1))

    def __len__(self):
        return len( self.eval_samples )
    
    def __getitem__(self, index):
        sample_filename = self.eval_samples[index]
        sample_path = os.path.join(self.eval_image_folder, sample_filename)
        sample_img = Image.open(sample_path).convert('RGB')
        # apply image transformation
        sample = self.transform_A(sample_img)
        return {'A': sample, 'A_filename': sample_filename}