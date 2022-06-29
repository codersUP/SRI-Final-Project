# SRI-Final-Project

Diseño, implementación, evaluación y análisis de un sistema de recuperación de la información

## Dependencias :gear:

Las dependencias necesarias para la ejecución del proyecto se hallan en el archivo `requirements.txt`. Puede ejecutar el comando:

```
make install
```

para ello o simplemente `make` (puesto que install es la regla por defecto)

## Modo de uso :computer:

Para la ejecución de la aplicación utilice el comando:

```
make run
```

Se le brindará la posibilidad al usuario de escribir tantas consultas como desee; para cada una se deberá obtener una lista con los documentos más relevantes, según el modelo llevado a cabo

### Ideas principales de implementación

El Modelo de Recuperación de Información que se llevó a cabo fue el modelo vectorial. Este modelo permite otorgar un ranking a cada documento de acuerdo con su grado de similitud a la consulta realizada.

En primer lugar se llevó a cabo un preprocesamiento de las palabras presentes en los documentos del set de datos, utilizando la biblioteca **spacy**. Esta transforma las palabras del texto en _tokens_; brinda facilidades para eliminar stopwords, tales como : símbolos de puntuación, números, conjunciones, preposiciones y otras. Luego se aplica _lemmatize_, proceso lingüístico para hallar la forma básica (el lema) de una palabra. Esto favorece la generación de un diccionario que contiene,por cada documento, la cantidad total de tokens por la que está compuesto y por cada token, su frecuencia en dicho documento; lo que permitirá más tarde, el cálculo del ranking de cada uno.

Después del análisis de los documentos, se realiza un análisis similar por cada consulta. Dada la consulta, se pasa al cálculo de la similitud entre esta y los documentos, definido a través del modelo vectorial como:

    $sim(d_j, q) = \frac{\sum_{i = 1}^{n} w_{i, j} \times w_{iq}}{\sqrt{\sum_{i = 1}^{n} w_{i, j}^2} \times \sqrt{\sum_{i = 1}^{n} w_{iq}^2}}$

donde:

- $sim(d_j, q)$ define la similitud entre el j-ésimo documento y la consulta dada
- $w_{i, j}$ define la frecuencia del token i-ésimo en el j-ésimo documento
- $w_{iq}$ define la frecuencia del token i-ésimo en la consulta.

Tras este cálculo de ranking se ordenan los documentos de forma decreciente según su puntuación y se retornan al usuario en ese orden, ya sea todos los documentos o una cantidad predeterminada de ellos.

En particular, actualmente no se realiza este proceso por todos los documentos, sino por un subconjunto que está definido en `files_path.json`, puesto que el código implementado carece de optimizaciones por lo que el análisis de todos los documentos del juego de datos tomaría demasiado tiempo. De ellos solo se muestran al usuario los 3 documentos más relevantes.

## Integrantes:

- Enrique Martínez González C-512
- Carmen Irene Cabrera Rodríguz C-512
- Osmany Perez C-512
