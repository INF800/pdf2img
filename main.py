import os, config
from pdf2image import convert_from_path

os.makedirs(f"{config.EXTRACTED_IMGS_FOLDER}", exist_ok=True)
main_folder = os.listdir(config.PDFS_FOLDER)
for folder in main_folder:
    
    # save images in folders which are named after every pdf file
    # inside category folders in main folder
    os.makedirs(f"{config.EXTRACTED_IMGS_FOLDER}/{folder}", exist_ok=True)
    
    for pdffile in os.listdir(f"{config.PDFS_FOLDER}/{folder}"):
        if pdffile.split(".")[1].lower() == 'pdf':
            pdf_path = f"{config.PDFS_FOLDER}/{folder}/{pdffile}"
            print('DEBUG ', pdf_path)
            # pdf = os.listdir(pdfs_path)
            os.makedirs(f"{config.EXTRACTED_IMGS_FOLDER}/{folder}/{pdffile}", exist_ok=True)
                
            saved_imgs_path = f"{config.EXTRACTED_IMGS_FOLDER}/{folder}/{pdffile}/"
            os.makedirs(saved_imgs_path, exist_ok=True)
            filepath = f"{config.PDFS_FOLDER}/{folder}/{pdffile}"
            print("DEBUG ", filepath)
            images = convert_from_path(filepath)   
            
            for idx, img in enumerate(images):
                img.save(f'{saved_imgs_path}/page_{idx}.jpg', 'JPEG')