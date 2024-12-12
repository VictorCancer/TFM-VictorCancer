import shutil
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os


def copy_and_rename(src_path, dest_path, new_name):

	shutil.copy(src_path, dest_path)

	new_path = f"{dest_path}\\{new_name}"
	shutil.move(f"{dest_path}\\{os.path.basename(src_path)}", new_path)



def show_bbox(image_path):
    # Buscamos el equivalente entre imagen y label
    label_path = image_path.replace('images', 'labels')
    label_path = label_path.replace('.JPG', '.txt')
    label_path = label_path.replace('.jpg', '.txt')

    # Abrimos la imagen
    image = Image.open(image_path)

    draw = ImageDraw.Draw(image)
    destino = 'C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\predicciones'
    list_folder = image_path.split(os.sep)
    name = os.path.basename(image_path)

    try:
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

        plt.savefig(destino +'\\osaconservation-' + list_folder[7]+ '-' + name[:-4]+'-etiqueta.jpg', dpi=300, bbox_inches='tight')
        
        # plt.show()
        plt.close()
    except FileNotFoundError:
        copy_and_rename(image_path,destino,'osaconservation-' + list_folder[7]+ '-' + name[:-4]+'-etiqueta.jpg')
        
    



# show_bbox('C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\images\\RollinsEast-RCE28082018-A_02850.jpg')
# show_bbox('C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\osaconservation\\116FTASK\\images\\IRX_3979.JPG')

source_folder = 'C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\Arribada2023GT'
i = 1
for root, dirs, files in os.walk(source_folder):
    for directory in dirs:
        if directory == 'images':
            source_images_path = os.path.join(root, directory)
            list_folder = source_images_path.split(os.sep)
            if list_folder[7] in ['102FTASK', '103FTASK', '105FTASK', '110FTASK', '111FTASK', '116FTASK', '117FTASK', '118FTASK', '121FTASK', '123FTASK', '124FTASK']:
                for file in os.listdir(source_images_path):
                    if i>600:
                        src_file = os.path.join(source_images_path, file)
                        show_bbox(src_file)
                    print(i)
                    i+=1


