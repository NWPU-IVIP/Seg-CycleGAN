import os
from data.base_dataset import BaseDataset, get_transform
from data.image_folder import make_dataset
from PIL import Image
import random
import cv2 as cv
import torch



class PaperWritingDataset(BaseDataset):
    """
    用于获取模型框图里的填充示意图
    """
    def __init__(self, opt):
        """Initialize this dataset class.

        Parameters:
            opt (Option class) -- stores all the experiment flags; needs to be a subclass of BaseOptions
        """
        BaseDataset.__init__(self, opt)
        self.eval_image_folder = "/home/ganwork507/zhn/Seg4Trans/paper_test/hrsid_dior/trainA" #"/home/ganwork507/zhn/WHU-OPT-SAR-GAN/train/trainA"
        self.eval_samples = os.listdir(self.eval_image_folder)
        btoA = self.opt.direction == 'BtoA'
        input_nc = self.opt.output_nc if btoA else self.opt.input_nc
        self.transform_A = get_transform(self.opt, grayscale=(input_nc == 1))

        output_nc = self.opt.input_nc if btoA else self.opt.output_nc 
        self.transform_B = get_transform(self.opt, grayscale=(output_nc == 1))
        self.opt_eval_image_folder = "/home/ganwork507/zhn/Seg4Trans/paper_test/hrsid_dior/trainB"
        self.opt_eval_samples = os.listdir(self.opt_eval_image_folder)

    def __len__(self):
        return len( self.eval_samples )
    
    def __getitem__(self, index):
        sample_filename = self.eval_samples[index]
        sample_path = os.path.join(self.eval_image_folder, sample_filename)
        sample_img = Image.open(sample_path).convert('RGB')
        # apply image transformation
        sample = self.transform_A(sample_img)

        opt_sample_filename = self.opt_eval_samples[index]
        opt_sample_path = os.path.join(self.opt_eval_image_folder, opt_sample_filename)
        opt_sample_img = Image.open(opt_sample_path).convert('RGB')
        opt_sample = self.transform_B(opt_sample_img)

        return {'A': sample, 'B': opt_sample, 'A_filename': sample_filename, 'B_filename': opt_sample_filename}
