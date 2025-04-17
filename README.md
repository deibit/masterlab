## Readme

Esta aplicación posee multitud de fallos a propósito para el aprendizaje de vulnerabilidades web y no está pensada para su puesta en
producción.

Su uso es estrictamente educativo.

### Descargo

Este repositorio ha sido creado exclusivamente con fines educativos y de aprendizaje sobre vulnerabilidades web y técnicas de seguridad informática.

El autor no se responsabiliza por el uso indebido de este contenido.

Cualquier acción realizada con base en este material debe estar enmarcada en un entorno controlado y legalmente autorizado.

No está permitido utilizar este código o conocimiento en sistemas que no te pertenezcan o sin el consentimiento explícito del propietario.

El uso de estas herramientas fuera de un entorno de laboratorio puede constituir una actividad ilegal. Utilízalo bajo tu propia responsabilidad.

### Imagen docker

`cd docker`

`docker build -t masterlab:latest`

### Arrancar el lab

`docker compose up -d` o `docker-compose up -d`

### Scripts auxiliares:

El script `scripts/clean_database.sh` reinicia la base de datos de la
aplicación. Sirve para limpiar los datos de esta y reiniciarlos a origen.

El script `scripts/fix_imgs_permissions.sh` cambia el propietario de la carpeta "imgs" dentro del contenedor
del servicio `ml_1`. Esto solo es necesario si te está dando problemas en caso
de que encuentres el RFI y no puedas subir nada.
