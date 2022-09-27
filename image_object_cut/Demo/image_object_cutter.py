#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    image_folder_path = "/home/chli/chLi/NeRF/3vjia_person/images/"
    color_mode = "green"
    background_image_file_path = "/home/chli/chLi/NeRF/ustc_niu_green_bg1/image_10.png"
    save_object_image_folder_path = "/home/chli/chLi/NeRF/3vjia_person/object/"
    print_progress = True

    image_object_cutter = ImageObjectCutter(color_mode,
                                            background_image_file_path)

    image_object_cutter.cutImageFolderObject(image_folder_path,
                                             save_object_image_folder_path,
                                             print_progress)
    return True
