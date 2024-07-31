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
    "krest": [image.load(f"images/towers/krest/wait/krest{i}.png") for i in range(1, 5)],

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
    "boomchick": [image.load(f"images/towers/boomchick/attack/boomchick{i}.png") for i in range(1, 5)],     # тут
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

towers_death = {
    "fire_mag": [image.load(f"images/towers/fire_mag/death/fire_mag{i}.png") for i in range(1, 5)],
    "davalka": [image.load(f"images/towers/davalka/death/davalka{i}.png") for i in range(1, 5)],
    "kopitel": [image.load(f"images/towers/kopitel/death/kopitel{i}.png") for i in range(1, 5)],
    "matricayshon": [image.load(f"images/towers/matricayshon/death/matricayshon{i}.png") for i in range(1, 5)],
    "parasitelniy": [image.load(f"images/towers/parasitelniy/death/parasitelniy{i}.png") for i in range(1, 5)],
    "spike": [image.load(f"images/towers/spike/death/spike{i}.png") for i in range(1, 5)],
    "terpila": [image.load(f"images/towers/terpila/death/terpila{i}.png") for i in range(1, 5)],
    "thunder": [image.load(f"images/towers/thunder/death/thunder{i}.png") for i in range(1, 5)],
    "thunder_kamen": [image.load(f"images/towers/thunder_kamen/death/thunder_kamen{i}.png") for i in range(1, 5)],
    "yascerica": [image.load(f"images/towers/yascerica/death/yascerica{i}.png") for i in range(1, 5)],
    "zeus": [image.load(f"images/towers/zeus/death/zeus{i}.png") for i in range(1, 5)],
    "barrier_mag": [image.load(f"images/towers/barrier_mag/death/barrier_mag{i}.png") for i in range(1, 5)],
    "urag_anus": [image.load(f"images/towers/urag_anus/death/urag_anus{i}.png") for i in range(1, 5)],
    "big_mechman": [image.load(f"images/towers/big_mechman/death/big_mechman{i}.png") for i in range(1, 5)],
    "boomchick": [image.load(f"images/towers/boomchick/death/boomchick{i}.png") for i in range(1, 5)],   # ухахах
    "pukish": [image.load(f"images/towers/pukish/death/pukish{i}.png") for i in range(1, 5)],
    "drachun": [image.load(f"images/towers/drachun/death/drachun{i}.png") for i in range(1, 5)],
    "tolkan": [image.load(f"images/towers/tolkan/death/tolkan{i}.png") for i in range(1, 5)],
    "knight_on_horse": [image.load(f"images/towers/knight_on_horse/death/knight_on_horse{i}.png") for i in range(1, 5)],
    "knight": [image.load(f"images/towers/knight/death/knight{i}.png") for i in range(1, 5)],
    "gnome_cannon1": [image.load(f"images/towers/gnome_cannon1/death/gnome_cannon1{i}.png") for i in range(1, 5)],
    "gnome_cannon2": [image.load(f"images/towers/gnome_cannon2/death/gnome_cannon2{i}.png") for i in range(1, 5)],
    "gnome_cannon3": [image.load(f"images/towers/gnome_cannon3/death/gnome_cannon3{i}.png") for i in range(1, 5)],
    "gnome_flamethrower": [image.load(f"images/towers/gnome_flamethrower/death/gnome_flamethrower{i}.png") for i in range(1, 5)],
    "electric": [image.load(f"images/towers/electric/death/electric{i}.png") for i in range(1, 5)],
    "struyniy": [image.load(f"images/towers/struyniy/death/struyniy{i}.png") for i in range(1, 5)],
    "dark_druid": [image.load(f"images/towers/dark_druid/death/dark_druid{i}.png") for i in range(1, 5)],
    "pen": [image.load(f"images/towers/pen/death/pen{i}.png") for i in range(1, 5)],
    "gribnik": [image.load(f"images/towers/gribnik/death/gribnik{i}.png") for i in range(1, 5)],
    "grib1": [image.load(f"images/towers/grib1/death/grib1{i}.png") for i in range(1, 5)],
    "grib2": [image.load(f"images/towers/grib2/death/grib2{i}.png") for i in range(1, 5)],
    "grib3": [image.load(f"images/towers/grib3/death/grib3{i}.png") for i in range(1, 5)],
    "bolotnik": [image.load(f"images/towers/bolotnik/death/bolotnik{i}.png") for i in range(1, 5)],
    "nekr": [image.load(f"images/towers/nekr/death/nekr{i}.png") for i in range(1, 5)],
    "electro_maga": [image.load(f"images/towers/electro_maga/death/electro_maga{i}.png") for i in range(1, 5)],
    "inquisitor": [image.load(f"images/towers/inquisitor/death/inquisitor{i}.png") for i in range(1, 5)],
    "priest": [image.load(f"images/towers/priest/death/priest{i}.png") for i in range(1, 5)],
    "ded_moroz": [image.load(f"images/towers/ded_moroz/death/ded_moroz{i}.png") for i in range(1, 5)],
    "uvelir": [image.load(f"images/towers/uvelir/death/uvelir{i}.png") for i in range(1, 5)],
    "krovnyak": [image.load(f"images/towers/krovnyak/death/krovnyak{i}.png") for i in range(1, 5)],
    "kokol": [image.load(f"images/towers/kokol/death/kokol{i}.png") for i in range(1, 5)],
    "sliz": [image.load(f"images/towers/sliz/death/sliz{i}.png") for i in range(1, 5)],
    "klonys": [image.load(f"images/towers/klonys/death/klonys{i}.png") for i in range(1, 5)],
    # "go_bleen1": [image.load(f"images/towers/go_bleen1/wait/go_bleen1{i}.png") for i in range(1, 3)],
    "bomb": [image.load(f"images/towers/bomb/death/bomb{i}.png") for i in range(1, 5)],
    "perec": [image.load(f"images/towers/perec/death/perec{i}.png") for i in range(1, 5)],
    "vodka": [image.load(f"images/towers/vodka/death/vodka{i}.png") for i in range(1, 5)],
    "easy_money": [image.load(f"images/towers/easy_money/death/easy_money{i}.png") for i in range(1, 5)],
    "vistrel": [image.load(f"images/towers/vistrel/death/vistrel{i}.png") for i in range(1, 5)],
    "molniya": [image.load(f"images/towers/molniya/death/molniya{i}.png") for i in range(1, 5)],
    "tp_back": [image.load(f"images/towers/tp_back/death/tp_back{i}.png") for i in range(1, 5)],
    "joltiy_pomidor": [image.load(f"images/towers/joltiy_pomidor/death/joltiy_pomidor{i}.png") for i in range(1, 5)],
    "krest": [image.load(f"images/towers/krest/death/krest{i}.png") for i in range(1, 5)],
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
    "fire_res": [image.load(f"images/enemies/fire_res/wait/fire_res{i}.png") for i in range(1, 5)],
    "ice_res": [image.load(f"images/enemies/ice_res/wait/ice_res{i}.png") for i in range(1, 5)],
    "water_res": [image.load(f"images/enemies/water_res/wait/water_res{i}.png") for i in range(1, 5)],
    "poison_res": [image.load(f"images/enemies/poison_res/wait/poison_res{i}.png") for i in range(1, 5)],
    "light_res": [image.load(f"images/enemies/light_res/wait/light_res{i}.png") for i in range(1, 5)],
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
    "fire_res": [image.load(f"images/enemies/fire_res/move/fire_res{i}.png") for i in range(1, 5)],
    "ice_res": [image.load(f"images/enemies/ice_res/move/ice_res{i}.png") for i in range(1, 5)],
    "water_res": [image.load(f"images/enemies/water_res/move/water_res{i}.png") for i in range(1, 5)],
    "poison_res": [image.load(f"images/enemies/poison_res/move/poison_res{i}.png") for i in range(1, 5)],
    "light_res": [image.load(f"images/enemies/light_res/move/light_res{i}.png") for i in range(1, 5)],
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
    "fire_res": [image.load(f"images/enemies/fire_res/attack/fire_res{i}.png") for i in range(1, 5)],
    "ice_res": [image.load(f"images/enemies/ice_res/attack/ice_res{i}.png") for i in range(1, 5)],
    "water_res": [image.load(f"images/enemies/water_res/attack/water_res{i}.png") for i in range(1, 5)],
    "poison_res": [image.load(f"images/enemies/poison_res/attack/poison_res{i}.png") for i in range(1, 5)],
    "light_res": [image.load(f"images/enemies/light_res/attack/light_res{i}.png") for i in range(1, 5)],
}

enemies_death = {
    "popusk": [image.load(f"images/enemies/popusk/death/popusk{i}.png") for i in range(1, 5)],
    "fire_res": [image.load(f"images/enemies/fire_res/death/fire_res{i}.png") for i in range(1, 5)],
    "ice_res": [image.load(f"images/enemies/ice_res/death/ice_res{i}.png") for i in range(1, 5)],
    "water_res": [image.load(f"images/enemies/water_res/death/water_res{i}.png") for i in range(1, 5)],
    "poison_res": [image.load(f"images/enemies/poison_res/death/poison_res{i}.png") for i in range(1, 5)],
    "light_res": [image.load(f"images/enemies/light_res/death/light_res{i}.png") for i in range(1, 5)],
    # "josky": [image.load(f"images/enemies/josky/death/josky{i}.png") for i in range(1, 5)],
    # "sigma": [image.load(f"images/enemies/sigma/death/sigma{i}.png") for i in range(1, 5)],
    # "zeleniy_strelok": [image.load(f"images/enemies/zeleniy_strelok/death/zeleniy_strelok{i}.png") for i in range(1, 5)],
    # "drobik": [image.load(f"images/enemies/drobik/death/drobik{i}.png") for i in range(1, 5)],
    # "klonik": [image.load(f"images/enemies/klonik/death/klonik{i}.png") for i in range(1, 5)],
    # "mega_strelok": [image.load(f"images/enemies/mega_strelok/death/mega_strelok{i}.png") for i in range(1, 5)],
    # "rojatel": [image.load(f"images/enemies/rojatel/death/rojatel{i}.png") for i in range(1, 5)],
    # "slabiy": [image.load(f"images/enemies/slabiy/death/slabiy{i}.png") for i in range(1, 5)],
    # "sportik": [image.load(f"images/enemies/sportik/death/sportik{i}.png") for i in range(1, 5)],
    # "teleportik": [image.load(f"images/enemies/teleportik/death/teleportik{i}.png") for i in range(1, 5)],
    # "armorik": [image.load(f"images/enemies/armorik/death/armorik{i}.png") for i in range(1, 5)],
    # "telezhnik": [image.load(f"images/enemies/telezhnik/death/telezhnik{i}.png") for i in range(1, 5)],
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

bullets_move = {
    "fireball": [image.load(f"images/bullets/fireball/move/fireball{i}.png") for i in range(1, 5)],
    "ab_kokol": [image.load(f"images/bullets/ab_kokol/move/ab_kokol{i}.png") for i in range(1, 5)],
    "amethyst": [image.load(f"images/bullets/amethyst/move/amethyst{i}.png") for i in range(1, 5)],
    "big_kamen": [image.load(f"images/bullets/big_kamen/move/big_kamen{i}.png") for i in range(1, 5)],
    "blackik": [image.load(f"images/bullets/blackik/move/blackik{i}.png") for i in range(1, 5)],
    "blue_bullet": [image.load(f"images/bullets/blue_bullet/move/blue_bullet{i}.png") for i in range(1, 5)],
    "bone_arrow": [image.load(f"images/bullets/bone_arrow/move/bone_arrow{i}.png") for i in range(1, 5)],
    "diamond": [image.load(f"images/bullets/diamond/move/diamond{i}.png") for i in range(1, 5)],
    "drachun_gulag": [image.load(f"images/bullets/drachun_gulag/move/drachun_gulag{i}.png") for i in range(1, 5)],
    "drobik_bullet": [image.load(f"images/bullets/drobik_bullet/move/drobik_bullet{i}.png") for i in range(1, 5)],
    "electric_bullet": [image.load(f"images/bullets/electric_bullet/move/electric_bullet{i}.png") for i in range(1, 5)],
    "electric_kulak": [image.load(f"images/bullets/electric_kulak/move/electric_kulak{i}.png") for i in range(1, 5)],
    "electro_maga_explosion": [image.load(f"images/bullets/electro_maga_explosion/move/electro_maga_explosion{i}.png") for i in range(1, 5)],
    "electro_maga_sfera": [image.load(f"images/bullets/electro_maga_sfera/move/electro_maga_sfera{i}.png") for i in range(1, 5)],
    "emerald": [image.load(f"images/bullets/emerald/move/emerald{i}.png") for i in range(1, 5)],
    "explosion": [image.load(f"images/bullets/explosion/move/explosion{i}.png") for i in range(1, 5)],
    "fire": [image.load(f"images/bullets/fire/move/fire{i}.png") for i in range(1, 5)],
    "fireball_big": [image.load(f"images/bullets/fireball_big/move/fireball_big{i}.png") for i in range(1, 5)],
    "gas": [image.load(f"images/bullets/gas/move/gas{i}.png") for i in range(1, 5)],
    "grib_bullet": [image.load(f"images/bullets/grib_bullet/move/grib_bullet{i}.png") for i in range(1, 5)],
    "horse": [image.load(f"images/bullets/horse/move/horse{i}.png") for i in range(1, 5)],
    "joltiy_explosion": [image.load(f"images/bullets/joltiy_explosion/move/joltiy_explosion{i}.png") for i in range(1, 5)],
    "klonys_punch1": [image.load(f"images/bullets/klonys_punch1/move/klonys_punch1{i}.png") for i in range(1, 5)],
    "klonys_punch2": [image.load(f"images/bullets/klonys_punch2/move/klonys_punch2{i}.png") for i in range(1, 5)],
    "klonys_punch3": [image.load(f"images/bullets/klonys_punch3/move/klonys_punch3{i}.png") for i in range(1, 5)],
    "klonys_punch4": [image.load(f"images/bullets/klonys_punch4/move/klonys_punch4{i}.png") for i in range(1, 5)],
    "klonys_punch5": [image.load(f"images/bullets/klonys_punch5/move/klonys_punch5{i}.png") for i in range(1, 5)],
    "krov_bul": [image.load(f"images/bullets/krov_bul/move/krov_bul{i}.png") for i in range(1, 5)],
    "krov_explosion": [image.load(f"images/bullets/krov_explosion/move/krov_explosion{i}.png") for i in range(1, 5)],
    "Laser": [image.load(f"images/bullets/Laser/move/Laser{i}.png") for i in range(1, 5)],
    "light_big_sword": [image.load(f"images/bullets/light_big_sword/move/light_big_sword{i}.png") for i in range(1, 5)],
    "light_spear": [image.load(f"images/bullets/light_spear/move/light_spear{i}.png") for i in range(1, 5)],
    "light_sword": [image.load(f"images/bullets/light_sword/move/light_sword{i}.png") for i in range(1, 5)],
    "mech_vzux": [image.load(f"images/bullets/mech_vzux/move/mech_vzux{i}.png") for i in range(1, 5)],
    "mega_strelok_bullet": [image.load(f"images/bullets/mega_strelok_bullet/move/mega_strelok_bullet{i}.png") for i in range(1, 5)],
    "mini_kamen": [image.load(f"images/bullets/mini_kamen/move/mini_kamen{i}.png") for i in range(1, 5)],
    "nephrite": [image.load(f"images/bullets/nephrite/move/nephrite{i}.png") for i in range(1, 5)],
    "obsidian": [image.load(f"images/bullets/obsidian/move/obsidian{i}.png") for i in range(1, 5)],
    "onyx": [image.load(f"images/bullets/onyx/move/onyx{i}.png") for i in range(1, 5)],
    "opal": [image.load(f"images/bullets/opal/move/opal{i}.png") for i in range(1, 5)],
    "opal_explosion": [image.load(f"images/bullets/opal_explosion/move/opal_explosion{i}.png") for i in range(1, 5)],
    "perec_bullet": [image.load(f"images/bullets/perec_bullet/move/perec_bullet{i}.png") for i in range(1, 5)],
    "pike": [image.load(f"images/bullets/pike/move/pike{i}.png") for i in range(1, 5)],
    "red_bullet": [image.load(f"images/bullets/red_bullet/move/red_bullet{i}.png") for i in range(1, 5)],
    "ruby": [image.load(f"images/bullets/ruby/move/ruby{i}.png") for i in range(1, 5)],
    "sapphire": [image.load(f"images/bullets/sapphire/move/sapphire{i}.png") for i in range(1, 5)],
    "sliz_bul": [image.load(f"images/bullets/sliz_bul/move/sliz_bul{i}.png") for i in range(1, 5)],
    "snejok": [image.load(f"images/bullets/snejok/move/snejok{i}.png") for i in range(1, 5)],
    "spear_ma": [image.load(f"images/bullets/spear_ma/move/spear_ma{i}.png") for i in range(1, 5)],
    "stone": [image.load(f"images/bullets/stone/move/stone{i}.png") for i in range(1, 5)],
    "struya": [image.load(f"images/bullets/struya/move/struya{i}.png") for i in range(1, 5)],
    "telezhnik_bullet": [image.load(f"images/bullets/telezhnik_bullet/move/telezhnik_bullet{i}.png") for i in range(1, 5)],
    "tolkan_bux": [image.load(f"images/bullets/tolkan_bux/move/tolkan_bux{i}.png") for i in range(1, 5)],
    "vistrel_bullet": [image.load(f"images/bullets/vistrel_bullet/move/vistrel_bullet{i}.png") for i in range(1, 5)],
    "yellow_bullet": [image.load(f"images/bullets/yellow_bullet/move/yellow_bullet{i}.png") for i in range(1, 5)],
    "zeleniy_strelok_bullet": [image.load(f"images/bullets/zeleniy_strelok_bullet/move/zeleniy_strelok_bullet{i}.png") for i in range(1, 5)],
}

bullets_death = {
    "fireball": [image.load(f"images/bullets/fireball/death/fireball{i}.png") for i in range(1, 5)],
    "ab_kokol": [image.load(f"images/bullets/ab_kokol/death/ab_kokol{i}.png") for i in range(1, 5)],
    "amethyst": [image.load(f"images/bullets/amethyst/death/amethyst{i}.png") for i in range(1, 5)],
    "big_kamen": [image.load(f"images/bullets/big_kamen/death/big_kamen{i}.png") for i in range(1, 5)],
    "blackik": [image.load(f"images/bullets/blackik/death/blackik{i}.png") for i in range(1, 5)],
    "blue_bullet": [image.load(f"images/bullets/blue_bullet/death/blue_bullet{i}.png") for i in range(1, 5)],
    "bone_arrow": [image.load(f"images/bullets/bone_arrow/death/bone_arrow{i}.png") for i in range(1, 5)],
    "diamond": [image.load(f"images/bullets/diamond/death/diamond{i}.png") for i in range(1, 5)],
    "drachun_gulag": [image.load(f"images/bullets/drachun_gulag/death/drachun_gulag{i}.png") for i in range(1, 5)],
    "drobik_bullet": [image.load(f"images/bullets/drobik_bullet/death/drobik_bullet{i}.png") for i in range(1, 5)],
    "electric_bullet": [image.load(f"images/bullets/electric_bullet/death/electric_bullet{i}.png") for i in range(1, 5)],
    "electric_kulak": [image.load(f"images/bullets/electric_kulak/death/electric_kulak{i}.png") for i in range(1, 5)],
    "electro_maga_explosion": [image.load(f"images/bullets/electro_maga_explosion/death/electro_maga_explosion{i}.png") for i in range(1, 5)],
    "electro_maga_sfera": [image.load(f"images/bullets/electro_maga_sfera/death/electro_maga_sfera{i}.png") for i in range(1, 5)],
    "emerald": [image.load(f"images/bullets/emerald/death/emerald{i}.png") for i in range(1, 5)],
    "explosion": [image.load(f"images/bullets/explosion/death/explosion{i}.png") for i in range(1, 5)],
    "fire": [image.load(f"images/bullets/fire/death/fire{i}.png") for i in range(1, 5)],
    "fireball_big": [image.load(f"images/bullets/fireball_big/death/fireball_big{i}.png") for i in range(1, 5)],
    "gas": [image.load(f"images/bullets/gas/death/gas{i}.png") for i in range(1, 5)],
    "grib_bullet": [image.load(f"images/bullets/grib_bullet/death/grib_bullet{i}.png") for i in range(1, 5)],
    "horse": [image.load(f"images/bullets/horse/death/horse{i}.png") for i in range(1, 5)],
    "joltiy_explosion": [image.load(f"images/bullets/joltiy_explosion/death/joltiy_explosion{i}.png") for i in range(1, 5)],
    "klonys_punch1": [image.load(f"images/bullets/klonys_punch1/death/klonys_punch1{i}.png") for i in range(1, 5)],
    "klonys_punch2": [image.load(f"images/bullets/klonys_punch2/death/klonys_punch2{i}.png") for i in range(1, 5)],
    "klonys_punch3": [image.load(f"images/bullets/klonys_punch3/death/klonys_punch3{i}.png") for i in range(1, 5)],
    "klonys_punch4": [image.load(f"images/bullets/klonys_punch4/death/klonys_punch4{i}.png") for i in range(1, 5)],
    "klonys_punch5": [image.load(f"images/bullets/klonys_punch5/death/klonys_punch5{i}.png") for i in range(1, 5)],
    "krov_bul": [image.load(f"images/bullets/krov_bul/death/krov_bul{i}.png") for i in range(1, 5)],
    "krov_explosion": [image.load(f"images/bullets/krov_explosion/death/krov_explosion{i}.png") for i in range(1, 5)],
    "Laser": [image.load(f"images/bullets/Laser/death/Laser{i}.png") for i in range(1, 5)],
    "light_big_sword": [image.load(f"images/bullets/light_big_sword/death/light_big_sword{i}.png") for i in range(1, 5)],
    "light_spear": [image.load(f"images/bullets/light_spear/death/light_spear{i}.png") for i in range(1, 5)],
    "light_sword": [image.load(f"images/bullets/light_sword/death/light_sword{i}.png") for i in range(1, 5)],
    "mech_vzux": [image.load(f"images/bullets/mech_vzux/death/mech_vzux{i}.png") for i in range(1, 5)],
    "mega_strelok_bullet": [image.load(f"images/bullets/mega_strelok_bullet/death/mega_strelok_bullet{i}.png") for i in range(1, 5)],
    "mini_kamen": [image.load(f"images/bullets/mini_kamen/death/mini_kamen{i}.png") for i in range(1, 5)],
    "nephrite": [image.load(f"images/bullets/nephrite/death/nephrite{i}.png") for i in range(1, 5)],
    "obsidian": [image.load(f"images/bullets/obsidian/death/obsidian{i}.png") for i in range(1, 5)],
    "onyx": [image.load(f"images/bullets/onyx/death/onyx{i}.png") for i in range(1, 5)],
    "opal": [image.load(f"images/bullets/opal/death/opal{i}.png") for i in range(1, 5)],
    "opal_explosion": [image.load(f"images/bullets/opal_explosion/death/opal_explosion{i}.png") for i in range(1, 5)],
    "perec_bullet": [image.load(f"images/bullets/perec_bullet/death/perec_bullet{i}.png") for i in range(1, 5)],
    "pike": [image.load(f"images/bullets/pike/death/pike{i}.png") for i in range(1, 5)],
    "red_bullet": [image.load(f"images/bullets/red_bullet/death/red_bullet{i}.png") for i in range(1, 5)],
    "ruby": [image.load(f"images/bullets/ruby/death/ruby{i}.png") for i in range(1, 5)],
    "sapphire": [image.load(f"images/bullets/sapphire/death/sapphire{i}.png") for i in range(1, 5)],
    "sliz_bul": [image.load(f"images/bullets/sliz_bul/death/sliz_bul{i}.png") for i in range(1, 5)],
    "snejok": [image.load(f"images/bullets/snejok/death/snejok{i}.png") for i in range(1, 5)],
    "spear_ma": [image.load(f"images/bullets/spear_ma/death/spear_ma{i}.png") for i in range(1, 5)],
    "stone": [image.load(f"images/bullets/stone/death/stone{i}.png") for i in range(1, 5)],
    "struya": [image.load(f"images/bullets/struya/death/struya{i}.png") for i in range(1, 5)],
    "telezhnik_bullet": [image.load(f"images/bullets/telezhnik_bullet/death/telezhnik_bullet{i}.png") for i in range(1, 5)],
    "tolkan_bux": [image.load(f"images/bullets/tolkan_bux/death/tolkan_bux{i}.png") for i in range(1, 5)],
    "vistrel_bullet": [image.load(f"images/bullets/vistrel_bullet/death/vistrel_bullet{i}.png") for i in range(1, 5)],
    "yellow_bullet": [image.load(f"images/bullets/yellow_bullet/death/yellow_bullet{i}.png") for i in range(1, 5)],
    "zeleniy_strelok_bullet": [image.load(f"images/bullets/zeleniy_strelok_bullet/death/zeleniy_strelok_bullet{i}.png") for i in range(1, 5)],
}

coins = {
    "city_coin": image.load("images/coins/city_coin.png"),
    "evil_coin": image.load("images/coins/evil_coin.png"),
    "forest_coin": image.load("images/coins/forest_coin.png"),
    "mountain_coin": image.load("images/coins/mountain_coin.png"),
    "snow_coin": image.load("images/coins/snow_coin.png")
}
