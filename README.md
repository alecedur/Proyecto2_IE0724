# Proyecto2_IE0724

Este proyecto es un sitio web el cual se planea utilizar para manejar las citas de una clinica dental. En este proyecto se pueden 
crear usuarios los cuales pueden escoger la hora y el dentista que los va a atender. Ademas los usuarios normales pueden borrar citas.
Aparte de esto existen super usuarios los cuales tienen acceso a todas las citas y pueden crear borrar las citas que deseen.
Este proyecto se puede correr a traves de docker. 

## Librerias necesarias

Se necesitan las siguientes librerias:

-[Docker] 

-[docker-compose]

Para instalar docker compose se usa el siguiente comando:

```bash
sudo apt install docker-compose
```

## Uso

En la carpeta dentist, se corren los siguientes comandos:

```bash
make build
make compose-start
```

Luego ya se puede accesar a la pagina principal, copiando el link que se ve en la terminal y pegandolo en un web browser




