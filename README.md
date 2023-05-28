# API-EgoDesign-PruebaTecnica
API de autos para prueba técnica de Ego Design

## Como iniciar en local
 ```sh
git clone git@github.com:carlosmperilla/API-EgoDesign-PruebaTecnica.git
python -v venv venv
venv\Scripts\activate
cd API-EgoDesign-PruebaTecnica
pip install -r requirements.txt
cd egoautos
python -m manage runserver
```

## Superusuario Admin
Ingresando a http://127.0.0.1:8000/admin/  
Con las siguientes credenciales:  
> Usuario: Carlos  
> Constraseña: 12345  
Se puede gestionar (Ingresar, actualizar, y eliminar) los modelos de autos.

## API con los modelos
http://127.0.0.1:8000/api/v1/modelos-autos/
Desde la API en el Browser se puede hacer el CRUD, directamente desde el navegador.

## Formas de ordenar o buscar en la API mediante Query-params
Para ordenar de más viejo a más nuevo:
> /modelos-autos/?ordering=anio

Para ordenar de más nuevo a más viejo:
> /modelos-autos/?ordering=-anio

Para ordenar de más barato a más costoso:
> /modelos-autos/?ordering=precio

Para ordenar de más costoso a más barato:
> /modelos-autos/?ordering=-precio

Para buscar por nombre (puede ser todo el nombre o una parte):
> /modelos-autos/?search=nombremodelo
