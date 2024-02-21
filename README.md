
# PyrVision


[English version](http://github.com/ArnauCampanera/PyrVision/README_en.md)



PyrVision és un model d'Intel·ligència Artificial desenvolupat al [Centre de Ciència i Tecnologia Forestal de Catalunya](https://www.ctfc.cat) amb la capacitat de detectar automàticament fins a 16 classes diferents.
PyrVision utilitza [YOLOv8](https://github.com/ultralytics/ultralytics/), l'estat de l'art dels models de detecció d'objectes, per tal de maximitzar precisió i rapidesa.

<div align="center">
  <img width="60%" src="https://github.com/ArnauCampanera/PyrVision/assets/159940202/bf3dd13b-a849-41c6-86c3-a59f3d8a8c64)">

</div>

## <div align="center">Documentació</div>

### Arquitectura del Model
PyrVision són, en realitat, dos models unificats; un per imatges en blanc i negre i un altre per imatges en color. 

Els mamífers del Pirineu tenen diferents hàbits . Algunes són més nocturnes, altres més diurnes i d'altres apareixen tant de dia com de nit. 
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


A continuació es detallen les instruccions per instal·lar i utilitzar PyrVision en funció de la plataforma que utilitzeu.

<details close>
<summary>Sistemes Apple amb macOS</summary>

### <div align="center">Instal·lació (macOS)</div>
Per poder utilitzar PyrVision localment cal instal·lar uns prerequisits. 

#### Prerequisits
Primer cal instal·lar ['miniconda'](https://docs.anaconda.com/free/miniconda/#latest-miniconda-installer-links) triant l'arquitectura de CPU adequada (Intel x86 / M1, M2, M3). Es recomana baixar la versió acabada en 'pkg'.

Executem el fitxer "Miniconda3-latest-MacOSX-x86_64.pkg" o "Miniconda3-latest-MacOSX-arm64.pkg" (depenent de l'arquitectura) i seguim els passos en pantalla.

Un cop finalitzat, executarem l'aplicació 'Terminal'. Es pot trobar a dins de la carpeta 'Altres' al menú d'aplicacions. També s'hi pot accedir utilitzant l'eina de cerca (Cmd+Espai) i escrivint 'Terminal'.

Seguidament, caldrà crea un 'entorn' per instal·lar-hi els requeriments de PyrVision sense trencar llibreries d'altres programes i que aquests puguin seguir funcionant independentment. Per fer-ho introduirem:

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

### <div align="center">Utilització</div>

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


### Resultats

Un cop finalitzat buscarem a dins de PyrVision la carpeta 'predicted' on hi trobarem totes les imatges classificades per espècie, així com una carpeta anomenada 'nuls' amb les imatges on no s'hi ha detectat res.



### <div align="center">Finalitzar</div>

Per finalitzar, anem a Jupyter Notebook. Si hem fet alguna modificació i volem que es mantingui per futures classificacions guardem els canvis mitjançant File > Save Notebook.

Per tancar el fitxer fem 'File > Close and Shut Down Notebook' i confirmem.

Fer finalitzar Jupyter Notebook fem 'File > Shut Down' i confirmem. Ara ja podem tancar la pestanya del navegador.

Per tancar la Terminal escriurem 'exit' i confirmarem. Ara ja podem tancar la Terminal.

</details>

<details close>
<summary>Sistemes Windows</summary>

### <div align="center">Instal·lació (Windows)</div>
Per poder utilitzar PyrVision localment cal instal·lar uns prerequisits. 

#### Prerequisits
##### Miniconda
Primer cal instal·lar ['miniconda'](https://docs.anaconda.com/free/miniconda/miniconda-other-installer-links/#windows-installers). Es recomana baixar la versió Python 3.10 .

Executem el fitxer descarregat i seguim els passos en pantalla.

Un cop finalitzada l'instal·lació trobarem al menú de Windows una nova carpeta anomenada 'Minoconda3 (64-bit)'. Executarem l'aplicació 'Anaconda Prompt (miniconda3)' i s'obrirà una pantalla de línia de comandes.

Seguidament, caldrà crea un 'entorn' per instal·lar-hi els requeriments de PyrVision sense trencar llibreries d'altres programes i que aquests puguin seguir funcionant independentment. Per fer-ho introduirem:

```bash
conda create --name pyrvision python=3.8
```

Quan ens pregunti si volem instal·lar els paquets amb 'Proceed ([y]/n)?' escriurem 'y' i presionarem 'Enter'.

Un cop creat l'entorn caldrà activar-lo per tal de treballar-hi. Escriurem:

```bash
conda activate pyrvision
```

Veurem que el començament de l'última línia ha passat de (base) a (pyrvision). Això ens indicarà que estem en l'entorn adequat.

Seguidament instal·larem les llibreries utilitzades per treballar amb intel·ligència artificial. Depenent de si el nostre equip conta amb una targeta gràfica (GPU) NVIDIA o no, haurem de fer servir una comanda o una altra.

- Si el nostre equip no té una GPU NVIDIA, o no n'estem segurs, executem la següent comanda:
```bash
conda install pytorch torchvision cpuonly -c pytorch
```

- Si el nostre equip té una GPU NVIDIA executem la següent comanda:

```bash
conda install pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia
```


Finalment, instal·lem Jupyter Notebook, una eina per poder executar el codi de PyrVision i poder modificar-ne algunes opcions.

```bash
conda install -c conda-forge notebook
```

#### Descarregar PyrVision

Per descarregar el codi de PyrVision, executem la següent comanda:

```bash
git clone https://github.com/ArnauCampanera/PyrVision.git
```
Això ens crearà la carpeta 'PyrVision' al nostre directori arrel (normalment amb el nom d'usuari).


### <div align="center">Utilització</div>

Per fer una classificació automàtica d'imatges seguim els següents passos:
- Copiar totes les imatges que volem detectar a la carpeta "inbox" que trobarem a dins de la carpeta PyrVision.
- Obrim l'aplicació 'Anaconda Prompt (miniconda3)' i executem la següent comanda per obrir Jupyter Notebook
```bash
cd PyrVision			# Ens col·loquem dins de la carpeta de PyrVision
conda activate pyrvision 	# Activem l'entorn que hem creat durant la instal·lació
jupyter notebook		# Executem Jupyter Notebook
```
Se'ns obrirà el navegador d'internet que tinguem configurat per defecte i ens apareixerà el contingut de la carpeta PyrVision. Es recomana utilitzar Google Chrome. 

- Fem doble-click al fitxer init.ipynb perquè s'obri.
- A la barra de menú, anirem a 'Run' i buscarem l'opció 'Run All Cells'

El programa començarà a detectar les imatges. Depenent del volum i de al rapidesa de l'ordinador pot tardar més o menys. Podem fer l'estimació d'uns 10 seg per imatge en un ordinador normal. Si disposem d'una GPU NVIDIA aquest temps es pot veure molt reduït, a 0.5 seg per imatge.


### Resultats

Un cop finalitzat buscarem a dins de PyrVision la carpeta 'predicted' on hi trobarem totes les imatges classificades per espècie, així com una carpeta anomenada 'nuls' amb les imatges on no s'hi ha detectat res.



### <div align="center">Finalitzar</div>

Per finalitzar, anem a Jupyter Notebook. Si hem fet alguna modificació i volem que es mantingui per futures classificacions guardem els canvis mitjançant File > Save Notebook.

Per tancar el fitxer fem 'File > Close and Shut Down Notebook' i confirmem.

Fer finalitzar Jupyter Notebook fem 'File > Shut Down' i confirmem. Ara ja podem tancar la pestanya del navegador.

Per tancar 'Anaconda Prompt (miniconda3)' escriurem 'exit' i confirmarem. Ara ja podem tancar l'aplicació.

</details>


### Opcions

#### Valor de confiança

Si observem que PyrVision s'està descuidant alguns animals i classificant la imatge com a buida, pot ser que el valor de confiança que li estem exigint al model sigui massa alt.

El valor de confiança és aquell que, en una escala de 0-1, indica com de segurs volem que estigui el model a l'hora de decidir si el que veu és un animal o no.

Si hi posem un valor molt alt (per exemple, 0.95) ens assegurarem que tot el que classifica és segurament correcte, però també és possible que es descuidi molts individus i que doni les imatges per buides, al no estar-ne molt segur.

Per contra, si li posem un valor molt baix (per exemple, 0.05) ens assegurarem de no deixar-nos cap individu, però alhora, també és possible que identifiqui branques o altres objectes com a animals si s'hi assemblen lleugerament.

Si volem canviar els valors de confiança del model haurem de modificar el fitxer 'init.ipynb'. Ho podem fer des de Jupyter Notebook.

Ens situem a la cel·la de codi d''Opcions de PyrVision'. Allà podem modificar els valors per defecte per cada model:
```python
conf_COLOR = 0.8
conf_BW = 0.6
```

#### Rectangle de detecció

Per defecte, PyrVision no dibuixa un rectangle al voltant de l'animal detectat. En cas que vulguem que ho faci, podem modificar la cel·la d'opcions dins del fitxer 'init.ipynb' amb Jupyter Notebook. Haurem de donar el valor de 'True' a la variable 'rectangle'.

```python
rectangle = True
```
