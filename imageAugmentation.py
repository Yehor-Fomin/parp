from PIL import Image, ImageFilter
import time
file_names = ['4329937.jpeg', '9604597.jpeg', '9676155.jpeg',
    '9676203.jpeg', '9979607.jpeg', '9980612.jpeg',
    '10155843.jpeg', '10184043.jpeg', '10266847.jpeg',
    '10275590.jpeg', '6665235.jpeg', '8902428.jpeg',
    '9962634.jpeg', '10099964.jpeg', '10278125.jpeg',
    '10288317.jpeg']
start = time.perf_counter()
size = (1200, 1200)
def augment_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'augmented-{img_name}')
    print(f'{img_name} was augmented...')

for f in file_names:
    augment_image(f)

end = time.perf_counter()
print(f'Finished in {round(end-start, 2)} seconds')
