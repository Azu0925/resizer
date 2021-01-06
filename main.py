from PIL import Image, ImageFilter
import os

image_path = input('画像ファイルのパスを入力：')
img = Image.open(image_path)
file_name = os.path.splitext(os.path.basename(image_path))[0]
file_extension = os.path.splitext(os.path.basename(image_path))[1]
file_dir = os.path.dirname(image_path)


for i in range(1, 11):
    size = i * 100
    img_resize = img.resize((size, size))
    img_resize.save(file_dir + '\\' + file_name + '_' + str(size) + file_extension)

