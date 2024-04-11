import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
from openpyxl import load_workbook
import psutil
import time
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import Config


def s_generate_identity():
    return str(random.randrange(10000000))


def v_generate_mask(mask):
    if len(mask) == 0:
        return

    # Cores padrão
    pattern_colors = [
        [1, 0, 0],  # Vermelho
        [0, 1, 0],  # Verde
        [0, 0, 1],  # Azul
        [1, 1, 0],  # Amarelo
        [1, 0, 1],  # Magenta
    ]

    # Inicializa o índice da cor
    index_color = 0

    sorted_ans = sorted(mask, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)

    color_labels = []  # Lista para armazenar as cores de cada pixel

    for ann in mask:
        m = ann['segmentation']
        img = np.ones((m.shape[0], m.shape[1], 3))

        # Mantém as áreas pretas da imagem original
        img[np.where(m == 0)] = [0, 0, 0]

        # Aplica a cor padrão apenas às áreas não pretas
        color_mask = pattern_colors[index_color]
        img[np.where(m != 0)] = color_mask

        index_color = (index_color + 1) % len(pattern_colors)

        ax.imshow(np.dstack((img, m)))

        # Adiciona as cores dos pixels à lista
        for y in range(m.shape[0]):
            for x in range(m.shape[1]):
                if m[y, x] != 0:
                    color_labels.append(tuple(img[y, x]))

    print(color_labels)




sam = sam_model_registry["vit_h"](checkpoint="Assets/sam_vit_h_4b8939.pth")
mask_generator = SamAutomaticMaskGenerator(sam)
Config.start_program()

image = cv2.imread('Assets/Images/teste.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

initial_time = time.time()
useMemoryInitial = str(psutil.virtual_memory().used / (1024 * 1024 * 1024)) + ' GB'
useCpuInitial = str(psutil.cpu_percent().real) + ' %'

print('Program starting')

masks = mask_generator.generate(image)
print("Mask generator finished!")

plt.figure(figsize=(10, 10))
plt.imshow(image)
identity = s_generate_identity()
v_generate_mask(masks)
plt.axis('off')
plt.show()

#plt.savefig('Assets/Results/Example16x16/' + str(identity) + '.png')

useMemoryFinal = str(psutil.virtual_memory().used / (1024 * 1024 * 1024)) + 'GB'
useCpuFinal = str(psutil.cpu_percent().real) + ' %'

final_time = time.time()
total_time = final_time - initial_time

wb = load_workbook('dados.xlsx')

sheet = wb['principal']

new_row = [useMemoryInitial, useMemoryFinal, useCpuInitial, useCpuFinal, image.size, total_time, str(identity) + '.png']
#sheet.append(new_row)

#wb.save('dados.xlsx')

# TODO: Criar uma forma de identificar as mascaras do resultado com o esperado para gerar uma precisão

print('Process finished!')
