# Litrevu
Développer une nouvelle application permet de demander ou publier des critiques de livres ou d’articles.

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



