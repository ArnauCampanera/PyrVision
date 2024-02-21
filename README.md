# PyrVision
[English below](github.com/ArnauCampanera/PyrVision/README.md#English)

PyrVision és un model d'Intel·ligència Artificial desenvolupat al [Centre de Ciència i Tecnologia Forestal de Catalunya](https://www.ctfc.cat) amb la capacitat de detectar automàticament fins a 16 classes diferents.
PyrVision utilitza [YOLOv8](https://github.com/ultralytics/ultralytics/), l'estat de l'art dels models de detecció d'objectes, per tal de maximitzar precisió i rapidesa.

## <div align="center">Documentació</div>

### Arquitectura del Model
PyrVision són en realitat dos models. Un per imatges en blanc i negre i un altre per imatges en color. 

Les espècies del Pirineu tenen diferents hàbits. Algunes són més nocturnes, altres més diurnes i d'altres apareixen tant de dia com de nit. 
Degut a que els models d'Intel·ligència Artificial requereixen de grans quantitats d'imatges per aprendre a detectar una espècie en concret, algunes només són reconeixibles en imatges de nit i d'altres només en imatges de dia.
Podeu trobar la llista d'aquestes espècies a continuació, en funció de si són reconegudes pel model de color [C] i/o del blanc i negre [BN].

### Espècies
PyrVision pot detectar les següents espècies de mamífers salvatges:
- Cabirol - Capreolus capreolus [C][BN]
- Gat fer - Felis silvestris [C][BN]
- Llebre - Lepus europaeus [C][BN]
- Isard - Rupicapra pyrenaica [C][BN]
- Porc senglar - Sus scrofa [C][BN]
- Guineu - Vulpes vulpes [C][BN]
- Cérvol - Cervus elaphus [C][BN]
- Esquirol - Sciurus vulgaris [C]
- Ós bru - Ursus arctos [C][BN]
- Daina - Dama dama [C][BN]
- Marta - Martes sp. [BN]
- Teixó - Meles meles [BN]

Altres classes:
- Vaca - Bos taurus [C][BN]
- Cavall - Equus caballus [C]
- Gos - Canis familiaris [C]
- Humà - Homo sapiens [C]
- Vehicle [C]


### Instal·lació (macOS)
Per poder utilitzar PyrVision localment cal instal·lar uns prerequisits. 

#### Prerequisits
Primer cal instal·lar ['miniconda'](https://docs.anaconda.com/free/miniconda/#latest-miniconda-installer-links) triant l'arquitectura de CPU adequada (Intel x86 / M1, M2, M3). Es recomana baixar la versió acabada en 'pkg'.

Executem el fitxer "Miniconda3-latest-MacOSX-x86_64.pkg" o "Miniconda3-latest-MacOSX-arm64.pkg" (depenent de l'arquitectura) i seguim els passos en pantalla.

Un cop finalitzat, executarem l'aplicació 'Terminal'. Es pot trobar a dins de la carpeta 'Altres' al menú d'aplicacions. També s'hi pot accedir utilitzant l'eina de cerca (Cmd+Espai) i escrivint 'Terminal'.

Seguidament, caldrà crea un 'entorn' per instal·lar-hi els requeriments de PyrVision sense trencar llibreries d'altres programes. Per fer-ho introduirem:

```bash
conda create --name pyrvision python=3.8
```

Quan ens pregunti si volem instal·lar els paquets amb 'Proceed ([y]/n)?' escriurem 'y' i presionarem 'Enter'.

Un cop creat l'entorn caldrà activar-lo per tal de treballar-hi. Escriurem:

```bash
conda activate pyrvision
```

Veurem que el començament de l'última línia ha passat de (base) a (pyrvision). Això ens indicarà que estem en l'entorn adequat.

Seguidament instal·larem les llibreries utilitzades per treballar amb intel·ligència artificial, seguint el mateix procediment que anteriorment:

```bash
conda install pytorch torchvision -c pytorch
```

```bash
conda install conda-forge::ultralytics
```

Finalment, instal·larem Jupyter Notebook, una eina per poder executar el codi de PyrVision i poder modificar-ne algunes opcions.

```bash
conda install -c conda-forge notebook
```

#### Descarregar PyrVision

Per descarregar el codi de PyrVision, executarem la següent comanda:

```bash
git clone https://github.com/ArnauCampanera/PyrVision.git
```

### Utilització

Per fer una classificació automàtica d'imatges seguirem els següents passos:
- Copiar totes les imatges que volem detectar a la carpeta "inbox" que trobarem a dins de la carpeta PyrVision.
- Obrirem la Terminal i executarem la següent comanda per obrir Jupyter Notebook
```bash
cd PyrVision			# Ens col·loquem dins de la carpeta de PyrVision
conda activate pyrvision 	# Activem l'entorn que hem creat durant la instal·lació
jupyter notebook		# Executem Jupyter Notebook
```
Se'ns obrirà el navegador d'internet que tinguem configurat per defecte i ens apareixerà el contingut de la carpeta PyrVision. Es recomana utilitzar Google Chrome. 

- Fem doble-click al fitxer init.ipynb perquè s'obri.
- A la barra de menú, anirem a 'Run' i buscarem l'opció 'Run All Cells'

El programa començarà a detectar les imatges. Depenent del volum i de al rapidesa de l'ordinador pot tardar més o menys. Podem fer l'estimació d'uns 10 seg per imatge en un ordinador normal.


#### Resultats

Un cop finalitzat buscarem a dins de PyrVision la carpeta 'predicted' on hi trobarem totes les imatges classificades per espècie, així com una carpeta anomenada 'nuls' amb les imatges on no s'hi ha detectat res.