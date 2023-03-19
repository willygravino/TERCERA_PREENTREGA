# TERCERA_PREENTREGA
TERCERA PREENTREGA GUILLERMO GRAVINO

## Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Instalación 🔧

Para probar el código, antes de ejecutarlo, se deberá hacer las migraciones necesarias que puedan crear la base de datos con la cual se trabajará. Eso se hace ejecutando los comandos:

python manage.py makemigrations
python manage.py migrate

Tras realizarlo se creará la base de datos y ya se estará en condiciones de ejecutar el código en el host local con el comando:

python manage.py runserver

Al acceder a la url "/principal", podrás ir seleccionando alguno de los tres formularios a través de los que podrás ingresar los diferentes datos a ser cargados en la base de datos. 

En el formulario de búsqueda de la barra de navegación se podrá ingresar un nombre de Estudiante, y listará los nombre de estudiantes que forman parte de la base de datos, que coincidan con este nombre ingresado.

En la opción ">> Busqueda en una página nueva" se abrirá una nueva página con un formulario de búsqueda para realizar una busqueda por "nombre de estudiante".
