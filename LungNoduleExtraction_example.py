# -- coding: utf-8 --
'''
@Time : 07/03/2022 16:46
@Author : "Jingxuan Wang"
@Email : j.wang02@umcg.nl
'''


import pydicom

def extract_lung_nodule(dicom_path, x, y):

    # read dicom image
    ds = pydicom.dcmread(dicom_path)
    imgarray = ds.pixel_array

    Xcenter = int(x)
    Ycenter = int(y)

    # extraction(crop)
    # [starting row:ending row, starting column:ending column]
    # crop_img = imgarray[Ycenter-32:Ycenter+32, Xcenter-32:Xcenter+32] # 64*64
    crop_img = imgarray[Ycenter-16:Ycenter+16, Xcenter-16:Xcenter+16]  # 32*32

    return crop_img

if __name__ == '__main__':

    dicom_path = "..." # your dicom path

    x = "..." # the value of lung nodule center on x-axis
    y = "..." # the value of lung nodule center on y-axis

    extract_lung_nodule(dicom_path, x, y)






