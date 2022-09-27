#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cv2

from image_object_cut.Config.color import H_RANGE_DICT


class ImageObjectCutter(object):

    def __init__(self):
        return

    def cutImageObject(self, image, color_mode):
        assert color_mode in H_RANGE_DICT

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        h_range_list = H_RANGE_DICT[color_mode]
        mask = cv2.inRange(hsv, tuple(h_range_list[0]), tuple(h_range_list[1]))

        cv2.bitwise_not(mask, mask)

        object_image = cv2.bitwise_and(image, image, mask=mask)

        cv2.imshow("input", image)
        cv2.imshow("mask", mask)
        cv2.imshow("result", object_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return object_image

    def cutImageFileObject(self, image_file_path, color_mode):
        assert os.path.exists(image_file_path)
        assert color_mode in H_RANGE_DICT

        image = cv2.imread(image_file_path)
        return self.cutImageObject(image, color_mode)
