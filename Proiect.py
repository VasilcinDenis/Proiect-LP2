
import cv2

import numpy as np

import glob
filenames = [img for img in glob.glob("C:/Users/40721/PycharmProjects/Proiect/*.png")]



images = []
for img in filenames:
    n= cv2.imread(img)
    images.append(n)
    print (img)
for img in images:


        image_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Alb - Negru', image_grey)

        sobel_vertical = np.float32([[-2, 0, 2],
                                    [-4, 0, 4],
                                    [-2, 0, 2]])
        sobel_orizontal = np.transpose(sobel_vertical)

        image_grey = np.float32(image_grey)
        sobel_vertical_frame = cv2.filter2D(image_grey, -1, sobel_vertical)
        sobel_orizontal_frame = cv2.filter2D(image_grey, -1, sobel_orizontal)

        sobel_orizontal_frame = cv2.convertScaleAbs(sobel_orizontal_frame)
        sobel_vertical_frame = cv2.convertScaleAbs(sobel_vertical_frame)
        cv2.imshow('Sobel orizontal', sobel_orizontal_frame)
        cv2.imshow('Sobel vertical', sobel_vertical_frame)
        sobel_orizontal_frame = np.float32(sobel_orizontal_frame)
        sobel_vertical_frame = np.float32(sobel_vertical_frame)

        image_edges = sobel_vertical_frame * sobel_vertical_frame + sobel_orizontal_frame * sobel_orizontal_frame
        image_edges = np.sqrt(image_edges)
        image_edges = cv2.convertScaleAbs(image_edges)
        cv2.imshow('Margini', image_edges)


        cv2.imshow('Final', img)

        cv2.waitKey()
        #Filtru Canny
        edges = cv2.Canny(img,100,200)
        cv2.imshow("Canny",edges)
        cv2.waitKey()
        #Filtru Laplacian
        laplacian = cv2.Laplacian(img,cv2.CV_64F)
        cv2.imshow("Laplacian",laplacian)
        cv2.waitKey()



