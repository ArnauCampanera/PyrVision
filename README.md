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
Per poder utilitzar PyrVision localment cal instal·lar uns prerequisits. Primer cal instal·lar ['miniconda'](https://docs.anaconda.com/free/miniconda/#latest-miniconda-installer-links) triant l'arquitectura de CPU adequada (Intel x86 / M1, M2, M3). Es recomana baixar la versió acabada en 'pkg'.

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

