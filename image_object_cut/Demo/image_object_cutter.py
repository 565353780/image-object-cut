#!/usr/bin/env python
# -*- coding: utf-8 -*-

from image_object_cut.Module.image_object_cutter import ImageObjectCutter


def demo():
    image_file_path = "/home/chli/chLi/image_object_cut/1.jpg"
    save_object_image_file_path = "/home/chli/chLi/image_object_cut/1_object.png"

    image_object_cutter = ImageObjectCutter()

    image_object_cutter.cutImageFileObject(image_file_path,
                                           save_object_image_file_path,
                                           "green")
    return True
