# pi api

test en python 3.9 con jwt y archivo docker


## Instalacion 

al iniciar este proyecto por primera vez se debe ejecutar el sig. comando

```bash
pip3  install Flask python-dotenv pyjwt
```
iniciar con el ide y debe levantar en el puerto 4000

## Request

se debe en primera instancia generar un token en la para esto se debe acceder a :

[http://127.0.0.1:4000/login](http://127.0.0.1:4000/login)

en esta peticion POST se debe agregar un body:

```
{
    "username": "shin",
    "password" : "say_hi!_hi_shin_chan"
}
```

esto debe generar un token que colocaremos en Authorization Bearer token

para ejecutar el ejercicio luego de generar el token se debe ir al endpoint:

[http://127.0.0.1:4000/pi/]( http://127.0.0.1:4000/pi/)
y se debe agregar un número al final de la peticion

ejemplo: 

[http://127.0.0.1:4000/pi/8](http://127.0.0.1:4000/pi/8)

 



## 