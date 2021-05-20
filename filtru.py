import os
import cv2
import img as img
import numpy as np
import glob
filenames = [img for img in glob.glob("C:/facultate an 2/Proiect LP2/imagini initiale/*.jpg")]

images = []
contor = 1
for img in filenames:
    n = cv2.imread(img)
    images.append(n)
    print(img)

def sobel():
    image_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Alb - Negru', image_grey)

    sobel_vertical = np.float32([[-1, -2, -1],
                                [0, 0, 0],
                                [1, 2, 1]])
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
    path = 'C:/facultate an 2/Proiect LP2/imagini rezultate'
    cv2.imwrite(os.path.join(path, 'Sobel' + str(contor) + '.jpg'), image_edges)
    cv2.waitKey()

def Canny():
    #cv2.waitKey()
    edges = cv2.Canny(img, 100, 200)
    cv2.imshow("Canny", edges)
    path = 'C:/facultate an 2/Proiect LP2/imagini rezultate'
    cv2.imwrite(os.path.join(path, 'Canny' + str(contor) + '.jpg'), edges)
    cv2.waitKey()

def Laplacian():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    cv2.imshow("Laplacian", laplacian)
    path = 'C:/facultate an 2/Proiect LP2/imagini rezultate'
    cv2.imwrite(os.path.join(path, 'Laplacian' + str(contor) + '.jpg'), laplacian)
    cv2.waitKey()

print("Filtrele disponibile sunt:Laplacian,Sobel,Canny")

for img in images:
    cv2.imshow("Imaginea originala", img)
    cv2.waitKey(2)
    x = input("Alegeti filtrul:")
    if x == "Laplacian":
        print(Laplacian())
        cv2.destroyAllWindows()
    elif x == "Canny":
        print(Canny())
        cv2.destroyAllWindows()
    elif x == "Sobel":
        print(sobel())
        cv2.destroyAllWindows()
    else:
        print("Filtrul nu exista")
    contor += 1
