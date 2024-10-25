level_waves = {
    # "1": {
    #     "n6700": 1,
    #     "n5000": 2,
    #     "n3000": 3,
    #     "v500": 5,
    # },
    "2": {
        "v13250+1": 1,
        "v11000+2": 2,
        "v8500+3": 3,
        "v6500+2": 3,
        "v5000+4": 5,
        "v2500+6": 7,
        "v500+1": 10,
    },
    # "3": {
    #     "v18000": 30,
    #     "v8000": 40,
    # },
    # "4": {
    #     "v18000": 40,
    #     "v12000": 50,
    #     "v6000": 50
    # },
    # "5": {
    #     "v31000": 60,
    #     "v25000": 40,
    #     "v22000": 60,
    #     "v12000": 60,
    #     "v6000": 60
    # },
}

level_allowed_enemies = {
    "1": ("popusk", ),   # ("popusk", "josky")
    "2": ("popusk", "josky"),
    "3": ("josky", "sportik", "popusk"),
    "4": ("josky", "sigma", "sportik", "popusk", "rojatel"),
    "5": ("popusk", "sigma", "josky", "zeleniy_strelok", "sportik", "rojatel", "mega_strelok", "armorik", "telezhnik", "drobik", "klonik", "teleportik"),
    "6в": ("popusk", "josky", "sportik", "rojatel", "fire_res")

}

level_instant_select_towers = {
    "1": {160: "terpila", 256: "davalka"},
}

chests_rewards = {
    (2, 3): {
        "evil_coin": 1,
        "snow_coin": 2,
        "terpila": "unlock",
        "big_mechman": "unlock",
    },
    (5, 5): {
        "forest_coin": 2,
        "mountain_coin": 1,
        "zeus": "unlock",
        "thunder": "unlock",
    },
    "village_event": {
        "city_coin": 2,
        "evil_coin": 1,
        "barrier_mag": "unlock",
        "drachun": "unlock",
    },
    "spike_chest": {
        "forest_coin": 6,
    },
    "spike": {
        "spike": "unlock",
    },
    "9в": {
        "forest_coin": 2,
        "evil_coin": 1,
        "gribnik": "unlock",
        "bolotnik": "unlock",
    }

}

level_meta_pool = [
    # {
    #     # "level_id": (i, j),
    #     "level_time": 31500,
    #     "time_to_spawn": 225,
    #     "start_money": 50,
    #     "waves": level_waves["5"],
    #     "allowed_enemies": ("popusk", "sigma", "josky", "zeleniy_strelok", "sportik", "rojatel", "mega_strelok", "armorik", "telezhnik", "drobik", "klonik", "teleportik"),
    #     # "allowed_cords": (192, 320, 448, 576, 704),
    #     # "blocked_slots": (),
    #     "level_image": "2",
    #     # "action_after_complete": None
    # },
    {
        # "level_id": (i, j),
        "level_time": 13500,
        "time_to_spawn": 375,
        "start_money": 20,
        "waves": level_waves["2"],
        "allowed_enemies": ("popusk", "josky", None, None),
        "allowed_cords": (320, 448, 576),
        # "blocked_slots": (),
        "level_image": "2",
        # "action_after_complete": None
    }
]

enemy_costs = {
    "josky": 2,
    "popusk": 1,
    "sigma": 4,
    "sportik": 3,
    "armorik": 4,
    "rojatel": 3,
    "tyazhik": 3,
    "klonik": 3,
    "teleportik": 2,
    "fire_res": 1,
    "ice_res": 1,
    "water_res": 1,
    "poison_res": 1,
    "light_res": 1,
    "zeleniy_strelok": 5,
    "drobik": 4,
    "telezhnik": 6,
    "mega_strelok": 20
}

tower_costs = {
    "boomchick": 30,
    "davalka": 10,
    "drachun": 15,
    "fire_mag": 20,
    "kopitel": 20,
    "matricayshon": 30,
    "barrier_mag": 30,
    "parasitelniy": 20,
    "pukish": 30,
    "spike": 20,
    "terpila": 20,
    "thunder": 30,
    "urag_anus": 40,
    "yascerica": 40,
    "zeus": 20,
    "tolkan": 30,
    "big_mechman": 25,
    "go_bleen1": 5,
    "knight_on_horse": 35,
    "gnome_cannon1": 40,
    "electric": 30,
    "struyniy": 30,
    "dark_druid": 25,
    "pen": 20,
    "gribnik": 15,
    "bolotnik": 15,
    "nekr": 35,
    "electro_maga": 35,
    "inquisitor": 10,
    "priest": 10,
    "ded_moroz": 25,
    "uvelir": 30,
    "krovnyak": 20,
    "kokol": 25,
    "sliz": 20,
    "klonys": 20,
    "kot": 20,
    "furry_druid": 20,
    "oruzhik": 25,
    "kar_mag": 20,
    "chistiy": 25,
    "prokach": 30,
    "pulelom": 15,
    "shabriri": 10,
    "ares": 20,
    "vozmezdik": 20,
    "bomb": 35,
    "perec": 30,
    "vodka": 15,
    "easy_money": 0,
    "vistrel": 1,
    "molniya": 30,
    "tp_back": 20,
    "joltiy_pomidor": 15,
    "heal": 15,
    "zaduv": 15,
    "holod": 20,
    "thunder_kamen": 0,
    "grib1": 0,
    "grib2": 0,
    "grib3": 0,
    "furry_medved": 0,
    "furry_volk": 0,
    "furry_zayac": 0,
    "oruzhik_claymore": 0,
    "oruzhik_daggers": 0,
    "oruzhik_bow": 0,

}

towers_kd = {
    "boomchick": 525,
    "davalka": 375,
    "drachun": 375,
    "fire_mag": 375,
    "kopitel": 450,
    "matricayshon": 1125,
    "barrier_mag": 2250,
    "parasitelniy": 900,
    "pukish": 250,
    "spike": 375,
    "terpila": 1875,
    "thunder": 525,
    "urag_anus": 1500,
    "yascerica": 1125,
    "zeus": 375,
    "tolkan": 750,
    "big_mechman": 600,
    "go_bleen1": 15,
    "knight_on_horse": 900,
    "gnome_cannon1": 1275,
    "electric": 375,
    "struyniy": 750,
    "dark_druid": 525,
    "pen": 525,
    "gribnik": 750,
    "bolotnik": 750,
    "nekr": 525,
    "electro_maga": 750,
    "inquisitor": 1125,
    "priest": 1125,
    "ded_moroz": 450,
    "uvelir": 900,
    "krovnyak": 375,
    "kokol": 375,
    "sliz": 600,
    "klonys": 525,
    "kot": 1875,
    "furry_druid": 525,
    "oruzhik": 450,
    "kar_mag": 450,
    "chistiy": 300,
    "prokach": 600,
    "pulelom": 750,
    "shabriri": 250,
    "ares": 450,
    "vozmezdik": 1875,
    "bomb": 1875,
    "perec": 1500,
    "vodka": 1500,
    "easy_money": 4500,
    "vistrel": 225,
    "molniya": 1500,
    "tp_back": 5625,
    "joltiy_pomidor": 1500,
    "heal": 1500,
    "zaduv": 3375,
    "holod": 1500,

}

targets = {}

upgrade_costs = {
    "fire_mag": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "pukish": {
        "1": "0 evil_coin",
        "2a": "1 evil_coin",
        "2b": "1 evil_coin",
        "3a": "2 evil_coin",
        "3b": "2 evil_coin",
    },
    "boomchick": {
        "1": "0 mountain_coin",
        "2a": "1 mountain_coin",
        "2b": "1 mountain_coin",
        "3a": "2 mountain_coin",
        "3b": "2 mountain_coin",
    },
    "davalka": {
        "1": "0 mountain_coin",
        "2a": "1 mountain_coin",
        "2b": "1 mountain_coin",
        "3a": "2 mountain_coin",
        "3b": "2 mountain_coin",
    },
    "kopitel": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "matricayshon": {
        "1": "0 snow_coin",
        "2a": "1 snow_coin",
        "2b": "1 snow_coin",
        "3a": "2 snow_coin",
        "3b": "2 snow_coin",
    },
    "parasitelniy": {
        "1": "0 forest_coin",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "spike": {
        "1": "0 forest_coin",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "easy_money": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "vistrel": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "terpila": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "thunder": {
        "1": "0 mountain_coin",
        "2a": "1 mountain_coin",
        "2b": "1 mountain_coin",
        "3a": "2 mountain_coin",
        "3b": "2 mountain_coin",
    },
    "yascerica": {
        "1": "0 evil_coin",
        "2a": "1 evil_coin",
        "2b": "1 evil_coin",
        "3a": "2 evil_coin",
        "3b": "2 evil_coin",
    },
    "zeus": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "barrier_mag": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "urag_anus": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "big_mechman": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "drachun": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "tolkan": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "knight_on_horse": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "gnome_cannon1": {
        "1": "0 mountain_coin",
        "2a": "1 mountain_coin",
        "2b": "1 mountain_coin",
        "3a": "2 mountain_coin",
        "3b": "2 mountain_coin",
    },
    "electric": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "struyniy": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "dark_druid": {
        "1": "0 forest_coin",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "gribnik": {
        "1": "0 forest_coin",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "pen": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "bolotnik": {
        "1": "0 forest_coin",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "nekr": {
        "1": "0 evil_coin",
        "2a": "1 evil_coin",
        "2b": "1 evil_coin",
        "3a": "2 evil_coin",
        "3b": "2 evil_coin",
    },
    "electro_maga": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "inquisitor": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "priest": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "ded_moroz": {
        "1": "0 snow_coin",
        "2a": "1 snow_coin",
        "2b": "1 snow_coin",
        "3a": "2 snow_coin",
        "3b": "2 snow_coin",
    },
    "uvelir": {
        "1": "0 mountain_coin",
        "2a": "1 mountain_coin",
        "2b": "1 mountain_coin",
        "3a": "2 mountain_coin",
        "3b": "2 mountain_coin",
    },
    "krovnyak": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "kokol": {
        "1": "0 forest_coin",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "sliz": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "klonys": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "kot": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "furry_druid": {
        "1": "0 forest_coin",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "oruzhik": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "kar_mag": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "chistiy": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "prokach": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "pulelom": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "shabriri": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "ares": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "vozmezdik": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "bomb": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "perec": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "molniya": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "vodka": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "tp_back": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "joltiy_pomidor": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "heal": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "zaduv": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "holod": {
        "1": "0 snow_coin",
        "2a": "1 snow_coin",
        "2b": "1 snow_coin",
        "3a": "2 snow_coin",
        "3b": "2 snow_coin",
    }
}

upgrade_descriptions = {
    "fire_mag": {
        "1": "Крутой огненный маг. Умеет швырять во врагов маленькие фаерболы. А ещё он первый в игре получил анимацию :)",
        "2a": "После получения навыка маг сможет кастовать большие фаерболы, которые наносят больше урона",
        "2b": "После получения навыка маг сможет поджигать врагов своими фаерболами",
        "3a": "После получения навыка маг сможет входить в ярость на небольшое время в которой он стреляет усиленными фаерболами и ускоряет скорость атаки",
        "3b": "После получения навыка от сгоревших врагов будут оставаться горящие останки, наносящие урон другим врагам",
    },
    "pukish": {
        "1": "Стреляет по врагам ядовитыми облаками теряющими урон с каждым последующим врагом пока не исчезнут, а также избегает угроз превращаясь в ядовитое облако",
        "2a": "Ядовитое облако может пролететь через большее количество врагов",
        "2b": "Ядовитое облако теряет не так много урона проходя через врагов",
        "3a": "Ядовитое облако игнорирует защиту врагов и наносит урон сразу по хп",
        "3b": "Ядовитое облако не теряет урон проходя через врагов",
        # "2a": "После получения навыка ядовитое облако сможет пролететь через большее количество врагов",
        # "2b": "После получения навыка ядовитое облако будет терять не так много урона проходя через врагов",
        # "3a": "После получения навыка ядовитое облако будет игнорировать защиту врагов и наносить урон сразу по хп",
        # "3b": "После получения навыка ядовитое облако не будет терять урон проходя через врагов",
    },
    "boomchick": {
        "1": "Кидает во врагов бомбы, которые взрываются при соприкосновении с врагом и наносят урон по области. После смерти создаёт мощный взрыв",
        "2a": "Каждую третью атаку кидает усиленную бомбу которая вызывает взрыв по увеличенной области. Область посмертного взрыва увеличивается",
        "2b": "1 mountain_coin",
        "3a": "2 mountain_coin",
        "3b": "2 mountain_coin",
    },
    "davalka": {
        "1": "Периодически даёт ману. Жена фаермага(да да не удивляйтесь)",
        "2a": "Может дать больше маны с небольшим шансом. С каждой неудачей шанс будет расти",
        "2b": "Увеличивает атаку союзнику перед собой",
        "3a": "Увеличивает шанс дать больше маны",
        "3b": "Увеличение атаки становится мощнее. Также может усиливать союзников сверху, снизу и позади себя",
    },
    "kopitel": {
        "1": "Создаёт мечи и копья света и запускает их во врагов. Если врагов нет, то может накопить вплоть до 7 единиц оружия",
        "2a": "Имеет шанс создать двуручный меч света, который занимает в 2 раза больше места чем обычное световое оружие, но наносит в 3 раза больше урона",
        "2b": "Если не имеет накопленных световых оружий, то создаёт сразу несколько",
        "3a": "Двуручный световой меч занимает меньше места и имеет повышенный шанс появления",
        "3b": "Копья света могут пробить одного врага, а мечи света наносят больше урона",
        # "2a": "После получения навыка получит шанс создать двуручный меч света, который занимает в 2 раза больше места чем обычное световое оружие, но наносит в 3 раза больше урона",
        # "2b": "После получения навыка сможет создавать сразу несколько световых оружий если не имеет накопленных",
        # "3a": "После получения навыка двуручный световой меч будет занимать меньше места и иметь повышенный шанс появления",
        # "3b": "После получения навыка копья света смогут пробить одного врага, а мечи света будут наносить в 2 раза больше урона",
    },
    "matricayshon": {
        "1": "СКЕЛЕТОН ЖОСКО ОТЖИГАЕТ НА ГИТАРЕ И БАФФАЕТ СОЮЗНИКОВ ВОКРУГ ОМГ!!!!!. Увеличивает скорость атаки союзных башень вокруг него",
        "2a": "1 snow_coin",
        "2b": "1 snow_coin",
        "3a": "2 snow_coin",
        "3b": "2 snow_coin",
    },
    "parasitelniy": {
        "1": "Имеет много хп и накладывает на врагов паразитов, которые наносят урон врагам и восстанавливают здоровье тому кто их отправил",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "spike": {
        "1": "Наносит урон врагам которых касается. После встречи с Великим кустом он практически никогда не превращался из куста в своё настоящее тело. Почти никто не знает как он выглядит вне формы куста",
        "2a": "На кусте начинают расти мана-ягоды. Даёт ману раз в продолжительное время",
        "2b": "Идущие по кусту враги замедляются",
        "3a": "Даёт больше маны за меньшее время. Каждая атака немного ускоряет рост ягод",
        "3b": "Замедление врагов повышается. После совершения определённого количества атак получает благословление Великого куста, что позволяет ему временно увеличиться в размерах. Замедление снижается во всех клетках кроме той, где изначально был посажен куст",
    },
    "easy_money": {
        "1": "Мгновенно даёт некоторое количество маны",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "vistrel": {
        "1": "Бесплатный выстрел наносящий урон",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "terpila": {
        "1": "Жирный и имеет много хп, эти 2 факта никак не связаны. Прокачки писать не буду тк нада Мишу спросить(да да тебя)",
        "2a": "Получает 25% сопротивление к физическому урону",
        "2b": "При получении определённого количества урона отталкивает всех врагов от себя",
        "3a": "Cопротивление к физическому урону увеличивается до 50%. При получении определённого количества урона становится неуязвимым на некоторое время",
        "3b": "Скорость атаки и передвижения врагов временно уменьшается после того как их оттолкнули. Также отталкивает врагов на соседних линиях",
    },
    "thunder": {
        "1": "Запускает во врага большой камень наносящий урон, но если на соседней линии есть враг, то камень раздробится и полетит по 3 линиям нанося меньше урона. При смерти превращается в камень и может сдержать врагов",
        "2a": "Увеличивает количество хп в обычной и каменной форме",
        "2b": "Раз в несколько секунд запускает не просто камень, а голема. Голем при попадании во врага наносит увеличенный урон, а потом остаётся на поле, чтобы защищать свой ряд. Может запустить 3 маленьких или 1 среднего голема. Големы миролюбивые и не атакуют врагов",
        "3a": "Ещё сильнее увеличивает количество хп в обычной и каменной форме. Может возродиться из каменной формы в обычную через некоторое время",
        "3b": "Урон при попадании голема во врага увеличивается. Может запустить 3 средних или 1 большого голема",
    },
    "yascerica": {
        "1": "Кормит своего ненасытного питомца врагами. Геворг летит вперёд и съедает первого попавшегося ему врага, а потом возвращается к хозяину и переваривает пищу",
        "2a": "Геворг теперь атакует самого заднего врага. Уменьшает перезарядку и увеличивает скорость Геворга",
        "2b": "Геворг может съесть 2 врага за раз. Перезарядка сокращается если Геворг не наелся",
        "3a": "Геворг также наносит урон всем врагам которых он коснулся. Ещё сильнее уменьшает перезарядку и увеличивает скорость Геворга",
        "3b": "Геворг может съесть 3 врага за раз. Перезарядка сокращается если Геворг не наелся",
    },
    "zeus": {
        "1": "Наносит небольшой урон, но его выстрел проходит сквозь всех врагов на линии. Умирает от каждого чиха",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "barrier_mag": {
        "1": "Накладывает барьер, впитывающий большое количество урона, на преднего союзника на своей линии, а также периодически его обновляет",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "urag_anus": {
        "1": "Притягивает врагов с соседних линий на свою",
        "2a": "Ураган длится дольше и относит врагов назад",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "big_mechman": {
        "1": "Наносит урон в ближнем бою по своей линии и двум соседним. Он отлично управляет своим огромным мечом",
        "2a": "Увеличивает наносимый своим мечом урон по врагам у которых больше 2/3 здоровья",
        "2b": "Раз в некоторое время усиливает свой меч, что позволяет ему ударить по увеличенной площади и нанести больше урона",
        "3a": "Теперь увеличивает наносимый своим мечом урон по врагам у которых больше 1/2 здоровья, а также ещё сильнее увеличивает урон от меча по врагам у которых больше 3/4 здоровья",
        "3b": "Уменьшает время необходимое для усиления меча. Наносит ещё больше урона если враг находится в зоне, в которой меч не мог его достать до усиления",
    },
    "drachun": {
        "1": "Бьёт врагов по морде используя свои любимые кулаки - Геворга и Геворга.",
        "2a": "Получает возможность входить в состояние ярости в котором увеличивает урон от своих атак. Восстанавливает половину здоровья при убийстве врага находясь в ярости",
        "2b": "Увеличивает количество хп. Увеличивает наносимый урон по мере уменьшения хп",
        "3a": "Во время ярости наносимый урон увеличивается ещё сильнее. Полностью восстанавливает здоровье и немного продлевает ярость при убийстве врага находясь в ярости ",
        "3b": "Ещё сильнее увеличивает хп. Скорость атаки увеличивается если хп меньше половины. Если хп опускаются до 0, входит в безумие в котором скорость атаки увеличивается ещё сильнее на несколько секунд, после чего умирает",
    },
    "tolkan": {
        "1": "Отталкивает врагов назад своими огромными металлическими перчатками и наносит им урон. Если находится за другой башней то отталкивает на меньшее расстояние",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "knight_on_horse": {
        "1": "Сидит верхом на лошади используя свою длинную пику для атаки врагов. Рыцарь принимает на себя урон в дальнем бою, а лошадь в ближнем, если рыцарь погибнет лошадь побежит вперёд и затопчет врагов на своём пути. А в другом случае рыцарь достнет щит и будет атаковать пикой на меньшее расстояние. Пусть Илья напишет по нормальному",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "gnome_cannon1": {
        "1": "Долго перезаряжается, но наносит большой урон. Если поставить пушку на другую пушку, то она улучшится вплоть до 4 уровня. 2 уровень: новый гном который упрочняет пушку и чинит её. 3 уровень: новый гном быстрее перезаряжает пушку. 4 уровень: новый гном с огнемётом",
        "2a": "1 mountain_coin",
        "2b": "1 mountain_coin",
        "3a": "2 mountain_coin",
        "3b": "2 mountain_coin",
    },
    "electric": {
        "1": "Выстреливает очередью молний наносящих урон и может дать ляпоса по роже в ближнем бою своей заряженной электричеством рукой",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "struyniy": {
        "1": "Отталкивает врагов мощной струёй воды",
        "2a": "Немного увеличивает длину струи",
        "2b": "1 city_coin",
        "3a": "Струя отталкивает в 2 раза сильнее",
        "3b": "2 city_coin",
    },
    "dark_druid": {
        "1": "Насылает на врагов своих воронов и разлетается на стаю воронов после смерти",
        "2a": "Количество ворон увеличивается",
        "2b": "1 forest_coin",
        "3a": "Количество ворон увеличивается ещё больше",
        "3b": "2 forest_coin",
    },
    "gribnik": {
        "1": "Кидает во врага грибы, которые прилипают к врагу. После смерти враг оставляет гриб прочность которого зависит от количества грибов на враге. Не может самостоятельно наложить на врага больше чем 1 гриб. После своей смерти оставляет грибную поляну",
        "2a": "После съедения грибы оставляют ядовитое облако, которое замедляет и наносит урон врагам. Урон от облака и его длительность зависят от размера съеденного гриба",
        "2b": "Грибы становятся более нестабильными, поэтому у них меньше хп и они взрываются. Урон и величина взрыва зависят от уровня гриба",
        "3a": "Увеличивает урон, длительность и замедление ядовитых облаков",
        "3b": "Урон от взрыва грибов увеличивается. Появляющаяся после смерти грибная поляна улучшается",
    },
    "pen": {
        "1": "Ускоряет снаряды союзников, позволяя им наносить больше урона и замедляет снаряды врагов, из-за чего они наносят меньше урона",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "bolotnik": {
        "1": "Разжижает землю на нескольких клетках перед собой, превращая её в болото. Скорость передвижения врагов в болоте уменьшается",
        "2a": "Увеличивает дальность появления клеток с болотом на 2",
        "2b": "Становится неуязвимым и может поглотить одного врага, после чего покинет поле",
        "3a": "Враги сильнее замедляются на заболоченных клетках",
        "3b": "Не покидает поле после поглощения врага. Может снова поглощать врагов после перезарядки",
    },
    "nekr": {
        "1": "Призывает отряд скелетов которые идут вперёд и сражаются с врагами. В случае смерти скелета некромант восстановит его в изначальной точке",
        "2a": "Дополнительно выпускает по 1 скелету сверху и снизу некроманта. Повышает скорость движения скелетов",
        "2b": "Скелеты обрастают плотью, превращаясь в зомби с повышенным здоровьем и немного увеличенным уроном",
        "3a": "3 скелета превращаются в скелетов с луком и могут наносить урон врагам на расстоянии. Ещё сильнее повышает скорость движения скелетов",
        "3b": "Передний зомби усиливается, ещё больше увеличивая свои здоровье и урон",
    },
    "electro_maga": {
        "1": "эм... нуу... короче... с помощью магии невероятно сложных электро магнитных мега супер ультра импульсов расталкивает врагов в области взрыва в разные стороны",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "inquisitor": {
        "1": "Помечает врагов и возвращает им часть урона, который они нанесли",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "priest": {
        "1": "Исцеляет союзников перед собой с помощью лечащих слов или прикосновений. Если союзник на клетке перед ним, то исцеление увеличивается",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "ded_moroz": {
        "1": "Стреляет во врагов морозными снарядами которые постепенно замораживают противника, сначала замедляя, а потом и вовсе останавливая его",
        "2a": "1 snow_coin",
        "2b": "1 snow_coin",
        "3a": "2 snow_coin",
        "3b": "2 snow_coin",
    },
    "uvelir": {
        "1": "Достаёт из мешка драгоценные(или не очень) камни имеющие разные эффекты: наносят урон, исцеляют, усиливают, делают врагов уязвимыми, дают <название валюты>, накладывают барьер, делают неуязвимым",
        "2a": "1 mountain_coin",
        "2b": "1 mountain_coin",
        "3a": "2 mountain_coin",
        "3b": "2 mountain_coin",
    },
    "krovnyak": {
        "1": "Использует свою кровь в качестве оружия запуская её в врагов и возвращая обратно. Имеет сопротивление к физическому урону. При получении урона получает дополнительный снаряд крови. Если какое-то время не получал урон, расходует снаряды крови и исцеляется",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "kokol": {
        "1": "Стреляет лесными снарядами наносящими урон и размещает на соседних линиях кусты, которые тоже стреляют лесными снарядами если на них стоит союзник",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "sliz": {
        "1": "Бросает во врага слизь которая не будет давать врагу двигаться пока её не убьют",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "klonys": {
        "1": "Атакует врага своими иллюзиями. Чем ближе враг тем больше иллюзий нанесут ему урон",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "kot": {
        "1": "Жирни кот. У него 9 жизней и каждый раз когда его хп кончаются вместо того чтобы покинуть поле он какое-то время отдыхает, чтобы потом снова жоска танчить вплоть до 9 раз",
        "2a": "Время отдыха снижается в 2 раза",
        "2b": "После четвёртого отдыха начинает царапать врагов",
        "3a": "Время отдыха снижается ещё сильнее. Враги замедляются если идут по клетке с котом пока он отдыхает",
        "3b": "Начинает царапать врагов сразу. Увеличивает количество ударов когтями каждые 3 отдыха",
    },
    "furry_druid": {
        "1": "бля как же я заебся... 5:30 утра... ну он типа кароч может в медведя танка который бьёт лапой превращаться и в волка и в зайца и всё конец",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "oruzhik": {
        "1": "бла бла бла",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "kar_mag": {
        "1": "вампум",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "chistiy": {
        "1": "Выстреливает множеством снарядов, которые наносят чистый урон. Если рядом с ним есть такие же башни как он, количество снарядов за выстрел увеличится",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "prokach": {
        "1": "Использует свой меч для нанесения урона врагам вблизи. Чем дольше он не атакует врагов, тем сильнее и больше становится его меч",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "pulelom": {
        "1": "Выпускает волну чего-то, уничтожающую вражеские снаряды на своём пути вплоть до 5 штук",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "shabriri": {
        "1": "Постепенно сходит с ума, усиливаясь, а потом и вовсе превращаясь в крипа",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "ares": {
        "1": "Контрудар делает бах",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "vozmezdik": {
        "1": "Хавает пули. Получает усиление после съедания пуль. В зависимости от количества съеденных пуль усиление улучшается",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "bomb": {
        "1": "Моментально взрывается нанося большой урон в области взрыва",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "perec": {
        "1": "Наносит большой урон врагам в выбранной линии",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "molniya": {
        "1": "Наносит огромный урон 3 врагам",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "vodka": {
        "1": "Временно ускоряет перезарядку союзников в области действия",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "tp_back": {
        "1": "Возвращает врагов с левой половины поля обратно. ТУДА ИХ",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "joltiy_pomidor": {
        "1": "Оглушает врагов в определённой области и за каждого задетого врага даёт ману",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "heal": {
        "1": "Лечит союзников в крестообразной области",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "zaduv": {
        "1": "Стягивает врагов в определённой области в один ряд",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "holod": {
        "1": "Замораживает врагов в своей колонне",
        "2a": "1 snow_coin",
        "2b": "1 snow_coin",
        "3a": "2 snow_coin",
        "3b": "2 snow_coin",
    }
}

keys_ru = {
    "a": "ф",
    "b": "и",
    "c": "с",
    "d": "в",
    "e": "у",
    "f": "а",
    "g": "п",
    "h": "р",
    "i": "ш",
    "j": "о",
    "k": "л",
    "l": "д",
    "m": "ь",
    "n": "т",
    "o": "щ",
    "p": "з",
    "q": "й",
    "r": "к",
    "s": "ы",
    "t": "е",
    "u": "г",
    "v": "м",
    "w": "ц",
    "x": "ч",
    "y": "н",
    "z": "я",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    ",": "б",
    ".": "ю",
    "/": ".",
    "`": "ё",
    "[": "х",
    "]": "ъ",
    ";": "ж",
    "'": "э",
    " ": " "
}
KEYS_EN = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z", "0", "1", "2", "3",
           "4", "5", "6", "7", "8", "9", ",", ".", "/", "`",
           "[", "]", ";", "'", " "]
kEYS_CODES = [x for x in range(97, 123)] + [x for x in range(48, 58)] + [44, 46, 47, 96, 91, 93, 59, 39, 32]
KEYS = dict(zip(kEYS_CODES, KEYS_EN))   # я хз куда это, но в мейн нах не надо
