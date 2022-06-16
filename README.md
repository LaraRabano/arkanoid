Para jugar

Clonar el repositorio
Crear un entorno virtual dentro de la raíz del repositorio
Instalar las dependencias
Arrancar el juego
# con ssh
git clone ssh://.....

# con https
git clone https://.....

cd arkanoid
python -m venv env

# windows
.\env\Scripts\activate

# linux / MacOs
source ./env/bin/activate

pip install -r requirements.txt

python main.py
Para colaborar en el proyecto

Clonar el repositorio
Crear un entorno virtual dentro de la raíz del repositorio
Instalar las dependencias
Abre el código en tu IDE favorito
# con ssh
git clone ssh://.....

# con https
git clone https://.....

cd arkanoid
python -m venv env

# windows
.\env\Scripts\activate

# linux / MacOs
source ./env/bin/activate

pip install -r requirements-dev.txt

# En VS Code
code .