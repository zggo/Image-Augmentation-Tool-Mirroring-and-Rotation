# -*- coding: utf-8 -*-

from PIL import Image
import os

file_dir = './img_mirror/'            # 原始图片路径
savepath = './img_mirror/'     # 保存路径
    
for img_name in os.listdir(file_dir):
    img_path = file_dir + img_name    #  批量读取图片
    # print(img_path)
    img = Image.open(img_path)
    LEFT_RIGHT = img.transpose(Image.FLIP_LEFT_RIGHT)                    # 左右翻转
    TOP_BOTTOM = img.transpose(Image.FLIP_TOP_BOTTOM)            # 上下翻转
    rotated_90 = img.transpose(Image.ROTATE_90)        # 旋转90度
    rotated_180 = img.transpose(Image.ROTATE_180)    # 旋转180度
    rotated_270 = img.transpose(Image.ROTATE_270)    # 旋转270度
    rotated_180.save(savepath + '180_' + img_name)  # 保存180度
    rotated_270.save(savepath + '270_' + img_name)  # 保存270度
    rotated_90.save(savepath + '90_' + img_name)  # 保存90度
    TOP_BOTTOM.save(savepath + 'top_' + img_name)  # 保存上下翻转
    LEFT_RIGHT.save(savepath + 'left_' + img_name)  # 保存左右翻转
    # f = open('train_img/180.txt', 'a')                                       
    # f.write('180_' + img_name + ' ' + '180' + '\n')        # 写入txt标签文件：imagename + 空格 + 角度
print('完成啦！')
