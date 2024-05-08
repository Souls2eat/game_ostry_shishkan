from pygame import *

towers_wait = {
    "fire_mag": [image.load(f"images/towers/fire_mag/wait/fire_mag{i}.png") for i in range(1, 3)],
    "davalka": [image.load(f"images/towers/davalka/wait/davalka{i}.png") for i in range(1, 3)],
    "kopitel": [image.load(f"images/towers/kopitel/wait/kopitel{i}.png") for i in range(1, 3)],
    "matricayshon": [image.load(f"images/towers/matricayshon/wait/matricayshon{i}.png") for i in range(1, 3)],
    "parasitelniy": [image.load(f"images/towers/parasitelniy/wait/parasitelniy{i}.png") for i in range(1, 3)],
    "spike": [image.load(f"images/towers/spike/wait/spike{i}.png") for i in range(1, 3)],
    "terpila": [image.load(f"images/towers/terpila/wait/terpila{i}.png") for i in range(1, 3)],
    "thunder": [image.load(f"images/towers/thunder/wait/thunder{i}.png") for i in range(1, 3)],
    "yascerica": [image.load(f"images/towers/yascerica/wait/yascerica{i}.png") for i in range(1, 3)],
    "zeus": [image.load(f"images/towers/zeus/wait/zeus{i}.png") for i in range(1, 3)],
    "oh_shit_i_am_sorry__barrier_mag": [image.load(f"images/towers/oh_shit_i_am_sorry__barrier_mag/wait/oh_shit_i_am_sorry__barrier_mag{i}.png") for i in range(1, 3)],
    "urag_anus": [image.load(f"images/towers/urag_anus/wait/urag_anus{i}.png") for i in range(1, 3)],
    # "big_mechman": [image.load(f"images/towers/big_mechman/wait/big_mechman{i}.png") for i in range(1, 3)],
    "boomchick": [image.load(f"images/towers/boomchick/wait/boomchick{i}.png") for i in range(1, 3)],

}
# for b in range(len(towers_wait)):
#     print(towers_wait["fire_mag_wait"][b])
# for i in range(2):
#     image.load("images/towers/fire_mag%d.png" % i)
