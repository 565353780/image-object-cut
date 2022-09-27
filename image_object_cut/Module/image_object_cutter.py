#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import cv2
import numpy as np
from tqdm import tqdm

from image_object_cut.Config.color import H_RANGE_DICT
from image_object_cut.Method.path import createFileFolder, renameFile


class ImageObjectCutter(object):

    def __init__(self, color_mode=None, background_image_file_path=None):
        self.h_range_list = []

        if color_mode is not None:
            self.setColorMode(color_mode)
        if background_image_file_path is not None:
            self.setBackground(background_image_file_path)
        return

    def reset(self):
        self.h_range_list = []
        return True

    def getColorModeList(self):
        return list(H_RANGE_DICT.keys())

    def setColorMode(self, color_mode):
        assert color_mode in H_RANGE_DICT.keys()
        self.h_range_list = H_RANGE_DICT[color_mode]
        return True

    def setBackground(self, background_image_file_path):
        assert os.path.exists(background_image_file_path)
        background_image = cv2.imread(background_image_file_path)

        background_hsv = cv2.cvtColor(background_image, cv2.COLOR_BGR2HSV)

        h_min_list = [
            np.min(background_hsv[:, :, 0]),
            np.min(background_hsv[:, :, 1]),
            np.min(background_hsv[:, :, 2])
        ]
        h_max_list = [
            np.max(background_hsv[:, :, 0]),
            np.max(background_hsv[:, :, 1]),
            np.max(background_hsv[:, :, 2])
        ]

        background_h_range_list = [h_min_list, h_max_list]

        print(self.h_range_list)
        print(background_h_range_list)
        # FIXME: use this to set background to cut image object
        #  self.h_range_list = background_h_range_list
        return True

    def getObjectImage(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        #  cv2.imshow("test", hsv)
        #  cv2.waitKey(3000)
        #  print(hsv[0][0])

        mask = cv2.inRange(hsv, np.array(self.h_range_list[0]),
                           np.array(self.h_range_list[1]))

        cv2.bitwise_not(mask, mask)

        object_black_image = cv2.bitwise_and(image, image, mask=mask)

        object_image = np.zeros(
            (object_black_image.shape[0], object_black_image.shape[1], 4))

        for i in range(object_black_image.shape[0]):
            for j in range(object_black_image.shape[1]):
                if (object_black_image[i][j] == [0, 0, 0]).all():
                    continue
                object_image[i][j][:3] = object_black_image[i][j]
                object_image[i][j][3] = 255

        return object_image

    def getObjectImageFromImageFile(self, image_file_path):
        assert os.path.exists(image_file_path)

        image = cv2.imread(image_file_path)

        return self.getObjectImage(image)

    def cutImageFileObject(self,
                           image_file_path,
                           save_object_image_file_path,
                           color_mode="green"):
        assert os.path.exists(image_file_path)
        assert color_mode in H_RANGE_DICT.keys()

        object_image = self.getObjectImageFromImageFile(image_file_path)

        createFileFolder(save_object_image_file_path)

        cv2.imwrite(save_object_image_file_path, object_image)
        return True

    def cutImageFolderObject(self,
                             image_folder_path,
                             save_object_image_folder_path,
                             print_progress=False):
        assert os.path.exists(image_folder_path)
        file_name_list = os.listdir(image_folder_path)

        image_file_name_list = []
        for file_name in file_name_list:
            if file_name[-4:] not in [".jpg", ".png"]:
                continue
            image_file_name_list.append(file_name)

        if len(image_file_name_list) == 0:
            return True

        os.makedirs(save_object_image_folder_path, exist_ok=True)

        for_data = image_file_name_list
        if print_progress:
            print("[INFO][ImageObjectCutter::cutImageFolderObject]")
            print("\t start cut image file object...")
            for_data = tqdm(for_data)
        for image_file_name in for_data:
            image_file_path = image_folder_path + image_file_name
            save_object_image_file_path = save_object_image_folder_path + image_file_name.split(
                ".")[0] + ".png"

            if os.path.exists(save_object_image_file_path):
                continue

            tmp_save_object_image_file_path = save_object_image_file_path[:
                                                                          -4] + "_tmp.png"
            assert self.cutImageFileObject(image_file_path,
                                           tmp_save_object_image_file_path)

            renameFile(tmp_save_object_image_file_path,
                       save_object_image_file_path)
        return True
