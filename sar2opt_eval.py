import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
import cv2 as cv
from util.util import tensor2im
from PIL import Image
import time
import numpy as np

#调用示例
# python sar2opt_eval.py --phase test --name cycle_whu_100 --dataroot overridden --dataset_mode evaluation --preprocess none --no_flip --epoch 200  --model cycle_gan
# "/home/ganwork507/zhn/Seg4Trans/Seg-CycleGAN/sar2opt_eval_test" : epoch_200的测试结果

if __name__ == '__main__':

    save_folder = "/speed-scratch/z_hannuo/projects/gan/Seg-CycleGAN/validation_whu/cycle_200/pseudo_test" #"/speed-scratch/z_hannuo/projects/gan/Seg-CycleGAN/beta_45_e50"

    opt = TestOptions().parse()  # get test options
    # hard-code some parameters for test
    opt.num_threads = 0   # test code only supports num_threads = 0
    opt.batch_size = 1    # test code only supports batch_size = 1
    opt.serial_batches = True  # disable data shuffling; comment this line if results on randomly chosen images are needed.
    opt.no_flip = True    # no flip; comment this line if results on flipped images are needed.
    opt.display_id = -1   # no visdom display; the test code saves the results to a HTML file.
    model = create_model(opt)      # create a model given opt.model and other options
    model.setup(opt)               # regular setup: load and print networks; create schedulers
    if opt.eval:
        model.eval()
    #model.load_networks(load_epoch)#opt需指定checkpoints_dir和name

    dataset = create_dataset(opt)
    for i, data in enumerate(dataset):
        #len(dataset) : 1902 | type(data) : <class 'dict'>
        #type(data[A]) : <class 'torch.Tensor'> | data[A].shape : torch.Size([1, 3, 256, 256])
        #type(data[A_filename]) : <class 'list'> | ['P0016_0_800_8400_9200_1.png']
        #fake_B : <class 'torch.Tensor'> | torch.Size([1, 3, 256, 256])
        model.set_input_evaluation(data)
        fake_B = model.netG_A(model.real_A)

        fake_B_name = data['A_filename'][0]
        fake_B_image = tensor2im(fake_B)

        
        image_pil = Image.fromarray(fake_B_image)
        image_pil.save( os.path.join(save_folder, fake_B_name) )