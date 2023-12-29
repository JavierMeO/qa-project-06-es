# Pruebas para el parámetro firstName al crear un/a usuario/a en []

### Acerca del proyecto

- El objetivo de este proyecto es la automatización de pruebas para comprobar la funcionalidad de el campo 'nombre' en el apartado para crear un nuevo kit en Urban.Groceries, al ejecutar las pruebas, no sera necesario crear manualmente un nuevo usuario pues el programa esta listo para crearlo e interceptar el auth_token por si mismo
- El proyecto contiene los siguientes archivos:
  1. configuration.py : Que contiene la URL al banco de datos asi como las rutas para la solicitud de la creacion del nuevo usuario y kit
  2. data.py : Donde se encuentran los datos necesarios para la creacion de un usuario y kit
  3. sender_stand_request.py : El archivo desde donde se envian las solicitudes
  4. create_kit_name_kit_test.py : Contiene una funcion que comprueba la creacion exitosa de un kit, y una segunda funcion para las pruebas negativas. Este archivo importa la clase kit_body desde 'data.py' para la ejecucion de pruebas.
  5. 
### Para clonar el repositorio en tu computadora

- Abre tu consola e ingresa el siguiente comando : 'git clone git@github.com:username/qa-project-06.git'

### Tecnologias

- Pycharm --Versión 2023.2.5
- Python --Versión 3.12.1
- Banco de pruebas para Urban.Groceries

### Librerias necesarias (pycharm)

- Pytest (Comando en terminal : pip install pytest)
- Requests (Comando en terminal : pip install requests)

### Pasos para la ejecucion de pruebas

1. Abre el archivo en PyCharm
2. Inicia el servidor del banco de pruebas para Urban.Groceries
3. Pegar la Url del banco de pruebas en el parametro 'URL_SERVICE' del archivo 'configuration.py'
4. Ejecuta todas las pruebas con el comando 'pytest create_kit_name_kit_test.py'


##### Meza Olivas Javier - 6To Sprint