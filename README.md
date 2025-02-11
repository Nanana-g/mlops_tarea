# MLOps Tarea - Práctica Git

Este proyecto contiene dos APIs simples creadas con FastAPI.

## Endpoints
- **POST /user**: Guarda un usuario en una lista.
- **GET /user**: Obtiene la lista de usuarios guardados.

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Nanana-g/mlops_tarea.git
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el servidor:
   ```bash
   uvicorn main:app --reload
   ```

## Uso
- Para guardar un usuario:
  ```bash
  curl -X POST "http://127.0.0.1:8000/user?name=John"
  ```
- Para obtener la lista de usuarios:
  ```bash
  curl "http://127.0.0.1:8000/user"
  ```
