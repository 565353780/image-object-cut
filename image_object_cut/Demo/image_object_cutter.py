#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2
from tqdm import tqdm

from image_object_cut.Module.image_object_cutter import ImageObjectCutter


def demo():
    image_file_path = "/home/chli/chLi/NeRF/green_test_1/paper.jpg"
    save_object_image_file_path = "/home/chli/chLi/NeRF/green_test_1/1_paper_object.png"

    image_object_cutter = ImageObjectCutter()

    image_object_cutter.cutImageFileObject(image_file_path,
                                           save_object_image_file_path,
                                           "green")
    return True


def demo_folder():
    for i in range(2, 9):
        num = str(i)
        image_folder_path = "/home/chli/chLi/NeRF/box_merge_8/" + num + "/images/"
        color_mode = "green"
        background_image_file_path = "/home/chli/chLi/NeRF/ustc_niu_green_bg2/image_10.png"
        background_image_file_path = None
        save_object_image_folder_path = "/home/chli/chLi/NeRF/box_merge_8/" + num + "/object/"
        print_progress = True

        image_object_cutter = ImageObjectCutter(color_mode,
                                                background_image_file_path)

        image_object_cutter.cutImageFolderObject(image_folder_path,
                                                 save_object_image_folder_path,
                                                 print_progress)
    return True

def demo_cut():
    image_folder_path = "/home/chli/chLi/NeRF/ustc_niu_nerfpl/images_source/"
    save_image_folder_path = "/home/chli/chLi/NeRF/ustc_niu_nerfpl/images/"

    os.makedirs(save_image_folder_path, exist_ok=True)
    image_filename_list = os.listdir(image_folder_path)
    for filename in tqdm(image_filename_list):
        if filename[-4:] not in [".jpg", ".png"]:
            continue
        image = cv2.imread(image_folder_path + filename, cv2.IMREAD_UNCHANGED)
        image = image[280:1000, :]
        cv2.imwrite(save_image_folder_path + filename, image)
    return True

def demo_resize():
    image_folder_path = "/home/chli/chLi/NeRF/ustc_niu_nerfpl/images_source/"
    save_image_folder_path = "/home/chli/chLi/NeRF/ustc_niu_nerfpl/images/"

    os.makedirs(save_image_folder_path, exist_ok=True)
    image_filename_list = os.listdir(image_folder_path)
    for filename in tqdm(image_filename_list):
        if filename[-4:] not in [".jpg", ".png"]:
            continue
        image = cv2.imread(image_folder_path + filename, cv2.IMREAD_UNCHANGED)
        image = cv2.resize(image, (720, 1280))
        cv2.imwrite(save_image_folder_path + filename, image)
    return True
