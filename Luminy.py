import numpy as np
import cv2
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry


def generate_mask(anns):
    if len(anns) == 0:
        return None

    sorted_anns = sorted(anns, key=(lambda x: x['area']), reverse=True)

    final_image = np.zeros((sorted_anns[0]['segmentation'].shape[0], sorted_anns[0]['segmentation'].shape[1], 3),
                           dtype=np.uint8)

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

    for idx, ann in enumerate(sorted_anns):
        m = ann['segmentation']
        color_mask = pattern_colors[idx % len(pattern_colors)]
        for y in range(m.shape[0]):
            for x in range(m.shape[1]):
                if m[y, x]:
                    final_image[y, x] = color_mask

    return final_image


def main():
    #TODO: Criar o excel para receber as informações

    #TODO: Ler todos os arquivos dentro da pasta images e armazenar o caminho deles para usar em seguida
    #TODO: ver a quantidade de arquivos dentro da pastas images

    #TODO: Fazer um for passando a quantidade de arquivos
    sam = sam_model_registry["vit_h"](checkpoint="Assets/sam_vit_h_4b8939.pth")
    mask_generator = SamAutomaticMaskGenerator(sam)

    # TODO: receber o string de caminho das imagens
    image = cv2.imread('Assets/Images/example_16x16.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print('Program starting')

    masks = mask_generator.generate(image)
    founded_image = generate_mask(masks)

    #TODO: receber o string de caminho das imagens
    expected_image = cv2.imread("/content/Expected/example_16x16.png")
    expected_image = cv2.cvtColor(expected_image, cv2.COLOR_BGR2RGB)
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

    pixels_count = expected_image.shape[0] * expected_image.shape[1]
    error_percentage = abs((error_count / pixels_count) * 100 - 100)

    #TODO: salvar as informações na tabela Results.xlsx

if __name__ == "__main__":
    main()
