![image](litRevu/static/images/LITrevu_banner.png)

# LITRevu


![Python](https://img.shields.io/badge/python-3.11.x-green.svg)
![Django](https://img.shields.io/badge/django-5.0.2.x-green.svg)

[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Flake8](https://img.shields.io/badge/flake8-checked-blueviolet)](https://flake8.pycqa.org/en/latest/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Djhtml](https://img.shields.io/badge/Django-HTML-Teal)](https://(https://github.com/rtts/djhtml))

Développer une nouvelle application permet de demander ou publier des critiques de livres ou d’articles.
L'application permet de demander ou publier des critiques de livres ou d’articles. L’application présente trois cas d’utilisation principaux :

1- la publication des critiques de livres ou d’articles ;
2- la demande des critiques sur un livre ou sur un article particulier ;
3- la recherche d’articles et de livres intéressants à lire, en se basant sur les critiques des autres.


Vous pouvez vous référer aux documents du projet dans le dossier docs

* __[La specification](spec/)__
* __[Consulter le cahier des charges](spec/Cahier_des_charges.pdf)__

- [Litrevu](#litrevu)
- [Cloner le dépôt du projet:](#cloner-le-dépôt-du-projet)
- [Aller sur le bon répertoire:](#aller-sur-le-bon-répertoire)
- [Installer l'environnement virtuel:](#installer-lenvironnement-virtuel)
- [Installer les dépendances et django:](#installer-les-dépendances-et-django)
- [Lancer le programme:](#lancer-le-programme)
- [Installer et run flake8:](#installer-et-run-flake8)
- [Aller sur l'applicaton:](#aller-sur-lapplicaton)

# Cloner le dépôt du projet:

`git clone https://github.com/boulila-n/litRevu`
  
# Aller sur le bon répertoire:

`cd LitRevuP9`

# Installer l'environnement virtuel:

`python3 -m venv venv`<br />
`source ./venv/bin/activate` (UNIX)<br />
`./venv/scripts/activate` (windows)

# Installer les dépendances et django:

`pip install -r requirements.txt`

## Usage

* Le projet est fourni avec une base de données exemple avec 3 utilisateurs :
    * __name :__ test1 __password :__ 123abcd*
    * __name :__ test2 __password :__ 123abcd*
    * __name :__ test3 __password :__ 123abcd*
* Un super utilsateur : 
    * __name :__ admin __password :__ 123abcd*

# Lancer le programme:

`cd litRevu`<br />
`py manage.py runserver` (windows)<br />
`python3 manage.py runserver` (UNIX)

# Installer et run flake8:

`pip install flake8`<br />
`flake8 --exclude .git,__pycache__,env/,*/migrations/,*/settings.py > .\flake8_report.txt`

# Aller sur l'applicaton:

`http://127.0.0.1:8000/`<br />
`http://127.0.0.1:8000/admin` (administration)



