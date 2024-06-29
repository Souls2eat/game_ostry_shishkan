from math import *
from random import randint, choice
from config import *
from animations import *
from pygame import *

init()
bugs = False  # ура изи победа. программирование пройдено. было слишком легко gg wp ez
clock = time.Clock()
screen = display.set_mode((1600, 900))
display.set_caption("game_ostry_shishkan")
icon = image.load("images/icon/icon.png").convert_alpha()
display.set_icon(icon)

mouse.set_visible(False)
screen.fill((255, 255, 255))

pause_menu = image.load("images/menu/pause_menu.png").convert_alpha()
pause_menu_copy = pause_menu.__copy__()
pause_menu_w = image.load("images/menu/pause_menu_w.png").convert_alpha()
pause_menu_w_copy = pause_menu_w.__copy__()
main_menu = image.load("images/menu/main_menu.png").convert_alpha()
additional_menu = image.load("images/menu/additional_menu.png").convert_alpha()
preview_menu = image.load("images/menu/preview_menu.png").convert_alpha()
select_menu = image.load("images/menu/level_select_menu.png").convert_alpha()
select_menu_copy = select_menu.__copy__()
entity_preview_menu = image.load("images/menu/entity_preview_menu.png").convert_alpha()
entity_preview_menu_copy = entity_preview_menu.__copy__()
modification_preview_menu = image.load("images/menu/modification_guide_menu.png").convert_alpha()
modification_preview_menu_copy = modification_preview_menu.__copy__()
amogus = image.load("images/other/!!!.png").convert_alpha()
cursor = image.load("images/other/cursor.png").convert_alpha()
tower_window_legendary = image.load("images/tower_select_windows/tower_select_window_legendary.png").convert_alpha()
tower_window_common = image.load("images/tower_select_windows/tower_select_window_common.png").convert_alpha()
tower_window_spell = image.load("images/tower_select_windows/tower_select_window_spell.png").convert_alpha()
line_ = image.load("images/other/line.png").convert_alpha()
unknown_entity = image.load("images/buttons_states/unknown_entity.png").convert_alpha()
game_map = image.load("images/maps/game_map.png").convert_alpha()
global_level = image.load("images/maps/global_level.png").convert_alpha()
ok = image.load("images/buttons_states/ok.png").convert_alpha()
upgrade_tower_red = image.load("images/buttons_states/upgrade_tower_red.png").convert_alpha()
upgrade_tower_green = image.load("images/buttons_states/upgrade_tower_green.png").convert_alpha()
upgrade_tower_select = image.load("images/buttons_states/upgrade_tower_select.png").convert_alpha()
upgrade_path = image.load("images/other/upgrade_path.png").convert_alpha()
new_bg = image.load("images/other/new_bg.png").convert_alpha()

font30 = font.Font("fonts/ofont.ru_Nunito.ttf", 30)
font35 = font.Font("fonts/ofont.ru_Nunito.ttf", 35)
font40 = font.Font("fonts/ofont.ru_Nunito.ttf", 40)
font50 = font.Font("fonts/ofont.ru_Nunito.ttf", 50)
font60 = font.Font("fonts/ofont.ru_Nunito.ttf", 60)

game_name = font60.render("GAME_OSTRY_SHISHIKAN", True, (255, 255, 255))  # GAME_OSTRY_SHISHIKAN
game_state = "main_menu"
last_game_state = game_state
buttons_group = []
scroll_offset = 0
coin_indent_x = 0
count_of_reward_coins = 0
current_scroll_offset_state = game_state
continue_level = False
free_money = default_free_money = 750
upgrades = {}
your_coins = {}


class ModGroup(sprite.Group):
    def __init__(self):
        super().__init__()

    def custom_draw(self, surf):
        for sprite_ in sorted(self.sprites(), key=self.sort_by_layer):
            if hasattr(sprite_, "active_game_states"):
                if "cheat" in sprite_.active_game_states:
                    if level.cheat:
                        surf.blit(sprite_.image, sprite_.rect)
                elif game_state in sprite_.active_game_states:
                    surf.blit(sprite_.image, sprite_.rect)
            else:
                surf.blit(sprite_.image, sprite_.rect)

    @staticmethod
    def sort_by_layer(obj_):
        return obj_.render_layer

    def draw_other(self, surf):
        for obj_ in self.sprites():
            if hasattr(obj_, "image2"):
                obj_.draw2(surf)
            if hasattr(obj_, "image3"):
                obj_.draw3(surf)


class BasePreviewGroup:
    def __init__(self, *supported_objects):
        self.entities = []
        self.scroll_pos = 0
        self.hovered_entity = None
        self.pushed_entity = None
        self.supported_objects = supported_objects
        self.turn = self.supported_objects[0]

    def add(self, *entity):
        for en in entity:
            self.entities.append(en)
            towers_group.remove(en)
            enemies_group.remove(en)
            all_sprites_group.remove(en)

    def clear_(self):
        self.entities.clear()
        self.scroll_pos = 0

    def move_element_by_scroll(self, vector="y"):
        for en in self.entities:
            if vector == "y":
                en.pos = en.pos[0], en.pos[1] + scroll_offset - self.scroll_pos
            if vector == "x":
                en.pos = en.pos[0] + scroll_offset - self.scroll_pos, en.pos[1]
            en.rect = en.image.get_rect(topleft=en.pos)
        self.scroll_pos = scroll_offset

    def check_hover(self, surf, offset_pos=(0, 0)):
        surf_width = surf.get_width()
        surf_height = surf.get_height()
        on_surf = surf_width + offset_pos[0] > mouse_pos[0] > offset_pos[0] and surf_height + offset_pos[1] > mouse_pos[1] > offset_pos[1]
        for en in filter(self.filter_by_turn, self.entities):
            en.rect = en.image.get_rect(topleft=(en.pos[0] + offset_pos[0], en.pos[1] + offset_pos[1]))
            if en.rect.collidepoint(mouse_pos) and on_surf:
                self.hovered_entity = en
                return True
        self.hovered_entity = None
        return False

    def check_click(self, surf, offset_pos=(0, 0)):
        surf_width = surf.get_width()
        surf_height = surf.get_height()
        on_surf = surf_width + offset_pos[0] > mouse_pos[0] > offset_pos[0] and surf_height + offset_pos[1] > mouse_pos[1] > offset_pos[1]
        for en in filter(self.filter_by_turn, self.entities):
            en.rect = en.image.get_rect(topleft=(en.pos[0] + offset_pos[0], en.pos[1] + offset_pos[1]))
            if not en.rect.collidepoint(mouse_pos):
                en.pushed = False
            if en.rect.collidepoint(mouse_pos):
                if mouse.get_pressed()[0] == 1 and not en.pushed:
                    en.pushed = True
            if mouse.get_pressed()[0] == 0 and en.pushed and on_surf:
                en.pushed = False
                self.pushed_entity = en
                return True
        return False

    def filter_by_turn(self, en):
        return isinstance(en, self.turn)  # noqa

    def __len__(self):
        return len(self.entities)


class PreviewGroup(BasePreviewGroup):
    def __init__(self, *supported_objects):
        super().__init__(*supported_objects)
        self.remember_entities = []

    def set_default_pushed_entity(self):
        if not self.pushed_entity:
            self.pushed_entity = self.entities[0]

    def remember_entity(self):
        if self.pushed_entity not in self.remember_entities:
            self.remember_entities.append(self.pushed_entity)

    def remove_remember_entity(self, obj_="pushed_entity"):
        if obj_ == "pushed_entity":
            if self.pushed_entity in self.remember_entities:
                self.remember_entities.remove(self.pushed_entity)
        else:
            if obj_ in self.remember_entities:
                self.remember_entities.remove(obj_)

    def remember_entities_empty(self):
        for tower in self.remember_entities:
            tower.in_slot = False
            tower.kill()
        self.remember_entities.clear()

    def custom_draw(self, surf, offset_pos=(0, 0)):
        for en in filter(self.filter_by_turn, self.entities):
            en.rect = en.image.get_rect(topleft=(en.pos[0] + offset_pos[0], en.pos[1] + offset_pos[1]))
            # draw.rect(screen, "GREEN", en.rect, 5)
            if en.name in received_towers or en.name in encountered_enemies:
                surf.blit(en.image, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))
            else:
                surf.blit(unknown_entity, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))
            if hasattr(en, "rarity"):
                if en.rarity == "legendary":
                    surf.blit(tower_window_legendary, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))
                if en.rarity == "common":
                    surf.blit(tower_window_common, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))
                if en.rarity == "spell":
                    surf.blit(tower_window_spell, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))
            else:
                surf.blit(tower_window_common, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))
            if en in self.remember_entities:
                surf.blit(ok, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))

    def go_animation(self):
        for en in self.entities:
            if en == self.hovered_entity:
                en.state = "attack"
            else:
                en.state = "wait"
            en.animation()

    def get_max_damage_per_sec(self):       # добавить 2 кд 2 атаку и белый список мб
        return self.get_damage_per_sec(sorted(filter(self.filter_by_turn, self.entities), key=PreviewGroup.get_damage_per_sec)[-1])

    @staticmethod
    def get_damage_per_sec(obj_):
        if hasattr(obj_, "basic_attack_cooldown"):
            return obj_.atk / (obj_.basic_attack_cooldown / 75)
        return 0

    def get_max_attack_range(self):
        return sorted(filter(self.filter_by_turn, self.entities), key=lambda en: en.attack_range)[-1].attack_range

    def get_max_hp(self):
        return sorted(filter(self.filter_by_turn, self.entities), key=lambda en: en.hp)[-1].hp
    
    def get_max_speed(self):
        return sorted(filter(self.filter_by_turn, self.entities), key=self.get_speed)[-1].speed

    @staticmethod
    def get_speed(en):
        if hasattr(en, "speed"):
            return en.speed
        return 0

    def entity_create(self, columns, indent=30):
        if Tower in self.supported_objects:
            for i, tower_name in enumerate([*received_towers, *not_received_towers]):
                line = int(i / columns)
                column = (i % columns)
                entity = Tower(tower_name, (indent + column * (128 + indent - 4), indent + (line * (128 + indent - 4))))  # 50, 100
                if hasattr(entity, "blackik"):
                    entity.blackik.kill()
                for b in buffs_group:
                    b.kill()
                self.add(entity)
        if Enemy in self.supported_objects:
            for i, enemy_name in enumerate([*encountered_enemies, *not_encountered_enemies]):
                line = int((i / columns))
                column = (i % columns)
                entity = Enemy(enemy_name, (indent + column * (128 + indent - 4), indent + (line * (128 + indent - 4))))
                self.add(entity)

    def refresh(self, columns, indent=30):
        self.clear_()
        self.entity_create(columns, indent)

    def get_len_remembered(self):
        return len(self.remember_entities)


class RewardsPreviewGroup(BasePreviewGroup):
    def __init__(self):
        super().__init__(Tower)
        self.rewards = []

    def new_reward(self, tower_name):
        if tower_name not in self.rewards:
            self.rewards.append(tower_name)
            if tower_name not in received_towers:
                received_towers.append(tower_name)

    def clear_rewards(self):
        for reward in self.entities:
            reward.kill()
        self.entities.clear()
        self.rewards.clear()

    def entity_create(self, columns, indent=30):
        for i, tower_name in enumerate(self.rewards):
            indent_x = (640 - (columns * 128)) // (columns + 1)
            column = (i % columns)
            entity = Tower(tower_name, (indent_x + (column * (128 + indent_x)), indent))
            if hasattr(entity, "blackik"):
                entity.blackik.kill()
            for b in buffs_group:
                b.kill()
            self.add(entity)

    def custom_draw(self, surf):
        for tower in self.entities:
            surf.blit(tower.image, tower.rect)
            if hasattr(tower, "rarity"):
                if tower.rarity == "legendary":
                    surf.blit(tower_window_legendary, tower.rect)
                if tower.rarity == "common":
                    surf.blit(tower_window_common, tower.rect)
                if tower.rarity == "spell":
                    surf.blit(tower_window_spell, tower.rect)

    def go_animation(self):
        for tower in self.entities:
            tower.animation()


class GlobalMap(BasePreviewGroup):
    def __init__(self):
        super().__init__(GlobalMapLevelButton)
        self.chest = None

    def custom_draw(self, surf):
        for level_ in self.entities:
            # draw.rect(screen, (0, 255, 0), level_.rect, 5)
            if level_.parent in passed_levels:
                surf.blit(level_.image, level_.rect)
                if not level_.chest:
                    if len(str(level_.number)) < 2:
                        surf.blit(font60.render(f"{str(level_.number)}", True, (0, 0, 0)), (level_.rect.x + 30, level_.rect.y + 6))
                    elif len(str(level_.number)) < 99:
                        surf.blit(font60.render(f"{str(level_.number)}", True, (0, 0, 0)), (level_.rect.x + 12, level_.rect.y + 6))
                else:
                    # surf.blit(levels[level_.number].image, level_.rect)
                    if level_.level:
                        surf.blit(level_.level.image, level_.rect)
                    if level_.chest:
                        surf.blit(level_.chest.image, level_.rect)

    def use_clicked_object(self):
        global scroll_offset, continue_level, last_game_state, game_state, level, passed_levels
        if self.pushed_entity:
            if self.pushed_entity.parent in passed_levels:
                if self.pushed_entity.level:
                    # level = levels[self.pushed_entity.number]
                    level = self.pushed_entity.level
                    scroll_offset = 0
                    continue_level = True
                    level.refresh()
                    last_game_state = game_state
                    game_state = "tower_select"
                if self.pushed_entity.chest:
                    if not self.pushed_entity.chest.open:
                        self.chest = self.pushed_entity.chest
                        self.chest.opening()
            self.pushed_entity = None


class TowerUpgradesGroup(BasePreviewGroup):
    def __init__(self):
        super().__init__(UpgradeTowerButton)

    def custom_draw(self, surf, offset_pos=(0, 0)):
        for upgrade in filter(self.filter_by_turn, self.entities):
            upgrade.rect = upgrade.image.get_rect(topleft=(upgrade.pos[0] + offset_pos[0], upgrade.pos[1] + offset_pos[1]))

            if preview_group.turn == Tower:
                if upgrade.number in upgrades[preview_group.pushed_entity.name]:
                    upgrade.set_active(True)
                else:
                    upgrade.set_active(False)
            surf.blit(upgrade.image, (upgrade.rect.x - offset_pos[0], upgrade.rect.y - offset_pos[1]))
            if self.pushed_entity == upgrade:
                surf.blit(upgrade_tower_select, (upgrade.rect.x - offset_pos[0], upgrade.rect.y - offset_pos[1]))

    @staticmethod
    def possible_upgrade_path():
        for up in upgrades[preview_group.pushed_entity.name]:
            if tower_upgrades_group.pushed_entity.number != "1" and up != "1":
                if up[1] != tower_upgrades_group.pushed_entity.number[1]:
                    return False

        last_update = str(int(tower_upgrades_group.pushed_entity.number[0]) - 1) + tower_upgrades_group.pushed_entity.number[1]
        if last_update in upgrades[preview_group.pushed_entity.name] or last_update[0] == "1":
            return True
        return False


class TextSprite(sprite.Sprite):
    def __init__(self, sprite_, pos, active_game_states=()):
        super().__init__(all_sprites_group, text_sprites_group)
        self.image = sprite_
        self.rect = self.image.get_rect(topleft=pos)
        self.render_layer = 2
        self.active_game_states = list(active_game_states)

    def update_text(self, sprite_):
        self.image = sprite_


class Level:
    def __init__(self, level_number, level_time, time_to_spawn, start_money, waves: dict, allowed_enemies: tuple, allowed_cords=(192, 320, 448, 576, 704), blocked_slots=(), level_image="default"):
        if level_image == "default":
            self.image = image.load(f"images/maps/map{level_number}.png").convert_alpha()
        else:
            self.image = image.load(f"images/maps/map{level_image}.png").convert_alpha()
        self.current_level = level_number
        self.money = self.start_money = start_money
        self.state = "not_run"
        self.level_time = self.start_level_time = level_time
        self.start_time_to_spawn = self.time_to_spawn = time_to_spawn
        self.cheat = False
        self.waves = waves
        self.allowed_enemies = allowed_enemies
        self.allowed_cords = allowed_cords
        self.blocked_slots = blocked_slots

        self.x = 384     # для полоски уровня
        self.y = 110
        self.w = 1151
        self.h = 40

    def draw_level_time(self):      # надо бы написать по-понятней
        ratio = self.level_time / self.start_level_time
        draw.rect(screen, (233, 126, 72), (self.x, self.y, self.w, self.h))
        draw.rect(screen, (55, 127, 236), (self.x, self.y, self.w * ratio, self.h))
        draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h), 4)
        for wave_time in self.waves:
            mark_ratio = wave_time / self.start_level_time
            screen.blit(amogus, (self.x + int(mark_ratio * self.w), self.y - 30))

    def wave_spawn_enemies(self, wave_time):
        waves_points = self.waves[wave_time]
        enemy_x_cord = 1600
        while waves_points > 0:
            enemy_name = choice(self.allowed_enemies)
            enemy_y_cord = choice(self.allowed_cords)
            Enemy(enemy_name, (enemy_x_cord, enemy_y_cord))
            waves_points -= enemy_costs[enemy_name]
            enemy_x_cord += randint(10, 30)

    def random_spawn_enemies(self):
        enemy_y_cord = choice(self.allowed_cords)
        enemy_name = choice(self.allowed_enemies)
        Enemy(enemy_name, (1600, enemy_y_cord))

    @staticmethod
    def clear(*dont_clear_groups):
        if buttons_group not in dont_clear_groups:
            for button in buttons_group:
                button.ok = False
        select_towers_preview_group.remember_entities_empty()
        if ui_group not in dont_clear_groups:
            for ui in ui_group:
                ui.kill()

        for sprite_ in all_sprites_group:
            if dont_clear_groups:
                for group in dont_clear_groups:
                    if sprite_ not in group and sprite_ not in text_sprites_group:
                        sprite_.kill()
            else:
                if sprite_ not in text_sprites_group:
                    sprite_.kill()

    @staticmethod
    def spawn():
        UI((1500, 800), "shovel", "lopata", False)

        Cloud((1000, 100))
        Cloud((600, 60))
        Cloud((300, 70))
        Cloud((720, 20))
        Cloud((1400, 50))
        Cloud((1200, 30))
        Cloud((1800, 90))

        return "run"

    def refresh(self):
        self.money = self.start_money
        self.level_time = self.start_level_time
        self.time_to_spawn = self.start_time_to_spawn
        self.state = "not_run"
        self.clear()

    def give_reward(self):
        global passed_levels

        random_coin = choice([c for c in your_coins.keys()])
        your_coins[random_coin] += 5

        # if len(not_received_towers) > 3:
        #     Alert("+ 3 башни открыто", (100, 100), 75)
        #     for i in range(3):
        #         new_tower = choice(not_received_towers)
        #         not_received_towers.remove(new_tower)
        #         received_towers.append(new_tower)
        # elif len(not_received_towers) == 3:
        #     Alert("Последние 3 башни открыты", (100, 100), 75)
        #     for i in range(3):
        #         new_tower = choice(not_received_towers)
        #         not_received_towers.remove(new_tower)
        #         received_towers.append(new_tower)
        # elif len(not_received_towers) >= 2:
        #     Alert("Последние 2 башни открыты", (100, 100), 75)
        #     for i in range(2):
        #         new_tower = choice(not_received_towers)
        #         not_received_towers.remove(new_tower)
        #         received_towers.append(new_tower)
        # elif len(not_received_towers) >= 1:
        #     Alert("Последняя башня открыта", (100, 100), 75)
        #     new_tower = choice(not_received_towers)
        #     not_received_towers.remove(new_tower)
        #     received_towers.append(new_tower)
        # else:
        #     Alert("Все башни открыты", (100, 100), 75)
        #
        # if len(not_encountered_enemies) >= 1:
        #     for enemy_ in levels[self.current_level][5]:
        #         if enemy_ not in encountered_enemies:
        #             encountered_enemies.append(enemy_)
        #             not_encountered_enemies.remove(enemy_)
        #             Alert("Новые враги известны", (100, 200), 75)
        # else:
        #     Alert("Все враги известны", (100, 200), 75)

        preview_group.refresh(3)
        if self.current_level not in passed_levels:
            passed_levels.append(self.current_level)
        save_data()

    def update(self):
        all_sprites_group.update()
        for wave_time in self.waves:
            if self.level_time == wave_time:
                self.wave_spawn_enemies(wave_time)
        if self.state == "not_run":
            self.state = self.spawn()
        if not self.cheat:
            if self.time_to_spawn > 0:
                self.time_to_spawn -= 1
            else:
                self.time_to_spawn = self.start_time_to_spawn
                self.random_spawn_enemies()
            if self.level_time > 0 or len(enemies_group) > 0:
                self.level_time -= 1
                return "run"
            else:
                self.give_reward()
                return "level_complited"
        else:
            return "run"

    def __repr__(self):
        return str((self.current_level, self.level_time, self.state))


class Chest:
    def __init__(self, parent_number: str, rewards: dict):
        self.rewards = rewards      # башни/коины
        if parent_number not in passed_levels:
            self.image = image.load("images/maps/chest.png")
            self.open = False
        else:
            self.open = True
            self.image = image.load("images/maps/chest_open.png")

    def opening(self):
        global game_state
        self.open = True
        self.image = image.load("images/maps/chest_open.png")
        if global_map.pushed_entity.number not in passed_levels:
            passed_levels.append(global_map.pushed_entity.number)
        game_state = "reward_first_stage"

    def refresh(self):
        self.open = False
        self.image = image.load("images/maps/chest.png")


class Tower(sprite.Sprite):
    def __init__(self, unit, pos):
        super().__init__(towers_group, all_sprites_group)
        self.image = image.load(f"images/towers/{unit}/wait/{unit}{str(1)}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pos
        self.name = unit
        if self.name in upgrades:
            self.upgrade_level = upgrades[self.name][-1]
        if self.name == "shovel":
            self.render_layer = 9
        else:
            self.render_layer = 4
        targets[id(self)] = None

        self.is_dead = False
        self.have_barrier = False
        self.barrier = None
        self.stack = False
        self.free_placement = False

        self.time_indicator = 1
        self.anim_tasks = []
        self.anim_count = 0
        self.anim_duration = 15     # сколько кадров будет оставаться 1 спрайт
        self.state = "wait"         # потом будет "attack", "death" и какие придумаете

        self.pushed = False
        self.in_slot = False

        # СТАТЫ начало

        if self.name == 'fire_mag':
            self.hp = 200
            self.atk = 10
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 75
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.rarity = "common"
            if self.upgrade_level == "2a" or self.upgrade_level == '3a':  # циферки поменять мб
                self.atk_big = 20
                self.attack_count = 0
                self.fire_form = False
                self.fire_form_duration = self.basic_fire_form_duration = 6
                self.fire_form_cooldown = self.basic_fire_form_cooldown = 6
            if self.upgrade_level == "2b" or self.upgrade_level == '3b':
                self.atk_dot = 1  # dot = damage_over_time    # типа он поджогом дамажит 5 сек по 1 урону и в итоге у него от каждой тычки дамаг в 1,5 раза увеличивается но растянуто
                # новый функционал

        if self.name == 'boomchick':  
            self.hp = 200
            self.atk = 10  # типа по кому попадёт получит 20 а остальные по 10
            self.bullet_speed_x = 4
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 150
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'kopitel':
            self.hp = 200
            self.atk = 32  # я так сделал чтобы анимации ахуенно ложились
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_spawn_something_cooldown = self.spawn_something_cooldown = 120
            self.spawned_things = []
            self.basic_attack_cooldown = self.attack_cooldown = 120
            self.damage_type = ''
            self.nakopleno = 0
            self.max_nakopit = 7
            self.rarity = "common"
            if self.upgrade_level == "2a" or self.upgrade_level == '3a':
                self.atk_big = 96

        if self.name == 'thunder':
            self.hp = 200
            self.atk = 15
            self.bullet_speed_x = 7
            self.bullet_speed_y = 3
            self.attack_cooldown = self.basic_attack_cooldown = 225
            self.target_phase = None
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'thunder_kamen':
            self.hp = 2000
            self.rarity = "common"

        if self.name == 'gribnik':
            self.hp = 300  # ну а почему бы и нет
            self.atk = 15
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 225
            self.target_phase = None
            self.damage_type = ''
            self.rarity = "common"

        for i in range(3):
            if self.name == 'grib' + str(i + 1):
                self.hp = 300 * (i + 1)
                self.rarity = "common"

        if self.name == 'zeus':
            self.hp = 50
            self.atk = 15
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = self.attack_cooldown = 150
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'yascerica':
            self.hp = 200
            self.atk = 0
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 1125
            if self.upgrade_level == '2a':
                self.basic_attack_cooldown = 900
            elif self.upgrade_level == '3a':
                self.basic_attack_cooldown = 750
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            if self.upgrade_level == '2b' or self.upgrade_level == '3b':
                if self.upgrade_level == '2b':
                    self.bullet_stomach_capacity = 2
                if self.upgrade_level == '3b':
                    self.bullet_stomach_capacity = 3
            self.blackik = Bullet("blackik", self.rect.centerx - 26, self.rect.centery, self.damage_type, 0, self.bullet_speed_x, self.bullet_speed_y, 'yas', self)
            self.blackik.remove(bullets_group)
            self.rarity = "legendary"

        if self.name == 'electric':
            self.hp = 200
            self.atk = 3  # типо дальней атакой он наносит 45 урона в 1 цель за 4 секунды(3 сек кд и 1 сек он всё выпускает)
            self.atk2 = 45  # а ближней он наносит 45 урона сплешом за 3 секунды
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 225
            self.attack_cooldown_burst = self.basic_attack_cooldown_burst = 5
            self.ammo = self.basic_ammo = 15
            self.target_phase = None
            self.bursting = False
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'struyniy':  # пока что он слишком имба под баффом но мы что-нибудь придумаем. хотя мб нет
            self.hp = 200
            self.atk = 2
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 1125
            self.attack_cooldown_burst = self.basic_attack_cooldown_burst = 3
            self.ammo = self.basic_ammo = 27
            self.bursting = False
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'dark_druid':
            self.hp = 200
            self.atk = 5
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 1500
            self.attack_cooldown = self.basic_attack_cooldown
            self.ravens = 3
            self.ravens_dead = 5
            self.damage_type = ''
            self.rarity = "common"
            if self.upgrade_level == "2a":
                self.ravens = 5
                self.ravens_dead = 7
            if self.upgrade_level == '3a':
                self.ravens = 10
                self.ravens_dead = 15
            for i in range(self.ravens):
                if self.ravens % 2 == 1:
                    if i % 2 == 0:
                        Parasite('raven', self.rect.centerx - 26, self.rect.bottom - 16*(i+1), self.damage_type, self.atk, self, self)
                    else:
                        Parasite('raven', self.rect.centerx - 58, self.rect.bottom - 16*(i+1), self.damage_type, self.atk, self, self)
                else:
                    if i % 2 == 0:
                        Parasite('raven', self.rect.centerx - 26, self.rect.bottom - 16*(i+1), self.damage_type, self.atk, self, self)
                    else:
                        Parasite('raven', self.rect.centerx - 58, self.rect.bottom - 16*i, self.damage_type, self.atk, self, self)

        if self.name == 'electro_maga':
            self.hp = 200
            self.atk = 0
            self.bullet_speed_x = 1
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 375
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.rarity = "legendary"

        if self.name == 'parasitelniy':
            self.hp = 2500
            self.max_hp = 2500
            self.atk = 5
            self.attack_cooldown = self.basic_attack_cooldown = 150
            self.damage_type = ''
            self.have_parasite = sprite.Group()
            self.rarity = "common"

        if self.name == 'nekr':
            self.hp = 200
            self.atk = 30  # я хз надо ли некру писать атк(атака сейчас нигде не используется, оставил чтобы не ломать справочник), можно сделать чтобы его призывники наследовали атаку, а можно и чтобы у них в ините она прописывалась, хз короч, потом решим
            self.attack_cooldown = self.basic_attack_cooldown = 750  # потом отбалансим. кстати можно его не через атаку сделать а через spawn_something, но это потом, пока что делаю через shoot
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'spike':  
            self.hp = 1
            self.atk = 20
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.damage_type = ''
            self.remove(towers_group)
            self.add(nekusaemie_group)
            self.rarity = "common"

        if self.name == 'pukish':
            self.hp = 1
            self.atk = 15
            self.atk2 = 2
            self.bullet_speed_x = 2
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 150
            self.attack_cooldown2 = self.basic_attack_cooldown2 = 15
            self.damage_type = ''
            self.hiding = False
            self.remove(towers_group)
            self.add(nekusaemie_group)
            self.rarity = "legendary"

        if self.name == 'urag_anus':
            self.hp = 700
            self.atk = 0
            self.uragan_duration = 450
            self.basic_attack_cooldown = 2250
            self.attack_cooldown = 375
            self.uragan = None
            self.rarity = "legendary"
            if self.upgrade_level == "2a" or self.upgrade_level == '3a':
                self.uragan_duration = 525
                self.uragan_speed = 0.5

        if self.name == 'drachun':
            self.hp = 700
            self.atk = self.basic_atk = 30
            self.basic_attack_cooldown = 60
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.rarity = "common"
            if self.upgrade_level == "2b" or self.upgrade_level == '3b':
                if self.upgrade_level == "2b":
                    self.hp = self.max_hp = 1200
                else:
                    self.hp = self.max_hp = 2000
                    self.self_buff_level = 0
                    self.kill_time = 375

        if self.name == 'knight_on_horse':       # нука кусни нет, потому что он подгружает картинки по кд
            self.knight_hp = 1500                 # nuka_kusni
            self.horse_hp = 1500  # уменьшить отхилл рыцарю
            self.hp = self.knight_hp + self.horse_hp
            self.atk = 20
            self.taran_atk = 400
            self.attack_cooldown = self.basic_attack_cooldown = 150
            self.damage_type = ''
            self.rarity = "legendary"

        if self.name == "knight":
            self.hp = 1500
            self.atk = 20
            self.attack_cooldown = self.basic_attack_cooldown = 150
            self.damage_type = ''
            self.rarity = "legendary"

        if self.name == 'tolkan':
            self.hp = 3000
            self.atk = 50
            self.ottalkivanie_solo = self.push = 384
            self.ottalkivanie_ne_solo = 192
            self.za_towerom = False
            self.basic_attack_cooldown = 1500
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'big_mechman':
            self.hp = 700
            self.atk = 100
            self.kulak_time = 15
            self.attack_cooldown = self.basic_attack_cooldown = 375
            self.damage_type = ''
            self.rarity = "common"

        # for i in range(16):                           # гоблина нет, потому что 16 папок это тупизм
        #     if self.name == 'go_bleen' + str(i+1):    # пока оставил
        #         self.hp = 100 * (i+1)
        #         self.atk = 10
        #         self.bullet_speed_x = 4
        #         self.bullet_speed_y = 0
        #         self.basic_attack_cooldown = 100
        #         self.attack_cooldown = self.basic_attack_cooldown
        #         self.damage_type = ''

        if self.name == 'gnome_cannon1':
            self.max_hp = 500
            self.hp = 500
            self.atk = 150
            self.bullet_speed_x = 10
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 750
            self.damage_type = ''
            self.stack = "gnome_cannon"
            self.rarity = "legendary"

        if self.name == 'gnome_cannon2':
            self.max_hp = 2500
            self.hp = 2500
            self.heal = 10
            self.atk = 150
            self.bullet_speed_x = 10
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 450
            self.healing_cooldown = self.basic_healing_cooldown = 75
            self.damage_type = ''
            self.stack = "gnome_cannon"
            self.rarity = "legendary"

        if self.name == 'gnome_cannon3':
            self.max_hp = 2500
            self.hp = 2500
            self.heal = 10
            self.atk = 150
            self.bullet_speed_x = 10
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 375
            self.healing_cooldown = self.basic_healing_cooldown = 75
            self.damage_type = ''
            self.stack = "gnome_cannon"
            self.rarity = "legendary"

        if self.name == 'gnome_flamethrower':
            self.max_hp = 1
            self.hp = 1
            self.atk = 0
            self.atk2 = 3   # баффающая башня не баффает скорость атаки огнемета, если надо будет сделаю чтобы баффала
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_cooldown2 = self.basic_attack_cooldown2 = 6
            self.damage_type = ''
            self.remove(towers_group)
            self.add(nekusaemie_group)
            self.rarity = "legendary"

        if self.name == 'terpila':
            self.hp = 7500
            self.rarity = "common"

        if self.name == 'barrier_mag':
            self.hp = 1500
            self.barrier_hp = 3000
            self.best_x = self
            self.basic_spawn_something_cooldown = 3375  # 3375
            self.spawn_something_cooldown = 0
            self.rarity = "common"

        if self.name == 'davalka':
            self.hp = 200
            self.skolko_deneg_dast = 10
            self.basic_spawn_something_cooldown = self.spawn_something_cooldown = 1500  # возможно надо 1875
            self.rarity = "common"

        if self.name == 'matricayshon':
            self.hp = 666
            for i in range(9):
                self.buff_x = 1 + (i % 3) * 128 - 128
                self.buff_y = 1 + (i // 3) * 128 - 128
                self.buff = Buff("mat", self.rect.x + self.buff_x, self.rect.y + self.buff_y, self)
            self.rarity = "legendary"

        if self.name == 'bolotnik':
            self.hp = 200
            for i in range(5):
                self.debuff_x = 1 + i * 128
                self.debuff = Buff('boloto', self.rect.x + self.debuff_x, self.rect.y, self)

        if self.name == 'pen':
            self.hp = 200
            self.rarity = "common"

        # я решил спеллы внизу писать

        if self.name == 'bomb':
            self.hp = 0
            self.atk = 700
            self.damage_type = ''
            self.rarity = "spell"

        if self.name == 'perec':
            self.hp = 0
            self.atk = 700
            self.free_placement = True
            self.damage_type = ''
            self.rarity = "spell"

        if self.name == 'vodka':
            self.hp = 0  # надо сделать предел усиления (3 сек)
            self.free_placement = True
            self.rarity = "spell"

        if self.name == 'easy_money':
            self.hp = 0
            self.free_placement = True
            self.rarity = "spell"

        if self.name == 'vistrel':
            self.hp = 0
            self.atk = 30
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.free_placement = True
            self.damage_type = ''
            self.rarity = "spell"

        if self.name == 'molniya':
            self.hp = 0
            self.atk = 1000
            self.free_placement = True
            self.damage_type = ''
            self.moiniya_popala = False
            self.rarity = "spell"

        if self.name == 'tp_back':
            self.hp = 0
            self.free_placement = True
            self.rarity = "spell"

        # СТАТЫ конец
        self.image2 = font30.render(str(self.hp), True, (0, 0, 0))
        self.rect2 = self.image.get_rect(topleft=(self.rect.x + 32, self.rect.y - 32))

    def add_anim_task(self, anim, func):
        if len(self.anim_tasks) == 0:
            self.anim_tasks.append([anim, (4 * self.anim_duration) // self.time_indicator, func])
            self.anim_count = 0
        else:
            already_in = [anim[0] for anim in self.anim_tasks]
            if anim not in already_in:
                self.anim_tasks.append([anim, (4 * self.anim_duration) // self.time_indicator, func])

    def prime_anim(self, anim, func):
        if anim not in [an[0] for an in self.anim_tasks]:
            self.anim_tasks.clear()
            self.add_anim_task(anim, func)

    def dead(self):
        if self.name == "gnome_cannon3":
            for tower in nekusaemie_group:
                if tower.rect.collidepoint(self.rect.centerx, self.rect.centery):
                    tower.kill()

        if self.name == "boomchick":
            Bullet("explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk * 5, 0, 0, 'explosion', self)

        if self.name == "thunder":
            Tower('thunder_kamen', self.pos)

        if self.name == 'gribnik':
            Tower('grib3', self.pos)
            for i in range(0, 8, 2):
                if i < 4:
                    grib = Tower('grib1', ((384 + ((self.rect.x - 384) // 128) * 128), (192 + ((self.rect.y+(128*(i-1)) - 192) // 128) * 128)))
                else:
                    grib = Tower('grib1', ((384 + ((self.rect.x+(128*(i-5)) - 384) // 128) * 128), (192 + ((self.rect.y - 192) // 128) * 128)))
                if not (1536 > grib.pos[0] >= 384 and 832 > grib.pos[1] >= 192) or not is_free(grib):
                    grib.kill()

        if self.name == 'dark_druid':
            self.kill()  # так надо
            for enemy in enemies_group:
                if self in enemy.parasite_parents:
                    enemy.parasite_parents.remove(self)
            for i in range(self.ravens_dead):
                if self.ravens_dead % 2 == 1:
                    if i % 2 == 0:
                        Parasite('raven', self.rect.right - 16, self.rect.bottom - 16*(i+1), self.damage_type, self.atk, self, self)
                    else:
                        Parasite('raven', self.rect.right - 48, self.rect.bottom - 16*(i+1), self.damage_type, self.atk, self, self)
                else:
                    if i % 2 == 0:
                        Parasite('raven', self.rect.right - 16, self.rect.bottom - 16*(i+1), self.damage_type, self.atk, self, self)
                    else:
                        Parasite('raven', self.rect.right - 48, self.rect.bottom - 16*i, self.damage_type, self.atk, self, self)
        # спеллы

        if self.name == "bomb":
            Bullet("explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'explosion', self)
        
        if self.name == "perec":
            Bullet("perec_bullet", 960, self.rect.bottom-8, self.damage_type, self.atk, 0, 0, 'explosion', self)

        if self.name == "vistrel":
            Bullet("vistrel_bullet", 384, self.rect.centery-10, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)

        if self.name == 'molniya':
            for i in range(3):
                for enemy in enemies_group:
                    if enemy.alive and self not in enemy.parasite_parents:
                        enemy.parasite_parents.add(self)
                        self.moiniya_popala = True
                        Parasite('mol', enemy.rect.centerx, enemy.rect.bottom - 450, self.damage_type, self.atk, enemy, self)
                        break
                if not self.moiniya_popala:
                    Parasite('mol', randint(384, 1536), randint(-258, 382), self.damage_type, self.atk, self, self)
                self.moiniya_popala = False

        if self.name == "vodka":
            for i in range(9):
                self.buff_x = 1 + (i % 3) * 128 - 128
                self.buff_y = 1 + (i // 3) * 128 - 128
                self.buff = Buff("vodkamat", self.rect.x + self.buff_x, self.rect.y + self.buff_y, self)

        if self.name == "easy_money":
            level.money += 30

        if self.name == "tp_back":
            for enemy_ in enemies_group:
                if enemy_.rect.centerx <= 1024:
                    enemy_.real_x = 1536

        if self.name == 'drachun' and self.upgrade_level == '3b':
            if self.kill_time > 0:
                self.kill_time -= 1
            else:
                self.kill()
        else:
            self.kill()     # + потом анимация смерти

    def check_hp(self):
        if self.name == 'drachun' and (self.upgrade_level == "2b" or self.upgrade_level == "3b"):
            if self.hp > 0:
                self.dop_damage = (self.max_hp - self.hp)//(self.max_hp*0.05)
            else:
                self.dop_damage = self.max_hp//(self.max_hp*0.05)
            self.atk = self.basic_atk + self.dop_damage
            if self.upgrade_level == '3b':
                if self.hp > self.max_hp//2 and self.self_buff_level != 0:
                    if self.self_buff_level == 1:
                        self.time_indicator //= 2
                        self.basic_attack_cooldown *= 2
                    elif self.self_buff_level == 2:
                        self.time_indicator //= 4
                        self.basic_attack_cooldown *= 4
                    self.self_buff_level = 0
                elif 0 < self.hp <= self.max_hp//2 and self.self_buff_level != 1:
                    if self.self_buff_level == 0:
                        self.time_indicator *= 2
                        self.basic_attack_cooldown //= 2
                    elif self.self_buff_level == 2:
                        self.time_indicator //= 2
                        self.basic_attack_cooldown *= 2
                    self.self_buff_level = 1
                elif self.hp <= 0 and self.self_buff_level != 2:
                    if self.self_buff_level == 0:
                        self.time_indicator *= 4
                        self.basic_attack_cooldown //= 4
                    elif self.self_buff_level == 1:
                        self.time_indicator *= 2
                        self.basic_attack_cooldown //= 2
                    self.self_buff_level = 2                  

    def is_additional_attack_allow(self):
        if self.name == "pukish":
            if self.hiding:
                return True
        if self.name == "gnome_flamethrower":
            if self.state == "attack":
                return True

    def find_target(self):
        if self.name == "fire_mag"\
                or self.name == "boomchick"\
                or self.name == "zeus"\
                or self.name == 'gnome_cannon1'\
                or self.name == 'gnome_cannon2'\
                or self.name == 'gnome_cannon3'\
                or self.name == 'struyniy'\
                or self.name == 'nekr'\
                or self.name == 'gribnik'\
                or self.name == 'electro_maga':
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                    return enemy
                
        if self.name == 'kopitel':
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive and self.nakopleno > 0:
                    return enemy

        if self.name == 'parasitelniy':
            for enemy in enemies_group:
                if self not in enemy.parasite_parents and enemy.alive:
                    return enemy

        if self.name == "thunder":
            for enemy in enemies_group:
                if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive and (-10 > enemy.rect.y - self.rect.y or enemy.rect.y - self.rect.y > 10):
                    self.target_phase = 'side'
                    return enemy
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                    self.target_phase = 'center'
                    return enemy

        if self.name == "electric":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256 and enemy.alive:
                    self.target_phase = 'close'
                    return enemy
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x > self.rect.x + 256 and enemy.alive:
                    self.target_phase = 'far'
                    return enemy

        if self.name == "urag_anus":
            enemies = [enemy for enemy in enemies_group if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive]
            if enemies:     # проверка, что список не пустой
                enemy_x_cords = [enemy.rect.x for enemy in enemies]
                return enemies[enemy_x_cords.index(min(enemy_x_cords))]         # не убирать

        if self.name == "yascerica":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and 1536 > enemy.rect.x >= self.rect.x and self.blackik.sumon == 'baza' and enemy.alive:
                    return enemy

        if self.name == "spike":            # ауе дамаг
            for enemy in enemies_group:
                if enemy.rect.colliderect(self.rect):
                    return enemy

        if self.name == 'big_mechman':      # ауе дамаг
            for enemy in enemies_group:
                if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.rect.x - self.rect.x <= 256:
                    return enemy

        if self.name == "drachun" or self.name == "tolkan" or self.name == "knight":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256 and enemy.alive:
                    return enemy

        if self.name == "knight_on_horse":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 384 and enemy.alive:
                    return enemy

        if self.name == "pukish":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.centerx >= self.rect.x-10 and enemy.alive:
                    return enemy

        if self.name == "gnome_flamethrower":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 192 and enemy.alive:
                    return enemy

        return None

    def check_target_alive(self):
        if targets[id(self)]:
            if targets[id(self)].rect.x < self.rect.x:
                targets[id(self)] = None
            elif (self.name == 'thunder' and self.target_phase == 'center') or (self.name == 'electric' and self.target_phase == 'far')or self.name == 'urag_anus':
                targets[id(self)] = None
            elif targets[id(self)].name == 'teleportik':
                targets[id(self)] = None

        if targets[id(self)]:
            if targets[id(self)].alive:
                self.attack_cooldown = self.basic_attack_cooldown
                self.add_anim_task("attack", self.shoot)
            else:
                targets[id(self)] = self.find_target()
                if targets[id(self)]:
                    if targets[id(self)].alive:
                        self.attack_cooldown = self.basic_attack_cooldown
                        self.add_anim_task("attack", self.shoot)
        else:
            targets[id(self)] = self.find_target()
            if targets[id(self)]:
                if targets[id(self)].alive:
                    self.attack_cooldown = self.basic_attack_cooldown
                    self.add_anim_task("attack", self.shoot)

    def dealing_damage(self, enemy):
        if hasattr(enemy, 'armor') and enemy.armor > 0:
            if self.atk <= enemy.armor:
                enemy.armor -= self.atk
            else:
                enemy.hp -= (self.atk - enemy.armor)
                enemy.armor = 0
        else:
            enemy.hp -= self.atk
        enemy.damaged = True
        enemy.check_hp()

    def shoot(self):
        if self.name == "fire_mag":
            if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                if not self.fire_form:
                    if self.attack_count < 2:
                        Bullet("fireball", self.rect.right - 10, self.rect.y + 45, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)
                        self.attack_count += 1
                        if self.upgrade_level == '3a':
                            self.fire_form_cooldown -= 1
                    else:
                        Bullet("fireball_big", self.rect.right - 10, self.rect.y + 45, self.damage_type, self.atk_big, self.bullet_speed_x, self.bullet_speed_y, 'default', self)
                        self.attack_count = 0
                        if self.upgrade_level == '3a':
                            self.fire_form_cooldown -= 1
                else:
                    Bullet("fireball_big", self.rect.right - 10, self.rect.y + 45, self.damage_type, self.atk_big, self.bullet_speed_x, self.bullet_speed_y, 'default', self)
                    self.fire_form_duration -= 1
            else:
                Bullet("fireball", self.rect.right - 10, self.rect.y + 45, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)

        if self.name == "boomchick":
            Bullet("yellow_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'boom', self)

        if self.name == "gribnik":
            Bullet("grib_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'spore', self)

        if self.name == "kopitel":
            for bullet in self.spawned_things:
                bullet.speed_x = 7
                bullet.add(bullets_group)
                self.nakopleno = 0
            self.spawned_things.clear()

        if self.name == "parasitelniy":
            self.parasix = randint(0, 32)
            self.parasiy = randint(-32, 32)
            Parasite('sosun', targets[id(self)].rect.centerx+self.parasix, targets[id(self)].rect.centery+self.parasiy, '', self.atk, targets[id(self)], self) # bug? no, juk.
            targets[id(self)].parasite_parents.add(self)
            targets[id(self)] = None

        if self.name == "nekr":
            if self.upgrade_level == "2a":
                if self.rect.y+128 <= 704:
                    Creep('nekr_skelet', (self.rect.x, self.rect.y + 128), self)
                if self.rect.y-128 >= 192:
                    Creep('nekr_skelet', (self.rect.x , self.rect.y - 128), self)
                for i in range(3):
                    Creep('nekr_skelet', (self.rect.x + (45*i), self.rect.y), self)
            elif self.upgrade_level == "3a":
                if self.rect.y+128 <= 704:
                    Creep('nekr_skelet_strelok', (self.rect.x, self.rect.y + 128), self)
                if self.rect.y-128 >= 192:
                    Creep('nekr_skelet_strelok', (self.rect.x, self.rect.y - 128), self)
                for i in range(5):
                    Creep('nekr_skelet', (self.rect.x + (25*i), self.rect.y), self)
            elif self.upgrade_level == "2b":
                for i in range(3):
                    Creep('nekr_zombie', (self.rect.x + (45*i), self.rect.y), self)
            elif self.upgrade_level == "3b":
                Creep('nekr_zombie_jirny', (self.rect.x + 90, self.rect.y), self)
                for i in range(2):
                    Creep('nekr_zombie', (self.rect.x + (45*i), self.rect.y), self)
            else:
                for i in range(3):
                    Creep('nekr_skelet', (self.rect.x + (45*i), self.rect.y), self)

        if self.name == "thunder":
            if self.target_phase == 'side':
                Bullet("mini_kamen", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk, self.bullet_speed_x, 0, 'hrom', self)
                if self.rect.centery+138 <= 832:
                    Bullet("mini_kamen", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'hrom', self)
                if self.rect.centery-138 >= 192:
                    Bullet("mini_kamen", self.rect.centerx - 8, self.rect.centery - 8,  self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y * -1, 'hrom', self)
            elif self.target_phase == 'center':  # я мог бы просто написать else, но пусть лучше так
                Bullet("big_kamen", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk*3, self.bullet_speed_x, 0, 'hrom', self)

        if self.name == "electric":
            if self.target_phase == 'close':
                Bullet("electric_kulak", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk2, 0, 0, 'drachun_gulag', self)
            elif self.target_phase == 'far':  # я мог бы просто написать else, но пусть лучше так
                self.bursting = True

        if self.name == "struyniy":
            self.bursting = True
            self.attack_cooldown = self.basic_attack_cooldown

        if self.name == "urag_anus":
            if targets[id(self)].rect.centerx+128 < 1500:
                self.uragan = Parasite('uragan', targets[id(self)].rect.centerx+128, self.rect.centery, '', self.atk, self, self)
            else:
                self.uragan = Parasite('uragan', 1472, self.rect.centery, '', self.atk, self, self)

        if self.name == "zeus":
            Bullet("Laser", self.rect.centerx + 640, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, 0, 'ls', self)

        if self.name == 'electro_maga':
            Bullet('electro_maga_sfera', self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'es', self)

        if self.name == "yascerica":
            if self.blackik.sumon == "baza":
                self.blackik.sumon = "ready"
                targets[id(self)] = None

        if self.name == "gnome_cannon1" or self.name == "gnome_cannon2" or self.name == "gnome_cannon3":
            Bullet("red_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)

        if self.name == "pukish":
            Bullet("gas", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'gas', self)

        if self.name == 'spike':    # fix?
            for enemy in enemies_group:
                if enemy.rect.colliderect:
                    self.dealing_damage(enemy)
            targets[id(self)] = None

        if self.name == "big_mechman":
            Bullet("mech_vzux", self.rect.right, self.rect.centery, self.damage_type, self.atk, 0, 0, 'mech', self)

        if self.name == "drachun":
            Bullet("drachun_gulag", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag', self)

        if self.name == 'tolkan':
            self.za_towerom = False
            Bullet("tolkan_bux", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'tolkan_bux', self)
            for tower in towers_group:
                if tower.rect.y == self.rect.y and tower.rect.x > self.rect.x and tower.rect.x - self.rect.x <= 128 and tower.name != 'pukish' and tower != self:
                    self.za_towerom = True
            if self.za_towerom:
                self.push = self.ottalkivanie_ne_solo
            else:
                self.push = self.ottalkivanie_solo

        if self.name == "knight_on_horse":
            Bullet("big_pike", self.rect.centerx + 192, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag', self)

        if self.name == "knight":
            Bullet("pike", self.rect.centerx + 128, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag', self)

        if self.name == "gnome_flamethrower":
            self.fire = Bullet("fire", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, "fire", self)

        # for i in range(16):                           # пока оставил
        #     if self.name == 'go_bleen' + str(i+1):
        #         if self.attack_cooldown <= 0:
        #             self.attack_cooldown = self.basic_attack_cooldown
        #             for j in range(i+1):
        #                 Bullet("spear_ma", self.rect.centerx, self.rect.y+(j*8), self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)

    def burst_attack(self):
        if self.name == 'electric':
            if self.target_phase == 'far':
                if self.ammo > 0:
                    Bullet("electric_bullet", self.rect.centerx, self.rect.centery+randint(-16, 16), None, self.atk, self.bullet_speed_x, self.bullet_speed_y, "default", self)
                    self.ammo -= 1
                else:
                    self.ammo = self.basic_ammo
                    self.attack_cooldown = self.basic_attack_cooldown
                    self.bursting = False
        
        if self.name == 'struyniy':
            if self.ammo > 0:
                Bullet("struya", self.rect.centerx, self.rect.centery, None, self.atk, self.bullet_speed_x, self.bullet_speed_y, "struya", self)
                self.ammo -= 1
            else:
                self.ammo = self.basic_ammo
                self.bursting = False

    def additional_attack(self):
        if self.name == "pukish":
            for enemy in enemies_group:
                if enemy.rect.colliderect(self.rect):
                    enemy.hp -= self.atk2

        if self.name == "gnome_flamethrower":
            if hasattr(self, "fire"):
                for enemy in enemies_group:
                    if enemy.rect.colliderect(self.fire.rect):
                        enemy.hp -= self.atk2

    def spawn_something(self):
        if self.name == 'kopitel':
            bullet = None
            if self.nakopleno < self.max_nakopit:
                joska_schitayu_y = 16 * self.nakopleno + 16
                if self.upgrade_level == "2a" or self.upgrade_level == '3a':
                    if self.upgrade_level == "2a":
                        if self.nakopleno < self.max_nakopit-1:
                            spear_or_sword = choice(["light_spear", "light_spear", "light_sword", "light_sword", "light_big_sword"])  # так надо
                        else:
                            spear_or_sword = choice(["light_spear", "light_sword"])
                        if spear_or_sword == 'light_big_sword':
                            self.nakopleno += 2
                            bullet = Bullet(spear_or_sword, self.rect.centerx-28, self.rect.y+joska_schitayu_y, self.damage_type, self.atk_big, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                        else:
                            self.nakopleno += 1
                            bullet = Bullet(spear_or_sword, self.rect.centerx-28, self.rect.y+joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                    else:
                        spear_or_sword = choice(["light_spear", "light_sword", "light_big_sword"])
                        self.nakopleno += 1
                        if spear_or_sword == 'light_big_sword':
                            bullet = Bullet(spear_or_sword, self.rect.centerx-28, self.rect.y+joska_schitayu_y, self.damage_type, self.atk_big, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                        else:
                            bullet = Bullet(spear_or_sword, self.rect.centerx-28, self.rect.y+joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                elif self.upgrade_level == "2b" or self.upgrade_level == '3b':
                    if self.nakopleno == 0:
                        for i in range(3): # тут менять сколько пуль будет сначала спавниться
                            joska_schitayu_y = 16 * self.nakopleno + 16
                            spear_or_sword = choice(["light_spear", "light_sword"])
                            self.nakopleno += 1
                            bullet = Bullet(spear_or_sword, self.rect.centerx-28, self.rect.y+joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                            if i < 2:
                                bullet.remove(bullets_group)
                                self.spawned_things.append(bullet)
                    else:
                        spear_or_sword = choice(["light_spear", "light_sword"])
                        self.nakopleno += 1
                        bullet = Bullet(spear_or_sword, self.rect.centerx-28, self.rect.y+joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                else:
                    spear_or_sword = choice(["light_spear", "light_sword"])
                    self.nakopleno += 1
                    bullet = Bullet(spear_or_sword, self.rect.centerx-28, self.rect.y+joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                bullet.remove(bullets_group)
                self.spawned_things.append(bullet)

        if self.name == 'barrier_mag':
            if self.best_x.barrier:
                self.best_x.barrier.owner.have_barrier = False
                self.best_x.barrier.kill()
            if self.best_x.barrier not in all_sprites_group:
                self.best_x = self
                self.best_x = sorted(towers_group, key=self.sort_by_x)[-1]
                self.best_x.have_barrier = True
                self.best_x.barrier = Parasite('barrier', self.best_x.rect.centerx, self.best_x.rect.centery, '', 0, self.best_x, self)

        if self.name == 'davalka':
            level.money += self.skolko_deneg_dast
            Alert("+10", (self.rect.centerx-15, self.rect.centery-55), 50, font30, (0, 70, 200))

    def sort_by_x(self, t):
        if t.rect.y == self.rect.y and t.have_barrier is False:
            return t.rect.x
        return 0

    def stop_hiding(self):
        self.hiding = True

    def animation(self):
        if 0 <= self.anim_count < self.anim_duration\
                or self.anim_duration <= self.anim_count < 2 * self.anim_duration\
                or self.anim_duration * 2 <= self.anim_count < 3 * self.anim_duration\
                or self.anim_duration * 3 <= self.anim_count < 4 * self.anim_duration:      # переделать
            if self.state == "wait":
                self.image = towers_wait[self.name][int(self.anim_count//self.anim_duration)]
            if self.state == "attack":
                if self.name in towers_attack:      # чтобы не ломались юниты без анимации атаки
                    self.image = towers_attack[self.name][int(self.anim_count//self.anim_duration)]
            if self.state == "give":
                self.image = towers_give[self.name][int(self.anim_count//self.anim_duration)]
            if self.state == "hide":
                self.image = towers_hide[self.name][int(self.anim_count//self.anim_duration)]
            if self.state == "death":
                ...

        if self.anim_count >= 4 * self.anim_duration:   # 4 -- так как в анимации 4 кадра
            self.anim_count = 0
        else:
            self.anim_count += self.time_indicator

    def move(self, change_pos):
        self.pos = self.pos[0], self.pos[1] + change_pos
        self.rect = self.image.get_rect(topleft=self.pos)

    def cooldown(self):                           # есть баг с перезарядкой, но там много всего должно сойтись и я пока забью
        if hasattr(self, "attack_cooldown"):      # там буквально 3 тика раз в 100 тиков голимые
            if self.attack_cooldown > 0:          # на определённой башне    !!!=
                self.attack_cooldown -= 1         # если я вам не скажу, вы и не заметите    ЗАМЕТИМ(наверн)
            else:
                self.check_target_alive()         # когда башня перезарядилась -> чекаем врага

        if self.anim_tasks:                          # порядок анимации
            if self.anim_tasks[0][1] > 0:            # -> self.anim_sequence = [("attack", 60, shoot), ("give", 50, spawn_something), ...]
                self.state = self.anim_tasks[0][0]   # -> какая анимация, время анимации, функция после анимации
                self.anim_tasks[0][1] -= 1
            elif self.anim_tasks[0][1] == 0:
                self.anim_tasks[0][2]()
                self.anim_tasks[0][1] -= 1
            else:
                self.anim_tasks.pop(0)
                self.anim_count = 0
        else:
            self.state = "wait"

        if hasattr(self, "attack_cooldown2"):
            if self.is_additional_attack_allow():
                if self.attack_cooldown2 > 0:
                    self.attack_cooldown2 -= 1
                else:
                    self.attack_cooldown2 = self.basic_attack_cooldown2
                    self.additional_attack()

        if hasattr(self, "spawn_something_cooldown"):
            if self.spawn_something_cooldown >= 0:
                self.spawn_something_cooldown -= 1
            else:
                if self.name == 'kopitel':
                    if self.nakopleno < self.max_nakopit:
                        self.spawn_something_cooldown = self.basic_spawn_something_cooldown
                        self.add_anim_task("give", self.spawn_something)
                else:
                    self.spawn_something_cooldown = self.basic_spawn_something_cooldown
                    self.add_anim_task("give", self.spawn_something)

        if hasattr(self, "healing_cooldown"):
            if self.healing_cooldown >= 0:
                self.healing_cooldown -= 1
            else:
                self.healing_cooldown = self.basic_healing_cooldown
                if self.hp <= (self.max_hp - self.heal):
                    self.hp += self.heal

        if self.name == 'fire_mag' and self.upgrade_level == '3a':  # надо чтобы миша сюда ещё и анимацию привязал, а то мне страшно туда лезть
            if not self.fire_form:
                if self.fire_form_cooldown <= 0:
                    self.fire_form_duration = self.basic_fire_form_duration
                    self.fire_form = True
                    self.time_indicator *= 2
                    self.basic_attack_cooldown //= 2
            else:
                if self.fire_form_duration <= 0:
                    self.fire_form_cooldown = self.basic_fire_form_cooldown
                    self.fire_form = False
                    self.time_indicator //= 2
                    self.basic_attack_cooldown *= 2

    def draw2(self, surf):
        surf.blit(self.image2, self.rect2)

    def update(self):
        self.cooldown()
        self.animation()
        self.image2 = font30.render(str(self.hp), True, (0, 0, 0))
        self.rect2 = self.image.get_rect(topleft=(self.rect.x + 32, self.rect.y - 32))

        if self.hp <= 0:
            self.dead()
            self.hp = 0

        if hasattr(self, "bursting"):
            if self.bursting:   # == True
                if self.attack_cooldown_burst > 0:
                    self.attack_cooldown_burst -= 1
                else:
                    self.attack_cooldown_burst = self.basic_attack_cooldown_burst
                    self.burst_attack()

        if hasattr(self, "horse_hp"):
            if self.horse_hp <= 0:
                hp = self.knight_hp + 500
                knight = Tower("knight", self.pos)
                knight.hp = hp
                self.kill()

        if hasattr(self, "knight_hp"):
            if self.knight_hp <= 0:
                Bullet("horse", self.rect.centerx, self.rect.centery, self.damage_type, self.taran_atk, 7, 0, 'gas', self)
                self.kill()

        if self.name == "pukish":
            if targets[id(self)]:                                                               # если есть цель
                if targets[id(self)].rect.colliderect(self.rect) and targets[id(self)].alive:   # если колизится с ней
                    self.prime_anim("hide", self.stop_hiding)                                   # запускаем важную анимацию
                elif self.hiding:                                                               # если уже прятался
                    targets[id(self)] = None                                                    # цель прошла дальше -- значит уже не цель
                    self.hiding = False                                                         # уже не прячится


class Enemy(sprite.Sprite):
    def __init__(self, name, pos):
        super().__init__(all_sprites_group, enemies_group)
        self.image = image.load(f"images/enemies/{name}.png").convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)
        self.rect2 = self.image.get_rect(topleft=(self.rect.x + 32, self.rect.y - 32))
        self.real_x = float(self.rect.x)
        self.real_y = float(self.rect.y)
        self.render_layer = 5
        self.name = name
        self.stop = False
        self.alive = True
        self.target = None
        self.parasite_parents = set()
        self.only_one_hit_bullets = set()

        self.pushed = False
        self.damaged = False
        self.gribs = 0

        # СТАТЫ начало

        if self.name == 'popusk':
            self.hp = 200
            self.atk = 100
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.attack_range = 0

        if self.name == 'josky':
            self.hp = 400
            self.atk = 80
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0

        if self.name == 'sigma':
            self.hp = 800
            self.atk = 200
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.attack_range = 0

        if self.name == 'armorik':
            self.hp = 300
            self.armor = 300
            self.have_armor = True
            self.atk = 100
            self.atk2 = 135
            self.speed = 0.5
            self.speed2 = 1
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.attack_cooldown2 = self.basic_attack_cooldown2 = 60
            self.attack_range = 0

        if self.name == 'slabiy':
            self.hp = 100
            self.atk = 50
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.attack_range = 0
            self.back_to_line()

        if self.name == 'rojatel':
            self.hp = 500
            self.atk = 50
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.attack_range = 0

        if self.name == 'sportik':  # надо пофиксить таргеты у пукиша
            self.hp = 200
            self.atk = 115
            self.speed = 1
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0

        if self.name == 'klonik':
            self.hp = 200
            self.atk = 100
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.klonirovanie_cooldown = self.basic_klonirovanie_cooldown = 1125
            self.attack_range = 0

        if self.name == 'teleportik':
            self.hp = 200
            self.atk = 100
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.tp_cooldown = self.basic_tp_cooldown = 75
            self.attack_range = 0

        if self.name == "zeleniy_strelok":
            self.hp = 200
            self.atk = 75
            self.bullet_speed_x = -5
            self.bullet_speed_y = 0
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.attack_range = 700

        if self.name == "telezhnik":
            self.hp = 370
            self.armor = 30
            self.have_armor = True
            self.atk = 70
            self.atk2 = 100
            self.bullet_speed_x = -5
            self.bullet_speed_y = 0
            self.speed = 0.5
            self.speed2 = 1
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.attack_range = 768
            self.attack_range2 = 0

        if self.name == "drobik":
            self.hp = 450
            self.atk = 50
            self.bullet_speed_x = -5
            self.bullet_speed_y = 4
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 100
            self.attack_range = 128

        if self.name == 'mega_strelok':
            self.hp = 600
            self.atk = 100
            self.bullet_speed_x = -5
            self.bullet_speed_y = 0
            self.speed = 0.25
            self.attack_cooldown = self.basic_attack_cooldown = 5
            self.attack_cooldown2 = self.basic_attack_cooldown2 = 750
            self.ammo = self.basic_ammo = 30
            self.attack_range = 640

        # СТАТЫ конец
        self.image2 = font30.render(str(self.hp), True, (0, 0, 0))

    def is_should_stop_to_attack(self):
        for tower in towers_group:
            if -64 < tower.rect.centery - self.rect.centery < 64 and -64 < self.rect.centerx - tower.rect.centerx < self.attack_range + 64 and self.rect.x < 1472:
                return True, tower
        for creep in creeps_group:
            if -64 < creep.rect.centery - self.rect.centery < 64 and -64 < self.rect.centerx - creep.rect.centerx < self.attack_range + 64 and self.rect.x < 1472:
                return True, creep
        return False, None

    def preparing_to_attack(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.attack_cooldown = self.basic_attack_cooldown
            if self.stop:
                if self.attack_range == 0:
                    self.melee_attack()
                if self.attack_range > 0:
                    self.shoot()

    def shoot(self):
        if self.name == "zeleniy_strelok" or self.name == 'telezhnik':
            Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery, None, self.atk, self.bullet_speed_x, self.bullet_speed_y, "zeleniy_strelok_bullet", self)

        if self.name == 'mega_strelok':
            if self.ammo > 0:
                Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery+randint(-16, 16), None, self.atk, self.bullet_speed_x, self.bullet_speed_y, "zeleniy_strelok_bullet", self)
                self.ammo -= 1
            else:
                self.ammo = self.basic_ammo
                self.attack_cooldown2 = self.basic_attack_cooldown2

        if self.name == 'drobik':
            Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery, None, self.atk, self.bullet_speed_x, 0, "anti_hrom", self)
            if self.rect.centery-138 >= 192:
                Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery, None, self.atk, self.bullet_speed_x, self.bullet_speed_y*-1, "anti_hrom", self)
            if self.rect.centery+138 <= 832:
                Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery, None, self.atk, self.bullet_speed_x, self.bullet_speed_y, "anti_hrom", self)

    def melee_attack(self):
        if self.target:
            if self.target.have_barrier:                     # проверка барьера
                self.target.barrier.hp -= self.atk
            elif self.target.name == 'knight_on_horse':      # проверка на коня
                self.target.horse_hp -= self.atk
            else:
                self.target.hp -= self.atk
                self.target.check_hp()

    def movement(self):
        if not self.stop:
            self.real_x -= self.speed
        self.rect.x = int(self.real_x)
        self.rect.y = int(self.real_y)

    def back_to_line(self):
        if (self.rect.y-192) % 128 < 64:
            # self.rect.y -= (self.rect.y-192) % 128
            self.real_y -= (self.rect.y-192) % 128
        else:
            # self.rect.y += 128 - ((self.rect.y-192) % 128)
            self.real_y += 128 - ((self.rect.y-192) % 128)
        if self.rect.y > 704:
            self.real_y -= 128
        elif self.rect.y < 192:
            self.real_y += 128

    def animation(self):
        pass    # не убирать, а то сломается справочник

    def armor_check(self):
        if hasattr(self, "armor") and self.have_armor:
            if self.armor <= 0:
                if self.name == 'armorik':
                    self.atk = self.atk2
                    self.basic_attack_cooldown = self.basic_attack_cooldown2
                    self.speed = self.speed2
                    self.have_armor = False
                    self.image = image.load(f"images/enemies/{self.name}_zloy.png").convert_alpha()

                elif self.name == 'telezhnik':
                    self.atk = self.atk2
                    self.speed = self.speed2
                    self.have_armor = False
                    self.attack_range = self.attack_range2
                    self.image = image.load(f"images/enemies/{self.name}_zloy.png").convert_alpha()

    def move(self, change_pos):
        self.pos = self.pos[0], self.pos[1] + change_pos
        self.rect = self.image.get_rect(topleft=self.pos)

    def additional_cooldowns(self):
        if self.name == 'klonik':
            if self.klonirovanie_cooldown > 0:
                self.klonirovanie_cooldown -= 1
            else:
                self.klonirovanie_cooldown = self.basic_klonirovanie_cooldown
                self.klon = Enemy('klonik', (self.rect.x+randint(64, 192), self.rect.y))
                self.klon.hp = self.hp

        if self.name == 'teleportik':
            if self.tp_cooldown > 0:
                self.tp_cooldown -= 1

    def dead(self):
        if self.name == 'rojatel':
            self.slabiy1 = Enemy('slabiy', (self.rect.x, self.rect.y+128))
            self.slabiy2 = Enemy('slabiy', (self.rect.x, self.rect.y-128))

        if 0 < self.gribs <= 3:
            self.grib = Tower('grib'+str(self.gribs), ((384 + ((self.rect.centerx+1 - 384) // 128) * 128), (192 + ((self.rect.y - 192) // 128) * 128)))
            self.gribs = 0
            if not (1536 > self.grib.pos[0] >= 384 and 832 > self.grib.pos[1] >= 192) or not is_free(self.grib):
                self.grib.kill()

        for parasite in parasites_group:
            if parasite.owner == self and parasite.name == 'ogonek_parasite' and parasite.parent.upgrade_level == '3b':
                Buff('fire_luja', (384 + ((self.rect.centerx+1 - 384) // 128) * 128), (192 + ((self.rect.y - 192) // 128) * 128), self)
                break

        self.alive = False
        self.kill()

    def check_hp(self):
        if self.hp <= 0:
            self.dead()
        
        if self.name == 'teleportik' and self.damaged:
            if self.tp_cooldown <= 0:
                self.tp_cooldown = self.basic_tp_cooldown
                self.y_direction = choice([-1, 1])
                if self.rect.y <= 202:  # 192 + 10
                    self.real_y = self.rect.y + 128
                elif self.rect.y >= 694:  # 704 - 10
                    self.real_y = self.rect.y - 128
                else:
                    self.real_y = self.rect.y + (128*self.y_direction)
                self.movement()
                self.back_to_line()


        self.damaged = False

    def draw2(self, surf):
        surf.blit(self.image2, self.rect2)

    def update(self):
        self.stop, self.target = self.is_should_stop_to_attack()

        if self.name == 'mega_strelok':
            if self.attack_cooldown2 > 0:
                self.attack_cooldown2 -= 1
            else:
                self.preparing_to_attack()
        else:
            self.preparing_to_attack()
        self.armor_check()
        self.additional_cooldowns()
        self.check_hp()
        self.movement()
        self.image2 = font30.render(str(self.hp), True, (0, 0, 0))
        self.rect2 = self.image.get_rect(topleft=(self.rect.x + 32, self.rect.y - 32))


class Creep(sprite.Sprite):
    def __init__(self, name, pos, parent):
        super().__init__(all_sprites_group, creeps_group)
        self.image = image.load(f"images/creeps/{name}.png").convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)
        self.real_x = float(self.rect.x)
        self.real_y = float(self.rect.y)
        self.render_layer = 5
        self.name = name
        self.parent = parent
        self.stop = False
        self.alive = True
        self.have_barrier = False
        self.barrier = None
        self.target = None

        if self.name == 'nekr_skelet':
            self.hp = 100
            self.atk = 30
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            if self.parent.upgrade_level == '2a':
                self.speed = 1
            if self.parent.upgrade_level == '3a':
                self.speed = 1.5

        if self.name == 'nekr_zombie':
            self.hp = 200
            self.atk = 40
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0

        if self.name == 'nekr_zombie_jirny':
            self.hp = 500
            self.atk = 100
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.attack_range = 0

        if self.name == 'nekr_skelet_strelok':
            self.hp = 100
            self.atk = 50
            self.speed = 0.5
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.attack_range = 256
            if self.parent.upgrade_level == '2a':
                self.speed = 1
            if self.parent.upgrade_level == '3a':
                self.speed = 1.5

    def is_should_stop_to_attack(self):
        for enemy in enemies_group:
            if -64 < enemy.rect.centery - self.rect.centery < 64 and -64 < enemy.rect.centerx - self.rect.centerx < self.attack_range + 64 and self.rect.centerx > 384:
                return True, enemy
        return False, None
    
    def preparing_to_attack(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.attack_cooldown = self.basic_attack_cooldown
            if self.stop:
                if self.attack_range == 0:
                    self.melee_attack()
                if self.attack_range > 0:
                    self.shoot()

    def melee_attack(self):
        if self.target:
            self.dealing_damage(self.target)

    def shoot(self):
        if self.name == 'nekr_skelet_strelok':
            Bullet('bone_arrow', self.rect.centerx, self.rect.centery, None, self.atk, self.bullet_speed_x, self.bullet_speed_y, "default", self)

    def dealing_damage(self, enemy):
        if hasattr(enemy, 'armor') and enemy.armor > 0:
            if self.atk <= enemy.armor:
                enemy.armor -= self.atk
            else:
                enemy.hp -= (self.atk - enemy.armor)
                enemy.armor = 0
        else:
            enemy.hp -= self.atk
        enemy.damaged = True
        enemy.check_hp()

    def movement(self):
        if not self.stop:
            self.real_x += self.speed
        self.rect.x = int(self.real_x)
        self.rect.y = int(self.real_y)

    def check_hp(self):
        if self.hp <= 0 or self.parent not in all_sprites_group or self.rect.x > 1700:
            self.alive = False
            self.kill()

    def update(self):
        self.stop, self.target = self.is_should_stop_to_attack()

        self.preparing_to_attack()
        self.movement()
        self.check_hp()


class Bullet(sprite.Sprite):
    def __init__(self, bullet_sprite, x, y, damage_type, damage, speed_x, speed_y, name, parent):
        super().__init__(all_sprites_group, bullets_group)
        self.image = image.load(f"images/bullets/{bullet_sprite}.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.render_layer = 7
        self.bullet_sprite = bullet_sprite  # так надо
        self.damage_type = damage_type
        self.damage = damage
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.name = name
        self.parent = parent
        self.penned = False

        if self.name == 'ls':
            self.off = 30
        if self.name == 'explosion' or self.name == "mech":
            self.off = 20
        if self.name == 'razlet':
            self.pushl = 128
            self.off = 20
        if self.name == "drachun_gulag" or self.name == "tolkan_bux":
            self.off = 15
        if self.name == "fire":
            self.off = 61

        if self.name == 'yas':
            self.sumon = 'baza'     # ready
            self.parent.attack_cooldownwn = 375
            self.default_pos = (self.rect.x, self.rect.y)
            if self.parent.upgrade_level == '2b' or self.parent.upgrade_level == '3b':
                self.stomach_capacity = self.basic_stomach_capacity = self.parent.bullet_stomach_capacity
            if self.parent.upgrade_level == '3a':
                self.damage = 25
        if self.name == 'gas':
            self.gazirovannie_group = sprite.Group()
            self.enemies_in_group = 0

        if (self.bullet_sprite == 'light_sword' or self.bullet_sprite == 'light_spear') and self.parent.upgrade_level == '3b':
            if self.bullet_sprite == 'light_sword':
                self.damage *= 2
            else:
                self.probitie_group = sprite.Group()
                self.enemies_in_group = 0

    def bullet_movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.name == 'hrom' or self.name == 'anti_hrom':
            if (self.parent.rect.centery - self.rect.centery) >= 128 or (self.rect.centery - self.parent.rect.centery) >= 128:
                self.speed_y = 0

        if self.name == 'yas':
            if self.sumon == 'ready':
                if self.parent.upgrade_level == '2a' or self.parent.upgrade_level == '3a':
                    if self.parent.upgrade_level == '2a':
                        self.speed_x = 4
                    else:
                        self.speed_x = 6
                        self.damage = 25
                    self.sumon = 'go'
                    self.add(bullets_group)
                else:
                    self.speed_x = 2
                    self.sumon = 'go'
                    self.add(bullets_group)

            elif self.rect.centerx >= 1520 and self.sumon == 'go':
                self.speed_x *= -1
                self.sumon = 'back'
                if self.parent.upgrade_level == '3a':
                    for enemy in enemies_group:
                        if self in enemy.only_one_hit_bullets:
                            enemy.only_one_hit_bullets.remove(self)

            elif self.rect.centerx <= self.parent.rect.centerx - 26 and self.sumon == 'back':
                self.speed_x = 0
                self.rect.centerx = self.parent.rect.centerx - 26
                self.sumon = 'baza'
                self.penned = False
                if self in bullets_group:  # наверное это надо, если не надо то круто, но проверять мне лень(это для корректной работы веток 2а и 3а если по пути нет врагов)
                    self.remove(bullets_group)

        if self.rect.x >= 1700 or self.rect.x <= -128:
            self.kill()

    def dealing_damage(self, enemy):
        if hasattr(enemy, 'armor') and enemy.armor > 0:
            if self.damage <= enemy.armor:
                enemy.armor -= self.damage
            else:
                enemy.hp -= (self.damage - enemy.armor)
                enemy.armor = 0
        else:
            enemy.hp -= self.damage
        enemy.damaged = True
        enemy.check_hp()

    def check_collision(self):
        if self.name != "zeleniy_strelok_bullet" and self.name != 'anti_hrom' and self.name != 'explosion' and self.name != 'razlet' and not self.penned:
            for tower in towers_group:
                if tower.name == 'pen' and self.rect.colliderect(tower.rect):
                    self.speed_x *= 1.5
                    self.damage *= 1.5
                    self.penned = True

        if self.name == "zeleniy_strelok_bullet" or self.name == 'anti_hrom':
            for tower in towers_group:
                if tower.name != "pukish":
                    if self.rect.colliderect(tower.rect):
                        if tower.barrier:
                            tower.barrier.hp -= self.damage
                            self.kill()
                        elif tower.name == "knight_on_horse":
                            tower.knight_hp -= self.damage
                            self.kill()
                        else:
                            tower.hp -= self.damage
                            tower.check_hp()
                            self.kill()
            for creep in creeps_group:
                if self.rect.colliderect(creep.rect):
                    if creep.barrier:
                        creep.barrier.hp -= self.damage
                        self.kill()
                    else:
                        creep.hp -= self.damage
                        creep.check_hp()
                        self.kill()


        if self.name == "yas":
            if self.sumon != "baza":
                for enemy in enemies_group:
                    if enemy.rect.colliderect(self.rect):
                        if self.sumon == 'go':
                            if self.parent.upgrade_level == '2b' or self.parent.upgrade_level == '3b':
                                self.stomach_capacity -= 1
                                enemy.hp -= enemy.hp
                                if self.stomach_capacity <= 0:
                                    self.speed_x *= -1
                                    self.sumon = 'back'
                                    self.remove(bullets_group)
                                    break
                            elif self.parent.upgrade_level == '3a' and self not in enemy.only_one_hit_bullets:
                                self.dealing_damage(enemy)
                                enemy.only_one_hit_bullets.add(self)
                            elif self.parent.upgrade_level == '1':
                                self.speed_x *= -1
                                self.sumon = 'back'
                                enemy.hp -= enemy.hp
                                self.remove(bullets_group)
                                self.parent.attack_cooldown = self.parent.basic_attack_cooldown
                                break
                        elif self.sumon == 'back' and (self.parent.upgrade_level == '2a' or self.parent.upgrade_level == '3a'):
                            if self.parent.upgrade_level == '3a' and self not in enemy.only_one_hit_bullets:
                                self.dealing_damage(enemy)
                                enemy.only_one_hit_bullets.add(self)
                            if self in bullets_group:
                                enemy.hp -= enemy.hp
                                self.remove(bullets_group)
                                break
                if self.sumon == 'back' and (self.parent.upgrade_level == '2b' or self.parent.upgrade_level == '3b') and self.stomach_capacity != self.basic_stomach_capacity:
                    self.parent.attack_cooldown = (self.parent.basic_attack_cooldown // self.basic_stomach_capacity) * (self.basic_stomach_capacity - self.stomach_capacity)
                    self.stomach_capacity = self.basic_stomach_capacity

        if self.name == 'gas': 
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, self) and enemy.hp > 0:
                    if enemy not in self.gazirovannie_group:
                        self.dealing_damage(enemy)
                        enemy.add(self.gazirovannie_group)
                        self.enemies_in_group += 1
                        if self.enemies_in_group >= 5:
                            self.kill()
                            break

        if self.name == 'ls' or self.name == 'explosion' or self.name == "mech" or self.name == "drachun_gulag" or self.name == "tolkan_bux" or self.name == 'razlet':
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, self) and enemy.hp > 0 and self not in enemy.only_one_hit_bullets:
                    self.dealing_damage(enemy)
                    if self.name == "tolkan_bux":
                        enemy.real_x += self.parent.push
                    if self.name == 'razlet':
                        if (enemy.rect.x >= self.rect.x and enemy.rect.centery == self.rect.centery) or enemy.rect.centery == 768 or enemy.rect.centery == 256:  #  тут же
                            enemy.real_x += self.pushl
                        elif enemy.rect.centery > self.rect.centery and enemy.rect.centery != 768:  # ниже
                            enemy.real_y += self.pushl
                        elif enemy.rect.centery < self.rect.centery and enemy.rect.centery != 256:  # выше
                            enemy.real_y -= self.pushl
                    enemy.only_one_hit_bullets.add(self)
            if self.name == "mech" or self.name == "drachun_gulag" or self.name == "tolkan_bux":
                targets[id(self.parent)] = None

        # if self.name == "mech" or self.name == "drachun_gulag":
        #     for enemy in enemies_group:
        #         if enemy.rect.colliderect(self.rect):
        #             enemy.hp -= self.parent.atk
        #             enemy.only_one_hit_bullets.add(self)
        #     targets[id(self.parent)] = None

        # if self.name == "tolkan_bux":
        #     for enemy in enemies_group:
        #         if enemy.rect.colliderect(self.rect):
        #             enemy.hp -= self.parent.atk
        #             #enemy.rect.x += self.parent.push
        #             enemy.real_x += self.parent.push
        #     targets[id(self.parent)] = None

        for enemy in enemies_group:
            if enemy.rect.collidepoint(self.rect.right, self.rect.centery):
                if self.name == 'kopilka':
                    if hasattr(self, 'probitie_group'):
                        if not enemy in self.probitie_group:
                            self.dealing_damage(enemy)
                            enemy.add(self.probitie_group)
                            self.enemies_in_group += 1
                            if self.enemies_in_group >= 2:  # через len() нельзя тк там кое какие неприятные нюансы
                                self.kill()
                                break
                    else:
                        self.dealing_damage(enemy)
                        self.kill()
                        break
        for enemy in enemies_group:
            if sprite.collide_rect(enemy, self) and enemy.hp > 0:
                if self.name == 'default' or self.name == 'hrom' or self.name == 'boom' or self.name == 'struya' or self.name == 'spore' or self.name == 'es':
                    self.dealing_damage(enemy)
                    if self.name == 'boom':
                        Bullet("explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.damage, 0, 0, 'explosion', self.parent)
                    elif self.name == 'struya':
                        enemy.real_x += 32
                    elif self.name == 'spore':
                        self.parent.parasix = randint(-32, 32)
                        self.parent.parasiy = randint(-48, 48)
                        Parasite('grib_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                    elif self.name == 'es':
                        Bullet('electro_maga_explosion', self.rect.centerx, self.rect.centery, self.damage_type, 0, 0, 0, 'razlet', self.parent)
                    if self.bullet_sprite == 'fireball' and (self.parent.upgrade_level == '2b' or self.parent.upgrade_level == '3b'):
                        self.parent.parasix = randint(-32, 32)
                        self.parent.parasiy = randint(-48, 48)
                        Parasite('ogonek_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', self.parent.atk_dot, enemy, self.parent)
                    self.kill()
                    
                break

    def check_parent(self):
        if self.name == 'kopilka':
            if self.parent not in all_sprites_group and self.speed_x == 0:
                self.kill()
        if self.name == 'yas':
            if self.parent not in all_sprites_group:
                self.kill()

    def cooldowns(self):
        # if self.name == 'yas' and self.sumon == 'wait':  # я хз что это и зачем поэтому решил закомментить
        #     if self.parent.attack_cooldown > 0:
        #         self.parent.attack_cooldown -= 1

        if self.name == 'ls' or self.name == 'explosion' or self.name == "mech" or self.name == "drachun_gulag" or self.name == "tolkan_bux" or self.name == "fire" or self.name == 'razlet':
            if self.off <= 0:
                self.kill()
            else:
                self.off -= 1

    def update(self):
        self.bullet_movement()
        self.cooldowns()
        self.check_collision()
        self.check_parent()


class Parasite(sprite.Sprite):
    def __init__(self, name, x, y, damage_type, damage, owner, parent):
        super().__init__(all_sprites_group, parasites_group)
        self.image = image.load(f"images/buffs/{name}.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.render_layer = 6
        self.is_dead = False
        self.damage_type = damage_type
        self.damage = damage
        self.name = name
        self.owner = owner  # это враг к которому привязан паразит
        self.parent = parent

        if self.name == 'sosun' or self.name == 'grib_parasite' or self.name == 'ogonek_parasite':
            self.parasix = self.parent.parasix
            self.parasiy = self.parent.parasiy
            if self.name == 'sosun' or self.name == 'ogonek_parasite':
                self.attack_cooldown = 75
            elif self.name == 'grib_parasite':
                self.owner.gribs += 1
                self.lifetime = 375
                for parasite in parasites_group:
                    if parasite != self and parasite.owner == self.owner and self.parent == parasite.parent:
                        parasite.kill()
                        self.owner.gribs -= 1
            if self.name == 'ogonek_parasite':
                self.lifetime = 375

        if self.name == 'barrier':
            self.hp = self.parent.barrier_hp
            # self.life_time = self.parent.basic_spawn_something_cooldown

        if self.name == 'uragan':
            self.duration = self.parent.uragan_duration
            self.attack_cooldown = 15
            self.render_layer = 3
            if self.parent.upgrade_level == '2a' or self.parent.upgrade_level == '3a':
                self.speed = self.parent.uragan_speed
                self.start_x = self.rect.centerx
                self.real_x = self.rect.x

        if self.name == 'raven':
            self.home_x = self.rect.centerx
            self.home_y = self.rect.centery
            self.speed = 5
            self.kluving_time = self.basic_kluving_time = 1125
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.rest_time = 0
            self.basic_rest_time = 375
            if self.parent not in all_sprites_group:
                self.lifetime = 375

        if self.name == 'mol':
            if self.owner != self.parent:
                self.dealing_damage(self.owner)
            self.lifetime = 75
    
    def dead(self):
        self.kill()
        if self.name == 'uragan':
            for enemy in enemies_group:
                enemy.back_to_line()
        if self.name == 'sosun':        
            self.parent.have_parasite.remove(self.owner)
        if self.name == 'barrier':
            self.owner.have_barrier = False
        if self.name == 'raven':
            if self.owner != self.parent and self.parent in self.owner.parasite_parents:
                self.owner.parasite_parents.remove(self.parent)

    def prisasivanie(self):  # если честно то это по сути delat_chtoto но для паразитов, когда-нибудь сделаем по-человечески
        if self.name != 'ogonek_parasite' and self.name != 'mol':
            if self.parent not in all_sprites_group:
                if self.name == 'raven' and (self.owner != self.parent or (hasattr(self, 'lifetime') and self.lifetime > 0)):
                    pass
                else:
                    self.dead()
        if self.name != 'mol':
            if self.owner not in all_sprites_group:
                if self.name == 'raven':
                    if self.parent not in all_sprites_group:
                        if hasattr(self, 'lifetime') and self.lifetime > 0 and self.owner == self.parent:
                            pass
                        else:
                            self.dead()
                    else:
                        self.owner = self.parent
                        self.rest_time = 9999
                else:
                    self.dead()

        if self.name == 'barrier' and self.hp <= 0:
            self.kill()
            self.owner.have_barrier = False

        if self.name == 'sosun' or self.name == 'grib_parasite' or self.name == 'ogonek_parasite':
            self.rect.centerx = self.owner.rect.centerx+self.parasix
            self.rect.centery = self.owner.rect.centery+self.parasiy
            if self.name == 'sosun' or self.name == 'ogonek_parasite':
                if self.attack_cooldown <= 0:
                    self.attack_cooldown = 75
                    self.dealing_damage(self.owner)
                    if self.name == 'sosun':
                        if self.parent.hp < self.parent.max_hp - self.damage:
                            self.parent.hp += self.damage
                        else:
                            self.parent.hp = self.parent.max_hp

        if self.name == 'grib_parasite':
            if self.owner.gribs > 3:
                self.kill()
                self.owner.gribs -= 1

        if self.name == 'uragan':
            for enemy in enemies_group:
                if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                    enemy.angle = atan2(self.rect.centery - enemy.rect.centery, self.rect.centerx - enemy.rect.centerx)
                    enemy.x_vel = cos(enemy.angle) * enemy.speed * 12
                    enemy.y_vel = sin(enemy.angle) * enemy.speed * 12
                    # enemy.rect.x += enemy.x_vel
                    # enemy.rect.y += enemy.y_vel
                    enemy.real_x += enemy.x_vel
                    enemy.real_y += enemy.y_vel

                    if self.attack_cooldown <= 0:
                        self.attack_cooldown = 15
                        self.dealing_damage(enemy)
            if self.parent.upgrade_level == '2a' or self.parent.upgrade_level == '3a':
                if self.rect.centerx - self.start_x < 256 and self.rect.centerx < 1472:
                    self.real_x += self.speed
                    self.rect.x = int(self.real_x)

        if self.name == 'raven':
            if self.rest_time > 0:
                self.rest_time -= 1
            else:
                if self.owner == self.parent:
                    for enemy in enemies_group:
                        if self.parent not in enemy.parasite_parents and enemy.alive and (self.parent in all_sprites_group or hasattr(self, 'lifetime')):
                            enemy.parasite_parents.add(self.parent)
                            self.owner = enemy
                            self.randix = randint(0, 48)
                            self.randiy = randint(0, 48)
                            break
            if self.owner == self.parent:
                if self.rect.centerx != self.home_x or self.rect.centery != self.home_y:
                    self.angle = atan2(self.home_y - self.rect.centery, self.home_x - self.rect.centerx)
                    self.x_vel = cos(self.angle) * self.speed
                    self.y_vel = sin(self.angle) * self.speed
                    self.rect.x += self.x_vel
                    self.rect.y += self.y_vel
                    if self.rect.collidepoint(self.home_x, self.home_y):
                        self.rect.centerx = self.home_x
                        self.rect.centery = self.home_y
                        self.rest_time = (self.basic_kluving_time-self.kluving_time)//3
                        self.kluving_time = self.basic_kluving_time
            else:
                if self.rect.centerx != self.owner.rect.x+self.randix or self.rect.centery != self.owner.rect.y+self.randiy:
                    self.angle = atan2(self.owner.rect.y+self.randiy - self.rect.centery, self.owner.rect.x+self.randix - self.rect.centerx)
                    self.x_vel = cos(self.angle) * self.speed
                    self.y_vel = sin(self.angle) * self.speed
                    self.rect.x += self.x_vel
                    self.rect.y += self.y_vel
                    if self.rect.collidepoint(self.owner.rect.x+self.randix, self.owner.rect.y+self.randiy):
                        self.rect.centerx = self.owner.rect.x+self.randix
                        self.rect.centery = self.owner.rect.y+self.randiy
                else:
                    self.rect.centerx = self.owner.rect.x+self.randix
                    self.rect.centery = self.owner.rect.y+self.randiy
                    if self.kluving_time > 0:
                        self.kluving_time -= 1
                        if self.attack_cooldown <= 0:
                            self.dealing_damage(self.owner)
                            self.attack_cooldown = self.basic_attack_cooldown
                    else:
                        if self.parent in self.owner.parasite_parents:
                            self.owner.parasite_parents.remove(self.parent)
                        if self.parent not in all_sprites_group:
                            self.dead()
                        else:
                            self.owner = self.parent
                            self.rest_time = 9999

    def dealing_damage(self, enemy):
        if hasattr(enemy, 'armor') and enemy.armor > 0:
            if self.damage <= enemy.armor:
                enemy.armor -= self.damage
            else:
                enemy.hp -= (self.damage - enemy.armor)
                enemy.armor = 0
        else:
            enemy.hp -= self.damage
        enemy.damaged = True
        enemy.check_hp()

    def update(self):
        self.prisasivanie()
        
        if self.name == 'sosun' or self.name == 'uragan' or self.name == 'ogonek_parasite' or self.name == 'raven':
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

        if self.name == 'uragan':
            if self.duration > 0:
                self.duration -= 1
            else:
                self.kill()
                for enemy in enemies_group:
                    enemy.back_to_line()

        if hasattr(self, 'lifetime'):
            if self.lifetime > 0:
                self.lifetime -= 1
            else:
                if self.name == 'raven' and self.owner != self.parent:
                    pass
                else:
                    self.dead()
                    if self.name == 'grib_parasite':
                        self.owner.gribs -= 1


class Buff(sprite.Sprite):
    def __init__(self, name, x, y, parent):
        super().__init__(all_sprites_group, buffs_group)
        self.image = image.load(f"images/buffs/{name}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.render_layer = 3
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.parent = parent
        if self.name == 'mat':
            self.rect2 = Rect(self.rect.x - 128, self.rect.y - 128, 384, 384)
        elif self.name == 'boloto':
            self.rect2 = Rect(self.rect.x - 512, self.rect.y, 640, 128)

        self.max_buff = None

        if self.name == 'mat' or self.name == 'vodkamat':
            self.gender = 'tower_buff'
            self.buffed_towers = sprite.Group()
        else:
            self.gender = 'field_debuff'

        if self.name == 'mat':
            self.mozhet_zhit = False
        else:
            self.mozhet_zhit = True

        if self.rect.x <= 384 or self.rect.x >= 1536 or self.rect.y < 192 or self.rect.y >= 832:  # по хорошему надо не >= 832, а > 704, но похуй
            self.kill()
        
        if self.name == 'vodkamat':
            self.lifetime = 750
        elif self.name == 'fire_luja':
            self.atk = 20
            self.attack_cooldown = self.basic_attack_cooldown = 75
            self.lifetime = 375

        if self.name == 'boloto':
            self.debuffed_enemies = sprite.Group()

        self.buff_collision()  # в апдейт не надо сувать
    
    def buff_collision(self):
        if self.name == 'mat' or self.name == 'vodkamat':
            for buff in buffs_group:
                if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff and (buff.name == 'mat' or buff.name == 'vodkamat'):
                    if self.name == 'vodkamat':
                        buff.mozhet_zhit = False
                        buff.check_tower()
                    else:
                        self.kill()

        elif self.name == 'boloto':
            for buff in buffs_group:
                if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff and self.name == buff.name:
                    for enemy in buff.debuffed_enemies:
                        enemy.speed *= 2
                    buff.kill()
        
        elif self.name == 'fire_luja':
            for buff in buffs_group:
                if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff and self.name == buff.name:
                    buff.lifetime += 375
                    self.kill()

    def delat_buff(self):
        for tower in towers_group:
            if tower not in self.buffed_towers:
                if self.rect.collidepoint(tower.rect.centerx, tower.rect.centery):
                    if tower.name == 'fire_mag' \
                            or tower.name == 'kopitel'\
                            or tower.name == 'thunder'\
                            or tower.name == 'yascerica'\
                            or tower.name == 'zeus'\
                            or tower.name == 'boomchick'\
                            or tower.name == 'parasitelniy'\
                            or tower.name == 'drachun'\
                            or tower.name == 'tolkan'\
                            or tower.name == 'big_mechman'\
                            or tower.name == 'knight_on_horse'\
                            or tower.name == "knight"\
                            or tower.name == "urag_anus"\
                            or tower.name == "gnome_cannon1"\
                            or tower.name == "gnome_cannon2"\
                            or tower.name == "gnome_cannon3"\
                            or tower.name == "electric"\
                            or tower.name == "gribnik"\
                            or tower.name == "nekr"\
                            or tower.name == "struyniy"\
                            or tower.name == 'electro_maga':

                        if tower.basic_attack_cooldown // 2 <= 225:
                            tower.basic_attack_cooldown //= 2
                            self.max_buff = False
                        else:
                            tower.basic_attack_cooldown -= 225
                            self.max_buff = True
                        tower.time_indicator *= 2
                        if tower.name == 'kopitel':
                            tower.basic_spawn_something_cooldown //= 2
                        tower.add(self.buffed_towers)

                    # for i in range(16):
                    #     if tower.name == 'go_bleen' + str(i+1):
                    #         tower.basic_attack_cooldown //= 2
                    #         tower.time_indicator *= 2
                    #         tower.add(self.buffed_towers)

        for nekusaemiy in nekusaemie_group:
            if nekusaemiy not in self.buffed_towers:
                if self.rect.collidepoint(nekusaemiy.rect.centerx, nekusaemiy.rect.centery):
                    if nekusaemiy.name == 'spike' or nekusaemiy.name == 'pukish':
                        if nekusaemiy.basic_attack_cooldown // 2 <= 225:
                            nekusaemiy.basic_attack_cooldown //= 2
                            self.max_buff = False
                        else:
                            nekusaemiy.basic_attack_cooldown -= 225
                            self.max_buff = True
                        nekusaemiy.time_indicator *= 2
                        nekusaemiy.add(self.buffed_towers)

    def delat_debuff(self):
        if self.name == 'boloto':
            for enemy in enemies_group:
                if enemy not in self.debuffed_enemies:
                    if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                        enemy.speed /= 2
                        enemy.add(self.debuffed_enemies)
                else:
                    if not self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                        enemy.speed *= 2
                        enemy.remove(self.debuffed_enemies)
            self.mozhet_zhit = False

    def check_life(self):
        if self.name == 'mat':
            for tower in towers_group:
                if tower.name == 'matricayshon':
                    if self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery):
                        self.mozhet_zhit = True
                
        if self.name == 'vodkamat' or self.name == 'fire_luja':
            if self.lifetime > 0:
                self.lifetime -= 1
            else:
                self.mozhet_zhit = False

        if self.name == 'boloto':
            for tower in towers_group:
                if tower.name == 'bolotnik':
                    if self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery):
                        self.mozhet_zhit = True
            if self.mozhet_zhit == False:
                if not hasattr(self, 'lifetime'):
                    self.lifetime = 225
                self.mozhet_zhit = True
            if hasattr(self, 'lifetime'):
                if self.lifetime > 0:
                    self.lifetime -= 1
                else:
                    self.mozhet_zhit = False
                    for enemy in self.debuffed_enemies:
                        enemy.speed *= 2

    def check_tower(self):
        if not self.mozhet_zhit:
            self.kill()
            for tower in self.buffed_towers:
                if tower.name == 'fire_mag'\
                        or tower.name == 'kopitel'\
                        or tower.name == 'thunder'\
                        or tower.name == 'yascerica'\
                        or tower.name == 'zeus'\
                        or tower.name == 'boomchick'\
                        or tower.name == 'parasitelniy'\
                        or tower.name == 'pukish'\
                        or tower.name == 'spike'\
                        or tower.name == 'drachun'\
                        or tower.name == 'tolkan'\
                        or tower.name == 'big_mechman'\
                        or tower.name == 'knight_on_horse'\
                        or tower.name == "knight"\
                        or tower.name == "urag_anus"\
                        or tower.name == "gnome_cannon1"\
                        or tower.name == "gnome_cannon2"\
                        or tower.name == "gnome_cannon3"\
                        or tower.name == "electric"\
                        or tower.name == "gribnik"\
                        or tower.name == "nekr"\
                        or tower.name == "struyniy"\
                        or tower.name == 'electro_maga':
                    if not self.max_buff:
                        tower.basic_attack_cooldown *= 2
                    else:
                        tower.basic_attack_cooldown += 225
                    tower.time_indicator //= 2
                    if tower.name == 'kopitel':
                        tower.basic_spawn_something_cooldown *= 2

                # for i in range(16):
                #     if tower.name == 'go_bleen' + str(i+1):
                #         tower.basic_attack_cooldown *= 2
                #         tower.time_indicator //= 2

                # if tower.name == 'urag_anus':
                #     tower.basic_uragan_cooldown *= 2
                #     tower.time_indicator //= 2

            # for nekusaemiy in self.buffed_towers:
            #     if nekusaemiy.name == 'spike' or nekusaemiy.name == 'pukish':
            #         nekusaemiy.basic_attack_cooldown *= 2
            #         nekusaemiy.time_indicator //= 2

            if self.name == 'vodkamat':
                Buff('mat', self.rect.x, self.rect.y, self)

        if self.name == 'mat':
            self.mozhet_zhit = False

    def attack(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.attack_cooldown = self.basic_attack_cooldown
            for enemy in enemies_group:
                if self.rect.colliderect(enemy.rect):
                    self.dealing_damage(enemy)

    def dealing_damage(self, enemy):
        if hasattr(enemy, 'armor') and enemy.armor > 0:
            if self.atk <= enemy.armor:
                enemy.armor -= self.atk
            else:
                enemy.hp -= (self.atk - enemy.armor)
                enemy.armor = 0
        else:
            enemy.hp -= self.atk
        enemy.damaged = True
        enemy.check_hp()

    def update(self):
        if self.gender == 'tower_buff':
            self.delat_buff()
            self.check_life()
            self.check_tower()
        else:
            self.delat_debuff()
            self.check_life()
            if hasattr(self, 'atk'):
                self.attack()
            if not self.mozhet_zhit:
                self.kill()

    def __repr__(self):
        return f"Я {self.name}"


class UI(sprite.Sprite):
    def __init__(self, pos, path, unit_inside, free_placement, kd_time=0):
        super().__init__(ui_group, all_sprites_group)
        self.image = image.load(f"images/{path}/images_inside/{unit_inside}_inside.png").convert_alpha()
        self.pos = pos
        self.default_pos = pos
        self.rect = self.image.get_rect(topleft=self.pos)
        self.image3 = image.load("images/other/nothing.png").convert_alpha()
        self.rect3 = self.image3.get_rect(topleft=self.default_pos)
        self.path = path
        self.unit_inside = unit_inside
        self.free_placement = free_placement
        self.is_move = False
        self.kd_time = 0
        self.default_kd_time = kd_time
        self.loaded_p = False
        self.render_layer = 3

        if self.path == "towers":
            self.cost = tower_costs[unit_inside]
            self.image2 = font30.render(str(self.cost), True, (255, 255, 255))
            self.rect2 = self.image2.get_rect(topleft=(self.default_pos[0] - 49, self.default_pos[1] + 4))

    def move(self):
        self.pos = mouse.get_pos()
        self.rect = self.image.get_rect(center=self.pos)
        self.render_layer = 9

    def back_to_default(self):
        self.image = image.load(f"images/{self.path}/images_inside/{self.unit_inside}_inside.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.default_pos)
        self.pos = self.default_pos
        self.render_layer = 3

    def draw2(self, surf):
        surf.blit(self.image2, self.rect2)

    def draw3(self, surf):
        surf.blit(self.image3, self.rect3)

    def update(self):
        if level.cheat:
            self.kd_time = -1

        if self.is_move and self.kd_time == -1:                                     # если нажал кнопку и кд откатилось
            self.image = image.load(f"images/{self.path}/{self.unit_inside}/wait/{self.unit_inside}1.png").convert_alpha()
            self.move()
        if self.is_move and self.kd_time != -1:                                     # если нажал кнопку и кд не откатилось
            self.is_move = False
        if self.is_move is not True and self.pos != self.default_pos:               # если отжал кнопку и не на дефолтной позиции.
            self.back_to_default()

        if self.kd_time == self.default_kd_time:                                    # когда  обновилось кд, загрузить картинку закрытого слота
            self.image3 = image.load("images/other/kd_slota.png").convert_alpha()
        if self.kd_time == 0:                                                       # когда кд дошло до нуля, загрузить картину юнита
            self.image3 = image.load(f"images/other/nothing.png").convert_alpha()
            self.kd_time = -1                                                       # чтобы картинка загрузилась только 1 раз, а потом проверка не пройдёт

        if self.kd_time > 0:                                                        # уменьшает кд с каждым циклом
            self.kd_time -= 1

        screen.blit(font30.render(str(self.kd_time), True, (255, 255, 255)), (self.default_pos[0] - 49, self.default_pos[1] + 50))  # потом будет графически так что пох что пропадает


class Button:               # Переделать на спрайты кнопок
    def __init__(self, data_type, font_or_path, text_or_img, closed=False, windowed=False):
        if data_type == "img":
            self.image = image.load(f"images/{font_or_path}/{text_or_img}.png").convert_alpha()
            self.unit_inside = text_or_img[:-1]
        if data_type == "text":
            self.font = font_or_path
            self.text = text_or_img

        self.rect = None
        self.data_type = data_type
        self.clicked = False
        self.pushed = False
        self.ok = False
        self.closed = closed
        self.windowed = windowed
        buttons_group.append(self)

    def click(self, surf, pos, col=(255, 255, 255), offset_pos=(0, 0)):  # offset_pos нужно только где есть скрол
        if self.data_type == "text":
            self.image = self.font.render(self.text, font, col)   # По дефолту цвет текста белый. Я ебал по 50 раз писать одно и тоже
        self.rect = self.image.get_rect(topleft=(pos[0] + offset_pos[0], pos[1] + offset_pos[1]))

        surf.blit(self.image, (self.rect.x - offset_pos[0], self.rect.y - offset_pos[1]))
        if self.ok is True:
            surf.blit(image.load("images/buttons_states/ok.png").convert_alpha(), (self.rect.x - offset_pos[0], self.rect.y - offset_pos[1]))

        if not self.rect.collidepoint(mouse_pos):
            self.pushed = False
        if self.rect.collidepoint(mouse_pos):
            if mouse.get_pressed()[0] == 1 and not self.pushed:
                self.pushed = True
        if mouse.get_pressed()[0] == 0 and self.pushed:
            self.pushed = False
            return True

    def on_hover(self, pos, offset_pos=(0, 0)):
        if self.image.get_rect(topleft=(pos[0] + offset_pos[0], pos[1] + offset_pos[1])).collidepoint(mouse_pos):
            return True
        return False


class Cloud(sprite.Sprite):
    def __init__(self, *pos):
        super().__init__(all_sprites_group, clouds_group)
        r = randint(1, 5)
        self.image = image.load(f"images/clouds/cloud{r}.png").convert_alpha()
        if pos:
            self.x = pos[0][0]
            self.y = pos[0][1]
        else:
            self.x = 1600
            self.y = randint(0, 100)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.render_layer = 1

    def update(self):
        self.x -= 1
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        if self.x < - 200:
            self.kill()
            Cloud()


class Alert(sprite.Sprite):
    def __init__(self, text, pos, alert_time, font_=font60, col=(255, 0, 0), after_sec=0):
        super().__init__(alert_group)
        self.image = self.standard_image = font_.render(text, True, col)
        self.rect = self.standard_image.get_rect(topleft=pos)
        self.alert_time = alert_time
        self.trigger = after_sec * 75
        self.already_triggered = False
        self.text = text

    def update(self):
        if self.trigger > 0 and not self.already_triggered:
            self.trigger -= 1
            self.image = image.load("images/other/nothing.png").convert_alpha()
        else:
            self.already_triggered = True
            self.image = self.standard_image

            if self.alert_time < 0:
                self.kill()
            else:
                self.alert_time -= 1


class Button2:
    def __init__(self):
        self.pushed = False
        self.activate = False


class GlobalMapLevelButton(Button2):
    def __init__(self, number: str, parent: str, pos: tuple, level=None, chest=None):   # noqa
        super().__init__()
        self.number = number
        self.chest = chest
        self.level = level
        self.pos = pos
        self.image = global_level
        self.rect = self.image.get_rect(topleft=self.pos)
        self.parent = parent
        global_map.add(self)


class UpgradeTowerButton(Button2):
    def __init__(self, number: str, pos):
        super().__init__()
        self.number = number
        self.pos = pos
        self.image = upgrade_tower_red
        self.rect = self.image.get_rect(topleft=self.pos)
        tower_upgrades_group.add(self)

    def set_active(self, state):
        self.activate = state
        if self.activate:
            self.image = upgrade_tower_green
        if not self.activate:
            self.image = upgrade_tower_red


def is_free(new_tower):
    is_free_list = []           # Проверка свободна ли клетка
    for tower in towers_group:
        if tower != new_tower:
            is_free_list.append(tower.rect.collidepoint(new_tower.rect.centerx, new_tower.rect.centery) is False)
    for nekusaemiy in nekusaemie_group:
        if nekusaemiy != new_tower:
            is_free_list.append(nekusaemiy.rect.collidepoint(new_tower.rect.centerx, new_tower.rect.centery) is False)
    if all(is_free_list) or new_tower.free_placement:
        is_free_list.clear()
        return True


def uniq_is_free(new_tower):
    if new_tower.unit_inside == "gnome_cannon1":
        for tower in towers_group:
            if tower.rect.collidepoint(new_tower.rect.centerx, new_tower.rect.centery) and tower.stack == "gnome_cannon":
                if tower.name == "gnome_cannon3":
                    tower.stack = None
                    return True, "gnome_flamethrower"
                if tower.name != "gnome_cannon3":
                    tower.kill()
                    num = int(tower.name[-1]) + 1
                    return True, tower.name[:-1] + str(num)
        return None, None


def tower_placement(new_tower):
    if is_free(new_tower):
        if level.money - tower_costs[new_tower.unit_inside] >= 0:
            Tower(new_tower.unit_inside, unit_pos)
            if not level.cheat:
                level.money -= tower_costs[new_tower.unit_inside]
            new_tower.kd_time = new_tower.default_kd_time

    elif new_tower.unit_inside == "gnome_cannon1" or new_tower.unit_inside == "go_bleen1":
        ok_, tower_name = uniq_is_free(new_tower)
        if ok_:
            if level.money - tower_costs[new_tower.unit_inside] >= 0:
                Tower(tower_name, unit_pos)
                if not level.cheat:
                    level.money -= tower_costs[new_tower.unit_inside]
                new_tower.kd_time = new_tower.default_kd_time


def random_add_to_slots(*blocked_slots_):    # жестко пофиксить
    all_towers = []
    for tower in select_towers_preview_group.entities:
        if tower not in select_towers_preview_group.remember_entities and tower.name in received_towers:
            all_towers.append(tower)
    random_unit = choice(all_towers)
    add_to_slots(random_unit, *blocked_slots_)


def add_to_slots(en, *blocked_slots_):    # жестко пофиксить
    if len(select_towers_preview_group.remember_entities) <= 6 - len(blocked_slots_) or en.in_slot:
        if not en.in_slot:
            UI((94, first_empty_slot(blocked_slots_)), "towers", en.name, en.free_placement, towers_kd[en.name])
            en.in_slot = True
            select_towers_preview_group.remember_entities.append(en)
        elif en.in_slot:
            for ui in ui_group:
                if ui.unit_inside == en.name:
                    ui.kill()
                    en.in_slot = False
                    select_towers_preview_group.remember_entities.remove(en)
    else:
        Alert("Закончились свободные слоты", (345, 760), 75)


def first_empty_slot(blocked_slots_):
    ui_pos_list = {160, 256, 352, 448, 544, 640, 736} - set(blocked_slots_)
    fill_pos = set()
    for ui in ui_group:
        if ui.rect.y in ui_pos_list:
            fill_pos.add(ui.rect.y)

    return min(ui_pos_list - fill_pos)


def scroll_offset_min_max(min_offset, max_offset):
    global scroll_offset, current_scroll_offset_state

    if scroll_offset < min_offset:
        scroll_offset = min_offset
    if scroll_offset > max_offset:
        scroll_offset = max_offset

    if current_scroll_offset_state != game_state:
        scroll_offset = 0
        current_scroll_offset_state = game_state


def upload_data(default=False):
    global continue_level, \
        passed_levels, \
        received_towers, \
        not_received_towers, \
        encountered_enemies, \
        not_encountered_enemies, \
        city_coins, \
        forest_coins, \
        evil_coins, \
        mountain_coins, \
        snow_coins

    load_file = "saves/current_save.save"
    if default:
        load_file = "saves/default_save.save"

    with open(load_file, "r", encoding="utf-8") as file:
        passed_levels = str(*file.readline().strip().split(" = ")[1:]).split(", ")
        received_towers = str(*file.readline().strip().split(" = ")[1:]).split(", ")       # считать список
        not_received_towers = str(*file.readline().strip().split(" = ")[1:]).split(", ")
        if not_received_towers[0] == "[]":
            not_received_towers = []
        encountered_enemies = str(*file.readline().strip().split(" = ")[1:]).split(", ")
        not_encountered_enemies = str(*file.readline().strip().split(" = ")[1:]).split(", ")
        if not_encountered_enemies[0] == "[]":
            not_encountered_enemies = []

        _ = file.readline().strip()                                                        # считать строку с дефисами

        for i in range(5):
            line = file.readline().strip().split()
            your_coins[line[0]] = int(line[2])

        _ = file.readline().strip()

        for i in range(len(received_towers) + len(not_received_towers)):
            line = file.readline().strip().split(" = ")
            if str(*line[1:]).split(", ")[0] == "[]":
                result = []
            else:
                result = str(*line[1:]).split(", ")
            upgrades[line[0]] = result


def save_data():
    with open("saves/current_save.save", "w", encoding="utf-8") as file:
        file.write(f"passed_levels = " + str(passed_levels).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"received_towers = " + str(received_towers).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"not_received_towers = " + str(not_received_towers).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"encountered_enemies = " + str(encountered_enemies).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"not_encountered_enemies = " + str(not_encountered_enemies).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"-----\n")
        for k, v in your_coins.items():
            file.write(f"{k} = {v}\n")
        # file.write(f"forest_coins = {forest_coins}\n")
        # file.write(f"evil_coins = {evil_coins}\n")
        # file.write(f"mountain_coins = {mountain_coins}\n")
        # file.write(f"snow_coins = {snow_coins}\n")
        file.write(f"-----\n")
        for k, v in upgrades.items():
            file.write(f"{k} = " + str(v).replace("['", "").replace("']", "").replace("'", "") + "\n")


def draw_info(pos, current_value, max_value, reversed_=False):       # (196, 380)
    w = 60  # а то ругается
    draw.rect(modification_preview_menu, (200, 0, 0), (*pos, 300, 35))
    if current_value != 0:
        current_value *= 10
        max_value *= 10
        if not reversed_:
            w = 60 * max(int(current_value / (max_value / 5)), 1)       # int, max и 1 убрать и будут не целые квадраты
        if reversed_:
            w = 60 * (6 - max(int(current_value / (max_value / 5)), 1))
        draw.rect(modification_preview_menu, (0, 200, 0), (*pos, w, 35))
        for i in range(1, 5):
            draw.line(modification_preview_menu, (0, 0, 0), (pos[0] + (60 * i), pos[1]), (pos[0] + (60 * i), pos[1] + 34), 5)
    else:
        draw.rect(modification_preview_menu, (128, 128, 128), (*pos, 300, 35))
    draw.rect(modification_preview_menu, (0, 0, 0), (*pos, 300, 35), 5)


def menu_positioning():
    global game_state,\
            continue_level,\
            running,\
            last_game_state,\
            passed_levels, \
            level,\
            scroll_offset, \
            coin_indent_x, \
            count_of_reward_coins

    if game_state == "main_menu":
        screen.blit(main_menu, (0, 0))
        screen.blit(game_name, (416, 10))

        if new_game_button.click(screen, (30, 380)):
            last_game_state = game_state
            game_state = "yes_no_window"  # новая игра

        if not continue_level:
            if resume_button.click(screen, (30, 460), col=(130, 130, 130)):
                Alert("<- Тыкай новую игру", (500, 380), 75)
        else:
            if resume_button.click(screen, (30, 460)):
                last_game_state = game_state
                if level.state == "run":
                    game_state = "run"
                else:
                    game_state = "global_map"
        if level_select_button.click(screen, (30, 540)):
            last_game_state = game_state
            game_state = "global_map"
        if preview_button.click(screen, (30, 620)):
            last_game_state = game_state
            game_state = "manual_menu"
        if settings_button.click(screen, (30, 700)):
            last_game_state = game_state
            game_state = "settings_menu"
        if quit_button.click(screen, (30, 780)):
            running = False

    if game_state == "yes_no_window":
        screen.blit(main_menu, (0, 0))
        screen.blit(pause_menu, (480, 250))
        screen.blit(font60.render("Начать новую игру?", True, (255, 255, 255)), (507, 280))

        if accept_button.click(screen, (620, 485)):
            upload_data(default=True)
            preview_group.refresh(3)

            for level_ in global_map.entities:
                if level_.chest:
                    level_.chest.refresh()

            last_game_state = game_state
            game_state = "global_map"
            # continue_level = False
            # level = levels[0]
            # level.refresh()
            # level.state = "not_run"

        if accept_button.on_hover((630, 485)):
            screen.blit(font30.render("!!! Весь прогресс сотрётся !!!", True, (200, 0, 0)), (598, 580))

        if deny_button.click(screen, (870, 485)):
            last_game_state, game_state = game_state, last_game_state

    if game_state == "manual_menu":
        screen.blit(preview_menu, (0, 0))
        preview_menu.blit(entity_preview_menu, (250, 120))      # 50 100 пофиксить/вырезать нафиг
        entity_preview_menu.blit(entity_preview_menu_copy, (0, 0))
        screen.blit(font50.render("Справочник", True, (0, 0, 0)), (370, 60))
        screen.blit(modification_preview_menu, (830, 120))
        modification_preview_menu.blit(modification_preview_menu_copy, (0, 0))
        modification_preview_menu.blit(line_, (0, 275))
        scroll_offset_min_max(-1200, 0)                          # одна линия -150

        preview_group.move_element_by_scroll()
        preview_group.go_animation()
        preview_group.check_hover(entity_preview_menu, offset_pos=(250, 120))
        if preview_group.check_click(entity_preview_menu, offset_pos=(250, 120)):
            tower_upgrades_group.pushed_entity = None

        preview_group.custom_draw(entity_preview_menu, offset_pos=(250, 120))
        preview_group.set_default_pushed_entity()

        if preview_group.turn == Tower and preview_group.pushed_entity.name in received_towers:
            modification_preview_menu.blit(upgrade_path, (0, 0))
            tower_upgrades_group.check_click(entity_preview_menu, offset_pos=(830, 120))
            tower_upgrades_group.custom_draw(modification_preview_menu, offset_pos=(830, 120))

        if preview_group.pushed_entity.name in received_towers or preview_group.pushed_entity.name in encountered_enemies:
            screen.blit(font50.render(f"{str(preview_group.pushed_entity.name):^34}", True, (0, 0, 0)), (800, 60))    # 960 60
        else:
            screen.blit(font50.render("???", True, (0, 0, 0)), (1030, 60))

        if not tower_upgrades_group.pushed_entity:
            modification_preview_menu.blit(font35.render("ХП", True, (0, 0, 0)), (10, 302))
            if hasattr(preview_group.pushed_entity, "hp") and (preview_group.pushed_entity.name in received_towers or preview_group.pushed_entity.name in encountered_enemies):
                draw_info((196, 310), preview_group.pushed_entity.hp, preview_group.get_max_hp())
            else:
                draw_info((196, 310), 0, 0)

            modification_preview_menu.blit(font35.render("Урон", True, (0, 0, 0)), (10, 352))
            if hasattr(preview_group.pushed_entity, "atk") and (preview_group.pushed_entity.name in received_towers or preview_group.pushed_entity.name in encountered_enemies):
                draw_info((196, 360), preview_group.get_damage_per_sec(preview_group.pushed_entity), preview_group.get_max_damage_per_sec())
            else:
                draw_info((196, 360), 0, 0)

            if preview_group.turn == Tower:
                modification_preview_menu.blit(font35.render("Кд", True, (0, 0, 0)), (10, 402))
                if preview_group.pushed_entity.name in towers_kd and (preview_group.pushed_entity.name in received_towers or preview_group.pushed_entity.name in encountered_enemies):
                    draw_info((196, 410), towers_kd[preview_group.pushed_entity.name], max(towers_kd.values()), reversed_=True)
                else:
                    draw_info((196, 410), 0, 0)

                modification_preview_menu.blit(font35.render("Цена", True, (0, 0, 0)), (10, 452))
                if preview_group.pushed_entity.name in tower_costs and (preview_group.pushed_entity.name in received_towers or preview_group.pushed_entity.name in encountered_enemies):
                    modification_preview_menu.blit(font40.render(str(tower_costs[preview_group.pushed_entity.name]), True, (0, 0, 0)), (450, 450))
                    # draw_info((196, 460), tower_costs[guide_group.pushed_entity.name], max(tower_costs.values()), reversed_=True)
                else:
                    draw_info((196, 460), 0, 0)

                modification_preview_menu.blit(font35.render("Редкость", True, (0, 0, 0)), (10, 502))
                if hasattr(preview_group.pushed_entity, "rarity"):    # просто слева автоматически не рисовалось
                    if preview_group.pushed_entity.rarity == "legendary":
                        modification_preview_menu.blit(font40.render(f"{preview_group.pushed_entity.rarity}", True, (255, 210, 0)), (310, 497))
                    if preview_group.pushed_entity.rarity == "common":
                        modification_preview_menu.blit(font40.render(f"{preview_group.pushed_entity.rarity}", True, (0, 200, 0)), (340, 497))
                    if preview_group.pushed_entity.rarity == "spell":
                        modification_preview_menu.blit(font40.render(f"{preview_group.pushed_entity.rarity}", True, (0, 0, 200)), (400, 497))
                else:
                    draw_info((196, 510), 0, 0)

                modification_preview_menu.blit(line_, (0, 560))

            if preview_group.turn == Enemy:
                modification_preview_menu.blit(font35.render("Скорость", True, (0, 0, 0)), (10, 402))
                if hasattr(preview_group.pushed_entity, "speed") and (preview_group.pushed_entity.name in received_towers or preview_group.pushed_entity.name in encountered_enemies):
                    draw_info((196, 410), preview_group.pushed_entity.speed, preview_group.get_max_speed())
                else:
                    draw_info((196, 410), 0, 0)

                modification_preview_menu.blit(font35.render("Дальность", True, (0, 0, 0)), (10, 452))
                if hasattr(preview_group.pushed_entity, "attack_range") and (preview_group.pushed_entity.name in received_towers or preview_group.pushed_entity.name in encountered_enemies):
                    if preview_group.pushed_entity.attack_range == 0:
                        modification_preview_menu.blit(font40.render("Рукопашная", True, (0, 0, 0)), (257, 447))
                    else:
                        draw_info((196, 460), preview_group.pushed_entity.attack_range, preview_group.get_max_attack_range())
                else:
                    draw_info((196, 460), 0, 0)

                modification_preview_menu.blit(line_, (0, 510))
        else:
            modification_preview_menu.blit(line_, (0, 560))
            if preview_group.pushed_entity.name in upgrade_costs:
                up_cost = upgrade_costs[preview_group.pushed_entity.name][tower_upgrades_group.pushed_entity.number].split()
                upgrade_cost = int(up_cost[0])
                upgrade_coin_name = up_cost[1]

                if your_coins[upgrade_coin_name] < 10:
                    modification_preview_menu.blit(font60.render(str(your_coins[upgrade_coin_name]), True, (0, 0, 0)), (385, 290))
                else:                                                                                        # больше 100 не будет
                    modification_preview_menu.blit(font60.render(str(your_coins[upgrade_coin_name]), True, (0, 0, 0)), (350, 290))
                modification_preview_menu.blit(coins[upgrade_coin_name], (430, 300))

                if tower_upgrades_group.pushed_entity.number not in upgrades[preview_group.pushed_entity.name] and tower_upgrades_group.possible_upgrade_path():
                    modification_preview_menu.blit(font60.render(str(upgrade_cost), True, (0, 0, 0)), (310, 470))
                    modification_preview_menu.blit(coins[upgrade_coin_name], (355, 480))

                    if buy_upgrade_button.click(modification_preview_menu, (80, 470), col=(0, 0, 0), offset_pos=(830, 120)) and your_coins[upgrade_coin_name] >= upgrade_cost:
                        upgrades[preview_group.pushed_entity.name].append(tower_upgrades_group.pushed_entity.number)
                        your_coins[upgrade_coin_name] -= upgrade_cost

                    if buy_upgrade_button.on_hover((80, 470), offset_pos=(830, 120)):
                        modification_preview_menu.blit(font30.render("Можно выбрать только 1 ветку !!!", True, (200, 0, 0)), (5, 580))
            # бла бла бла, screen.blit(описание)

        if back_button.click(screen, (1000, 750), col=(0, 0, 0)):
            game_state, last_game_state = last_game_state, game_state
            scroll_offset = 0

        if change_preview_turn_button.click(screen, (1280, 90)):
            if preview_group.turn == Enemy:
                preview_group.turn = Tower
                change_preview_turn_button.image = image.load("images/coins/city_coin.png").convert_alpha()
            else:
                preview_group.turn = Enemy
                change_preview_turn_button.image = image.load("images/coins/evil_coin.png").convert_alpha()
            preview_group.pushed_entity = list(filter(preview_group.filter_by_turn, preview_group.entities))[0]

    if game_state != "main_menu"\
            and game_state != "main_settings_menu"\
            and game_state != "level_select"\
            and game_state != "manual_menu"\
            and game_state != "yes_no_window"\
            and game_state != "global_map"\
            and game_state != "reward":
        screen.blit(level.image, (0, 0))
        if level.cheat:
            # screen.blit(font40.render("CHEAT MODE", True, (255, 0, 0)), (853, 110))
            pass
        else:
            level.draw_level_time()
            # screen.blit(font40.render(str(level.level_time) + " осталось", True, (255, 255, 255)), (853, 110))    # циферки
        # screen.blit(font40.render(str(level.current_level) + " уровень", True, (255, 255, 255)), (893, 30))
        level_num.update_text(font40.render(level.current_level + " уровень", True, (255, 255, 255)))
        # screen.blit(font40.render(str(level.money), True, (0, 0, 0)), (88, 53))
        level_money.update_text(font40.render(str(level.money), True, (0, 0, 0)))

        all_sprites_group.custom_draw(screen)
        all_sprites_group.draw_other(screen)

    if game_state == "global_map":
        scroll_offset_min_max(-1600, 0)
        screen.blit(game_map, (0 + scroll_offset, 0))

        # global_map.check_hover(screen)        # если нужно при наведении что то делать
        global_map.check_click(screen)
        global_map.use_clicked_object()
        global_map.move_element_by_scroll(vector="x")
        global_map.custom_draw(screen)

        if back_button.click(screen, (30, 20), col=(200, 0, 0)):
            last_game_state = game_state
            game_state = "main_menu"

    if game_state == "run":
        game_state = level.update()
        if pause_button.click(screen, (1550, 30)):
            last_game_state = game_state
            Alert("Пауза", (700, 200), 75)
            game_state = "paused"

    if game_state == "paused":
        screen.blit(pause_menu, (480, 250))
        if resume_button.click(screen, (614, 280)):
            last_game_state = game_state
            if level.state == "run":
                game_state = "run"
            else:
                game_state = "tower_select"
        if settings_button.click(screen, (642, 360)):
            last_game_state = game_state
            game_state = "settings_menu"
        if level.state == "run":           # белая кнопка
            if restart_button.click(screen, (582, 440)):
                last_game_state = game_state
                level.refresh()
                game_state = "tower_select"
                level.state = "not_run"
        else:
            if restart_button.click(screen, (582, 440), col=(130, 130, 130)):  # 2 кнопка серая
                pass
        if main_menu_button.click(screen, (567, 520)):
            last_game_state = game_state
            game_state = "main_menu"
        if pause_button.click(screen, (1550, 30)):
            Alert("Пауза", (700, 200), 75)
            if level.state == "run":
                last_game_state = game_state
                game_state = "run"
            else:
                game_state, last_game_state = last_game_state, game_state

    if game_state == "level_complited":
        screen.blit(pause_menu, (480, 250))
        screen.blit(font60.render("Уровень пройден", True, (193, 8, 42)), (544, 280))
        # if str(level.current_level + 1) not in passed_levels:
        #     passed_levels.append(str(level.current_level + 1))    # переписать

        if to_map_button.click(screen, (669, 360)):     # 449
            # level.refresh()
            # level = Level(*levels_config[str(level.current_level + 1)])   # fix
            game_state = "global_map"
        if restart_button.click(screen, (582, 440)):
            last_game_state = game_state
            level.refresh()
            game_state = "tower_select"
        if main_menu_button.click(screen, (567, 520)):
            last_game_state = game_state
            game_state = "main_menu"

    if game_state == "tower_select":
        screen.blit(select_menu, (250, 150))
        select_menu.blit(select_menu_copy, (0, 0))
        screen.blit(additional_menu, (1210, 150))
        scroll_offset_min_max(-450, 0)      # насколько сильно прокручивается вниз

        select_towers_preview_group.move_element_by_scroll()
        select_towers_preview_group.check_hover(select_menu, offset_pos=(250, 150))
        if select_towers_preview_group.check_click(select_menu, offset_pos=(250, 150)):
            if select_towers_preview_group.pushed_entity.name in received_towers:
                add_to_slots(select_towers_preview_group.pushed_entity, *level.blocked_slots)
        select_towers_preview_group.go_animation()
        select_towers_preview_group.custom_draw(select_menu)

        if clear_button.click(screen, (1250, 470), col=(0, 0, 0)):
            select_towers_preview_group.remember_entities_empty()
            for ui in ui_group:
                ui.kill()

        if random_choice_button.click(screen, (1248, 550), col=(0, 0, 0)):
            if len(select_towers_preview_group.remember_entities) == 7 - len(level.blocked_slots):
                level.clear()
            for i in range(7 - len(select_towers_preview_group.remember_entities) - len(level.blocked_slots)):
                random_add_to_slots(*level.blocked_slots)

        if start_level_button.click(screen, (1265, 630), col=(0, 0, 0)):
            if len(select_towers_preview_group.remember_entities) == 7 - len(level.blocked_slots):
                scroll_offset = 0
                game_state = "run"
                level.clear(ui_group)
                level.state = "not_run"
                continue_level = True
                select_towers_preview_group.remember_entities.clear()
            else:
                Alert("Остались свободные слоты", (400, 760), 75)
        if pause_button.click(screen, (1550, 30)):
            last_game_state = game_state
            Alert("Пауза", (700, 200), 75)
            game_state = "paused"
        ui_group.draw(screen)

    if game_state == "settings_menu":
        if last_game_state == "main_menu" or last_game_state == "level_select":
            screen.blit(main_menu, (0, 0))
            screen.blit(game_name, (416, 10))
        screen.blit(pause_menu, (480, 250))

        if back_button.click(screen, (709, 520)):
            game_state = last_game_state

        if cheat_button.click(screen, (736, 280)):
            if level.cheat:
                cheat_button.ok = False
                level.cheat = False
            else:
                cheat_button.ok = True
                level.cheat = True

        if unlock_all_button.click(screen, (600, 420)):
            unlock_all_button.ok = True

            for tower in not_received_towers:
                received_towers.append(tower)
            not_received_towers.clear()

            for enemy_ in not_encountered_enemies:
                encountered_enemies.append(enemy_)
            not_encountered_enemies.clear()

            passed_levels = ["0", "1", "2", "3", "4", "5", "6", "6а"]
            preview_group.refresh(3)
            print("all_unlocked")

    if game_state == "death":
        screen.blit(pause_menu, (480, 250))
        screen.blit(font60.render("Вы проиграли", True, (193, 8, 42)), (590, 280))
        if settings_button.click(screen, (642, 360)):
            last_game_state = game_state
            game_state = "settings_menu"
        if restart_button.click(screen, (582, 440)):
            last_game_state = game_state
            level.refresh()
            game_state = "tower_select"
        if main_menu_button.click(screen, (567, 520)):
            continue_level = False
            last_game_state = game_state
            game_state = "main_menu"

    if game_state == "reward_first_stage":
        count_of_reward_coins = 0
        for i, (k, v) in enumerate(global_map.chest.rewards.items()):
            if k in [*received_towers, *not_received_towers]:
                rewards_preview_group.new_reward(k)
            if k in coins:
                your_coins[k] += v
                count_of_reward_coins += 1

        coin_indent_x = (640 - (count_of_reward_coins * 64)) // (count_of_reward_coins + 1)
        rewards_preview_group.entity_create(len(rewards_preview_group.rewards), indent=80)
        game_state = "reward_second_stage"

    if game_state == "reward_second_stage":
        screen.blit(game_map, (0 + scroll_offset, 0))
        global_map.custom_draw(screen)
        screen.blit(pause_menu_w, (480, 250))
        pause_menu_w.blit(pause_menu_w_copy, (0, 0))
        pause_menu_w.blit(font60.render("Награда", True, (0, 0, 0)), (195, 0))

        for i, (k, v) in enumerate(global_map.chest.rewards.items()):
            if k in coins:
                column = (i % count_of_reward_coins)
                pause_menu_w.blit(coins[k], (coin_indent_x + (column * (64 + coin_indent_x)) + (column * 22.5), 230))
                pause_menu_w.blit(font60.render(str(v), True, (0, 0, 0)), (coin_indent_x + (column * (64 + coin_indent_x)) - ((2 - column) * 22.5), 225))

        rewards_preview_group.custom_draw(pause_menu_w)
        rewards_preview_group.go_animation()

        if take_button.click(screen, (680, 540), col=(0, 0, 0)):
            last_game_state = game_state
            game_state = "global_map"
            rewards_preview_group.clear_rewards()
    # -------


bullets_group = sprite.Group()
parasites_group = sprite.Group()
buffs_group = sprite.Group()
creeps_group = sprite.Group()
enemies_group = sprite.Group()
towers_group = sprite.Group()
nekusaemie_group = sprite.Group()
ui_group = sprite.Group()
all_sprites_group = ModGroup()
clouds_group = sprite.Group()
alert_group = sprite.Group()
level_group = sprite.Group()
preview_group = PreviewGroup(Tower, Enemy)
select_towers_preview_group = PreviewGroup(Tower)
global_map = GlobalMap()
tower_upgrades_group = TowerUpgradesGroup()
text_sprites_group = sprite.Group()
rewards_preview_group = RewardsPreviewGroup()

pause_button = Button("text", font40, "||",)
restart_button = Button("text", font60, "Перезапустить")
resume_button = Button("text", font60, "Продолжить")
settings_button = Button("text", font60, "Настройки")
main_menu_button = Button("text", font60, "В главное меню")
back_button = Button("text", font60, "Назад")
quit_button = Button("text", font60, "Выход")
new_game_button = Button("text", font60, "Новая игра",)
level_select_button = Button("text", font60, "Выбрать уровень")
to_map_button = Button("text", font60, "На карту")
cheat_button = Button("img", "menu", "cheat")
start_level_button = Button("text", font60, "Начать")
random_choice_button = Button("text", font50, "Случайно")
preview_button = Button("text", font60, "Справочник")
change_preview_turn_button = Button("img", "coins", "city_coin")
accept_button = Button("text", font60, "Да")
deny_button = Button("text", font60, "Нет")
unlock_all_button = Button("text", font60, "Открыть всё")
buy_upgrade_button = Button("text", font60, "Купить")
clear_button = Button("text", font50, "Очистить")
take_button = Button("text", font60, "Забрать")

TextSprite(font40.render("CHEAT MODE", True, (255, 0, 0)), (853, 110), ("run", "paused", "level_complited", "tower_select", "death", "cheat", "settings_menu"))
level_num = TextSprite(font40.render("0" + " уровень", True, (255, 255, 255)), (893, 30), ("run", "paused", "level_complited", "tower_select", "death", "settings_menu"))
level_money = TextSprite(font40.render("300", True, (0, 0, 0)), (88, 53), ("run", "paused", "level_complited", "tower_select", "death", "settings_menu"))

# --- from save
passed_levels = []
received_towers = []
not_received_towers = []
encountered_enemies = []
not_encountered_enemies = []
city_coins = 0
forest_coins = 0
evil_coins = 0
mountain_coins = 0
snow_coins = 0
upload_data()
# ---


# levels = {
#     "1": Level("1", 22500, 750, 50, level_1_waves, ("popusk", "josky")),
#     "2": Level("2", 22500, 575, 50, level_2_waves, ("josky", "sigma", "sportik", "popusk"), level_image="1"),
#     "3": Level("3", 22500, 500, 50, level_3_waves, ("josky", "sigma", "sportik", "armorik", "zeleniy_strelok", "popusk", "teleportik"), level_image="1"),
#     "3а": Level("3а", 22500, 500, 50, level_3_waves, ("josky", "sigma", "sportik", "armorik", "zeleniy_strelok", "popusk", "teleportik"), level_image="1"),
#     "4": Level("4", 22500, 225, 50, level_4_waves, ("telezhnik", "rojatel", "sigma", "armorik", "zeleniy_strelok", "drobik", "klonik"), level_image="1"),
#     "5": Level("5", 31500, 225, 50, level_5_waves, ("popusk", "sigma", "josky", "zeleniy_strelok", "sportik", "rojatel", "mega_strelok", "armorik", "telezhnik", "drobik", "klonik", "teleportik"), level_image="1"),
#     "6б": Chest(parent_number="6б", rewards={"city_coin": 5, "evil_coin": 2, "zeus": "unlock"})
# }

# level = levels["1"]


GlobalMapLevelButton("1", "0", (100, 714), level=Level("1", 22500, 750, 50, level_waves["1"], level_allowed_enemies["1"]))     # !!! все буквы русские !!!
GlobalMapLevelButton("2", "1", (250, 544), level=Level("2", 22500, 575, 50, level_waves["2"], level_allowed_enemies["2"], level_image="1"))
GlobalMapLevelButton("3", "2", (500, 500), level=Level("3", 22500, 500, 50, level_waves["3"], level_allowed_enemies["3"], level_image="1"))
GlobalMapLevelButton("3а", "3", (700, 700), chest=Chest(parent_number="3а", rewards=chests_rewards["3а"]))
GlobalMapLevelButton("4", "3", (750, 400), level=Level("4", 22500, 225, 50, level_waves["4"], level_allowed_enemies["4"], level_image="1"))
GlobalMapLevelButton("5", "4", (1000, 400), level=Level("5", 31500, 225, 50, level_waves["5"], level_allowed_enemies["5"], level_image="1"))
GlobalMapLevelButton("6", "5", (1200, 300))
GlobalMapLevelButton("6а", "6", (1000, 100))
GlobalMapLevelButton("6б", "6а", (750, 100), chest=Chest(parent_number="6б", rewards=chests_rewards["6б"]))
GlobalMapLevelButton("6в", "6б", (500, 100))
GlobalMapLevelButton("6г", "6в", (250, 200))
GlobalMapLevelButton("7", "6", (1400, 200))
GlobalMapLevelButton("8", "7", (1650, 200))

level = global_map.entities[0].level

UpgradeTowerButton("1", (50, 104))
UpgradeTowerButton("2a", (216, 36))
UpgradeTowerButton("3a", (384, 36))
UpgradeTowerButton("2b", (216, 172))
UpgradeTowerButton("3b", (384, 172))


preview_group.entity_create(3)
select_towers_preview_group.entity_create(6)

running = True
while running:

    mouse_pos = mouse.get_pos()
    menu_positioning()

    if level.state == 'run':
        if free_money > 0:
            free_money -= 1
        else:
            free_money = default_free_money
            level.money += 5
            Alert('+5', (200, 30), 75, col=(0, 0, 0))

    alert_group.update()
    alert_group.draw(screen)
    if mouse.get_focused():
        screen.blit(cursor, mouse_pos)
        # screen.blit(font30.render(str(mouse_pos), True, (255, 0, 0)), (mouse_pos[0] - 60, mouse_pos[1] - 40))
        # draw.line(screen, (0, 0, 0), (800, 0), (800, 900), 5)
        # draw.line(screen, (0, 0, 0), (0, 450), (1600, 450), 5)

    for enemy in enemies_group:
        if enemy.rect.x <= 150:
            if not level.cheat:
                game_state = "death"
            enemy.kill()

    clock.tick(75)
    display.update()
    for e in event.get():
        if e.type == MOUSEWHEEL and (game_state == "level_select" or game_state == "tower_select" or game_state == "manual_menu" or game_state == "global_map"):
            scroll_offset += e.y * 50
            # scroll_pos = mouse_pos    # пока что забью
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE and (game_state == "run"
                                      or game_state == "paused"
                                      or game_state == "settings_menu"
                                      or game_state == "tower_select"
                                      or game_state == "level_select"):
                if game_state == "run":
                    last_game_state = game_state
                    Alert("Пауза", (700, 200), 75)
                    game_state = "paused"
                elif game_state == "level_select":
                    last_game_state = game_state
                    game_state = "main_menu"
                elif game_state == "tower_select":
                    last_game_state = game_state
                    Alert("Пауза", (700, 200), 75)
                    game_state = "paused"
                elif game_state == "settings_menu" and last_game_state != "main_menu":
                    game_state = "paused"
                elif game_state == "settings_menu" and last_game_state == "main_menu":
                    game_state = "main_menu"
                elif last_game_state == "tower_select":
                    last_game_state = game_state
                    game_state = "tower_select"
                elif game_state == "paused" and level.state == "run":    # !!! ВОЗМОЖЕН БАГ
                    game_state = "run"
                elif game_state == "paused" and level.state == "not_run":
                    game_state = "tower_select"
            if e.key == K_z:
                Enemy("popusk", (1508, 192))
            if e.key == K_x:
                Enemy("josky", (1508, 320))
            if e.key == K_c:
                Enemy("sigma", (1508, 448))
            if e.key == K_v:
                Enemy("sportik", (1508, 576))
            if e.key == K_b:
                Enemy("zeleniy_strelok", (1508, 704))

            if e.key == K_KP_7:
                Enemy("mega_strelok", (1508, 192))
            if e.key == K_KP_8:
                Enemy("telezhnik", (1508, 192))
            if e.key == K_KP_9:
                Enemy("teleportik", (1508, 192))
            if e.key == K_KP_4:
                Enemy("rojatel", (1508, 448))
            if e.key == K_KP_5:
                Enemy("armorik", (1508, 448))
            if e.key == K_KP_6:
                Enemy("drobik", (1508, 448))
            if e.key == K_KP_1:
                Enemy("rojatel", (1508, 704))
            if e.key == K_KP_2:
                Enemy("drobik", (1508, 704))
            if e.key == K_KP_3:
                Enemy("klonik", (1508, 704))

            if e.key == K_a:
                scroll_offset += 600
            if e.key == K_d:
                scroll_offset -= 600

            if e.key == K_r:
                level.give_reward()
            if e.key == K_o:
                for ent in global_map.entities:
                    if ent.chest:
                        ent.chest.refresh()
            if e.key == K_w:
                game_state = "level_complited"
            if e.key == K_q:
                running = False
        if e.type == QUIT:
            running = False
        # может потом кто то захочет сделать слайдер
        # if e.type == MOUSEMOTION and (game_state == "level_select" or game_state == "tower_select"):
        #     if mouse.get_pressed()[0]:
        #         scroll_offset -= e.rel[1] * 2
        #         print(scroll_offset)
        if e.type == MOUSEBUTTONDOWN:                                                       # При нажатии кнопки мыши
            mouse_pos = mouse.get_pos()
            for el in ui_group:
                if el.rect.collidepoint(mouse_pos):
                    el.is_move = True
        if e.type == MOUSEBUTTONUP:                                                          # При отжатии кнопки мыши
            mouse_pos = mouse.get_pos()
            unit_pos = (384 + ((mouse_pos[0] - 384) // 128) * 128), (192 + ((mouse_pos[1] - 192) // 128) * 128)

            for el in ui_group:
                if el.rect.collidepoint(mouse_pos):                                          # если элемент отпущен
                    el.is_move = False

                    if 1536 > unit_pos[0] >= 384 and 832 > unit_pos[1] >= 192:
                        if el.path == "towers":
                            tower_placement(el)

                        if el.path == "shovel":
                            for obj in [*towers_group, *nekusaemie_group]:                  # Сразу по 2 группам
                                if obj.rect.collidepoint(el.rect.centerx, el.rect.centery):
                                    if not level.cheat:
                                        level.money += tower_costs[obj.name] // 2
                                    if hasattr(obj, "bullet"):
                                        obj.bullet.kill()
                                    obj.kill()
save_data()
