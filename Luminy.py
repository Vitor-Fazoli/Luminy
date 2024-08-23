import os
import numpy as np
import cv2
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
from openpyxl import load_workbook
import skimage as ski


def save_data(data, excel_file):
    workbook = load_workbook(filename=excel_file)

    sheet = workbook['dados']
    indicate_column = 'A'
    next_line = 1
    while sheet[f"{indicate_column}{next_line}"].value is not None:
        next_line += 1

    sheet.append(*[data])

    workbook.save(excel_file)


def generate_mask(anns):
    if len(anns) == 0:
        return None

    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)

    final_image = np.zeros((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 3),
                           dtype=np.uint8)

    # Esse padrão de cores não tem nenhuma interferencia verdadeira,
    # pois na analíse ele recebe a referencia da imagem e recebe um match de cores

    pattern_colors = [
        [255, 0, 0],  # Vermelho
        [0, 255, 0],  # Verde
        [0, 0, 255],  # Azul
        [255, 255, 0],  # Amarelo
        [255, 0, 255],  # Magenta
        [0, 255, 255],  # ciano
        [255, 255, 255],  # Branco
        [50, 50, 50]  # cinza
    ]

    #
    for idx, ann in enumerate(sorted_anns):
        m = ann['segmentation']
        color_mask = pattern_colors[idx % len(pattern_colors)]
        for y in range(m.shape[0]):
            for x in range(m.shape[1]):
                if m[y, x]:
                    final_image[y, x] = color_mask

    return final_image

def err_percent(expected_image, founded_image):
    color_expected = expected_image[0, 0]
    color_founded = founded_image[0, 0]

    error_count = 0

    for y in range(founded_image.shape[1]):
        for x in range(founded_image.shape[0]):
            if not np.array_equal(expected_image[x, y], color_expected):
                color_expected = expected_image[x, y]
                color_founded = founded_image[x, y]

            if np.array_equal(founded_image[x, y], color_founded):
                continue
            else:
                error_count += 1

    return abs((error_count / pixels_count) * 100 - 100)

def main():
    files = os.listdir('Assets/Expected')

    for image_path in files:
        sam = sam_model_registry["vit_h"](checkpoint="Assets/sam_vit_h_4b8939.pth")
        mask_generator = SamAutomaticMaskGenerator(sam)

        image = cv2.imread('Assets/Images/' + image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        masks = mask_generator.generate(image)
        founded_image = generate_mask(masks)
        
        expected_image = cv2.imread('Assets/Expected/' + image_path)

        #Passando as duas imagens para um mesmo padrão de cores
        founded_image = cv2.cvtColor(founded_image, cv2.COLOR_BGR2RGB)
        expected_image = cv2.cvtColor(expected_image, cv2.COLOR_BGR2RGB)
       
        # Normalizando as imagens
        founded_image = founded_image.astype(np.float32) / 255.0
        expected_image = expected_image.astype(np.float32) / 255.0

        # MSE
        mse = ski.metrics.mean_squared_error(founded_image, expected_image)
        
        f1_score = ski.metrics.f1_score(founded_image, expected_image, average='weighted')
        
        r_squared = ski.metrics.r2_score(founded_image, expected_image)
        
        error_percentage = err_percent(expected_image, founded_image)
        
        pixels_count = founded_image.shape[0] * founded_image.shape[1]
        
        size_image = founded_image.shape[0] + "x" + founded_image.shape[1] 
        
        save_data([image_path, pixels_count,size_image, error_percentage, mse, f1_score, r_squared], 'dados.xlsx')

if __name__ == "__main__":
    main()