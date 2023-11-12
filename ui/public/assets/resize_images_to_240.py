from PIL import Image
import os

def resize_images_in_folder(folder_path, output_folder, size=(240, 240)):
    """ Resize all images found in folder_path to the specified size and save them to output_folder. """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            img = Image.open(image_path)
            img = img.resize(size, Image.LANCZOS)

            output_path = os.path.join(output_folder, filename)
            img.save(output_path)

# Usage
folder_path = '.'
resize_images_in_folder(folder_path, folder_path, size=(240, 240))
