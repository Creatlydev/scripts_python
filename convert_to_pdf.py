
import os
from PIL import Image
from fpdf import FPDF




def convert_images_to_pdf(image_dir, output_path):
    # Obtener la lista de archivos en el directorio de imágenes
    image_files = [f for f in os.listdir(
        image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]

    # Ordenar los archivos de imágenes alfabéticamente
    image_files.sort()

    # Crear el objeto FPDF
    pdf = FPDF()

    # Recorrer cada archivo de imagen y agregarlo al PDF
    for image_file in image_files:
        # Abrir la imagen utilizando PIL
        image_path = os.path.join(image_dir, image_file)
        image = Image.open(image_path)

        # Obtener el tamaño de la imagen
        image_width, image_height = image.size

        # Calcular el tamaño máximo del PDF
        max_width = 210  # Ancho de página A4 en mm
        max_height = 297  # Alto de página A4 en mm

        # Calcular la escala de la imagen para ajustarla dentro de la página PDF
        scale = min(max_width / image_width, max_height / image_height)

        # Calcular la posición centrada de la imagen en la página PDF
        x = (max_width - (image_width * scale - 20)) / 2
        y = (max_height - (image_height * scale - 20)) / 2

        # Agregar una nueva página al PDF
        pdf.add_page()

        # Agregar la imagen al PDF, centrada
        pdf.image(image_path, x, y, image_width * scale - 20, image_height * scale - 20)

    # Guardar el PDF resultante
    pdf.output(output_path, 'F')
    print(f'Se ha creado el PDF: {output_path}')


# Ejemplo de uso
image_directory = 'D:/samir/Pictures/Saved Pictures'
output_pdf_path = 'C:/Users/samir/OneDrive/Escritorio/convert_pdf_result.pdf'
convert_images_to_pdf(image_directory, output_pdf_path)
