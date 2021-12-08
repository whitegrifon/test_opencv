import cv2

def read_img():
    return cv2.imread('wallpaper.png')


def print_img_par(img):
    print(img.shape)
def resize_img(img,nw):
    r=float(nw)/ img.shape[1]
    dim=(nw, int(img.shape[0]*r))

    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

def show_img(name,img):
    cv2.imshow(name, img)
img=read_img()
print_img_par(img)
nw=150
nw1=600
resized = resize_img(img, nw)
resized1 = resize_img(resized, nw1)
show_img('wallpaper.png', resized)
show_img('wallpaper_big.png', resized1)
#cropped = img[200:100, 150:100]
#show_img('wallpaper_crop.png', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
