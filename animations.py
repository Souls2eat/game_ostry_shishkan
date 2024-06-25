from pygame import image

towers_wait = {
    "fire_mag": [image.load(f"images/towers/fire_mag/wait/fire_mag{i}.png") for i in range(1, 5)],
    "davalka": [image.load(f"images/towers/davalka/wait/davalka{i}.png") for i in range(1, 5)],
    "kopitel": [image.load(f"images/towers/kopitel/wait/kopitel{i}.png") for i in range(1, 5)],
    "matricayshon": [image.load(f"images/towers/matricayshon/wait/matricayshon{i}.png") for i in range(1, 5)],
    "parasitelniy": [image.load(f"images/towers/parasitelniy/wait/parasitelniy{i}.png") for i in range(1, 5)],
    "spike": [image.load(f"images/towers/spike/wait/spike{i}.png") for i in range(1, 5)],
    "terpila": [image.load(f"images/towers/terpila/wait/terpila{i}.png") for i in range(1, 5)],
    "thunder": [image.load(f"images/towers/thunder/wait/thunder{i}.png") for i in range(1, 5)],
    "thunder_kamen": [image.load(f"images/towers/thunder_kamen/wait/thunder_kamen{i}.png") for i in range(1, 5)],
    "yascerica": [image.load(f"images/towers/yascerica/wait/yascerica{i}.png") for i in range(1, 5)],
    "zeus": [image.load(f"images/towers/zeus/wait/zeus{i}.png") for i in range(1, 5)],
    "barrier_mag": [image.load(f"images/towers/barrier_mag/wait/barrier_mag{i}.png") for i in range(1, 5)],
    "urag_anus": [image.load(f"images/towers/urag_anus/wait/urag_anus{i}.png") for i in range(1, 5)],
    "big_mechman": [image.load(f"images/towers/big_mechman/wait/big_mechman{i}.png") for i in range(1, 5)],
    "boomchick": [image.load(f"images/towers/boomchick/wait/boomchick{i}.png") for i in range(1, 5)],
    "pukish": [image.load(f"images/towers/pukish/wait/pukish{i}.png") for i in range(1, 5)],
    "drachun": [image.load(f"images/towers/drachun/wait/drachun{i}.png") for i in range(1, 5)],
    "tolkan": [image.load(f"images/towers/tolkan/wait/tolkan{i}.png") for i in range(1, 5)],
    "knight_on_horse": [image.load(f"images/towers/knight_on_horse/wait/knight_on_horse{i}.png") for i in range(1, 5)],
    "knight": [image.load(f"images/towers/knight/wait/knight{i}.png") for i in range(1, 5)],
    "gnome_cannon1": [image.load(f"images/towers/gnome_cannon1/wait/gnome_cannon1{i}.png") for i in range(1, 5)],
    "gnome_cannon2": [image.load(f"images/towers/gnome_cannon2/wait/gnome_cannon2{i}.png") for i in range(1, 5)],
    "gnome_cannon3": [image.load(f"images/towers/gnome_cannon3/wait/gnome_cannon3{i}.png") for i in range(1, 5)],
    "gnome_flamethrower": [image.load(f"images/towers/gnome_flamethrower/wait/gnome_flamethrower{i}.png") for i in range(1, 5)],
    "electric": [image.load(f"images/towers/electric/wait/electric{i}.png") for i in range(1, 5)],
    "struyniy": [image.load(f"images/towers/struyniy/wait/struyniy{i}.png") for i in range(1, 5)],
    "dark_druid": [image.load(f"images/towers/dark_druid/wait/dark_druid{i}.png") for i in range(1, 5)],
    "pen": [image.load(f"images/towers/pen/wait/pen{i}.png") for i in range(1, 5)],
    "gribnik": [image.load(f"images/towers/gribnik/wait/gribnik{i}.png") for i in range(1, 5)],
    "grib1": [image.load(f"images/towers/grib1/wait/grib1{i}.png") for i in range(1, 5)],
    "grib2": [image.load(f"images/towers/grib2/wait/grib2{i}.png") for i in range(1, 5)],
    "grib3": [image.load(f"images/towers/grib3/wait/grib3{i}.png") for i in range(1, 5)],
    "bolotnik": [image.load(f"images/towers/bolotnik/wait/bolotnik{i}.png") for i in range(1, 5)],
    "nekr": [image.load(f"images/towers/nekr/wait/nekr{i}.png") for i in range(1, 5)],
    "electro_maga": [image.load(f"images/towers/electro_maga/wait/electro_maga{i}.png") for i in range(1, 5)],
    # "go_bleen1": [image.load(f"images/towers/go_bleen1/wait/go_bleen1{i}.png") for i in range(1, 3)],
    "bomb": [image.load(f"images/towers/bomb/wait/bomb{i}.png") for i in range(1, 5)],
    "perec": [image.load(f"images/towers/perec/wait/perec{i}.png") for i in range(1, 5)],
    "vodka": [image.load(f"images/towers/vodka/wait/vodka{i}.png") for i in range(1, 5)],
    "easy_money": [image.load(f"images/towers/easy_money/wait/easy_money{i}.png") for i in range(1, 5)],
    "vistrel": [image.load(f"images/towers/vistrel/wait/vistrel{i}.png") for i in range(1, 5)],
    "molniya": [image.load(f"images/towers/molniya/wait/molniya{i}.png") for i in range(1, 5)],
    "tp_back": [image.load(f"images/towers/tp_back/wait/tp_back{i}.png") for i in range(1, 5)],

}

towers_attack = {
    "fire_mag": [image.load(f"images/towers/fire_mag/attack/fire_mag{i}.png") for i in range(1, 5)],
    "kopitel": [image.load(f"images/towers/kopitel/attack/kopitel{i}.png") for i in range(1, 5)],
    "parasitelniy": [image.load(f"images/towers/parasitelniy/attack/parasitelniy{i}.png") for i in range(1, 5)],
    "spike": [image.load(f"images/towers/spike/attack/spike{i}.png") for i in range(1, 5)],
    "thunder": [image.load(f"images/towers/thunder/attack/thunder{i}.png") for i in range(1, 5)],
    "yascerica": [image.load(f"images/towers/yascerica/attack/yascerica{i}.png") for i in range(1, 5)],
    "zeus": [image.load(f"images/towers/zeus/attack/zeus{i}.png") for i in range(1, 5)],
    "urag_anus": [image.load(f"images/towers/urag_anus/attack/urag_anus{i}.png") for i in range(1, 5)],
    "big_mechman": [image.load(f"images/towers/big_mechman/attack/big_mechman{i}.png") for i in range(1, 5)],
    "boomchick": [image.load(f"images/towers/boomchick/attack/boomchick{i}.png") for i in range(1, 5)],
    "pukish": [image.load(f"images/towers/pukish/attack/pukish{i}.png") for i in range(1, 5)],
    "drachun": [image.load(f"images/towers/drachun/attack/drachun{i}.png") for i in range(1, 5)],
    "tolkan": [image.load(f"images/towers/tolkan/attack/tolkan{i}.png") for i in range(1, 5)],
    "knight_on_horse": [image.load(f"images/towers/knight_on_horse/attack/knight_on_horse{i}.png") for i in range(1, 5)],
    "knight": [image.load(f"images/towers/knight/attack/knight{i}.png") for i in range(1, 5)],
    "gnome_cannon1": [image.load(f"images/towers/gnome_cannon1/attack/gnome_cannon1{i}.png") for i in range(1, 5)],
    "gnome_cannon2": [image.load(f"images/towers/gnome_cannon2/attack/gnome_cannon2{i}.png") for i in range(1, 5)],
    "gnome_cannon3": [image.load(f"images/towers/gnome_cannon3/attack/gnome_cannon3{i}.png") for i in range(1, 5)],
    "gnome_flamethrower": [image.load(f"images/towers/gnome_flamethrower/attack/gnome_flamethrower{i}.png") for i in range(1, 5)],
    "electric": [image.load(f"images/towers/electric/attack/electric{i}.png") for i in range(1, 5)],
    "struyniy": [image.load(f"images/towers/struyniy/attack/struyniy{i}.png") for i in range(1, 5)],
    "dark_druid": [image.load(f"images/towers/dark_druid/attack/dark_druid{i}.png") for i in range(1, 5)],
    "gribnik": [image.load(f"images/towers/gribnik/attack/gribnik{i}.png") for i in range(1, 5)],
    "nekr": [image.load(f"images/towers/nekr/attack/nekr{i}.png") for i in range(1, 5)],
    "electro_maga": [image.load(f"images/towers/electro_maga/attack/electro_maga{i}.png") for i in range(1, 5)],
    # "go_bleen1": [image.load(f"images/towers/go_bleen1/attack/go_bleen1{i}.png") for i in range(1, 3)],

}

towers_give = {
    "barrier_mag": [image.load(f"images/towers/barrier_mag/give/barrier_mag{i}.png") for i in range(1, 5)],
    "kopitel": [image.load(f"images/towers/kopitel/give/kopitel{i}.png") for i in range(1, 5)],
    "davalka": [image.load(f"images/towers/davalka/give/davalka{i}.png") for i in range(1, 5)],
}

towers_hide = {
    "pukish": [image.load(f"images/towers/pukish/hide/pukish{i}.png") for i in range(1, 5)],
}

coins = {
    "city_coin": image.load("images/coins/city_coin.png"),
    "evil_coin": image.load("images/coins/evil_coin.png"),
    "forest_coin": image.load("images/coins/forest_coin.png"),
    "mountain_coin": image.load("images/coins/mountain_coin.png"),
    "snow_coin": image.load("images/coins/snow_coin.png")
}
