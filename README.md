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

  
