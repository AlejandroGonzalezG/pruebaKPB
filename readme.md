## Instrucciones para la ejecución de cada pregunta. Pueden ir incluidos para cada pregunta comentarios sobre el alcance o cosas que pudiesen haber faltado.

### Pregunta 1

Ejecutar archivo function.py el cual le haara la request a la api y hará un print de las respuestas a las preguntas planteadas.
El script se puede ejecutar con ´python function.py´

### Pregunta 2

Se adjuntan las preguntas y las sentencias SQL correspondientes en un archivo txt.

### Pregunta 3

Aquí se realizarán algunos comentarios respecto al alcance de la solución.
Primero, se debe ingresar a la carpeta con ´cd pruebaKPB/Pregunta3/integrations_erp´, luego se buildean los contenedores con ´docker-compose build´,
se levantan los contenedores ´docker-compose up -d´, y se aplican las migraciones con ´docker exec -it integrations_erp_web_1 python manage.py migrate´,
con esto ya podemos ejecutar el script con ´docker exec -it integrations_erp_web_1 python /code/posts/jsonplaceholder_api.py´ el cual
ira a la API de jsonplaceholder y creará los objetos según lo indicado.
Entre las consideraciones se puede comentar que se habilito el Admin de Django, por lo que, se pueden revisar los datos creados en la db ingresando
a ´http://localhost:8000/admin/´, para ello, se necesita un superuser, el cual se puede crear (teniendo los contenedores arriba) con
´docker-compose exec web python manage.py createsuperuser´. Con el usuario creado podremos ingresar al Admin de Django.
Dentro de las indicaciones, se solicitaba el crear algún método para actualización diaria. No he trabajado con funciones que se ejecuten directamente
en la nube, pero lo que podría plantear como solución es crear contenedores para ejecutar tareas cronometradas (levantar un container para celery,
beat y redis), con eso se podrían ejecutar funciones indicandole al beat el tiempo de ejecución.
Respecto a la base de datos, no había trabajado con una modelada en forma de estrella. En ese sentido, cree una tabla Fact que es la central que posee
las relaciones a las DimUsers y DimPosts, en donde la DimUsers posee sus relaciones con DimAddress y DimCompany.

### Pregunta 4

Se adjuntan las preguntas y las sentencias SQL correspondientes en un archivo txt.
