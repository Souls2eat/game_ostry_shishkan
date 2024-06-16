# Примеры волн
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


# Примеры стоимости врагов
enemy_costs = {"josky": 2,
               "popusk": 1,
               "sigma": 4,
               "sportik": 3,
               "armorik": 4,
               "rojatel": 3,
               "zeleniy_strelok": 5,
               "drobik": 4,
               "telezhnik": 6,
               "mega_strelok": 20}


# Цены башен
tower_costs = {
    "boomchick": 30,
    "davalka": 10,
    "drachun": 15,
    "fire_mag": 20,
    "kopitel": 20,
    "matricayshon": 30,
    "barrier_mag": 30,
    "parasitelniy": 20,
    "pukish": 35,
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
    "pen": 15,
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
    "pen": 525,
    "gribnik": 375,
    "bomb": 1875,
    "perec": 1500,
    "vodka": 1500,
    "easy_money": 4500,
    "vistrel": 225,
    "tp_back": 5625
    
}

targets = {}

# level_number, level_time, time_to_spawn, start_money, waves: dict, allowed_enemies: tuple, allowed_cords=(192, 320, 448, 576, 704
#
levels_config = {"1": [1, 22500, 750, 50, level_1_waves, ("popusk", "josky")],
                 "2": [2, 22500, 575, 50, level_2_waves, ("josky", "sigma", "sportik", "popusk")],
                 "3": [3, 22500, 500, 50, level_3_waves, ("josky", "sigma", "sportik", "armorik", "zeleniy_strelok", "popusk")],
                 "4": [4, 22500, 225, 50, level_4_waves, ("telezhnik", "rojatel", "sigma", "armorik", "zeleniy_strelok", "drobik")],
                 "5": [5, 31500, 225, 50, level_5_waves, ("popusk", "sigma", "josky", "zeleniy_strelok", "sportik", "rojatel", "mega_strelok", "armorik", "telezhnik", "drobik")]}
