import cv2

img = cv2.imread("Resources/shapes.png")
print(img.shape) # 获取图片尺寸: height, width, channels
print(f"高:{img.shape[0]} 宽:{img.shape[1]} 通道：:{img.shape[2]}")

imgResize = cv2.resize(img,(1000,500)) # 重置图片尺寸
print(imgResize.shape)
print(f"高:{img.shape[0]} 宽:{img.shape[1]} 通道：:{img.shape[2]}")

imgCropped = imgResize[300:500,700:1000] # 获取制定像素区域内的内容

cv2.imshow("Raw Image",img)
cv2.imshow("Image Resized",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)