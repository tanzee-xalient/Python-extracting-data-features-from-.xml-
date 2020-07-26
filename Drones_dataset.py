
import csv
import os
import cv2
from xml.etree import ElementTree as ET

with open('ddata_Tan.csv', 'w', newline='') as f:
    d_writer = csv.writer(f,delimiter=',')
    d_writer.writerow(['image_name', 'image_width', 'image_height', 'classname', 'xmin', 'ymin', 'xmax', 'ymax'])
    for file in os.listdir('datasetxml1'):
        tree = ET.parse(os.path.join('datasetxml1',file))
        root = tree.getroot()
        image_name = root.find('filename').text
        print(image_name)
    
        child = root.find('object')
        for size in root.findall('size'):
            w = int(size.find('width').text)
            h = int(size.find('height').text)
            isize = h * w
            print('size of image=', isize)
            for bndbox in child.findall('bndbox'):
                x1 = int(bndbox.find('xmin').text)
                x2 = int(bndbox.find('xmax').text)
                y1 = int(bndbox.find('ymin').text)
                y2 = int(bndbox.find('ymax').text)
                bboxsize = (x2 - x1) * (y2 - y1)
                print('size of bbox=', bboxsize)
                d_writer.writerow([image_name, w, h, 'Drones', x1, y1, x2, y2])