
<h2 align="center">Sistema simple de recomendación de películas</h2>
<h4 align="center">Algoritmo de filtrado colaborativo (FC) para recomendación de películas</h4>

<p align="center">
 <a href="https://www.python.org/downloads/">
    <img alt="Python - Python Version" src="https://img.shields.io/github/pipenv/locked/python-version/quiquereds/movieRecommender?style=for-the-badge">
  </a>
 <a href="https://numpy.org/doc/stable/">
    <img alt="Numpy" src="https://img.shields.io/github/pipenv/locked/dependency-version/quiquereds/movieRecommender/numpy?style=for-the-badge">
  </a>
  <a href="https://pandas.pydata.org/docs/index.html">
    <img alt="Pandas" src="https://img.shields.io/github/pipenv/locked/dependency-version/quiquereds/movieRecommender/pandas?style=for-the-badge">
  </a>
  <a href="https://matplotlib.org/">
    <img alt="Matplotlib" src="https://img.shields.io/github/pipenv/locked/dependency-version/quiquereds/movieRecommender/matplotlib?style=for-the-badge">
  </a>
  <a href="https://seaborn.pydata.org/">
    <img alt="Seaborn" src="https://img.shields.io/github/pipenv/locked/dependency-version/quiquereds/movieRecommender/seaborn?style=for-the-badge">
  </a>
  <a href="https://scikit-learn.org/stable/getting_started.html">
    <img alt="Scikit Learn" src="https://img.shields.io/github/pipenv/locked/dependency-version/quiquereds/movieRecommender/scikit-learn?style=for-the-badge">
  </a>
</p>


___

## <img align="left" alt="Eyes" width="35px" style="padding-right:10px;" src="https://user-images.githubusercontent.com/70863031/214644849-1240d6f2-329f-46a9-8bc4-458d3d215ef8.gif"/> Descripción

Este proyecto implementa un **sistema de recomendación de películas** utilizando el **algoritmo de filtrado colaborativo basado en contenido** con la técnica de **K-Nearest Neighbors (KNN)**. Los sistemas de recomendación son herramientas que sugieren ítems a los usuarios basándose en sus interacciones previas. En este caso, el sistema, dada una película de entrada, busca películas con características similares y que hayan sido calificadas de forma similar entre los usuarios.

Este proyecto es ideal para quienes desean explorar el uso de la inteligencia artificial en sistemas de recomendación y aprender a implementar soluciones con datasets del mundo real como **MovieLens**.


### Construido con:

El proyecto está desarrollado con las siguientes librerías y herramientas:

- **Python 3.12+**
- [**Dataset MovieLens**](https://grouplens.org/datasets/movielens/) (Conjunto de datos para investigación de sistemas de recomendación)
- **Jupyter Notebook**

---

## <img align="left" alt="Gear" width="35px" style="padding-right:10px;" src="https://fonts.gstatic.com/s/e/notoemoji/latest/2699_fe0f/512.webp"/> Clona el repositorio

A continuación, se detallan los pasos para configurar este proyecto localmente y ejecutarlo.

### Requisitos Previos:

- Instalar [**Python 3.12+**](https://www.python.org/) en tu sistema y su variable de entorno agregada al PATH.
- Tener instalado el sistema de versiones [**Git**](https://git-scm.com/) para clonar este repositorio.
- Tener instalado el editor de código [**VS Code**](https://code.visualstudio.com/) para trabajar con el código.
- Tener instaladas las extensiones de Python y Jupyter para activar el soporte de estas herramientas en el editor de código.
- Instalar `pipenv` para trabajar con entornos virtuales de Python

```bash
pip install pipenv
```

### Empezando:

1. Utiliza git desde un directorio de tu preferencia para descargar el código a tu computadora

```bash
git clone https://github.com/quiquereds/movieRecommender.git
```

2. Navega al directorio del proyecto generado

```bash
cd movieRecommender
```

3. Utiliza `pipenv` para descargar las librerías definidas en el pipfile

```bash
pipenv install
```

4. Activa el entorno virtual y verifica que tu interprete de Python haya cambiado

```bash
pipenv shell
```
>[!NOTE]
> Al estar trabajando con un Jupyter Notebook, deberás verificar o seleccionar manualmente el kernel para ejecutar los fragmentos de código de Python, este kernel hace referencia al interprete.


## <img align="left" alt="Pencil" width="35px" style="padding-right:10px;" src="https://fonts.gstatic.com/s/e/notoemoji/latest/270f_fe0f/512.webp"/> Uso de LaTeX dentro de VS Code

Para la difusión de la experimentación, se redactó un artículo en proceso de envío a revista indizada por el Conahcyt, donde para ello, se utilizó LaTeX para la redacción y generación del archivo PDF.

Existen múltiples herramientas para trabajar con LaTeX, sin embargo, las interfaces carecen del poder que tiene VS Code con sus extensiones. Por ello, aquí se enlistan los pasos para trabajar con LaTeX desde VS Code.

### 1. Instalar MikTeX:

- Descargar e instalar [MiKTeX](https://miktex.org/download) (macOS, Linux y Windows).
- Durante la instalación, seleccionar la opción de instalar paquetes automáticamente.

### 2. Instalar StrawberryPerl (solo Windows)
- Descargar e instalar [Strawberry Perl](https://strawberryperl.com/). Esto es necesario para que algunas funcionalidades avanzadas de LaTeX se ejecuten correctamente.

### 3. Descargar LaTeX Workshop
- En VS Code, abre la tienda de extensiones y busca LaTeX Workshop. Instala esta extensión para habilitar el soporte completo de LaTeX dentro del editor.

### 4. Compilación del archivo .tex

- Una vez instalada la extensión, abre tu archivo `.tex` en VS Code y compílalo utilizando la opción Build LaTeX Project que aparece en la barra de tareas o con el atajo de teclado `Ctrl + Alt + B` (Windows/Linux) o `Cmd + Alt + B` (macOS).

---

## <img align="left" alt="Rocket" width="35px" style="padding-right:10px;" src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f44b_1f3fb/512.webp"/> Autores


- **F. Maxwell Harper and Joseph A. Konstan** - MovieLens Dataset

---

### <img align="left" alt="Rocket" width="35px" style="padding-right:10px;" src="https://user-images.githubusercontent.com/70863031/215303334-56d6d712-055a-4704-ab00-2a8d9538e974.gif"/> Lenguajes y herramientas utilizadas 

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://go-skill-icons.vercel.app/api/icons?i=python,numpy,pandas,matplotlib,seaborn,scikitlearn,perl,latex,vscode,jupyter&perline=8" />
  </a>
</p>