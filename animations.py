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
    "boomchick": [image.load(f"images/towers/boomchick/wait/boomchick{i}.png") for i in range(1, 5)],   # ухахах
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
    "inquisitor": [image.load(f"images/towers/inquisitor/wait/inquisitor{i}.png") for i in range(1, 5)],
    "priest": [image.load(f"images/towers/priest/wait/priest{i}.png") for i in range(1, 5)],
    "ded_moroz": [image.load(f"images/towers/ded_moroz/wait/ded_moroz{i}.png") for i in range(1, 5)],
    "uvelir": [image.load(f"images/towers/uvelir/wait/uvelir{i}.png") for i in range(1, 5)],
    "krovnyak": [image.load(f"images/towers/krovnyak/wait/krovnyak{i}.png") for i in range(1, 5)],
    "kokol": [image.load(f"images/towers/kokol/wait/kokol{i}.png") for i in range(1, 5)],
    "sliz": [image.load(f"images/towers/sliz/wait/sliz{i}.png") for i in range(1, 5)],
    "klonys": [image.load(f"images/towers/klonys/wait/klonys{i}.png") for i in range(1, 5)],
    # "go_bleen1": [image.load(f"images/towers/go_bleen1/wait/go_bleen1{i}.png") for i in range(1, 3)],
    "bomb": [image.load(f"images/towers/bomb/wait/bomb{i}.png") for i in range(1, 5)],
    "perec": [image.load(f"images/towers/perec/wait/perec{i}.png") for i in range(1, 5)],
    "vodka": [image.load(f"images/towers/vodka/wait/vodka{i}.png") for i in range(1, 5)],
    "easy_money": [image.load(f"images/towers/easy_money/wait/easy_money{i}.png") for i in range(1, 5)],
    "vistrel": [image.load(f"images/towers/vistrel/wait/vistrel{i}.png") for i in range(1, 5)],
    "molniya": [image.load(f"images/towers/molniya/wait/molniya{i}.png") for i in range(1, 5)],
    "tp_back": [image.load(f"images/towers/tp_back/wait/tp_back{i}.png") for i in range(1, 5)],
    "joltiy_pomidor": [image.load(f"images/towers/joltiy_pomidor/wait/joltiy_pomidor{i}.png") for i in range(1, 5)],

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
    "boomchick": [image.load(f"images/towers/boomchick/attack/boomchick{i}.png") for i in range(1, 11)],     # тут
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
    "inquisitor": [image.load(f"images/towers/inquisitor/attack/inquisitor{i}.png") for i in range(1, 5)],
    "priest": [image.load(f"images/towers/priest/attack/priest{i}.png") for i in range(1, 5)],
    "ded_moroz": [image.load(f"images/towers/ded_moroz/attack/ded_moroz{i}.png") for i in range(1, 5)],
    "uvelir": [image.load(f"images/towers/uvelir/attack/uvelir{i}.png") for i in range(1, 5)],
    "krovnyak": [image.load(f"images/towers/krovnyak/attack/krovnyak{i}.png") for i in range(1, 5)],
    "kokol": [image.load(f"images/towers/kokol/attack/kokol{i}.png") for i in range(1, 5)],
    "sliz": [image.load(f"images/towers/sliz/attack/sliz{i}.png") for i in range(1, 5)],
    "klonys": [image.load(f"images/towers/klonys/attack/klonys{i}.png") for i in range(1, 5)],
    # "go_bleen1": [image.load(f"images/towers/go_bleen1/attack/go_bleen1{i}.png") for i in range(1, 3)],

}

towers_give = {
    "barrier_mag": [image.load(f"images/towers/barrier_mag/give/barrier_mag{i}.png") for i in range(1, 5)],
    "kopitel": [image.load(f"images/towers/kopitel/give/kopitel{i}.png") for i in range(1, 5)],
    "davalka": [image.load(f"images/towers/davalka/give/davalka{i}.png") for i in range(1, 5)],
    "uvelir": [image.load(f"images/towers/uvelir/give/uvelir{i}.png") for i in range(1, 5)],
}

towers_hide = {
    "pukish": [image.load(f"images/towers/pukish/hide/pukish{i}.png") for i in range(1, 5)],
}

enemies_wait = {
    "popusk": [image.load(f"images/enemies/popusk/wait/popusk{i}.png") for i in range(1, 5)],
    "josky": [image.load(f"images/enemies/josky/wait/josky{i}.png") for i in range(1, 5)],
    "sigma": [image.load(f"images/enemies/sigma/wait/sigma{i}.png") for i in range(1, 5)],
    "zeleniy_strelok": [image.load(f"images/enemies/zeleniy_strelok/wait/zeleniy_strelok{i}.png") for i in range(1, 5)],
    "drobik": [image.load(f"images/enemies/drobik/wait/drobik{i}.png") for i in range(1, 5)],
    "klonik": [image.load(f"images/enemies/klonik/wait/klonik{i}.png") for i in range(1, 5)],
    "mega_strelok": [image.load(f"images/enemies/mega_strelok/wait/mega_strelok{i}.png") for i in range(1, 5)],
    "rojatel": [image.load(f"images/enemies/rojatel/wait/rojatel{i}.png") for i in range(1, 5)],
    "slabiy": [image.load(f"images/enemies/slabiy/wait/slabiy{i}.png") for i in range(1, 5)],
    "sportik": [image.load(f"images/enemies/sportik/wait/sportik{i}.png") for i in range(1, 5)],
    "teleportik": [image.load(f"images/enemies/teleportik/wait/teleportik{i}.png") for i in range(1, 5)],
    "armorik": [image.load(f"images/enemies/armorik/wait/armorik{i}.png") for i in range(1, 5)],
    "telezhnik": [image.load(f"images/enemies/telezhnik/wait/telezhnik{i}.png") for i in range(1, 5)],
}

enemies_move = {
    "popusk": [image.load(f"images/enemies/popusk/move/popusk{i}.png") for i in range(1, 5)],
    "josky": [image.load(f"images/enemies/josky/move/josky{i}.png") for i in range(1, 5)],
    "sigma": [image.load(f"images/enemies/sigma/move/sigma{i}.png") for i in range(1, 5)],
    "zeleniy_strelok": [image.load(f"images/enemies/zeleniy_strelok/move/zeleniy_strelok{i}.png") for i in range(1, 5)],
    "drobik": [image.load(f"images/enemies/drobik/move/drobik{i}.png") for i in range(1, 5)],
    "klonik": [image.load(f"images/enemies/klonik/move/klonik{i}.png") for i in range(1, 5)],
    "mega_strelok": [image.load(f"images/enemies/mega_strelok/move/mega_strelok{i}.png") for i in range(1, 5)],
    "rojatel": [image.load(f"images/enemies/rojatel/move/rojatel{i}.png") for i in range(1, 5)],
    "slabiy": [image.load(f"images/enemies/slabiy/move/slabiy{i}.png") for i in range(1, 5)],
    "sportik": [image.load(f"images/enemies/sportik/move/sportik{i}.png") for i in range(1, 5)],
    "teleportik": [image.load(f"images/enemies/teleportik/move/teleportik{i}.png") for i in range(1, 5)],
    "armorik": [image.load(f"images/enemies/armorik/move/armorik{i}.png") for i in range(1, 5)],
    "telezhnik": [image.load(f"images/enemies/telezhnik/move/telezhnik{i}.png") for i in range(1, 5)],
}

enemies_attack = {
    "popusk": [image.load(f"images/enemies/popusk/attack/popusk{i}.png") for i in range(1, 5)],
    "josky": [image.load(f"images/enemies/josky/attack/josky{i}.png") for i in range(1, 5)],
    "sigma": [image.load(f"images/enemies/sigma/attack/sigma{i}.png") for i in range(1, 5)],
    "zeleniy_strelok": [image.load(f"images/enemies/zeleniy_strelok/attack/zeleniy_strelok{i}.png") for i in range(1, 5)],
    "drobik": [image.load(f"images/enemies/drobik/attack/drobik{i}.png") for i in range(1, 5)],
    "klonik": [image.load(f"images/enemies/klonik/attack/klonik{i}.png") for i in range(1, 5)],
    "mega_strelok": [image.load(f"images/enemies/mega_strelok/attack/mega_strelok{i}.png") for i in range(1, 5)],
    "rojatel": [image.load(f"images/enemies/rojatel/attack/rojatel{i}.png") for i in range(1, 5)],
    "slabiy": [image.load(f"images/enemies/slabiy/attack/slabiy{i}.png") for i in range(1, 5)],
    "sportik": [image.load(f"images/enemies/sportik/attack/sportik{i}.png") for i in range(1, 5)],
    "teleportik": [image.load(f"images/enemies/teleportik/attack/teleportik{i}.png") for i in range(1, 5)],
    "armorik": [image.load(f"images/enemies/armorik/attack/armorik{i}.png") for i in range(1, 5)],
    "telezhnik": [image.load(f"images/enemies/telezhnik/attack/telezhnik{i}.png") for i in range(1, 5)],
}

enemies_rage_wait = {
    "armorik": [image.load(f"images/enemies/armorik/rage_wait/armorik_zloy{i}.png") for i in range(1, 5)],
    "telezhnik": [image.load(f"images/enemies/telezhnik/rage_wait/telezhnik_zloy{i}.png") for i in range(1, 5)],
}

enemies_rage_move = {
    "armorik": [image.load(f"images/enemies/armorik/rage_move/armorik_zloy{i}.png") for i in range(1, 5)],
    "telezhnik": [image.load(f"images/enemies/telezhnik/rage_move/telezhnik_zloy{i}.png") for i in range(1, 5)],
}

enemies_rage_attack = {
    "armorik": [image.load(f"images/enemies/armorik/rage_attack/armorik_zloy{i}.png") for i in range(1, 5)],
    "telezhnik": [image.load(f"images/enemies/telezhnik/rage_attack/telezhnik_zloy{i}.png") for i in range(1, 5)],
}

coins = {
    "city_coin": image.load("images/coins/city_coin.png"),
    "evil_coin": image.load("images/coins/evil_coin.png"),
    "forest_coin": image.load("images/coins/forest_coin.png"),
    "mountain_coin": image.load("images/coins/mountain_coin.png"),
    "snow_coin": image.load("images/coins/snow_coin.png")
}
