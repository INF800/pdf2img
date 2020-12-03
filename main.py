import os, config
from pdf2image import convert_from_path

os.makedirs(f"{config.EXTRACTED_IMGS_FOLDER}", exist_ok=True)
for folder in config.PDFS_FOLDER:
    
    # save images in folders which are named after every pdf file
    # inside category folders in main folder
    os.makedirs(f"{config.EXTRACTED_IMGS_FOLDER}/{folder}", exist_ok=True)
    
    for sub_folder in folder:
        
        pdfs_path = f"{config.PDFS_FOLDER}/{folder}/{sub_folder}/"
        pdfs = os.listdir(pdfs_path)
        os.makedirs(f"{config.EXTRACTED_IMGS_FOLDER}/{folder}/{sub_folder}", exist_ok=True)
        
        for filename in pdfs:
            
            saved_imgs_path = f"{config.EXTRACTED_IMGS_FOLDER}/{folder}/{sub_folder}/{filename}"
            os.makedirs(saved_imgs_path, exist_ok=True)
            images = convert_from_path(f'{pdfs_path}{filename}')   
            
            for idx, img in enumerate(images):
                img.save(f'{saved_imgs_path}/output_{idx}.jpg', 'JPEG')