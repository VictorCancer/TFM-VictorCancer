import shutil
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt






def show_bbox(image_path):
    # Buscamos el equivalente entre imagen y label
    label_path = image_path.replace('images', 'labels')
    label_path = label_path.replace('.JPG', '.txt')
    label_path = label_path.replace('.jpg', '.txt')

    # Abrimos la imagen
    image = Image.open(image_path)

    draw = ImageDraw.Draw(image)

    with open(label_path, 'r') as f:
        for line in f.readlines():
            # Extraemos los 5 valores:
            label, x, y, w, h = line.split(' ')

            # Pasamos a float
            x = float(x)
            y = float(y)
            w = float(w)
            h = float(h)

            # Desnormalizamos la etiqueta
            W, H = image.size
            x1 = (x - w/2) * W
            y1 = (y - h/2) * H
            x2 = (x + w/2) * W
            y2 = (y + h/2) * H


            # Dibujamos los recuadros
            draw.rectangle((x1, y1, x2, y2),
                           outline=(255, 0, 0), 
                           width=5)             
    plt.imshow(image)
    plt.axis('off')
    plt.show()



show_bbox('C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\images\\RollinsEast-RCE28082018-A_02850.jpg')