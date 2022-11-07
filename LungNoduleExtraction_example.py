# -- coding: utf-8 --
'''
@Time : 07/03/2022 16:46
@Author : "wxlearncoding"
'''

import pydicom

def extract_lung_nodule_from_center(dicom_path, x, y):

    # read dicom image
    ds = pydicom.dcmread(dicom_path)
    imgarray = ds.pixel_array

    Xcenter = int(x)
    Ycenter = int(y)

    # extraction
    radius = 32  # just an example, for a diameter of 64 pixels
    crop_img = imgarray[Ycenter-radius:Ycenter+radius, Xcenter-radius:Xcenter+radius] 


def extract_lung_nodule_by_boundingbox(dicom_path, x1, y1, x2, y2):
    
    # read dicom image
    ds = pydicom.dcmread(dicom_path)
    imgarray = ds.pixel_array
    
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    
    crop_img = imgarray[x1:x2, y2:y1] 
    

    
if __name__ == '__main__':
    
    '''
    There are two methods for extraction, one is extract_lung_nodule_from_center, the other one is extract_lung_nodule_by_boundingbox
    '''

    dicom_path = "..." # your dicom path

    x = "..." # the value of lung nodule center on x-axis
    y = "..." # the value of lung nodule center on y-axis

    extract_lung_nodule_from_center(dicom_path, x, y)
    
    print("Extract lung nodule successfully!")
    
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
    
    print("Extract lung nodule successfully!")
    
    
