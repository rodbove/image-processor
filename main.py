import cv2

image = cv2.imread('/home/rodrigo/Imagens/self.jpg')

width = image.shape[1]
height = image.shape[2]

(b, g, r) = image[0, 0]

for y in range(0, image.shape[0]):
    for x in range(0, image.shape[1]):
        if x%2 == 0:
            (b, g, r) = image[y, x]
            image[y, x] = ((y/2)%256, (y/2)%256, r)


cv2.imshow('My image', image)
cv2.waitKey(0)
