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
    sorted_ans = sorted(mask, key=(lambda x: x['area']), reverse=True)
    ax = plt.gca()
    ax.set_autoscale_on(False)
    for ann in sorted_ans:
        m = ann['segmentation']
        img = np.ones((m.shape[0], m.shape[1], 3))
        color_mask = np.random.random((1, 3)).tolist()[0]
        for n in range(3):
            img[:, :, n] = color_mask[n]
        ax.imshow(np.dstack((img, m * 0.35)))


Config.start_program()

image = cv2.imread('Assets/Images/example_16x16.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

initial_time = time.time()
useMemoryInitial = str(psutil.virtual_memory().used / (1024 * 1024 * 1024)) + ' GB'
useCpuInitial = str(psutil.cpu_percent().real) + ' %'

print('Program starting')
sam = sam_model_registry["vit_h"](checkpoint="Assets/sam_vit_h_4b8939.pth")
mask_generator = SamAutomaticMaskGenerator(sam)
masks = mask_generator.generate(image)

plt.figure(figsize=(10, 10))
plt.imshow(image)
identity = s_generate_identity()
v_generate_mask(masks)
plt.axis('off')
plt.savefig('Assets/Results/Example16x16/' + str(identity) + '.png')

useMemoryFinal = str(psutil.virtual_memory().used / (1024 * 1024 * 1024)) + 'GB'
useCpuFinal = str(psutil.cpu_percent().real) + ' %'

final_time = time.time()
total_time = final_time - initial_time

wb = load_workbook('dados.xlsx')

sheet = wb['principal']

new_row = [useMemoryInitial, useMemoryFinal, useCpuInitial, useCpuFinal, image.size, total_time, str(identity) + '.png']
sheet.append(new_row)

wb.save('dados.xlsx')

# TODO: Criar uma forma de identificar as mascaras do resultado com o esperado para gerar uma precisão

print('Process finished!')
