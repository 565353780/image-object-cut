#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import cv2
import numpy as np

from image_object_cut.Config.color import H_RANGE_DICT
from image_object_cut.Method.path import createFileFolder


class ImageObjectCutter(object):

    def __init__(self):
        return

    def getColorModeList(self):
        return list(H_RANGE_DICT.keys())

    def getObjectImage(self, image, color_mode="green"):
        assert color_mode in H_RANGE_DICT.keys()

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        h_range_list = H_RANGE_DICT[color_mode]
        mask = cv2.inRange(hsv, tuple(h_range_list[0]), tuple(h_range_list[1]))

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

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return object_image

    def getObjectImageFromImageFile(self, image_file_path, color_mode="green"):
        assert os.path.exists(image_file_path)
        assert color_mode in H_RANGE_DICT.keys()

        image = cv2.imread(image_file_path)
        return self.getObjectImage(image, color_mode)

    def cutImageFileObject(self,
                           image_file_path,
                           save_object_image_file_path,
                           color_mode="green"):
        assert os.path.exists(image_file_path)
        assert color_mode in H_RANGE_DICT.keys()

        object_image = self.getObjectImageFromImageFile(
            image_file_path, color_mode)

        createFileFolder(save_object_image_file_path)

        cv2.imwrite(save_object_image_file_path, object_image)
        return True
