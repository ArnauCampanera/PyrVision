import csv
from ultralytics import YOLO
from PIL import Image
import os
import os.path
import shutil

# Valor de confiança en les prediccions en una escala de 0-1
conf_COLOR = 0.8
conf_BW = 0.6

# Altres opcions
rectangle = False

# Ruta de la carpeta a vigilar
watchDirectory = r"inbox"

# Ruta de les prediccions
prediction_labels_path = "runs/detect/predict/labels"
prediction_path = "runs/detect/predict"

# Obrir el fitxer CSV
with open("models/especies.csv", "r") as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Initialize an empty list
    especies = []

    # Iterate over each row in the CSV file
    for row in reader:
        # Append the row values to the list
        especies.append(row)

# Print the list of data
for especie in especies:
    print(especie)


# function to return files in a directory
onlyfiles = [
    f
    for f in os.listdir(watchDirectory)
    if os.path.isfile(os.path.join(watchDirectory, f))
]


def readPredictedSpecies():
    detections = []
    label = os.listdir(prediction_labels_path)
    if len(label) != 0:
        with open("{}/{}".format(prediction_labels_path, label[0]), "r") as file:
            # Read classes
            linies = file.readlines()
            for linia in linies:
                # Remove leading/trailing whitespace and newline characters
                especie = linia.split()
                detections.append(especie[0])

        # Print the first value
        return detections
    else:
        return


def storefiles(file):
    especie = readPredictedSpecies()
    if (especie is None) != 0:
        # Si no hi ha cap detecció a la imatge
        try:
            shutil.move(
                "{}/{}".format(watchDirectory, file),
                "{}/{}/".format("predicted", "nuls"),
            )
        except IOError as io_err:
            os.makedirs(os.path.dirname("{}/{}/".format("predicted", "nuls")))
            shutil.move(
                "{}/{}".format(watchDirectory, file),
                "{}/{}/".format("predicted", "nuls"),
            )
    else:
        try:
            shutil.move(
                "{}/{}".format(watchDirectory, file),
                "{}/{}/".format("predicted", *especies[int(especie[0])]),
            )
        except IOError as io_err:
            os.makedirs(
                os.path.dirname(
                    "{}/{}/".format("predicted", *especies[int(especie[0])])
                )
            )
            shutil.move(
                "{}/{}".format(watchDirectory, file),
                "{}/{}/".format("predicted", *especies[int(especie[0])]),
            )
        shutil.copytree(
            "{}/{}".format(prediction_path, "labels"),
            "{}/{}".format("predicted", *especies[int(especie[0])]),
            dirs_exist_ok=True,
        )
    shutil.rmtree(prediction_path)


for file in onlyfiles:
    im = Image.open("{}/{}".format(watchDirectory, file))
    w, h = im.size
    impalette = im.getpixel((w / 2, h / 2))
    if impalette[0] == impalette[1] == impalette[2]:
        model = YOLO("models/best_BW.pt")
        imatge = "{}/{}".format(watchDirectory, file)
        results = model.predict(imatge, save_txt=False, save=rectangle, conf=conf_BW)
    else:
        model = YOLO("models/best_COLOR.pt")
        imatge = "{}/{}".format(watchDirectory, file)
        results = model.predict(imatge, save_txt=False, save=rectangle, conf=conf_COLOR)
    readPredictedSpecies
    storefiles(file)
