# -- coding: utf-8 --
'''
@Time : 07/03/2022 16:46
@Author : "Jingxuan Wang"
'''

import pydicom

def extract_lung_nodule_from_center(dicom_path, x, y):

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

def extract_lung_nodule_by_boundingbox(dicom_path, x, y):
    
    # read dicom image
    ds = pydicom.dcmread(dicom_path)
    imgarray = ds.pixel_array
    
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    
    crop_img = imgarray[x1:x2, y2:y1] 
    
    return crop_img
    

if __name__ == '__main__':

    dicom_path = "..." # your dicom path

    x = "..." # the value of lung nodule center on x-axis
    y = "..." # the value of lung nodule center on y-axis

    extract_lung_nodule_from_center(dicom_path, x, y)
    
    # lung nodule boundingbox[(x1,y1),(x1,y2),(x2,y2),(x2,y1)]
    
    '''
    x1,y1: the value of top & left pixel coordinate
    x1,y2: the value of bottom & left pixel coordinate
    x2,y2: the value of bottom & right pixel coordinate
    x2,y1: the value of top & right pixel coordinate
    '''
    
    x1 = "..."
    x2 = "..."
    y1 = "..."
    y2 = "..."
    
    extract_lung_nodule_by_boundingbox(dicom_path, x1, y1, x2, y2)
    

