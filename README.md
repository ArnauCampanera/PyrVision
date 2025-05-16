# <div align="center">PyrVision</div>

[Catalan version](https://github.com/ArnauCampanera/PyrVision/blob/main/README_ca.md)

Last code update: 22/03/2025

Last model version: 22/03/2025


PyrVision is an Artificial Intelligence model developed at the [Forest Science and Technology Centre of Catalonia](https://www.ctfc.cat) in collaboration with the [Computer Vision Center](https://www.cvc.uab.es). It is capable of automatically detecting up to 18 different classes.  
PyrVision uses [RT-DETR](https://docs.ultralytics.com/models/rtdetr/), a state-of-the-art object detection model, to maximize accuracy and speed.

<div align="center">
  <img width="60%" src="https://github.com/ArnauCampanera/PyrVision/assets/159940202/bf3dd13b-a849-41c6-86c3-a59f3d8a8c64)">

</div>



## <div align="center">Documentation</div>

### Model Architecture

PyrVision is actually two unified models: one for black and white images and another for color images.

Mammals in the Pyrenees have different habits — some are more nocturnal, others more diurnal, and some appear both day and night.  
Because AI models require large amounts of images to learn how to detect a specific species, some are only recognizable in night images, others only in day images.  
You can find the list of these species below, depending on whether they are recognized by the color model [C] and/or the black and white model [BW].

### Species

PyrVision can detect the following wild mammal species:

- Roe deer - *Capreolus capreolus* [C][Bw]  
- Wildcat - *Felis silvestris* [C][BW]  
- Hare - *Lepus europaeus* [C][BW]  
- Chamois - *Rupicapra pyrenaica* [C][BW]  
- Wild boar - *Sus scrofa* [C][BW]  
- Fox - *Vulpes vulpes* [C][BW]  
- Red deer - *Cervus elaphus* [C][BW]  
- Squirrel - *Sciurus vulgaris* [C]  
- Brown bear - *Ursus arctos* [C][BW]  
- Wolf - *Canis lupus* [C][BW]  
- Fallow deer - *Dama dama* [C][BW]  
- Marten - *Martes sp.* [BW]  
- Badger - *Meles meles* [BW]  

Other classes:  
- Cow - *Bos taurus* [C][BW]  
- Horse - *Equus caballus* [C]  
- Dog - *Canis familiaris* [C]  
- Human - *Homo sapiens* [C]  
- Vehicle [C]

Instructions for installing and using PyrVision depend on your platform.

<details close>
<summary>macOS Systems</summary>

### <div align="center">Installation (macOS)</div>
To use PyrVision locally, you'll need to install some prerequisites.

#### Prerequisites
First, install ['miniconda'](https://docs.anaconda.com/free/miniconda/#latest-miniconda-installer-links), choosing the correct CPU architecture (Intel x86 / M1, M2, M3). Python 3.10 is recommended.

Run the appropriate file (Miniconda3-latest-MacOSX-x86_64.pkg or Miniconda3-latest-MacOSX-arm64.pkg) and follow the on-screen instructions.

Then open the Terminal (found in Applications > Other or via Spotlight search with Cmd+Space).

Create a new environment to install PyrVision’s requirements without affecting other libraries:

```bash
conda create --name pyrvision python=3.10
```

When prompted Proceed ([y]/n)?, type y and press Enter.

Activate the environment:

```
conda activate pyrvision
```

Install the required libraries:

```bash
conda install pytorch torchvision -c pytorch
```
```bash
conda install conda-forge::ultralytics
```

Install Jupyter Notebook:

```bash
conda install -c conda-forge notebook
```

#### Download PyrVision

To download PyrVision type the following commands:

```bash
git clone https://github.com/ArnauCampanera/PyrVision.git
```

This will create a PyrVision folder in your home directory.


### <div align="center">Usage</div>

To classify images automatically:

- Copy your images to the inbox folder inside PyrVision.
- Open Terminal and run:
```bash
cd PyrVision
conda activate pyrvision
jupyter notebook
```

Your default web browser will open. Chrome is recommended.

- Double-click init.ipynb to open it.
- Go to the menu and select Run > Run All Cells.

The program will begin detecting images. Estimate around 10 seconds per image on a typical machine.

### <div align="center">Finish</div>

To finish:

Save changes via File > Save Notebook if needed.

Close via File > Close and Shut Down Notebook.

Shut down Jupyter via File > Shut Down.

Close Terminal with exit.

</details>

<details close>
<summary>Windows Systems</summary>

### <div align="center">Installation (Windows)</div>

#### Prerequisites
##### Miniconda

Install ['miniconda'](https://docs.anaconda.com/free/miniconda/miniconda-other-installer-links/#windows-installers). Python 3.10 is recommended.

Run the installer and follow the instructions.

A new folder 'Miniconda3 (64-bit)' will be available from the start menu. Navigate to the folder and open Anaconda Prompt (miniconda3).

Create and activate a new environment:

```bash
conda create --name pyrvision python=3.10
```
```bash
conda activate pyrvision
```


Install required libraries:

Without NVIDIA GPU:
```bash
conda install -c pytorch -c conda-forge pytorch torchvision cpuonly ultralytics
```

With NVIDIA GPU:
```bash
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics
```

Install Jupyter Notebook:

```bash
conda install -c conda-forge notebook
```


#### Download PyrVision

```bash
git clone https://github.com/ArnauCampanera/PyrVision.git
```

### <div align="center">Usage</div>

To classify images automatically:

- Copy images into the inbox folder in PyrVision.
- Open 'Anaconda Prommpt (miniconda3)' application and run:
```bash
cd PyrVision
conda activate pyrvision
jupyter notebook
```

Your default web browser will open. Chrome is recommended.

- Double-click init.ipynb to open it.
- Go to the menu and select Run > Run All Cells.

The program will begin detecting images. Estimate around 10 seconds per image on CPU, 0.2-0.5 seconds on GPU.

### <div align="center">Finish</div>

To finish:

Save changes via File > Save Notebook if needed.

Close via File > Close and Shut Down Notebook.

Shut down Jupyter via File > Shut Down.

Exit Anaconda Prompt: exit

</details>

<details close>
<summary>Linux Systems</summary>

### <div align="center">Installation (Linux)</div>

#### Prerequisites

First, install ['miniconda'](https://docs.anaconda.com/free/miniconda/miniconda-other-installer-links/#linux-installers), choosing the correct CPU architecture (Intel x86 / M1, M2, M3). Python 3.10 is recommended.

Open terminal and type:

```bash
bash filename
```
(replace filename with the path to the downloaded file)

Close and reopen Terminal after setup.

Create and activate environment:

```bash
conda create --name pyrvision python=3.10
conda activate pyrvision
```

Install the required libraries:

Without NVIDIA GPU:
```bash
conda install pytorch torchvision cpuonly -c pytorch
```

With NVIDIA GPU:
```bash
conda install pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia
```

Also,
```bash
conda install conda-forge::ultralytics
```

Install Jupyter Notebook:
```bash
conda install -c conda-forge notebook
```

#### Download PyrVision

To download PyrVision type the following commands:

```bash
git clone https://github.com/ArnauCampanera/PyrVision.git
```

This will create a PyrVision folder in your home directory.


### <div align="center">Usage</div>

To classify images automatically:

- Copy your images to the inbox folder inside PyrVision.
- Open Terminal and run:
```bash
cd PyrVision
conda activate pyrvision
jupyter notebook
```

Your default web browser will open. Chrome is recommended.

- Double-click init.ipynb to open it.
- Go to the menu and select Run > Run All Cells.

The program will begin detecting images. Estimate around 10 seconds per image on a typical machine.

### <div align="center">Finish</div>

To finish:

Save changes via File > Save Notebook if needed.

Close via File > Close and Shut Down Notebook.

Shut down Jupyter via File > Shut Down.

Close Terminal with exit.

</details>

### Options

#### Confidence Value

If PyrVision misses animals and marks images as empty, it might be due to a high confidence threshold.

Confidence value (0–1) controls how sure the model must be to classify something as an animal.

High (e.g., 0.95) = fewer false positives but more missed animals.
Low (e.g., 0.05) = captures everything but may misclassify branches or shadows.
You can adjust this in init.ipynb under the PyrVision Options cell:

```python
conf_COLOR = 0.8
conf_BW = 0.6
```

#### Bounding Box

By default, PyrVision doesn't draw bounding boxes. To enable them, edit the rectangle variable in init.ipynb:

```python
rectangle = True
```

## Results

When done, check the predicted folder inside PyrVision. It will contain images sorted by species and a nuls folder with empty detections.