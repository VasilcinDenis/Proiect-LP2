import cv2
import numpy as np

image = cv2.imread('test.png')
cv2.imshow('Imagine initiala', image)

image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Imagine ALB-NEGRU', image_grey)

sobel_vertical = np.float32([[-2, 0, 2],
                            [-4, 0, 4],
                            [-2, 0, 2]])
sobel_orizontal = np.transpose(sobel_vertical)

image_grey = np.float32(image_grey)
sobel_vertical_frame = cv2.filter2D(image_grey, -1, sobel_vertical)
sobel_orizontal_frame = cv2.filter2D(image_grey, -1, sobel_orizontal)

sobel_orizontal_frame = cv2.convertScaleAbs(sobel_orizontal_frame)
sobel_vertical_frame = cv2.convertScaleAbs(sobel_vertical_frame)
cv2.imshow('Sobel Orizontal', sobel_orizontal_frame)
cv2.imshow('Sobel Vertical', sobel_vertical_frame)
sobel_orizontal_frame = np.float32(sobel_orizontal_frame)
sobel_vertical_frame = np.float32(sobel_vertical_frame)

image_edges = sobel_vertical_frame * sobel_vertical_frame + sobel_orizontal_frame * sobel_orizontal_frame
image_edges = np.sqrt(image_edges)
image_edges = cv2.convertScaleAbs(image_edges)
cv2.imshow('Margini', image_edges)

puncte_albe= np.argwhere(image_edges > 45)

for i in puncte_albe:
     image[i[0]][i[1]][0] = 128 # blue
     image[i[0]][i[1]][1] = 128 # green
     image[i[0]][i[1]][2] = 128 # red

cv2.imshow('Imagine finala', image)

cv2.waitKey()