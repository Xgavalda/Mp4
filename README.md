# MP4 Metadata Tagger

`mp4tag.py` es un script en Python que permite modificar los metadatos de archivos MP4 usando `FFmpeg`. Puedes agregar etiquetas como el título, género, serie, temporada y episodio a archivos MP4. También admite personalización del nombre del archivo de salida y cuenta con un modo de depuración para ver información detallada sobre el proceso.

## Requisitos

- Python 3.6 o superior
- `FFmpeg` instalado en tu sistema.

### Instalación de `FFmpeg`

**Linux** (Debian/Ubuntu):

    sudo apt-get install ffmpeg

**MacOS (usando Homebrew):**

    brew install ffmpeg

**Windows:**

    Descarga el binario desde la página oficial de FFmpeg y asegúrate de que ffmpeg esté disponible en el PATH.**

## Instalación
Clona el repositorio o descarga el archivo mp4tag.py.

Asegúrate de tener instaladas las dependencias de Python. Puedes instalar argparse si no lo tienes ya:

```bash
    pip install argparse
```

## Uso
Ejecuta el script mp4tag.py desde la línea de comandos para modificar los metadatos de un archivo MP4.

### Parámetros
    input_file: Ruta al archivo MP4 de entrada (requerido).
    --output: Nombre del archivo de salida (opcional). Si no se proporciona, se usará output_{nombre_sin_extensión}.mp4.
    --genre: Género del contenido (opcional).
    --show: Nombre de la serie (opcional, para series).
    --season: Número de la temporada (opcional, para series).
    --episode: Número del episodio (opcional, para series).
    --debug: Activa el modo debug para mostrar más información detallada sobre el proceso.
## Ejemplos
Modificando solo el título (usando el nombre del archivo sin extensión como título):

```bash
python mp4tag.py entrada.mp4
```

Esto generará un archivo output_entrada.mp4 con el título basado en el nombre del archivo entrada.mp4.

Modificando título, género, y generando un archivo de salida personalizado:

```bash
python mp4tag.py entrada.mp4 --output "mi_pelicula.mp4" --genre "Acción"
```
Esto creará un archivo mi_pelicula.mp4 con el título entrada y el género "Acción".

Añadiendo metadatos de serie (nombre de serie, temporada, episodio):
```bash
python mp4tag.py entrada.mp4 --show "Mi Serie" --season 1 --episode 2
Esto genera un archivo output_entrada.mp4 con el título entrada, la serie "Mi Serie", temporada 1 y episodio 2.
```

Activando el modo debug:

```bash
python mp4tag.py entrada.mp4 --debug`
```
Esto mostrará información detallada sobre el comando FFmpeg ejecutado y el progreso.

## Contribución
Si encuentras algún problema o tienes sugerencias, por favor, abre un "Issue" o envía un "Pull Request". Todas las contribuciones son bienvenidas.

## Licencia
Este proyecto está licenciado bajo la licencia MIT. ¡Siéntete libre de usarlo, modificarlo y distribuirlo!

¡Gracias por usar mp4tag.py! Si tienes alguna pregunta o sugerencia, no dudes en contactarnos.