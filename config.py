level_1_waves = {       # время волны : поинты спавна на волну
    18000: 10,
    8000: 20,
}

level_2_waves = {
    18000: 20,
    10000: 30,
    3500: 30
}

level_3_waves = {
    18000: 30,
    8000: 40,
}

level_4_waves = {
    18000: 40,
    12000: 50,
    6000: 50
}
level_5_waves = {
    25000: 40,
    22000: 60,
    12000: 60,
    6000: 60
}

enemy_costs = {
    "josky": 2,
    "popusk": 1,
    "sigma": 4,
    "sportik": 3,
    "armorik": 4,
    "rojatel": 3,
    "klonik": 3,
    "teleportik": 2,
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
    "gribnik": 30,
    "bomb": 35,
    "perec": 30,
    "vodka": 15,
    "easy_money": 0,
    "vistrel": 0,
    "tp_back": 20,
    "thunder_kamen": 0,
    "grib1": 0,
    "grib2": 0,
    "grib3": 0,

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
    "bomb": 1875,
    "perec": 1500,
    "vodka": 1500,
    "easy_money": 4500,
    "vistrel": 225,
    "tp_back": 5625,
    "pen": 525,
    "gribnik": 375,
    
}

targets = {}

# level_number, level_time, time_to_spawn, start_money, waves: dict, allowed_enemies: tuple, allowed_cords=(192, 320, 448, 576, 704
levels_config = {
    "1": [1, 22500, 750, 50, level_1_waves, ("popusk", "josky")],
    "2": [2, 22500, 575, 50, level_2_waves, ("josky", "sigma", "sportik", "popusk")],
    "3": [3, 22500, 500, 50, level_3_waves, ("josky", "sigma", "sportik", "armorik", "zeleniy_strelok", "popusk", "teleportik")],
    "4": [4, 22500, 225, 50, level_4_waves, ("telezhnik", "rojatel", "sigma", "armorik", "zeleniy_strelok", "drobik", "klonik")],
    "5": [5, 31500, 225, 50, level_5_waves, ("popusk", "sigma", "josky", "zeleniy_strelok", "sportik", "rojatel", "mega_strelok", "armorik", "telezhnik", "drobik", "klonik", "teleportik")]
}

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
        "1": "0 forest_coin",
        "2a": "1 forest_coin",
        "2b": "1 forest_coin",
        "3a": "2 forest_coin",
        "3b": "2 forest_coin",
    },
    "davalka": {
        "1": "0 mountain_coin",
        "2a": "1 mountain_coin",
        "2b": "1 mountain_coin",
        "3a": "2 mountain_coin",
        "3b": "2 mountain_coin",
    },
    "kopitel": {
        "1": "0 snow_coin",
        "2a": "1 snow_coin",
        "2b": "1 snow_coin",
        "3a": "2 snow_coin",
        "3b": "2 snow_coin",
    },
    "matricayshon": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "parasitelniy": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "spike": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
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
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
    },
    "yascerica": {
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
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
        "1": "0 city_coin",
        "2a": "1 city_coin",
        "2b": "1 city_coin",
        "3a": "2 city_coin",
        "3b": "2 city_coin",
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
    }
}
