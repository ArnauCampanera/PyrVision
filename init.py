import csv
from ultralytics import YOLO
from PIL import Image
import os
import os.path
import shutil
from pathlib import Path


def read_predicted_species():
    detections = []
    label = os.listdir(prediction_labels_path)
    if len(label) != 0:
        with open(f"{prediction_labels_path}/{label[0]}", "r") as file:
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
    especie = read_predicted_species()
    if (especie is None) != 0:
        # Si no hi ha cap detecció a la imatge
        try:
            shutil.move(
                Path(f"{watch_directory}/{file}/predicted/nuls"),
            )
        except IOError as io_err:
            os.makedirs(os.path.dirname(Path("predicted/nuls")))
            shutil.move(Path(f"{watch_directory}/{file}/predicted/nuls"))
    else:
        try:
            shutil.move(
                Path(
                    "{}/{}".format(watch_directory, file),
                    "{}/{}/".format("predicted", *especies[int(especie[0])]),
                )
            )
        except IOError as io_err:
            os.makedirs(
                os.path.dirname(
                    Path("{}/{}/".format("predicted", *especies[int(especie[0])]))
                )
            )
            shutil.move(
                "{}/{}".format(watch_directory, file),
                "{}/{}/".format("predicted", *especies[int(especie[0])]),
            )
        shutil.copytree(
            "{}/{}".format(prediction_path, "labels"),
            "{}/{}".format("predicted", *especies[int(especie[0])]),
            dirs_exist_ok=True,
        )
    shutil.rmtree(prediction_path)


if __name__ == "__main__":
    # Valor de confiança en les prediccions en una escala de 0-1
    conf_COLOR = 0.8
    conf_BW = 0.6

    # Altres opcions
    rectangle = False

    # Ruta de la carpeta a vigilar
    watch_directory = r"inbox"

    # Ruta de les prediccions
    prediction_labels_path = Path("runs/detect/predict/labels")
    prediction_path = Path("runs/detect/predict")

    # Obrir el fitxer CSV
    with open(Path("models/especies.csv"), "r") as csvfile:
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
        for f in os.listdir(watch_directory)
        if os.path.isfile(os.path.join(watch_directory, f))
    ]

    for file in onlyfiles:
        im = Image.open(f"{watch_directory}/{file}")
        w, h = im.size
        impalette = im.getpixel((w / 2, h / 2))
        if impalette[0] == impalette[1] == impalette[2]:
            model = YOLO(Path("models/best_BW.pt"))
            imatge = f"{watch_directory}/{file}"
            results = model.predict(
                imatge, save_txt=False, save=rectangle, conf=conf_BW
            )
        else:
            model = YOLO(Path("models/best_COLOR.pt"))
            imatge = Path(f"{watch_directory}/{file}")
            results = model.predict(
                imatge, save_txt=False, save=rectangle, conf=conf_COLOR
            )
        read_predicted_species
        storefiles(file)
