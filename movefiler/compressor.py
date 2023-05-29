from PIL import Image
import os
import shutil



def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format 
        e.g:
            >>> 1253656 => '1.20MB'
            >>> 1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            good_format= f"{b:.2f}{unit}{suffix}"
            if good_format.split('.')[1].startswith('00') :
                good_format= f"{b:.0f}{unit}{suffix}"
            return good_format
        b /= factor
    return f"{b:.2f}Y{suffix}"


def compress_img(path_image_src, path_image_dst, **kwrg):
    _kwarg = {
        'new_size_ratio': 1.0,
        'quality': 90,
        'width': None,
        'height': None,
        'to_jpg': False
    }
    # load the image to memory
    img = Image.open(path_image_src)
    if kwrg.get('new_size_ratio', 1.0) < 1.0:
        # if resizing ratio is below 1.0, then multiply width & height with this ratio to reduce image size
        img = img.resize((int(img.size[0] * kwrg.get('new_size_ratio', 1.0)), int(img.size[1] * kwrg.get('new_size_ratio', 1.0))), Image.LANCZOS)
    elif kwrg.get('width', None) and kwrg.get('height', None):
        # if width and height are set, resize with them instead
        img = img.resize((int(kwrg.get('width', 0)), int(kwrg.get('height', 0))), Image.LANCZOS) # Image.LANCZOS == Image.ANTIALIAS
    # split the filename and extension
    filename, ext = os.path.splitext(path_image_src)
    # make new filename appending _compressed to the original file name
    if kwrg.get('to_jpg', False):
        # change the extension to JPEG
        new_filename = f"{path_image_dst}_compressed.jpg"
    else:
        # retain the same extension of the original image
        new_filename = f"{path_image_dst}_compressed{ext}"
    try:
        # save the image with the corresponding quality and optimize set to True
        img.save(new_filename, quality=kwrg.get('quality', 90), optimize=True)
    except OSError:
        # convert the image to RGB mode first
        img = img.convert("RGB")
        # save the image with the corresponding quality and optimize set to True
        img.save(new_filename, quality=kwrg.get('quality', 90), optimize=True)


def move_files(downloadFolder, picturesFolder, musicFolder, videoFolder, documentsFolder, **kw) :

    for filename in os.listdir(downloadFolder) :
        pathFile = downloadFolder + filename 
        name, extension = os.path.splitext(filename) 
        if extension in ['.jpg', '.jpeg', '.png'] :
            compress_img(
                pathFile,
                picturesFolder + name,
                **kw
            )
            # picture = Image.open(pathFile)
            # picture.save(picturesFolder + 'compressed_' + filename, optimize= True, quality= 60)
            os.remove(pathFile)

        if extension in ['.mp3', '.ogg', '.wav'] :
            shutil.move(pathFile, musicFolder + filename)

        elif extension in ['.mp4', '.webm'] :
            shutil.move(pathFile, videoFolder + filename)

        elif extension in ['.docx', '.xlsx', '.pdf', '.pptx'] :
            shutil.move(pathFile, documentsFolder + filename)