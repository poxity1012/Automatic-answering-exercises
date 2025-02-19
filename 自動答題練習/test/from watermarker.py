from watermarker.marker import add_mark
import os

files = os.listdir('image_2')
for file in files:
    file_path = os.path.join('image_2',file)
    add_mark(file_path,mark='ddg4gg3g',color='#8B8B1B',size=21)


