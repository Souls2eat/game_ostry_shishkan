# Примеры волн
level_1_waves = {       # время волны : поинты спавна на волну
    3000: 20,
    2000: 20,
    1000: 20
}

level_2_waves = {
    2000: 30,
    1000: 30,
    500: 30
}

level_3_waves = {
    4000: 40,
    2000: 40
}

level_4_waves = {
    3000: 50,
    2000: 50,
    1000: 50
}
level_5_waves = {
    6000: 60,
    4500: 60,
    3000: 60,
    1500: 60
}


# Примеры стоимости врагов
enemy_costs = {"josky": 2,
               "popusk": 1,
               "sigma": 4,
               "sportik": 3,
               "armorik": 5,
               "rojatel": 4,
               "zeleniy_strelok": 4,
               "drobik": 4,
               "telezhnik": 5,
               "mega_strelok": 20}


# Цены башен
tower_costs = {
    "boomchick": 20,
    "davalka": 20,
    "drachun": 10,
    "fire_mag": 10,
    "kopitel": 20,
    "matricayshon": 30,
    "barrier_mag": 20,
    "parasitelniy": 20,
    "pukish": 25,
    "spike": 10,
    "terpila": 20,
    "thunder": 15,
    "urag_anus": 20,
    "yascerica": 10,
    "zeus": 20,
    "tolkan": 30,
    "big_mechman": 15,
    "nuka_kusni": 15,
    "sushnost_v_vide_gnomika1": 35,
    "go_bleen1": 5,
    "knight_on_horse": 15,
    "gnome_cannon1": 30,
    "bomb": 30,
    "perec": 25,
    "vodka": 30,

}

towers_kd = {
    "boomchick": 200,
    "davalka": 200,
    "drachun": 100,
    "fire_mag": 100,
    "kopitel": 200,
    "matricayshon": 300,
    "barrier_mag": 200,
    "parasitelniy": 200,
    "pukish": 250,
    "spike": 100,
    "terpila": 200,
    "thunder": 150,
    "urag_anus": 200,
    "yascerica": 100,
    "zeus": 200,
    "tolkan": 300,
    "big_mechman": 150,
    "nuka_kusni": 150,
    "sushnost_v_vide_gnomika1": 300,
    "go_bleen1": 15,
    "knight_on_horse": 150,
    "gnome_cannon1": 300,
    "bomb": 1200,
    "perec": 900,
    "vodka": 1500
    
}

targets = {}

# level_number, level_time, time_to_spawn, start_money, waves: dict, allowed_enemies: tuple, allowed_cords=(192, 320, 448, 576, 704
#
levels_config = {1: [1, 4000, 150, 300, level_1_waves, ("popusk", "josky")],
                 2: [2, 3000, 150, 300, level_2_waves, ("josky", "sigma", "sportik", "popusk")],
                 3: [3, 6000, 225, 300, level_3_waves, ("josky", "sigma", "sportik", "armorik", "zeleniy_strelok")],
                 4: [4, 4000, 75, 300, level_4_waves, ("telezhnik", "rojatel", "sigma", "armorik", "zeleniy_strelok", "drobik")],
                 5: [5, 7500, 75, 300, level_5_waves, ("popusk", "sigma", "josky", "zeleniy_strelok", "sportik", "rojatel", "mega_strelok", "armorik", "telezhnik", "drobik")]}
