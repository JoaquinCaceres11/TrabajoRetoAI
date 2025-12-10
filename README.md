# Proyecto OCR con Tesseract

## Descripción
Este proyecto permite procesar imágenes para extraer texto automáticamente mediante **OCR**. Se eligió la opción **Tesseract** para el reconocimiento óptico de caracteres.  
La API está construida con **FastAPI** y ofrece un endpoint `/extract` que recibe imágenes (multipart/form-data) y devuelve un JSON con el texto extraído.

## Tecnologías utilizadas
- **Python 3.x**  
- **FastAPI**  
- **pytesseract**  

## Instalación y ejecución
# 1. Clonar el repositorio:
git clone <URL_DEL_REPOSITORIO>
cd TrabajoRetoIA


# 2. Crear y activar el entorno virtual:
python -m venv venv
# Windows PowerShell
    .\venv\Scripts\activate
# Linux / macOS
    source venv/bin/activate


# 3. Instalar dependencias:
pip install -r requirements.txt



# 4. Iniciar el servidor:

uvicorn main:app --reload

El servidor estará disponible en `http://127.0.0.1:8000` y listo para recibir solicitudes en el endpoint `/extract`.