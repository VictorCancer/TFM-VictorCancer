import cv2
import os

output_folder_images = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\images"          
output_folder_labels = 'C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\labels'

# Creamos las carpetas si no existen
os.makedirs(output_folder_labels, exist_ok=True)
os.makedirs(output_folder_images, exist_ok=True)

############################################
#                                          #
#               IMAGES                     #
#                                          #
############################################



def images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame):
    # Abrimos el video
    video_capture = cv2.VideoCapture(video_path)

    frame_count = 0
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        
        # Guardamos las imagenes con una resolución menor
        if frame_count%frame_ratio == 0 and frame_count >= minimum_frame:
            image_name = dataset_name + '-' + video_name[:-4] +f"_{frame_count:05d}.jpg"
            frame_filename = os.path.join(output_folder_images, image_name)
            frame_resized = cv2.resize(frame,(960,540))
            cv2.imwrite(frame_filename, frame_resized)
            print(frame_count)
        
        frame_count += 1

    # # Resolución original del video:
    # width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))  
    # print(f"Width: {width}")
    # print(f"Height: {height}")

    video_capture.release()
    print(f"Imagenes creadas del dataset {dataset_name} y el video {video_name}")



############################################
#                                          #
#               LABELS                     #
#                                          #
############################################



def label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame):

    # Iteramos sobre los ficheros .txt
    for filename in os.listdir(labels_path):

        if filename.endswith(".txt"):
            input_file = os.path.join(labels_path, filename)
            
            # Leemos el fichero
            with open(input_file, "r") as file:
                lines = file.readlines()
            
            for line in lines:
                # Separamos en columnas
                columns = line.strip().split()

                # La primera columna es el Frame
                frame = int(columns[0])

                if frame%frame_ratio == 0 and frame >= minimum_frame:
                    new_filename = dataset_name + '-' + video_name[:-4] + f"_{frame:05d}" + ".txt"
                    new_filepath = os.path.join(output_folder_labels, new_filename)
                    
                    # Cambiamos la primera columna por un "0"
                    columns[0] = "0"
                    width = int(columns[3])-int(columns[1])
                    height = int(columns[4])-int(columns[2])
                    
                    # Normalizamos las etiquetas
                    columns[1] = "{:.6f}".format((int(columns[1]) + width/2) / 1280)
                    columns[2] = "{:.6f}".format((int(columns[2]) + height/2)  / 720)
                    columns[3] = "{:.6f}".format(width / 1280)
                    columns[4] = "{:.6f}".format(height / 720)

                    # Si ya existe el fichero añadimos una nueva linea
                    with open(new_filepath, "a") as new_file:
                        new_file.write(" ".join(columns) + "\n")


    print(f"Labels creados del dataset {dataset_name} y el video {video_name}")




# Parametros:
dataset_name = "StarvedCreek"
dataset_source = dataset_name + "\\20180611SCF\\SC11062018-B"
labels_source = "Starved Creek\\20180611SCF\\"
video_name = "SC11062018-B.MOV" 
frame_ratio = 30
minimum_frame = 2000

# Variables:
video_path =  "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\" + dataset_source + "\\" + video_name
labels_path = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\annotations\\" + labels_source +  video_name[:-4]

images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame)
label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame)



 
# Parametros:
dataset_name = "StarvedCreek"
dataset_source = dataset_name + "\\20190301SC\\20190301SC-A"
labels_source = "Starved Creek\\20190301SC\\"
video_name = "20190301SC-A.MOV" 
frame_ratio = 30
minimum_frame = 2000

# Variables:
video_path =  "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\" + dataset_source + "\\" + video_name
labels_path = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\annotations\\" + labels_source +  video_name[:-4]

images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame)
label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame)

 




# Parametros:
dataset_name = "DeepCreekWhole"
dataset_source = dataset_name 
labels_source = "Deep Creek Whole\\20181015DC\\"
video_name = "DC15102018-B.MOV" 
frame_ratio = 30
minimum_frame = 0

# Variables:
video_path =  "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\" + dataset_source + "\\" + video_name
labels_path = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\annotations\\" + labels_source +  video_name[:-4]

images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame)
label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame)





# Parametros:
dataset_name = "DeepCreekWhole"
dataset_source = dataset_name 
labels_source = "Deep Creek Whole\\20180927DC\\"
video_name = "DC27092018_B.MOV" 
frame_ratio = 30
minimum_frame = 0

# Variables:
video_path =  "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\" + dataset_source + "\\" + video_name
labels_path = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\annotations\\" + labels_source +  video_name[:-4]

images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame)
label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame)



# Parametros:
dataset_name = "DeepCreekWhole"
dataset_source = dataset_name 
labels_source = "Deep Creek Whole\\20181113DC\\"
video_name = "DC13112018-B.MOV" 
frame_ratio = 30
minimum_frame = 2000

# Variables:
video_path =  "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\" + dataset_source + "\\" + video_name
labels_path = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\annotations\\" + labels_source +  video_name[:-4]

images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame)
label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame)





# Parametros:
dataset_name = "HalfSoundCreek"
dataset_source = dataset_name 
labels_source = "Half Sound Creek\\20190406HS\\"
video_name = "HS04062019 - B.MOV" 
frame_ratio = 30
minimum_frame = 0

# Variables:
video_path =  "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\" + dataset_source + "\\" + video_name
labels_path = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\annotations\\" + labels_source +  video_name[:-4]

images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame)
label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame)


# Parametros:
dataset_name = "HalfSoundCreek"
dataset_source = dataset_name 
labels_source = "Half Sound Creek\\20190506HS\\"
video_name = "HS05062019A.MOV" 
frame_ratio = 30
minimum_frame = 0

# Variables:
video_path =  "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\" + dataset_source + "\\" + video_name
labels_path = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\annotations\\" + labels_source +  video_name[:-4]

images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame)
label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame)



 
# Parametros:
dataset_name = "RollinsEast"
dataset_source = dataset_name 
labels_source = "Rollins East\\20180721RCE\\"
video_name = "RCE21072018-B.MOV" 
frame_ratio = 30
minimum_frame = 0

# Variables:
video_path =  "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\" + dataset_source + "\\" + video_name
labels_path = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\annotations\\" + labels_source +  video_name[:-4]

images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame)
label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame)

 

# Parametros:
dataset_name = "RollinsEast"
dataset_source = dataset_name
labels_source = "Rollins East\\20180828RC\\"
video_name = "RCE28082018-A.MOV" 
frame_ratio = 30
minimum_frame = 0

# Variables:
video_path =  "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\" + dataset_source + "\\" + video_name
labels_path = "C:\\Users\\Cancer\\Desktop\\Miscelanea\\datasets\\bahamas\\annotations\\" + labels_source +  video_name[:-4]

images_generator(video_path,output_folder_images,dataset_name,video_name,frame_ratio,minimum_frame)
label_generator(labels_path,output_folder_labels,dataset_name,video_name,frame_ratio,minimum_frame)

 










