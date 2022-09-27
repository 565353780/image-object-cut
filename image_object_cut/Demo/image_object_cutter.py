#!/usr/bin/env python
# -*- coding: utf-8 -*-

from image_object_cut.Module.image_object_cutter import ImageObjectCutter

def demo():
    image_file_path = "/home/chli/chLi/image_object_cut/1.jpg"

    image_object_cutter = ImageObjectCutter()

    object_image = image_object_cutter.cutImageFileObject(image_file_path, "green")
    return True
