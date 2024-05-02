Podrias corregir y ordenar:
<div align="center">
  <img src="https://res.cloudinary.com/murste/image/upload/v1698907632/stevolve_x8ioeu.png" alt="Stephen Murichu's Logo" width="100" />
</div>

# Gestión de inventario de Django
[![Licencia](https://img.shields.io/badge/Licencia-MIT-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Versión de Python](https://img.shields.io/badge/Python-3.10-green)](https://www.python.org/downloads/)

## Descripción
Este sistema está construido con Python (Django), JavaScript, Bootstrap, HTML y CSS. El sistema ofrece una interfaz de usuario amigable para usuarios generales y un backend seguro exclusivamente accesible para administradores. El backend recupera y muestra sin problemas datos vitales de la base de datos.

El sistema atiende a dos roles de usuario distintos: administradores y miembros del personal. Los administradores tienen el privilegio de iniciar sesión y gestionar la información de los productos, mientras que los miembros del personal manejan ventas, compras, facturas y creación de facturas.

Con una base de datos sqlite3, nuestro sistema no solo almacena toda la información esencial, sino que también cuenta con una interfaz de usuario amigable para una interacción sin esfuerzos. Los usuarios ingresan datos a través de esta interfaz y el sistema los procesa, generando información valiosa basada en la entrada del usuario. Además, el sistema archiva diligentemente los datos procesados en la base de datos para futuras referencias.

## Instalación

Antes de poder ejecutar la aplicación, asegúrate de tener los siguientes requisitos y dependencias:

- Docker

Para instalar la aplicación, sigue estos pasos:

1. Clona el repositorio:

   ```bash
   cd sales-and-inventory-management
   
2. Ejecuta el archivo setup.sh (Construye el contenedor Docker):

    ```bash
    ./bin/setup.sh

## Instalación

Antes de poder ejecutar la aplicación, asegúrate de tener los siguientes requisitos y dependencias:

- Docker

Además, necesitarás instalar las dependencias del archivo `requirements.txt`. Puedes hacerlo ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```
Configuración inicial
Una vez que hayas instalado las dependencias, asegúrate de ejecutar las migraciones para configurar la base de datos. Utiliza el siguiente comando:

```bash
python manage.py migrate
```
Después de ejecutar las migraciones, necesitarás crear un superusuario para acceder al panel de administración. Puedes hacerlo con este comando y siguiendo las instrucciones en pantalla:

```bash
python manage.py createsuperuser
```
Agregar datos a las tablas
Para agregar datos a las tablas store_category y accounts_vendor, puedes hacerlo manualmente a través del panel de administración o utilizando un script de gestión personalizado. Por ejemplo, podrías crear un script populate_data.py y ejecutarlo con el siguiente comando:

El contenido de populate_data.py sería algo así:

# Agregar más datos si es necesario
Ejecutar la aplicación Django
Una vez que hayas completado todos los pasos anteriores, puedes ejecutar la aplicación Django con el siguiente comando:

```bash
python manage.py runserver
```
## Capturas de pantalla

## Screenshots

![Screenshot (47)](https://user-images.githubusercontent.com/51537638/218985189-8ca2046e-02a8-4c8b-8243-0027fbfd728c.png)

![Screenshot (48)](https://user-images.githubusercontent.com/51537638/218985199-dfd74679-006a-4fe7-bd9a-fc1f244b8a5f.png)

![Screenshot (49)](https://user-images.githubusercontent.com/51537638/218985218-2c00c2f4-bf8a-4ab0-88cf-b374bcf1cdb2.png)

![Screenshot (50)](https://user-images.githubusercontent.com/51537638/218985221-3af9c58f-1015-4e3d-99b6-a93f1586d5aa.png)

![Screenshot (51)](https://user-images.githubusercontent.com/51537638/218985224-544832e1-938e-4b18-aec8-2efe8f55415e.png)

![Screenshot (52)](https://user-images.githubusercontent.com/51537638/218985242-e52fe221-3fb7-4393-b205-8d930f673037.png)

![Screenshot (53)](https://user-images.githubusercontent.com/51537638/218985248-2a2864a1-7b07-40b0-ab28-fdb3d40b0742.png)

![Screenshot (54)](https://user-images.githubusercontent.com/51537638/218985262-ce21da7e-dc14-47f2-b31d-94de04b49bb7.png)

![Screenshot (37)](https://user-images.githubusercontent.com/51537638/218985266-2bdf70a6-8f41-4e07-bafb-3cb97562ef85.png)

![Screenshot (38)](https://user-images.githubusercontent.com/51537638/218985272-1773c6af-db04-4221-9149-8b56f50638df.png)

![Screenshot (39)](https://user-images.githubusercontent.com/51537638/218985280-7a6a8116-6cdb-4281-9aae-a036a0c42157.png)

![Screenshot (40)](https://user-images.githubusercontent.com/51537638/218985289-d50e317c-a4c8-4546-88c9-b71a03e0cb37.png)

![Screenshot (41)](https://user-images.githubusercontent.com/51537638/218985303-a61516c4-b28d-4807-909e-761d820dc60c.png)

![Screenshot (42)](https://user-images.githubusercontent.com/51537638/218985321-fe56bfcf-2498-4ed0-bc7c-1611b7e9b2cd.png)

![Screenshot (43)](https://user-images.githubusercontent.com/51537638/218985330-ba9eea5c-ee39-4f5c-8cd4-5e9fadeb4e24.png)

![Screenshot (44)](https://user-images.githubusercontent.com/51537638/218985343-5dcb504a-0096-4138-9572-0f293ef25d98.png)

![Screenshot (45)](https://user-images.githubusercontent.com/51537638/218985351-356f0f61-f3e5-480b-ab88-9818cbfb91c1.png)

![Screenshot (46)](https://user-images.githubusercontent.com/51537638/218985357-fc0e7f3b-5729-4a32-95b3-c016aa48c219.png)

...
 (Se omiten algunas capturas de pantalla por brevedad)

## Autores

- [Eliazar Noa ]

                                            ¡Feliz codificación! 🚀