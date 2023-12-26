# Pruebas para el parámetro firstName al crear un/a usuario/a en []

### En general
- El objetivo de este proyecto es la automatizacion de pruebas para comprobar la funcionalidad de el campo 'nombre' en el apartado para crear un nuevo kit en Urban.Groceries, al ejecutar las pruebas, no sera necesario crear manualmente un nuevo usuario pues el programa esta listo para crearlo e interceptar el auth_token por si mismo

### Para clonar el repositorio en tu computadora
- Abre tu consola e ingresa el siguiente comando : 'git clone git@github.com:username/qa-project-06.git'

### Pasos para la ejecucion de pruebas
1. Abre el archivo en PyCharm
2. Inicia el servidor del banco de pruebas para Urban.Groceries
3. Pegar la Url del banco de pruebas en el parametro 'URL_SERVICE' del archivo 'configuration.py'
4. Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
5. Ejecuta todas las pruebas con el comando 'pytest create_kit_name_kit_test.py'

