import os
import subprocess
import argparse
import logging
from pyfiglet import Figlet


class Metadata:
    """
    Clase para gestionar los metadatos de un archivo multimedia.
    """

    def __init__(self, title, genre=None, show=None, season_number=None, episode_id=None):
        self.title = title
        self.genre = genre
        self.show = show
        self.season_number = season_number
        self.episode_id = episode_id

    def to_ffmpeg_args(self):
        """
        Convierte los metadatos en una lista de argumentos para FFmpeg.
        """
        args = []
        if self.title:
            args += ["-metadata", f"title={self.title}"]
        if self.genre:
            args += ["-metadata", f"genre={self.genre}"]
        if self.show:
            args += ["-metadata", f"show={self.show}"]
        if self.season_number:
            args += ["-metadata", f"season_number={self.season_number}"]
        if self.episode_id:
            args += ["-metadata", f"episode_id={self.episode_id}"]
        return args


class FFmpegProcessor:
    """
    Clase para ejecutar comandos FFmpeg y modificar metadatos de un archivo multimedia.
    """

    def __init__(self, debug=False):
        self.debug = debug
        self.logger = logging.getLogger("FFmpegProcessor")
        if self.debug:
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.INFO)

    def process_file(self, input_file, metadata: Metadata, output_file):
        """
        Ejecuta FFmpeg para añadir metadatos al archivo multimedia.
        """
        command = ["ffmpeg", "-i", input_file] + metadata.to_ffmpeg_args() + ["-c", "copy", output_file]

        if self.debug:
            self.logger.debug(f"FFmpeg Command: {' '.join(command)}")

        try:
            subprocess.run(command, check=True)
            self.logger.info(f"Archivo procesado correctamente: {output_file}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Error al procesar el archivo: {e}")
            raise


class FileManager:
    """
    Clase para gestionar archivos.
    """
    @staticmethod
    def extract_filename_without_extension(file_path):
        """
        Extrae el nombre del archivo sin la extensión.
        """
        return os.path.splitext(os.path.basename(file_path))[0]


class Application:
    """
    Clase principal para ejecutar la aplicación.
    """

    def __init__(self, debug=False):
        self.ffmpeg_processor = FFmpegProcessor(debug=debug)

    def run(self, input_file, output_file=None, genre=None, show=None, season_number=None, episode_id=None):
        """
        Corre la aplicación para modificar los metadatos del archivo.
        """
        # Extraer el nombre del archivo sin extensión para usarlo como título
        title = FileManager.extract_filename_without_extension(input_file)

        # Crear la metadata
        metadata = Metadata(
            title=title,
            genre=genre,
            show=show,
            season_number=season_number,
            episode_id=episode_id
        )

        # # Definir el archivo de salida si no se proporciona
        if output_file is None:
            os.rename(input_file, f"{title}_original.mp4")
            input_file = f"{title}_original.mp4"
            output_file = f"{title}.mp4"

        # Procesar el archivo
        print(input_file, output_file)
        self.ffmpeg_processor.process_file(input_file, metadata, output_file)


def parse_arguments():
    """
    Función para analizar los argumentos de línea de comandos.
    """
    parser = argparse.ArgumentParser(description="Script para modificar metadatos de archivos MP4 usando FFmpeg.")
    parser.add_argument("input_file", help="Ruta al archivo MP4 de entrada.")
    parser.add_argument("-o", "--output", help="Nombre del archivo de salida (opcional).")
    parser.add_argument("-g", "--genre", help="Género del contenido.")
    parser.add_argument("-sh", "--show", help="Nombre de la serie.")
    parser.add_argument("-se", "--season", type=int, help="Número de la temporada (si aplica).")
    parser.add_argument("-e", "--episode", type=int, help="Número del episodio (si aplica).")
    parser.add_argument("-d", "--debug", action="store_true", help="Activar modo debug para ver más información.")

    return parser.parse_args()


if __name__ == "__main__":
    # Title
    f = Figlet(font='slant')
    print(f.renderText('MP4 Tag'))
    # Parsear los argumentos de la línea de comandos
    args = parse_arguments()

    # Inicializar y ejecutar la aplicación
    app = Application(debug=args.debug)
    app.run(
        input_file=args.input_file,
        output_file=args.output,
        genre=args.genre,
        show=args.show,
        season_number=args.season,
        episode_id=args.episode
    )
