from math import *
from random import randint, choice
from config import *
from animations import *
from pygame import *
import functools

mixer.pre_init(44100, -16, 1, 512)
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
main_menu = image.load("images/maps/global_map/events/bg_images/hello_game_event.png").convert_alpha()     # "images/menu/main_menu.png"
additional_menu = image.load("images/menu/additional_menu.png").convert_alpha()
preview_menu = image.load("images/menu/preview_menu.png").convert_alpha()
select_menu = image.load("images/menu/level_select_menu.png").convert_alpha()
botton_select_menu = image.load("images/menu/bottom_select_menu.png").convert_alpha()
select_menu_copy = select_menu.__copy__()
entity_preview_menu = image.load("images/menu/entity_preview_menu.png").convert_alpha()
entity_preview_menu_copy = entity_preview_menu.__copy__()
modification_preview_menu = image.load("images/menu/modification_guide_menu.png").convert_alpha()
modification_preview_menu_copy = modification_preview_menu.__copy__()
dialog_menu = image.load("images/menu/dialog_menu.png").convert_alpha()
amogus = image.load("images/other/!!!.png").convert_alpha()
cursor = image.load("images/other/cursor.png").convert_alpha()
rage = image.load("images/other/rage.png").convert_alpha()
unvulnerable = image.load("images/other/unvulnerable.png").convert_alpha()
great_spike_form = image.load("images/buffs/great_spike_form.png").convert_alpha()  # возможно это лучше куда-то в другое место запихнуть. я прост хз куда
red_32x32 = image.load("images/other/red_32x32.png").convert_alpha()
nota = image.load("images/other/nota.png").convert_alpha()
tower_window_legendary = image.load("images/tower_select_windows/tower_select_window_legendary.png").convert_alpha()
tower_window_common = image.load("images/tower_select_windows/tower_select_window_common.png").convert_alpha()
tower_window_spell = image.load("images/tower_select_windows/tower_select_window_spell.png").convert_alpha()
tower_window_active = image.load("images/tower_select_windows/tower_select_window_active.png").convert_alpha()
line_ = image.load("images/other/line.png").convert_alpha()
unknown_entity = image.load("images/buttons_states/unknown_entity.png").convert_alpha()
# game_map = image.load("images/maps/global_map/game_map.png").convert_alpha()
game_map = image.load("images/maps/global_map/game_map_new3.png").convert_alpha()
global_level_image = image.load("images/maps/global_map/global_level.png").convert_alpha()
ok = image.load("images/buttons_states/ok.png").convert_alpha()
upgrade_tower_red = image.load("images/buttons_states/upgrade_tower_red.png").convert_alpha()
upgrade_tower_green = image.load("images/buttons_states/upgrade_tower_green.png").convert_alpha()
upgrade_tower_select = image.load("images/buttons_states/upgrade_tower_select.png").convert_alpha()
current_tower_upgrade = image.load("images/buttons_states/current_tower_upgrade.png").convert_alpha()
upgrade_path = image.load("images/other/upgrade_path.png").convert_alpha()
new_bg = image.load("images/other/new_bg.png").convert_alpha()
map_secret_3 = image.load("images/maps/global_map/secrets/map_3_secret.png").convert_alpha()
map_secret_6 = image.load("images/maps/global_map/secrets/map_6_secret.png").convert_alpha()
villager = image.load("images/dialog_nps/villager.png").convert_alpha()
fire_mag = image.load("images/dialog_nps/fire_mag.png").convert_alpha()
global_map_overlay = image.load("images/maps/global_map/global_map_owerlay.png").convert_alpha()
gg_on_map = image.load("images/other/gg_on_map.png").convert_alpha()
gg_dialog = image.load("images/dialog_nps/gg_dialog.png").convert_alpha()
smoke = image.load("images/maps/global_map/fog.png").convert_alpha()
enemy_tile = image.load("images/maps/global_map/enemy_tile.png").convert_alpha()

mixer.init()
# mixer.music.load('jungles.ogg')  # фоновая музыка
# mixer.music.play()
general_volume = 0
music_volume = 1.0
sound_effects_volume = 1.0

font25 = font.Font("fonts/ofont.ru_Nunito.ttf", 25)
font30 = font.Font("fonts/ofont.ru_Nunito.ttf", 30)
font35 = font.Font("fonts/ofont.ru_Nunito.ttf", 35)
font40 = font.Font("fonts/ofont.ru_Nunito.ttf", 40)
font50 = font.Font("fonts/ofont.ru_Nunito.ttf", 50)
font60 = font.Font("fonts/ofont.ru_Nunito.ttf", 60)


game_name = font60.render("GAME_OSTRY_SHISHKAN", True, (255, 255, 255))  # GAME_OSTRY_SHISHKAN
game_state = "main_menu"
last_game_state = game_state
buttons_group = []
scroll_offset = 0
coin_indent_x = 0
count_of_reward_coins = 0
current_scroll_offset_state = game_state
free_money = default_free_money = 75
upgrades = {}
your_coins = {}
event_stage = 0
developer_mode = True
temp_hero_pos = (9, 5)
temp_scroll_offset = (0, 0)


class ExtendedGroup(sprite.Group):
    def __init__(self):
        super().__init__()

    def custom_draw(self, surf):
        for sprite_ in sorted(self.sprites(), key=self.sort_by_layer):
            surf.blit(sprite_.image, sprite_.rect)

            if level.rect_visible:
                if hasattr(sprite_, "rect"):
                    draw.rect(screen, (0, 200, 0), sprite_.rect, 5)
                if hasattr(sprite_, "rect_pen"):
                    draw.rect(screen, (200, 0, 0), sprite_.rect_pen, 5)

    @staticmethod
    def sort_by_layer(obj_):
        return obj_.render_layer

    def draw_other(self, surf):
        for obj_ in self.sprites():
            if hasattr(obj_, "image2"):
                surf.blit(obj_.image2, obj_.rect2)
            if hasattr(obj_, "image3"):
                surf.blit(obj_.image3, obj_.rect3)


class BasePreviewGroup:
    def __init__(self, *supported_objects):
        self.entities = []
        self.scroll_pos = (0, 0)
        self.hovered_entity = None
        self.pushed_entity = None
        self.dragged_entity = None
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
        self.scroll_pos = (0, 0)

    def move_element_by_scroll(self):
        for en in self.entities:
            en.pos = en.pos[0] + scroller.scroll_offset_x - self.scroll_pos[0], en.pos[1] + scroller.scroll_offset_y - self.scroll_pos[1]
            en.rect = en.image.get_rect(topleft=en.pos)
        self.scroll_pos = scroller.current_scroll_offset()

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

    def __iter__(self):
        return iter(self.entities)


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
                if self.hovered_entity == en:
                    surf.blit(tower_window_active, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))
            else:
                surf.blit(tower_window_common, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))
                if self.hovered_entity == en:
                    surf.blit(tower_window_active, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))

            # if hasattr(en, "rarity"):
            #     if self.hovered_entity == en:
            #         if en.rarity == "common":
            #             self.repaint_to_default()
            #         if en.rarity == "legendary":
            #             self.repaint_to_legendary()
            #         if en.rarity == "spell":
            #             self.repaint_to_spell()
            #
            if en in self.remember_entities:
                surf.blit(ok, (en.rect.x - offset_pos[0], en.rect.y - offset_pos[1]))

    def go_animation(self):
        for en in self.entities:
            if en == self.hovered_entity:
                if en.name in towers_attack or en.name in enemies_attack:
                    en.state = "attack"
                else:
                    en.state = "wait"
            else:
                if isinstance(en, Tower):
                    en.state = "wait"
                if isinstance(en, Enemy):
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
                not_received_towers.remove(tower_name)

    def clear_rewards(self):
        for reward in self.entities:
            reward.kill()
        self.entities.clear()
        self.rewards.clear()

    def entity_create(self, columns, indent=30):
        for i, tower_name in enumerate(self.rewards):
            indent_x = (640 - (columns * 128)) // (columns + 1)
            column = (i % columns)
            entity = Tower(tower_name, (indent_x + (column * (128 + indent_x)) + 480, indent + 250))
            if hasattr(entity, "blackik"):
                entity.blackik.kill()
            for b in buffs_group:
                b.kill()
            self.add(entity)

    def custom_draw(self, surf, offset_pos=(0, 0)):
        for tower in self.entities:
            tower.rect = tower.image.get_rect(topleft=(tower.pos[0] + offset_pos[0], tower.pos[1] + offset_pos[1]))
            surf.blit(tower.image, (tower.rect.x - offset_pos[0], tower.rect.y - offset_pos[1]))
            if hasattr(tower, "rarity"):
                if tower.rarity == "legendary":
                    surf.blit(tower_window_legendary, (tower.rect.x - offset_pos[0], tower.rect.y - offset_pos[1]))
                if tower.rarity == "common":
                    surf.blit(tower_window_common, (tower.rect.x - offset_pos[0], tower.rect.y - offset_pos[1]))
                if tower.rarity == "spell":
                    surf.blit(tower_window_spell, (tower.rect.x - offset_pos[0], tower.rect.y - offset_pos[1]))
            if self.hovered_entity == tower:
                surf.blit(tower_window_active, (tower.rect.x - offset_pos[0], tower.rect.y - offset_pos[1]))

    def go_animation(self):
        for tower in self.entities:
            tower.animation()


class GlobalMap:
    def __init__(self):
        self.map_size = Rect((66, 66), (1280, 768))
        self.on_map = False
        self.pushed = False
        self.next_hero_pos = self.last_hero_pos = self.hero_pos = (0, 0)
        self.tiles = {}
        self.chest = None
        self.event = None
        self.smokes_pos = []
        self.where_is_smoke()

    def add(self, tile):
        if tile.id not in self.tiles:
            self.tiles[tile.id] = tile

    @staticmethod
    def build_tiles(default=False):

        GlobalMapTile((8, 4), event=Event(lost_in_forest_event, on_map_image="None"))
        GlobalMapTile((8, 5), event=Event(lost_in_forest_event, on_map_image="None"))
        GlobalMapTile((8, 6), event=Event(lost_in_forest_event, on_map_image="None"))
        GlobalMapTile((8, 7), event=Event(lost_in_forest_event, on_map_image="None"))
        GlobalMapTile((9, 4), event=Event(lost_in_forest_event, on_map_image="None"))
        GlobalMapTile((10, 4), event=Event(lost_in_forest_event, on_map_image="None"))
        GlobalMapTile((10, 5), event=Event(lost_in_forest_event, on_map_image="None"))
        GlobalMapTile((10, 6), event=Event(lost_in_forest_event, on_map_image="None"))
        GlobalMapTile((11, 7), event=Event(lost_in_forest_event, on_map_image="None"))
        GlobalMapTile((12, 12), cant_step=True)

        GlobalMapTile((13, 8), event=Event(village_event, bg_image="hello_game_event"))

        GlobalMapTile((9, 6), level_meta={
                                "level_id": (9, 6),
                                "level_time": 6750,
                                "time_to_spawn": 1500,
                                "start_money": 20,
                                "waves": level_waves["1"],
                                "allowed_enemies": level_allowed_enemies["1"],
                                "allowed_cords": (448,),
                                # "blocked_slots": (),
                                "level_image": "2",
                                # "action_after_complete": None
                            })

        if default:
            enemy_levels.clear()
            enemy_levels.append((9, 6))
            for i in range(41):         # тут создавалось 1025 объектов уровня в 1 тик и игра не отвечала +-5 секунд)))
                for j in range(25):
                    enemy_tile_ = choice([0, 0, 0, 1])   # 25%
                    if enemy_tile_ == 1:
                        level_meta = choice(level_meta_pool)
                        level_meta.update({"level_id": (i, j)})
                        GlobalMapTile((i, j), level_meta=level_meta.copy())
                        enemy_levels.append((i, j))
                    else:
                        GlobalMapTile((i, j))
            save_data()

        if not default:
            for i in range(41):
                for j in range(25):
                    if (i, j) in enemy_levels:
                        level_meta = choice(level_meta_pool)
                        level_meta.update({"level_id": (i, j)})
                        GlobalMapTile((i, j), level_meta=level_meta.copy())
                    else:
                        GlobalMapTile((i, j))

    @staticmethod
    def is_level_available(level_id):
        for i in range(2):
            for j in range(2):
                if level_id[0] >= 0 and level_id[1] >= 0:
                    if ((level_id[0] + i, level_id[1] + j) in passed_levels
                            or ((level_id[0] - i, level_id[1] - j) in passed_levels)
                            or ((level_id[0] + i, level_id[1] - j) in passed_levels)
                            or ((level_id[0] - i, level_id[1] + j) in passed_levels)) \
                            and (i != j or i == j == 0):
                        return True
        return False

    def actions(self):
        global game_state, last_game_state, event_stage

        def go_level():
            global last_game_state, game_state, level
            level = Level(**self.tiles[self.hero_pos].level_meta)   # тут мегафикс
            scroller.remembered_scroll_offsets["global_map"] = scroller.current_scroll_offset()
            scroller.scroll_offset_y = 0
            level.refresh()
            last_game_state = game_state
            game_state = "tower_select"

        if self.on_click() and self.on_map:
            new_pos = (mouse_pos[0] - 66 - scroller.scroll_offset_x) // 128, (mouse_pos[1] - 66 - scroller.scroll_offset_y) // 128
            if self.is_level_available(new_pos):
                self.last_hero_pos = self.hero_pos
                self.hero_pos = new_pos
                scroller.set_target_scroll_offset(((self.hero_pos[0] + 1) * -128 + 640 + 64, (self.hero_pos[1] + 1) * -128 + 384 + 64))

            if self.hero_pos in self.tiles:
                global_level = self.tiles[self.hero_pos]
                if global_level.level_meta:
                    if self.is_level_available(self.hero_pos) and global_level.id not in passed_levels:
                        go_level()

                if global_level.chest:
                    if self.is_level_available(self.hero_pos):
                        if not self.tiles[self.hero_pos].chest.open:
                            self.chest = self.tiles[self.hero_pos].chest
                            self.chest.opening()

                if global_level.event:
                    if self.is_level_available(self.hero_pos):
                        self.event = global_level.event
                        last_game_state = game_state
                        event_stage = 1
                        self.event.do()

            if self.hero_pos in self.tiles:
                if (not self.tiles[self.hero_pos].level_meta) and (not self.tiles[self.hero_pos].chest) and (not self.tiles[self.hero_pos].event):
                    if self.tiles[self.hero_pos].id not in passed_levels:
                        self.level_completed(self.tiles[self.hero_pos].id)

    def focus_on_hero(self):
        scroller.set_scroll_offset(((self.next_hero_pos[0] + 1) * -128 + 640 + 64, (self.next_hero_pos[1] + 1) * -128 + 384 + 64))  # камера улетает на нажатый объект
        scroller.set_target_scroll_offset(((self.hero_pos[0] + 1) * -128 + 640 + 64, (self.hero_pos[1] + 1) * -128 + 384 + 64))     # затем плавно возвращается на чела

    def where_is_smoke(self):
        self.smokes_pos = []
        for i in range(41):
            for j in range(25):
                if not self.is_level_available((i, j)):
                    self.smokes_pos.append((i, j))

    def render_overlay(self):
        for smoke_pos in self.smokes_pos:
            if -128 <= 66 + smoke_pos[0] * 128 + scroller.scroll_offset_x <= 1408 and -128 <= 66 + smoke_pos[1] * 128 + scroller.scroll_offset_y <= 896:
                screen.blit(smoke, (66 + smoke_pos[0] * 128 + scroller.scroll_offset_x, 66 + smoke_pos[1] * 128 + scroller.scroll_offset_y))

        for pos, global_tile in self.tiles.items():
            if global_tile.chest and self.is_level_available(pos):
                screen.blit(global_tile.chest.image, (66 + pos[0] * 128 + scroller.scroll_offset_x, 66 + pos[1] * 128 + scroller.scroll_offset_y))
            if global_tile.event and self.is_level_available(pos):
                if global_tile.event.image is not None:
                    screen.blit(global_tile.event.image, (66 + pos[0] * 128 + scroller.scroll_offset_x, 66 + pos[1] * 128 + scroller.scroll_offset_y))
            if global_tile.level_meta and self.is_level_available(pos) and pos not in passed_levels:
                screen.blit(enemy_tile, (66 + pos[0] * 128 + scroller.scroll_offset_x, 66 + pos[1] * 128 + scroller.scroll_offset_y))

        screen.blit(gg_on_map, (66 + self.hero_pos[0] * 128 + scroller.scroll_offset_x, 66 + self.hero_pos[1] * 128 + scroller.scroll_offset_y))
        screen.blit(global_map_overlay, (0, 0))

    def on_click(self) -> bool:
        if mouse.get_pressed()[0] == 1 and not self.pushed:
            self.pushed = True
        if mouse.get_pressed()[0] == 0 and self.pushed:
            self.pushed = False
            return True
        return False

    def level_completed(self, level_id, detect_smoke=True):
        if level_id not in passed_levels:
            passed_levels.append(level_id)
        if detect_smoke:
            self.where_is_smoke()

    def refresh(self):
        for level_ in self.tiles.values():
            if level_.chest:
                level_.chest.refresh()
        self.where_is_smoke()
        self.hero_pos = (9, 5)
        scroller.remembered_scroll_offsets["global_map"] = (-578, -318)

    def update(self):
        if self.map_size.collidepoint(mouse_pos):
            self.on_map = True
        else:
            self.on_map = False


class TowerUpgradesGroup(BasePreviewGroup):
    def __init__(self):
        super().__init__(UpgradeTowerButton)

    def custom_draw(self, surf, offset_pos=(0, 0)):
        for upgrade in filter(self.filter_by_turn, self.entities):
            upgrade.rect = upgrade.image.get_rect(topleft=(upgrade.pos[0] + offset_pos[0], upgrade.pos[1] + offset_pos[1]))
            surf.blit(upgrade.image, (upgrade.rect.x - offset_pos[0], upgrade.rect.y - offset_pos[1]))

            if self.pushed_entity == upgrade:
                surf.blit(upgrade_tower_select, (upgrade.rect.x - offset_pos[0], upgrade.rect.y - offset_pos[1]))
            if self.hovered_entity == upgrade:
                upgrade.repaint_to_hovered()
            else:
                upgrade.repaint_to_default()

            if upgrade.number in upgrades[preview_group.pushed_entity.name] and preview_group.pushed_entity.upgrade_level == upgrade.number:
                surf.blit(current_tower_upgrade, (upgrade.rect.x - offset_pos[0], upgrade.rect.y - offset_pos[1]))

            if preview_group.turn == Tower:
                if upgrade.number in upgrades[preview_group.pushed_entity.name]:
                    upgrade.set_active(True)
                else:
                    upgrade.set_active(False)

    @staticmethod
    def possible_upgrade_path():
        last_update = str(int(tower_upgrades_group.pushed_entity.number[0]) - 1) + tower_upgrades_group.pushed_entity.number[1]
        if last_update in upgrades[preview_group.pushed_entity.name] or last_update[0] == "1":
            return True
        return False


class SlotsGroup(BasePreviewGroup):
    def __init__(self, slots_rarity: dict):
        super().__init__(Slot)
        self.slots_rarity = slots_rarity
        self.default_slots_rarity = self.slots_rarity.copy()

    def clear_units(self):
        select_towers_preview_group.remember_entities_empty()
        self.slots_rarity = self.default_slots_rarity.copy()
        for slot_ in self:
            if slot_.unit_inside:
                slot_.remove_unit()

    def random_add_to_slots(self):
        def count_empty_slots():
            nonlocal common_slots, spell_slots
            common_slots = self.slots_rarity["common"]
            spell_slots = self.slots_rarity["spell"]
            return common_slots + spell_slots

        common_slots = 0
        spell_slots = 0
        common_towers = []
        spell_towers = []

        if count_empty_slots() - len(level.blocked_slots) == 0:
            self.clear_units()
            count_empty_slots()

        for tower in select_towers_preview_group.entities:
            if tower not in select_towers_preview_group.remember_entities and tower.name in received_towers:
                if tower.rarity == "common":
                    common_towers.append(tower)
                if tower.rarity == "spell":
                    spell_towers.append(tower)

        for i in range(common_slots):
            new_tower = choice(common_towers)
            common_towers.remove(new_tower)
            self.add_to_slots(new_tower)
        for i in range(spell_slots):
            new_tower = choice(spell_towers)
            spell_towers.remove(new_tower)
            self.add_to_slots(new_tower)

    def add_to_slots(self, tower):
        def directly_add():     # непосредственно добавление
            slot_.add_unit(tower)
            tower.in_slot = True
            select_towers_preview_group.remember_entities.append(tower)

        if len(select_towers_preview_group.remember_entities) <= 6 - len(level.blocked_slots) or tower.in_slot:
            if not tower.in_slot:
                for slot_ in sorted(self.entities, key=lambda s: s.pos[1]):
                    if not slot_.unit_inside:
                        if tower.rarity in self.slots_rarity and self.slots_rarity[tower.rarity] > 0:
                            if not slot_.blocked:
                                self.slots_rarity[tower.rarity] -= 1
                                slot_.allowed_rarity = tower.rarity
                                directly_add()
                                return True

            elif tower.in_slot:
                for slot_ in self.entities:
                    if slot_.unit_inside:
                        if slot_.unit_inside.name == tower.name:
                            slot_.remove_unit()
                            self.slots_rarity[slot_.allowed_rarity] += 1
                            tower.in_slot = False
                            select_towers_preview_group.remember_entities.remove(tower)
                            return True
            return False
        else:
            Alert("Закончились свободные слоты", (345, 760), 75)

    @staticmethod
    def sort_by_layer(slot_):
        if slot_.unit_inside:
            return slot_.unit_inside.render_layer
        return 0

    def custom_draw(self, surf):
        for slot_ in self.entities:
            surf.blit(slot_.image, slot_.rect)

            if slot_.unit_inside:

                img = font30.render(str(slot_.unit_cost), True, (255, 255, 255))
                if slot_.unit_cost > 9:
                    surf.blit(img, img.get_rect(topleft=(slot_.pos[0] + 14, slot_.pos[1] + 4)))
                else:
                    surf.blit(img, img.get_rect(topleft=(slot_.pos[0] + 21, slot_.pos[1] + 4)))

                additional_pixels = 0
                if 0 <= slot_.kd_time < 10:     # формулу сделать нельзя
                    additional_pixels = 21
                elif 10 <= slot_.kd_time < 100:
                    additional_pixels = 14
                elif 100 <= slot_.kd_time < 1000:
                    additional_pixels = 5
                elif 1000 <= slot_.kd_time < 10000:
                    additional_pixels = -5
                if additional_pixels != 0:
                    surf.blit(font30.render(str(slot_.kd_time), True, (255, 255, 255)), (slot_.pos[0] + additional_pixels, slot_.pos[1] + 50))

        for slot_ in sorted(self.entities, key=self.sort_by_layer):
            if slot_.unit_inside:
                surf.blit(slot_.unit_inside.image, slot_.unit_inside.rect)

        if game_state == "tower_select":
            screen.blit(font60.render(str(self.slots_rarity["common"]), True, (61, 243, 69)), (30, 820))
            screen.blit(font60.render(str(self.slots_rarity["spell"]), True, (70, 109, 249)), (60, 820))
            # screen.blit(font60.render(str(self.slots_rarity["legendary/common"]), True, (202, 239, 28)), (90, 820))
            # screen.blit(font60.render(str(self.slots_rarity["spell/common"]), True, (28, 227, 239)), (120, 820))

    def update(self):
        for slot_ in self.entities:
            slot_.update()


class TextFieldsGroup:
    def __init__(self):
        self.entities = []

    def add(self, text_field):
        if text_field not in self.entities:
            self.entities.append(text_field)

    def clear(self):
        self.entities.clear()

    def finish_text_animation(self):
        for entity in self.entities:
            entity.text = entity.default_text
            entity.not_shown_text = ""

    def update(self) -> bool:
        anim_over = []
        for entity in self.entities:
            entity.render_text(screen)
            anim_over.append(entity.update())

        if all(anim_over):
            return True
        return False


class GlobalMapTile:
    def __init__(self, level_id: tuple, level_meta=None, chest=None, event=None, cant_step=False):    # noqa
        self.id = level_id
        self.level_meta = level_meta
        self.chest = chest
        self.event = event
        if cant_step:
            self.event = Event(cant_step_event, on_map_image="None", bg_image="None", has_event_stages=False)
        global_map.add(self)


class Level:
    def __init__(self, level_id: tuple,
                 level_time: int,
                 time_to_spawn: int,
                 start_money: int,
                 waves: dict,
                 allowed_enemies: tuple,
                 allowed_cords=(192, 320, 448, 576, 704),
                 blocked_slots=(),
                 level_image="default",
                 action_after_complete=None):
        if level_image == "default":
            self.image = image.load(f"images/maps/levels/map{level_id}.png").convert_alpha()
        else:
            self.image = image.load(f"images/maps/levels/map{level_image}.png").convert_alpha()
        self.current_level = level_id
        self.money = self.start_money = start_money
        self.state = "not_run"
        self.level_time = self.start_level_time = level_time
        self.start_time_to_spawn = self.time_to_spawn = time_to_spawn
        self.rate_of_increase_random_points = 1
        self.random_points_to_spawn = 0
        self.cheat = True
        self.rect_visible = False
        self.no_death_animation = True
        self.kill_enemy_on_click = False
        self.waves = waves
        self.allowed_enemies = allowed_enemies
        self.allowed_cords = allowed_cords
        self.blocked_slots = blocked_slots

        self.x = 384     # для полоски уровня
        self.y = 110
        self.w = 1151
        self.h = 40

        self.action_after_complete = action_after_complete

    def draw_level_time(self):      # надо бы написать по-понятней
        ratio = self.level_time / self.start_level_time
        draw.rect(screen, (233, 126, 72), (self.x, self.y, self.w, self.h))
        draw.rect(screen, (55, 127, 236), (self.x, self.y, self.w * ratio, self.h))
        draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h), 4)
        for dirty_wave in self.waves:
            wave = dirty_wave.split("+")[0]
            wave_description = wave[:1]
            wave_time = int(wave[1:])
            mark_ratio = wave_time / self.start_level_time
            if wave_description == "v":
                screen.blit(amogus, (self.x + int(mark_ratio * self.w), self.y - 30))

    def wave_spawn_enemies(self, waves_points):
        # waves_points = self.waves[wave_description + str(wave_time)]
        enemy_x_cord = 1600
        while waves_points > 0:
            enemy_name = choice(self.allowed_enemies)
            if enemy_name:
                if waves_points - enemy_costs[enemy_name] >= 0:
                    enemy_y_cord = choice(self.allowed_cords)
                    Enemy(enemy_name, (enemy_x_cord, enemy_y_cord))
                    waves_points -= enemy_costs[enemy_name]
                    enemy_x_cord += randint(10, 30)

    def random_spawn_enemies(self):
        self.random_points_to_spawn += self.rate_of_increase_random_points
        enemy_name = choice(self.allowed_enemies)
        if enemy_name:
            if self.random_points_to_spawn > enemy_costs[enemy_name]:
                self.random_points_to_spawn -= enemy_costs[enemy_name]
                enemy_y_cord = choice(self.allowed_cords)
                Enemy(enemy_name, (1600, enemy_y_cord))

    @staticmethod
    def clear(*dont_clear_groups):
        if buttons_group not in dont_clear_groups:
            for button_ in buttons_group:
                button_.ok = False

        if slots_group not in dont_clear_groups:
            select_towers_preview_group.remember_entities_empty()
            slots_group.slots_rarity = slots_group.default_slots_rarity.copy()
            for s in slots_group:
                if s.unit_inside:
                    s.remove_unit()
        else:
            for s in slots_group:
                if s.unit_inside:
                    s.kd_time = -1

        for sprite_ in all_sprites_group:
            if dont_clear_groups:
                for group in dont_clear_groups:
                    if sprite_ not in group and sprite_ not in clouds_group and hasattr(sprite_, "name") and sprite_.name != "shovel":
                        sprite_.kill()
            else:
                if sprite_ not in clouds_group:
                    if hasattr(sprite_, "name"):
                        if sprite_.name != "shovel" and sprite_.name != "krest":
                            sprite_.kill()
                    else:
                        sprite_.kill()

    def refresh(self, *dont_clear_groups):
        self.money = self.start_money
        self.level_time = self.start_level_time
        self.time_to_spawn = self.start_time_to_spawn
        self.state = "not_run"
        self.clear(*dont_clear_groups)

        for slot_ in slots_group:
            if slot_.pos[1] in self.blocked_slots:
                slot_.blocked = True
            else:
                slot_.blocked = False

    def give_reward(self):
        global passed_levels

        random_coin = choice([c for c in your_coins.keys()])
        your_coins[random_coin] += 5

        preview_group.refresh(3)
        if self.current_level not in passed_levels:
            passed_levels.append(self.current_level)

        global_map.where_is_smoke()
        save_data()

    def update(self):
        all_sprites_group.update()
        slots_group.update()
        for dirty_wave in self.waves:

            wave = dirty_wave.split("+")[0]
            rate_of_increase_random_points = int(dirty_wave.split("+")[1])
            wave_time = int(wave[1:])
            wave_description = wave[:1]
            if self.level_time == wave_time:
                self.rate_of_increase_random_points = rate_of_increase_random_points
                self.wave_spawn_enemies(self.waves[wave_description + str(wave_time) + "+" + str(rate_of_increase_random_points)])
                # if wave_description == "a":
                #     Alert("БомБом", (750, 450), 225)
        if self.state == "not_run":
            self.state = "run"
            row1 = False  # ну блин сорян
            row2 = False
            row3 = False
            row4 = False
            row5 = False
            for i in self.allowed_cords:
                if i == 192:
                    row1 = True
                elif i == 320:
                    row2 = True
                elif i == 448:
                    row3 = True
                elif i == 576:
                    row4 = True
                elif i == 704:
                    row5 = True
            if not row1:
                for i in range(9):
                    Tower('krest', (384 + (i * 128), 192))
            if not row2:
                for i in range(9):
                    Tower('krest', (384 + (i * 128), 320))
            if not row3:
                for i in range(9):
                    Tower('krest', (384 + (i * 128), 448))
            if not row4:
                for i in range(9):
                    Tower('krest', (384 + (i * 128), 576))
            if not row5:
                for i in range(9):
                    Tower('krest', (384 + (i * 128), 704))
        if not self.cheat:
            if self.level_time > 0:
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
    def __init__(self, parent_number: tuple or str, rewards: dict, bg_image="default", action_after_open=None):
        self.rewards = rewards      # башни/коины
        if bg_image != "default":
            self.bg_image = image.load(f"images/maps/global_map/chests/bg_images/{bg_image}.png").convert_alpha()
        else:
            self.bg_image = image.load(f"images/maps/global_map/chests/bg_images/bg_image_{parent_number}.png").convert_alpha()

        if parent_number not in passed_levels:
            self.image = image.load("images/maps/global_map/chests/chest.png")
            self.open = False
        else:
            self.open = True
            self.image = image.load("images/maps/global_map/chests/chest_open.png")

        self.action_after_open = action_after_open

    def opening(self):
        global game_state
        self.open = True
        self.image = image.load("images/maps/global_map/chests/chest_open.png")
        if global_map.hero_pos not in passed_levels:
            passed_levels.append(global_map.hero_pos)
        game_state = "reward_first_stage"

    def refresh(self):
        self.open = False
        self.image = image.load("images/maps/global_map/chests/chest.png")


class Event:
    def __init__(self, action, event_name="default", on_map_image="default", bg_image="default", action_args=None, has_event_stages=True):   # , image_=None
        self.action = action
        self.has_event_stages = has_event_stages

        if event_name != "default":
            self.name = event_name
        else:
            self.name = f"{action.__name__}"

        if on_map_image == "None":
            self.image = None
        elif on_map_image == "default":
            self.image = image.load(f"images/maps/global_map/events/{action.__name__}.png").convert_alpha()
        else:
            self.image = image.load(f"images/maps/global_map/events/{on_map_image}.png").convert_alpha()

        if bg_image == "None":
            self.bg_image = None
        elif bg_image == "default":
            self.bg_image = image.load(f"images/maps/global_map/events/bg_images/{action.__name__}.png").convert_alpha()
        else:
            self.bg_image = image.load(f"images/maps/global_map/events/bg_images/{bg_image}.png").convert_alpha()

        self.action_args = action_args

    def do(self):
        global game_state, last_game_state
        global_map.event = self
        game_state = "event"
        if self.action_args:
            self.action(self.action_args)
        else:
            self.action()

    def finish_event(self, next_game_state="global_map", can_repeat=False):
        global game_state, last_game_state, event_stage
        if self.name not in completed_events:
            if not can_repeat:
                completed_events.append(self.name)
            last_game_state = game_state
            game_state = next_game_state
            event_stage = 1

    def __repr__(self):
        return str(self.action)


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
        self.alive = True
        self.have_barrier = False
        self.barrier = None
        self.onyx_barrier = None
        self.stack = False
        self.free_placement = False
        self.damaged = False
        self.stunned = False
        self.banished = False
        self.vulnerabled = 0
        self.unvulnerable = 0
        self.vulnerables_and_resists = {}  # dict()  # 'damage_type' : resist%

        self.time_indicator = 1
        self.anim_tasks = []
        self.anim_count = 0
        self.last_anim_frame = -1
        self.anim_duration = 15     # сколько кадров будет оставаться 1 спрайт
        self.state = "wait"         # потом будет "attack", "death" и какие придумаете

        self.pushed = False
        self.in_slot = False

        # СТАТЫ начало
        if self.name == 'fire_mag':
            self.hp = self.max_hp = 20
            self.atk = 10
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.damage_type = 'fire'
            self.rarity = "common"
            self.vulnerables_and_resists['fire'] = -50
            if self.upgrade_level == "2a" or self.upgrade_level == '3a':  # циферки поменять мб
                self.atk_big = self.atk*2  #20
                self.attack_count = 0
                self.fire_form = False
                self.fire_form_duration = self.basic_fire_form_duration = 6
                self.fire_form_cooldown = self.basic_fire_form_cooldown = 6
            if self.upgrade_level == "2b" or self.upgrade_level == '3b':
                self.atk_dot = self.atk/10  #1  # dot = damage_over_time    # типа он поджогом дамажит 5 сек по 1 урону и в итоге у него от каждой тычки дамаг в 1,5 раза увеличивается но растянуто

        if self.name == 'boomchick':
            self.hp = self.max_hp = 20
            self.atk = 10  # типа по кому попадёт получит 20 а остальные по 10
            self.bullet_speed_x = 4
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.damage_type = 'fire'
            self.rarity = "common"
            if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                self.attack_count = 0

        if self.name == 'holodilnik':
            self.hp = self.max_hp = 20
            self.atk = 10  # типа по кому попадёт получит 10 а остальные по 30
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 240
            self.damage_type = 'ice'  # а потом фаер
            self.rarity = "common"

        if self.name == 'kopitel':
            self.hp = self.max_hp = 20
            self.atk = 20
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_spawn_something_cooldown = self.spawn_something_cooldown = 120
            self.spawned_things = []
            self.basic_attack_cooldown = self.attack_cooldown = 120
            self.damage_type = 'light'
            self.nakopleno = 0
            self.max_nakopit = 7
            self.rarity = "common"
            self.vulnerables_and_resists['dark'] = -25
            if self.upgrade_level == "2a" or self.upgrade_level == '3a':
                self.atk_big = self.atk*3  #60

        if self.name == 'elf':
            self.hp = self.max_hp = 20
            self.atk = 5
            self.atk_dot = self.atk/5  # 1
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.damage_type = 'poison'
            self.rarity = "common"

        if self.name == 'uvelir':
            self.hp = self.max_hp = 20
            self.atk = 1
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_spawn_something_cooldown = self.spawn_something_cooldown = 120
            # self.spawned_things = []
            self.gems = ['stone', 'stone', 'stone', 'emerald', 'emerald', 'amethyst', 'amethyst', 'onyx', 'onyx', 'opal', 'opal', 'nephrite', 'nephrite', 'obsidian', 'obsidian', 'sapphire', 'ruby', 'diamond'] * 3
            self.basic_gems = self.gems.copy()
            self.gem = ''
            self.basic_attack_cooldown = self.attack_cooldown = 120
            self.damage_type = ''
            # self.nakopleno = 0  # думаю в прокачку закинуть чтобы несколько камней мог накапливать
            # self.max_nakopit = 3
            self.rarity = "common"

        if self.name == 'thunder':
            self.hp = self.max_hp = 25
            self.atk = 10
            self.bullet_speed_x = 7
            self.bullet_speed_y = 3
            self.attack_cooldown = self.basic_attack_cooldown = 180
            self.target_phase = None
            self.damage_type = 'bludgeoning'  # дробящий
            self.rarity = "common"
            if self.upgrade_level == '2a':
                self.hp = self.max_hp = 32.5
            elif self.upgrade_level == '3a':
                self.hp = self.max_hp = 50
                self.kamen_hp = 500
            elif self.upgrade_level == '2b' or self.upgrade_level == '3b':
                self.golem_cooldown = self.basic_golem_cooldown = 900

        if self.name == 'thunder_kamen':
            self.upgrade_level = upgrades["thunder"][-1]
            self.hp = self.max_hp = 250
            self.vulnerables_and_resists['poison'] = -100
            self.vulnerables_and_resists['piercing'] = -25
            self.vulnerables_and_resists['slashing'] = -25
            self.vulnerables_and_resists['bludgeoning'] = 50
            self.rarity = "common"
            if self.upgrade_level == '2a':
                self.hp = self.max_hp = 325
            elif self.upgrade_level == '3a':
                self.hp = self.max_hp = 500
                self.revive_cooldown = 900

        if self.name == 'gribnik':
            self.hp = self.max_hp = 30  # ну а почему бы и нет
            self.atk = 15
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 180
            self.target_phase = None
            self.damage_type = 'poison'
            self.rarity = "common"

        for i in range(3):
            if self.name == 'grib' + str(i + 1):
                self.upgrade_level = upgrades["gribnik"][-1]
                self.hp = self.max_hp = 30 * (i + 1)
                self.rarity = "common"
                if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                    self.atk = 1 * (i + 1)
                    self.damage_type = 'poison'
                    if self.upgrade_level == '2a':
                        self.gas_attack_cooldown = 30
                        self.gas_duration = 120 * (i + 1)
                    elif self.upgrade_level == '3a':
                        self.gas_attack_cooldown = 15
                        self.gas_duration = 240 * (i + 1)
                if self.upgrade_level == '2b' or self.upgrade_level == '3b':
                    self.damage_type = 'fire'
                    self.hp = self.max_hp = 5 * (i + 1)
                    if self.upgrade_level == '2b':
                        self.atk = 5 * ((i + 1)**2)
                    elif self.upgrade_level == '3b':
                        self.atk = 20 * ((i + 1)**2)

        if self.name == 'ded_moroz':
            self.hp = self.max_hp = 20
            self.atk = 5
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.damage_type = 'ice'
            self.rarity = "common"
            if self.upgrade_level == "2a" or self.upgrade_level == '3a':
                self.attack_count = 0
                self.ice_form = False
                self.ice_form_duration = self.basic_ice_form_duration = 4
                self.ice_form_cooldown = self.basic_ice_form_cooldown = 4

        if self.name == 'chistiy':
            self.hp = self.max_hp = 20
            self.atk = 1
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 180
            self.rect_chistiy = Rect(self.rect.x-128, self.rect.y-128, 384, 384)
            self.damage_type = 'clean'
            self.rarity = "common"

        if self.name == 'sliz':
            self.hp = self.max_hp = 20
            self.sliz_hp = 50
            self.atk = 0
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 300
            self.damage_type = 'water'
            self.vulnerables_and_resists['piercing'] = -75
            self.vulnerables_and_resists['slashing'] = -75
            self.vulnerables_and_resists['bludgeoning'] = -75
            self.rarity = "common"

        if self.name == 'zeus':
            self.hp = self.max_hp = 5
            self.atk = 15
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = self.attack_cooldown = 120     # 150
            self.damage_type = 'light'
            self.rarity = "common"

        if self.name == 'yascerica':
            self.hp = self.max_hp = 20
            self.atk = 0
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 900  #1125
            if self.upgrade_level == '2a':
                self.basic_attack_cooldown = 720
            elif self.upgrade_level == '3a':
                self.basic_attack_cooldown = 600
            self.attack_cooldown = self.basic_attack_cooldown // 2
            self.damage_type = ''
            if self.upgrade_level == '2b' or self.upgrade_level == '3b':
                if self.upgrade_level == '2b':
                    self.bullet_stomach_capacity = 2
                if self.upgrade_level == '3b':
                    self.bullet_stomach_capacity = 3
            self.blackik = Bullet("blackik", self.rect.centerx - 26, self.rect.centery, self.damage_type, 0, self.bullet_speed_x, self.bullet_speed_y, 'yas', self)
            self.blackik.remove(bullets_group)
            self.rarity = "common"

        if self.name == 'krovnyak':
            self.hp = self.max_hp = 20
            self.atk = 10
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.not_damaged_time = 0
            self.damage_type = 'water'
            self.krovs = sprite.Group()
            Bullet("krov_bul", self.rect.centerx - 21, self.rect.centery + 48, self.damage_type, 0, self.bullet_speed_x, self.bullet_speed_y, 'krov_bul', self).remove(bullets_group)
            Bullet("krov_bul", self.rect.centerx - 42, self.rect.centery + 48, self.damage_type, 0, self.bullet_speed_x, self.bullet_speed_y, 'krov_bul', self).remove(bullets_group)
            self.vulnerables_and_resists['piercing'] = -75
            self.vulnerables_and_resists['slashing'] = -75
            self.vulnerables_and_resists['bludgeoning'] = -75
            self.rarity = "common"

        if self.name == 'electric':
            self.hp = self.max_hp = 20
            self.atk = 3  # типо дальней атакой он наносит 45 урона в 1 цель за 4,5 секунды(3,5 сек кд и 1 сек он всё выпускает)
            self.atk2 = self.atk*15  #45  # а ближней он наносит 45 урона сплешом за 3,5 секунды
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 210
            self.attack_cooldown_burst = self.basic_attack_cooldown_burst = 4
            self.ammo = self.basic_ammo = 15
            self.target_phase = None
            self.bursting = False
            self.damage_type = 'electric'
            self.rarity = "common"

        if self.name == 'struyniy':  # пока что он слишком имба под баффом но мы что-нибудь придумаем. хотя мб нет
            self.hp = self.max_hp = 20
            self.atk = 2
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 900
            self.attack_cooldown_burst = self.basic_attack_cooldown_burst = 3
            self.ammo = self.basic_ammo = 28
            self.bursting = False
            self.damage_type = 'water'
            self.rarity = "common"
            if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                self.ammo = self.basic_ammo = 36 

        if self.name == 'dark_druid':
            self.hp = self.max_hp = 20
            self.atk = 5
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 1200
            self.attack_cooldown = self.basic_attack_cooldown
            self.ravens = 3
            self.ravens_dead = 5
            self.damage_type = 'dark'
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
            self.hp = self.max_hp = 20
            self.atk = 0
            self.bullet_speed_x = 1
            self.bullet_speed_y = 0
            self.basic_attack_cooldown = 300
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'parasitelniy':
            self.hp = self.max_hp = 250
            self.atk = 5
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.damage_type = 'piercing'
            self.have_parasite = sprite.Group()
            self.rarity = "common"

        if self.name == 'inquisitor':
            self.hp = self.max_hp = 20
            self.atk = 0
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.damage_type = 'light'
            self.have_parasite = sprite.Group()
            self.rarity = "common"
            self.vulnerables_and_resists['dark'] = -25

        if self.name == 'nekr':
            self.hp = self.max_hp = 20
            self.atk = 30  # я хз надо ли некру писать атк(атака сейчас нигде не используется, оставил чтобы не ломать справочник), можно сделать чтобы его призывники наследовали атаку, а можно и чтобы у них в ините она прописывалась, хз короч, потом решим
            self.attack_cooldown = self.basic_attack_cooldown = 600  # потом отбалансим. кстати можно его не через атаку сделать а через spawn_something, но это потом, пока что делаю через shoot
            self.creeps = sprite.Group()
            self.cr1 = None
            self.cr2 = None
            self.cr3 = None
            self.cr4 = None
            self.cr5 = None
            self.damage_type = ''
            self.rarity = "common"  # по резистам поговорить с мишей

        if self.name == 'spike':
            self.hp = self.max_hp = 1
            self.atk = 20
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.damage_type = 'piercing'  # колющий
            self.remove(towers_group)
            self.add(nekusaemie_group)
            self.rarity = "common"
            if self.upgrade_level == '2a':
                self.skolko_deneg_dast = 10
                self.dengi_cooldown = self.basic_dengi_cooldown = 3600
            elif self.upgrade_level == '3a':
                self.skolko_deneg_dast = 15
                self.dengi_cooldown = self.basic_dengi_cooldown = 2400
                self.dengi_cooldown_reducing = 40
            elif self.upgrade_level == '2b':
                self.slowed_group = sprite.Group()  # замедляет в 1.25 раз
            elif self.upgrade_level == '3b':
                self.great_rect = Rect(self.rect.x-128, self.rect.y-128, 384, 384)
                self.great_form = False
                self.slowed_group = sprite.Group()  # замедляет в 1.5 раз в центре всегда и в 1.25 раз по бокам в форме большого куста
                self.slowed_group2 = sprite.Group()
                self.great_form_cooldown = self.basic_great_form_cooldown = 20  # атак
                self.great_form_duration = self.basic_great_form_duration = 600  # циклов

        if self.name == 'pukish':
            self.hp = self.max_hp = 1
            self.atk = 20
            self.atk2 = self.atk/10  #2
            self.bullet_speed_x = 2
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 180
            self.attack_cooldown2 = self.basic_attack_cooldown2 = 15
            self.damage_type = 'poison'
            self.hiding = False
            self.remove(towers_group)
            self.add(nekusaemie_group)
            self.rarity = "common"

        if self.name == 'urag_anus':
            self.hp = self.max_hp = 70
            self.atk = 0
            self.uragan_duration = 540
            self.basic_attack_cooldown = 2340
            self.attack_cooldown = 300
            self.uragan = None
            self.rarity = "common"
            if self.upgrade_level == "2a":
                self.uragan_speed = 0.5
            elif self.upgrade_level == "3a":
                self.uragan_speed = 1
            elif self.upgrade_level == "2b":
                self.atk = 1.5
            elif self.upgrade_level == "3b":
                self.atk = 0.75  # это чтобы конечный урон от урагана не увеличился(а то там х2 увеличение урона)

        if self.name == 'drachun':
            self.hp = self.max_hp = 70
            self.atk = self.basic_atk = 30
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.damage_type = 'bludgeoning'
            self.rarity = "common"
            if self.upgrade_level == "2a" or self.upgrade_level == '3a':
                self.rage_duration = self.basic_rage_duration = 666 # так надо это не по рофлу это реально механика сломается если по другому сделать(вроде можно 661, но 666 круче)
                self.rage_cooldown = 0
                self.basic_rage_cooldown = 1200
                self.rage_amp = 2
                self.rage = False
                if self.upgrade_level == '3a':
                    self.rage_amp = 3
            if self.upgrade_level == "2b" or self.upgrade_level == '3b':
                if self.upgrade_level == "2b":
                    self.hp = self.max_hp = 1200
                else:
                    self.hp = self.max_hp = 2000
                    self.self_buff_level = 0
                    self.kill_time = 375

        if self.name == 'drachun_plavniy':
            self.hp = self.max_hp = 70
            self.atk = self.basic_atk = 30
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.damage_type = 'bludgeoning'
            self.rarity = "common"
            self.time_indicator *= 2

        if self.name == 'boomchick_plavniy':
            self.hp = self.max_hp = 70
            self.atk = self.basic_atk = 30
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.damage_type = 'bludgeoning'
            self.rarity = "common"
            self.time_indicator *= 2

        if self.name == 'kirka':
            self.hp = self.max_hp = 50
            self.atk = 50
            self.damage_multiplier = 10  # х10 урон по армированным
            self.attack_cooldown = self.basic_attack_cooldown = 300
            self.damage_type = 'piercing'
            self.rarity = "common"

        if self.name == 'knight_on_horse':       # нука кусни нет, потому что он подгружает картинки по кд
            self.knight_hp = 150                # nuka_kusni
            self.horse_hp = 150  # уменьшить отхилл рыцарю
            self.hp = self.max_hp = self.knight_hp + self.horse_hp
            self.atk = 20
            self.taran_atk = self.atk*20  #400
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.damage_type = 'piercing'  # у лошади надо bludgeoning
            self.rarity = "common"

        if self.name == "knight":
            self.hp = self.max_hp = 150
            self.atk = 20
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.damage_type = 'piercing'
            self.rarity = "common"

        if self.name == 'tolkan':
            self.hp = self.max_hp = 300
            self.atk = 50
            self.ottalkivanie_solo = self.push = 384
            self.ottalkivanie_ne_solo = 192
            self.za_towerom = False
            self.basic_attack_cooldown = 1200
            self.attack_cooldown = self.basic_attack_cooldown
            self.damage_type = 'bludgeoning'
            self.rarity = "common"

        if self.name == 'big_mechman':
            self.hp = self.max_hp = 70
            self.atk = 60
            self.kulak_time = 15
            self.attack_cooldown = self.basic_attack_cooldown = 300
            self.damage_type = 'slashing'  # рубящий
            self.rarity = "common"
            if self.upgrade_level == "2b":
                self.big_mech_cooldown = self.basic_big_mech_cooldown = 900
            elif self.upgrade_level == '3b':
                self.big_mech_cooldown = self.basic_big_mech_cooldown = 600

        if self.name == 'sekirshik':
            self.hp = self.max_hp = 70
            self.atk = 30  # максимум 180 при 16 врагах
            self.kulak_time = 15
            self.attack_cooldown = self.basic_attack_cooldown = 300
            self.damage_type = 'slashing'
            self.rarity = "common"
            if self.upgrade_level == "2b":
                self.spin_attack_cooldown = self.basic_spin_attack_cooldown = 900
            if self.upgrade_level == "3a":
                self.hp = self.max_hp = 200

        if self.name == 'prokach':  # статы фаермага чтобы справочник не сломался, переделаю его попозже
            self.hp = self.max_hp = 20
            self.atk = 30
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 180
            self.attack_areas = sprite.Group()
            self.mech_level = 0
            self.max_mech_level = 7
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'klonys':
            self.hp = self.max_hp = 20
            self.atk = self.basic_atk = 30
            self.attack_cooldown = self.basic_attack_cooldown = 420
            self.illusions = self.basic_illusions = 5
            self.damage_type = 'bludgeoning'
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
            self.hp = self.max_hp = 50
            self.atk = 150
            self.bullet_speed_x = 10
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 600
            self.damage_type = 'bludgeoning'
            self.stack = "gnome_cannon"
            self.rarity = "common"

        if self.name == 'gnome_cannon2':
            self.hp = self.max_hp = 250
            self.heal = 1
            self.atk = 150
            self.bullet_speed_x = 10
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 600
            self.self_healing_cooldown = self.basic_healing_cooldown = 60
            self.damage_type = 'bludgeoning'
            self.stack = "gnome_cannon"
            self.rarity = "common"

        if self.name == 'gnome_cannon3':
            self.hp = self.max_hp = 250
            self.heal = 1
            self.atk = 150
            self.bullet_speed_x = 10
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 300
            self.self_healing_cooldown = self.basic_healing_cooldown = 75
            self.damage_type = 'bludgeoning'
            self.stack = "gnome_cannon"
            self.rarity = "common"

        if self.name == 'gnome_flamethrower':
            self.hp = self.max_hp = 1
            self.atk = 0
            self.atk2 = 3   # баффающая башня не баффает скорость атаки огнемета, если надо будет сделаю чтобы баффала
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_cooldown2 = self.basic_attack_cooldown2 = 6
            self.damage_type = 'fire'
            self.remove(towers_group)
            self.add(nekusaemie_group)
            self.rarity = "common"

        if self.name == 'kokol':
            self.hp = self.max_hp = 20
            self.atk = 10
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.damage_type = 'physical'
            for i in range(0, 3, 2):
                self.buff_y = 1 + i * 128 - 128
                self.buff = Buff('kuklo', self.rect.x+1, self.rect.y + self.buff_y, self) # с обычным ректом и вычитанием из него не спавнится на крайней левой полосе
            self.rarity = "common"
            self.vulnerables_and_resists['fire'] = 25

        if self.name == 'kar_mag':
            self.hp = self.max_hp = 20
            self.atk = 20
            self.atkf = (self.atk/4)*3  #15
            self.bullet_speed_x = 0
            self.bullet_speed_y = 0
            self.basic_spawn_something_cooldown = self.spawn_something_cooldown = 120
            self.spawned_things = []
            self.basic_attack_cooldown = self.attack_cooldown = 120
            self.target_phase = None
            self.v_falange = 0
            #self.z_falange = 5
            self.damage_type = 'light'
            self.rarity = "common"

        if self.name == 'shabriri':
            self.hp = self.max_hp = 30
            self.atk = 5
            self.atk_big = 7.5
            self.bullet_speed_x = 6
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.spawn_something_cooldown = 0
            self.bezumie = 0
            self.creeps = sprite.Group()
            self.damage_type = 'fire'
            self.vulnerables_and_resists['fire'] = -10
            self.rarity = "common"

        if self.name == 'pulelom':
            self.hp = self.max_hp = 20
            self.atk = 0
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 180
            self.pulelomka_hp = 5
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'chorniy':
            self.hp = self.max_hp = 20
            self.atk = 0
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = 60
            self.basic_attack_cooldown = 600
            self.marks = sprite.Group()
            self.damage_type = 'dark'
            self.rarity = "common"

        if self.name == 'terpila':
            self.hp = self.max_hp = 750
            if self.upgrade_level == "2b" or self.upgrade_level == '3b' or self.upgrade_level == '3a':
                self.received_damage = 0
                self.max_received_damage = 100
            if self.upgrade_level == "2b":
                self.ottalkivanie_rect = Rect(self.rect.x+64, self.rect.y, 128, 128)
            elif self.upgrade_level == "3b":
                self.ottalkivanie_rect = Rect(self.rect.x+64, self.rect.y-128, 128, 384)
            elif self.upgrade_level == "2a":
                self.vulnerables_and_resists['piercing'] = -25
                self.vulnerables_and_resists['slashing'] = -25
                self.vulnerables_and_resists['bludgeoning'] = -25
            elif self.upgrade_level == '3a':
                self.vulnerables_and_resists['piercing'] = -50
                self.vulnerables_and_resists['slashing'] = -50
                self.vulnerables_and_resists['bludgeoning'] = -50
            self.rarity = "common"
        
        if self.name == 'kot':
            self.hp = self.max_hp = 150
            self.lives = 9
            self.chill_time = 0
            self.basic_chill_time = 600
            self.hiding = False
            self.rarity = "common"
            if self.upgrade_level == "2a":
                self.basic_chill_time = 300
            elif self.upgrade_level == "3a":
                self.basic_chill_time = 120
                self.slowed_group = sprite.Group()
            if self.upgrade_level == "2b" or self.upgrade_level == "3b":
                self.atk = self.basic_atk = 30
                self.attack_cooldown = self.basic_attack_cooldown = 300
                self.damage_type = 'slashing'

        if self.name == 'ares':
            self.hp = self.max_hp = 150
            self.atk = 25
            self.vpitano_damaged = 0
            self.contrudar = 0
            self.cooldown_contratack = 300
            self.time_contratack = 300
            self.damage_type = 'slashing'
            self.rarity = "common"

        if self.name == 'barrier_mag':
            self.hp = self.max_hp = 150
            self.barrier_hp = 300
            self.best_x = self
            self.basic_spawn_something_cooldown = 2700  # 3375
            self.spawn_something_cooldown = 0
            self.rarity = "common"

        if self.name == 'vozmezdik':
            self.hp = self.max_hp = 300
            self.basic_spawn_something_cooldown = self.spawn_something_cooldown = 600
            self.vremya_casta = self.basic_vremya_casta = 300
            self.col_vo_poglash = 0
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'priest':
            self.hp = self.max_hp = 20
            self.atk = 10
            self.attack_cooldown = self.basic_attack_cooldown = 180
            # self.healing = 100
            # self.healing_cooldown = self.basic_healing_cooldown = 180
            self.rarity = "common"
            self.vulnerables_and_resists['dark'] = -25

        if self.name == 'davalka':
            self.hp = self.max_hp = 20
            self.skolko_deneg_dast = 10
            self.basic_spawn_something_cooldown = self.spawn_something_cooldown = 1200
            self.rarity = "common"
            if self.upgrade_level == '2a':
                self.chance = self.basic_chance = 17 #%  хотел 20% но по ощущениям это слишком жирно
                self.multiplier = 3
            if self.upgrade_level == '3a':
                self.chance = self.basic_chance = 50 #%
                self.multiplier = 3
            elif self.upgrade_level == "2b":
                Buff("mana", self.rect.x + 128, self.rect.y, self)
            elif self.upgrade_level == "3b":
                Buff("mana", self.rect.x + 128, self.rect.y, self)  # впадлу формулу писать
                Buff("mana", self.rect.x - 128, self.rect.y, self)
                Buff("mana", self.rect.x, self.rect.y + 128, self)
                Buff("mana", self.rect.x, self.rect.y - 128, self)

        if self.name == 'matricayshon':
            self.hp = self.max_hp = 66
            for i in range(9):
                self.buff_x = 1 + (i % 3) * 128 - 128
                self.buff_y = 1 + (i // 3) * 128 - 128
                self.buff = Buff("mat", self.rect.x + self.buff_x, self.rect.y + self.buff_y, self)
            self.rarity = "common"
            self.vulnerables_and_resists['piercing'] = -25
            self.vulnerables_and_resists['poison'] = -100
            self.vulnerables_and_resists['fire'] = -25
            self.vulnerables_and_resists['bludgeoning'] = 50

        if self.name == 'cvetochnica':
            self.hp = self.max_hp = 20
            for i in range(9):
                self.buff_x = 1 + (i % 3) * 128 - 128
                self.buff_y = 1 + (i // 3) * 128 - 128
                self.buff = Buff("cvetok", self.rect.x + self.buff_x, self.rect.y + self.buff_y, self)
            self.rarity = "common"

        if self.name == 'bolotnik':
            self.hp = self.max_hp = 20
            self.bolotos = 5
            if self.upgrade_level == "2a" or self.upgrade_level == "3a":
                self.bolotos = 7
            for i in range(self.bolotos):
                self.debuff_x = 1 + i * 128
                self.debuff = Buff('boloto', self.rect.x + self.debuff_x, self.rect.y, self)
                self.rarity = "common"
            if self.upgrade_level == "2b" or self.upgrade_level == "3b":
                self.remove(towers_group)
                self.add(nekusaemie_group)
                self.atk = 0
                self.attack_cooldown = 0
                self.basic_attack_cooldown = 1200

        if self.name == 'pen':
            self.hp = self.max_hp = 20
            self.rect_pen = Rect(self.rect.x, self.rect.y, 384, 128)
            self.rarity = "common"  # резисты попозже

        if self.name == 'furry_druid':
            self.hp = self.max_hp = 0
            self.rarity = "common"

        if self.name == 'furry_medved':  # надо чтобы он сплэшил
            self.hp = self.max_hp = 550
            self.atk = self.basic_atk = 30
            self.attack_cooldown = self.basic_attack_cooldown = 300
            self.damage_type = 'slashing'
            self.rarity = "common"

        if self.name == 'furry_volk':  # а он нет(как драчун)
            self.hp = self.max_hp = 50
            self.rect_furry_volk = Rect(self.rect.x-128, self.rect.y-128, 384, 384)
            self.atk = self.basic_atk = 40  # 80 (8*5=40, 40+40=80)
            self.plus_atk = self.atk/8  #5
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.damage_type = 'slashing'
            self.rarity = "common"

        if self.name == 'furry_zayac':
            self.hp = self.max_hp = 20
            self.atk = 10
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.bullet_stun_time = 15
            self.attack_cooldown = self.basic_attack_cooldown = 240
            self.damage_type = 'bludgeoning'
            self.rarity = "common"

        if self.name == 'oruzhik':
            self.hp = self.max_hp = 0
            self.rarity = "common"

        if self.name == 'oruzhik_claymore':
            self.hp = self.max_hp = 550
            self.atk = 100
            self.received_damage = 0
            self.max_received_damage = 100
            self.damage_type = 'slashing'
            self.rarity = "common"

        if self.name == 'oruzhik_daggers':
            self.hp = self.max_hp = 20
            self.atk = 10
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.daggers = ['fire_dagger', 'ice_dagger']
            self.daggers_damage_type = ['fire', 'ice']
            self.dagger = 0
            self.target_phase = None
            self.damage_type = ''
            self.rarity = "common"

        if self.name == 'oruzhik_bow':
            self.hp = self.max_hp = 20
            self.atk = 10
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.arrows = ['fire_arrow', 'ice_arrow', 'electric_arrow', 'earth_arrow', 'water_arrow']
            self.arrows_damage_type = ['fire', 'ice', 'electric', 'piercing', 'water']  # не кайф земляную стрелу переименовывать
            self.arrow = 0  # номер текущей стрелы
            self.damage_type = ''
            self.rarity = "common"

        # я решил спеллы внизу писать

        if self.name == 'bomb':
            self.hp = self.max_hp = 0
            self.atk = 700
            self.damage_type = 'fire'
            self.rarity = "spell"

        if self.name == 'perec':
            self.hp = self.max_hp = 0
            self.atk = 700
            self.free_placement = True
            self.damage_type = 'fire'
            self.rarity = "spell"

        if self.name == 'vodka':
            self.hp = self.max_hp = 0  # надо сделать предел усиления (3 сек)
            self.free_placement = True
            self.rarity = "spell"

        if self.name == 'easy_money':
            self.hp = self.max_hp = 0
            self.free_placement = True
            self.rarity = "spell"

        if self.name == 'vistrel':
            self.hp = self.max_hp = 0
            self.atk = 30
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.free_placement = True
            self.damage_type = 'clean'
            self.rarity = "spell"

        if self.name == 'molniya':
            self.hp = self.max_hp = 0
            self.atk = 1000
            self.free_placement = True
            self.damage_type = 'electric'
            self.moiniya_popala = False
            self.rarity = "spell"

        if self.name == 'tp_back':
            self.hp = self.max_hp = 0
            self.free_placement = True
            self.rarity = "spell"

        if self.name == 'joltiy_pomidor':
            self.hp = self.max_hp = 0
            self.atk = 0
            self.damage_type = ''
            self.money_per_enemy = 5
            self.enemy_stunned_time = 225
            self.rarity = "spell"
        
        if self.name == 'heal':
            self.hp = self.max_hp = 0
            self.free_placement = True
            self.heal = 1500
            self.damage_type = ''
            self.rect_krest1 = Rect(self.rect.x-128, self.rect.y, 384, 128)
            self.rect_krest2 = Rect(self.rect.x, self.rect.y-128, 128, 384)
            self.rarity = "spell"

        if self.name == 'zaduv':
            self.hp = self.max_hp = 0
            self.free_placement = True
            self.uragan_duration = 360
            self.damage_type = ''
            self.rarity = "spell"

        if self.name == 'holod':
            self.hp = self.max_hp = 0
            self.free_placement = True
            self.damage_type = ''
            self.rarity = "spell"

        if self.name == 'krest':
            self.hp = self.max_hp = 1
            self.atk = 0
            self.damage_type = ''
            self.rarity = "spell"
            krests_group.add(self)

        # СТАТЫ конец
        # if hasattr(self, "attack_cooldown"):
        #     self.shoot_sound = mixer.Sound(f"sounds/sound_effects/towers/shoot/pukish.wav")
        # self.death_sound = mixer.Sound(f"sounds/sound_effects/towers/death/{unit}.ogg")   # откоментить

        if self.rarity == "spell":
            self.remove(towers_group)
            self.add(nekusaemie_group)
        self.image2 = font30.render(str(self.hp), True, (0, 0, 0))
        self.rect2 = self.image.get_rect(topleft=(self.rect.x + 32, self.rect.y - 32))

    def add_anim_task(self, anim, func):
        if len(self.anim_tasks) == 0:
            self.state = anim
            self.anim_tasks.append([anim, (self.get_count_anim_frames() * self.anim_duration) // self.time_indicator - 1, func])  # (self.get_count_anim_frames() * self.anim_duration) // self.time_indicator
            self.anim_count = 0
        else:
            already_in = [anim[0] for anim in self.anim_tasks]
            if anim not in already_in:
                self.state = anim
                self.anim_tasks.append([anim, (self.get_count_anim_frames() * self.anim_duration) // self.time_indicator - 1, func])

        # print(self.state, (self.get_count_anim_frames() * self.anim_duration) // self.time_indicator)

    def prime_anim(self, anim, func):
        if anim not in [an[0] for an in self.anim_tasks]:
            self.anim_tasks.clear()
            self.add_anim_task(anim, func)

    def dead(self):
        for i in range(3):
            if self.name == 'grib' + str(i + 1):
                if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                    Buff('grib_gas', self.rect.x, self.rect.y, self)
                if self.upgrade_level == '2b' or self.upgrade_level == '3b':
                    if self.name == 'grib1':
                        Bullet("mini_explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'explosion', self)
                    else:
                        Bullet("explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'explosion', self)

        if self.name == "gnome_cannon3":
            for tower in nekusaemie_group:
                if tower.rect.collidepoint(self.rect.centerx, self.rect.centery):
                    tower.kill()

        elif self.name == "boomchick":
            if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                Bullet("mega_explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk * 5, 0, 0, 'explosion', self)
            else:
                Bullet("explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk * 5, 0, 0, 'explosion', self)

        elif self.name == "thunder":
            self.kamen = Tower('thunder_kamen', self.pos)
            if self.upgrade_level == '3a':
                self.kamen.hp = self.kamen_hp

        elif self.name == 'gribnik':
            Tower('grib3', self.pos)
            if self.upgrade_level == '3b':
                for i in range(0, 8, 2):
                    if i < 4:
                        grib = Tower('grib3', ((384 + ((self.rect.x - 384) // 128) * 128), (192 + ((self.rect.y+(128*(i-1)) - 192) // 128) * 128)))
                    else:
                        grib = Tower('grib3', ((384 + ((self.rect.x+(128*(i-5)) - 384) // 128) * 128), (192 + ((self.rect.y - 192) // 128) * 128)))
                    if not (1536 > grib.pos[0] >= 384 and 832 > grib.pos[1] >= 192) or not is_free(grib):
                        grib.kill()
            else:
                for i in range(0, 8, 2):
                    if i < 4:
                        grib = Tower('grib1', ((384 + ((self.rect.x - 384) // 128) * 128), (192 + ((self.rect.y+(128*(i-1)) - 192) // 128) * 128)))
                    else:
                        grib = Tower('grib1', ((384 + ((self.rect.x+(128*(i-5)) - 384) // 128) * 128), (192 + ((self.rect.y - 192) // 128) * 128)))
                    if not (1536 > grib.pos[0] >= 384 and 832 > grib.pos[1] >= 192) or not is_free(grib):
                        grib.kill()

        elif self.name == 'dark_druid':
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

        elif self.name == 'knight_on_horse':
            if self.horse_hp <= 0:
                hp = self.knight_hp + 500
                knight = Tower("knight", self.pos)
                knight.hp = hp
                self.kill()
            elif self.knight_hp <= 0:
                self.taran_atk = self.atk*20
                Bullet("horse", self.rect.centerx, self.rect.centery, self.damage_type, self.taran_atk, 7, 0, 'horse', self)
                self.kill()

        elif self.name == 'furry_druid':
            if 1536 > self.rect.x >= 1152:
                Tower("furry_medved", self.pos)
            elif 1152 > self.rect.x >= 768:
                Tower("furry_volk", self.pos)
            elif 768 > self.rect.x >= 384:
                Tower("furry_zayac", self.pos)

        elif self.name == 'oruzhik':
            if 1536 > self.rect.x >= 1152:
                Tower("oruzhik_claymore", self.pos)
            elif 1152 > self.rect.x >= 768:
                Tower("oruzhik_daggers", self.pos)
            elif 768 > self.rect.x >= 384:
                Tower("oruzhik_bow", self.pos)
        # спеллы

        elif self.name == "bomb":
            Bullet("explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'explosion', self)

        elif self.name == "perec":
            Bullet("perec_bullet", 960, self.rect.bottom-8, self.damage_type, self.atk, 0, 0, 'explosion', self)

        elif self.name == "vistrel":
            Bullet("vistrel_bullet", 384, self.rect.centery-10, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)

        elif self.name == 'molniya':
            for i in range(3):
                for enemy in enemies_group:
                    if enemy.alive and self not in enemy.parasite_parents:
                        enemy.parasite_parents.add(self)
                        self.moiniya_popala = True
                        Parasite('mol', enemy.rect.centerx, enemy.rect.bottom - 450, self.damage_type, self.atk, enemy, self)
                        break
                if not self.moiniya_popala:
                    for enemy in neutral_objects_group:
                        if enemy.height == "high":
                            if enemy.alive and self not in enemy.parasite_parents:
                                enemy.parasite_parents.add(self)
                                self.moiniya_popala = True
                                Parasite('mol', enemy.rect.centerx, enemy.rect.bottom - 450, self.damage_type, self.atk, enemy, self)
                                break
                    if not self.moiniya_popala:
                        Parasite('mol', randint(384, 1536), randint(-258, 382), self.damage_type, self.atk, self, self)
                self.moiniya_popala = False

        elif self.name == "vodka":
            for i in range(9):
                self.buff_x = 1 + (i % 3) * 128 - 128
                self.buff_y = 1 + (i // 3) * 128 - 128
                self.buff = Buff("vodkamat", self.rect.x + self.buff_x, self.rect.y + self.buff_y, self)

        elif self.name == "easy_money":
            level.money += 30

        elif self.name == "tp_back":
            for enemy_ in enemies_group:
                if enemy_.rect.centerx <= 1024:
                    enemy_.real_x = 1536

        elif self.name == "joltiy_pomidor":
            Bullet("joltiy_explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'joltiy_explosion', self)

        elif self.name == "heal":
            Bullet("heal_field", self.rect.centerx, self.rect.centery, self.damage_type, 0, 0, 0, 'visual_effect', self)
            for tower in towers_group:
                if tower.rect.colliderect(self.rect_krest1) or tower.rect.colliderect(self.rect_krest2):
                    if tower.max_hp - tower.hp > self.heal:
                        tower.hp += self.heal
                    else:
                        tower.hp = tower.max_hp

        elif self.name == "zaduv":
            Parasite("potok_y", self.rect.centerx, self.rect.centery, self.damage_type, 0, self, self)

        elif self.name == "holod":
            Bullet("holod_row", self.rect.centerx, 512, self.damage_type, 0, 0, 0, 'holod_row', self)

        if self.name == 'drachun' and self.upgrade_level == '3b':   # работает неправильно наверно!!!
            if self.kill_time > 0:
                self.kill_time -= 1
            else:
                self.kill()
                self.alive = False
        elif self.name == 'kot' and self.lives > 1:
            self.lives -= 1
            self.chill_time = self.unvulnerable = self.basic_chill_time
            towers_group.remove(self)
            nekusaemie_group.add(self)
            self.hp = self.max_hp
        else:
            # self.alive = False
            self.sound('death')
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

        if self.name == 'terpila' and (self.upgrade_level == '2b' or self.upgrade_level == '3b' or self.upgrade_level == '3a'):
            if self.received_damage >= self.max_received_damage:
                self.received_damage -= self.max_received_damage
                if self.upgrade_level == '2b' or self.upgrade_level == '3b':
                    for enemy in enemies_group:
                        if enemy.rect.colliderect(self.ottalkivanie_rect):
                            if not enemy.heavy:
                                enemy.real_x += 128
                            if self.upgrade_level == '3b':
                                Parasite('terpila_debuff', enemy.rect.centerx, enemy.rect.centery, '', 0, enemy, self)
                elif self.upgrade_level == '3a':
                    self.unvulnerable = 300

        if self.name == 'oruzhik_claymore':
            if self.received_damage >= self.max_received_damage:
                self.received_damage -= self.max_received_damage
                self.add_anim_task("attack", self.shoot)
        
        if self.name == 'krovnyak':
            if self.damaged:
                if len(self.krovs) < 8:
                    Bullet("krov_bul", self.rect.centerx - (len(self.krovs) % 2 + 1) * 21, self.rect.centery + 48 - (32*(len(self.krovs) // 2)), self.damage_type, 0, self.bullet_speed_x, self.bullet_speed_y, 'krov_bul', self).remove(bullets_group)
                self.not_damaged_time = 1800

        self.damaged = False

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
                or self.name == 'ded_moroz'\
                or self.name == 'kokol'\
                or self.name == 'sliz'\
                or self.name == 'furry_zayac'\
                or self.name == 'oruzhik_bow'\
                or self.name == 'chistiy'\
                or self.name == 'electro_maga'\
                or self.name == 'elf'\
                or self.name == 'holodilnik'\
                or self.name == 'chorniy'\
                or self.name == 'shabriri': 
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                        return enemy
            

        if self.name == 'kopitel':
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive and self.nakopleno > 0:
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive and self.nakopleno > 0:
                        return enemy

        if self.name == 'pulelom':      
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.attack_range > 0 and (enemy.state == 'attack' or enemy.state == 'rage_attack'):
                    return enemy
                elif -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.attack_range > 0 and (enemy.state == 'attack' or enemy.state == 'rage_attack') and enemy.name == 'drobik':
                    return enemy
            for bullet in bullets_group:
                if bullet.zloy and -10 <= bullet.rect.y - self.rect.y <= 10 and bullet.rect.x >= self.rect.x:
                    return bullet.parent

        if self.name == 'kar_mag':
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 384 and enemy.alive:
                    self.target_phase = 'close'
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 384 and enemy.alive:
                        self.target_phase = 'close'
                        return enemy
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                    self.target_phase = 'far'
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                        self.target_phase = 'far'
                        return enemy
                
        if self.name == 'uvelir':
            if self.gem == 'stone' or self.gem == 'obsidian' or self.gem == 'diamond' or self.gem == 'opal':
                for enemy in enemies_group:
                    if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                        return enemy
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                            return enemy
            elif self.gem == 'onyx' or self.gem == 'amethyst':
                best_x = self
                for tower in towers_group:
                    if tower.rect.y == self.rect.y and tower.rect.x > best_x.rect.x:
                        best_x = tower
                return best_x
            elif self.gem == 'emerald':
                best_target = self
                for tower in towers_group:
                    if tower.hp < tower.max_hp and -10 <= tower.rect.y - self.rect.y <= 10 and tower.hp > 0:
                        best_target = tower
                        for tower in towers_group:
                            if best_target.rect.x < tower.rect.x and tower.hp < tower.max_hp and -10 <= tower.rect.y - self.rect.y <= 10 and tower.hp > 0:
                                best_target = tower
                return best_target
            elif self.gem == 'ruby':
                best_atk = self
                for tower in towers_group:
                    if tower.rect.y == self.rect.y and hasattr(tower, 'atk') and tower.atk > best_atk.atk:
                        best_atk = tower
                return best_atk
            elif self.gem == 'sapphire' or self.gem == 'nephrite':
                return self

        if self.name == 'parasitelniy':
            for enemy in enemies_group:
                if self not in enemy.parasite_parents and enemy.alive:
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if self not in enemy.parasite_parents and enemy.alive:
                        return enemy

        if self.name == 'inquisitor':
            self.best_target = None
            for enemy in enemies_group:
                if self not in enemy.parasite_parents and enemy.alive:
                    self.best_target = enemy
                    for enemy in enemies_group:
                        if len(enemy.parasites) < len(self.best_target.parasites) and self not in enemy.parasite_parents and enemy.alive:
                            self.best_target = enemy
                    self.best_target.parasites.add(self)
                    return self.best_target
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if self not in enemy.parasite_parents and enemy.alive:
                        self.best_target = enemy
                        for enemy in enemies_group:
                            if len(enemy.parasites) < len(self.best_target.parasites) and self not in enemy.parasite_parents and enemy.alive:
                                self.best_target = enemy
                        self.best_target.parasites.add(self)
                        return self.best_target

        if self.name == "thunder":
            for enemy in enemies_group:
                if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive and (-10 > enemy.rect.y - self.rect.y or enemy.rect.y - self.rect.y > 10):
                    self.target_phase = 'side'
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive and (-10 > enemy.rect.y - self.rect.y or enemy.rect.y - self.rect.y > 10):
                        self.target_phase = 'side'
                        return enemy
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                    self.target_phase = 'center'
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                        self.target_phase = 'center'
                        return enemy

        if self.name == "electric" or self.name == 'oruzhik_daggers':
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive:
                    self.target_phase = 'close'
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive:
                        self.target_phase = 'close'
                        return enemy
            for enemy in enemies_group:
                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x + 256 and enemy.alive:
                    self.target_phase = 'far'
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x + 256 and enemy.alive:
                        self.target_phase = 'far'
                        return enemy

        if self.name == "urag_anus":
            enemies = [enemy for enemy in enemies_group if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive]
            if enemies:     # проверка, что список не пустой
                enemy_x_cords = [enemy.rect.x for enemy in enemies]
                return enemies[enemy_x_cords.index(min(enemy_x_cords))]         # не убирать

        if self.name == "yascerica":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and 1536 > enemy.rect.x >= self.rect.x and self.blackik.summon == 'baza' and enemy.alive:
                    return enemy
        
        if self.name == "krovnyak":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and 1536 > enemy.rect.x >= self.rect.x and enemy.alive:
                    for krov in self.krovs:
                        if krov.summon == 'baza':
                            return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and 1536 > enemy.rect.x >= self.rect.x and enemy.alive:
                        for krov in self.krovs:
                            if krov.summon == 'baza':
                                return enemy

        if self.name == "spike":            # аое дамаг
            for enemy in enemies_group:
                if self.upgrade_level == '3b' and self.great_form:
                    if enemy.rect.colliderect(self.great_rect) and enemy.alive:
                        return enemy
                else:
                    if enemy.rect.colliderect(self.rect) and enemy.alive:
                        return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if self.upgrade_level == '3b' and self.great_form:
                        if enemy.rect.colliderect(self.great_rect) and enemy.alive:
                            return enemy
                    else:
                        if enemy.rect.colliderect(self.rect) and enemy.alive:
                            return enemy
                
        if self.name == 'bolotnik' and (self.upgrade_level == "2b" or self.upgrade_level == "3b"):
            for enemy in enemies_group:
                if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery) and enemy.alive:
                    enemies_group.remove(enemy)
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery) and enemy.alive:
                        enemies_group.remove(enemy)
                        return enemy

        if self.name == 'big_mechman':      # аое дамаг
            for enemy in enemies_group:
                if self.upgrade_level == '2b' or self.upgrade_level == '3b':
                    if self.big_mech_cooldown > 0:
                        if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.rect.x - self.rect.x < 256:
                            return enemy
                    else:
                        if -266 <= enemy.rect.y - self.rect.y <= 266 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.rect.x - self.rect.x < 384:
                            return enemy
                else:
                    if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.rect.x - self.rect.x < 256:
                        return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if self.upgrade_level == '2b' or self.upgrade_level == '3b':
                        if self.big_mech_cooldown > 0:
                            if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.rect.x - self.rect.x < 256:
                                return enemy
                        else:
                            if -266 <= enemy.rect.y - self.rect.y <= 266 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.rect.x - self.rect.x < 384:
                                return enemy
                    else:
                        if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.rect.x - self.rect.x < 256:
                            return enemy
                    
        if self.name == "sekirshik":
            for enemy in enemies_group:
                if (self.upgrade_level == '2b' and self.spin_attack_cooldown <= 0) or self.upgrade_level == '3b':
                    if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.right >= self.rect.x - 128 and enemy.alive and enemy.rect.x - self.rect.x < 256:
                        return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if (self.upgrade_level == '2b' and self.spin_attack_cooldown <= 0) or self.upgrade_level == '3b':
                        if -138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.right >= self.rect.x - 128 and enemy.alive and enemy.rect.x - self.rect.x < 256:
                            return enemy
                    
        if self.name == "kirka":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive and hasattr(enemy, 'armor') and enemy.armor > 0:
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive and hasattr(enemy, 'armor') and enemy.armor > 0:
                        return enemy

        if self.name == "drachun" or self.name == "kirka" or self.name == "tolkan" or self.name == "knight" or self.name == "sekirshik" or self.name == 'furry_medved' or self.name == 'furry_volk' or (self.name == 'kot' and ((self.upgrade_level == '2b' and self.lives <= 5) or self.upgrade_level == '3b')):
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive:
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive:
                        return enemy

        if self.name == "knight_on_horse":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 384 and enemy.alive:
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 384 and enemy.alive:
                        return enemy
                
        if self.name == "klonys":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= ((self.basic_illusions+1) * 128) and enemy.alive:
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= ((self.basic_illusions+1) * 128) and enemy.alive:
                        return enemy
                
        if self.name == "prokach":
            if self.mech_level <= 2:
                for enemy in enemies_group:
                    if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive:
                        return enemy
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive:
                            return enemy
            elif self.mech_level == 3:
                for enemy in enemies_group:
                    if (enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive:
                        return enemy
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if (enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 256 and enemy.alive:
                            return enemy
            elif self.mech_level == 4:
                for enemy in enemies_group:
                    if (((enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x - self.rect.x < 384) or ((enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x - self.rect.x < 256)) and enemy.rect.x >= self.rect.x and enemy.alive:
                        return enemy
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if (((enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x - self.rect.x < 384) or ((enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x - self.rect.x < 256)) and enemy.rect.x >= self.rect.x and enemy.alive:
                            return enemy
            elif self.mech_level == 5:
                for enemy in enemies_group:
                    if (enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 384 and enemy.alive:
                        return enemy
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if (enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 384 and enemy.alive:
                            return enemy
            elif self.mech_level == 6:
                for enemy in enemies_group:
                    if (((enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x - self.rect.x < 512) or ((enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x - self.rect.x < 384)) and enemy.rect.x >= self.rect.x and enemy.alive:
                        return enemy
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if (((enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x - self.rect.x < 512) or ((enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x - self.rect.x < 384)) and enemy.rect.x >= self.rect.x and enemy.alive:
                            return enemy
            elif self.mech_level == 7:
                for enemy in enemies_group:
                    if (enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 512 and enemy.alive:
                        return enemy
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if (enemy.rect.y - self.rect.y <= 138 and self.rect.y - enemy.rect.y <= 138) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 512 and enemy.alive:
                            return enemy
            if self.mech_level < self.max_mech_level:
                self.mech_level += 1
                self.attack_cooldown = self.basic_attack_cooldown
            

        if self.name == "pukish":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.centerx >= self.rect.x-10 and enemy.alive:
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.centerx >= self.rect.x-10 and enemy.alive:
                        return enemy

        if self.name == "gnome_flamethrower":
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 192 and enemy.alive:
                    return enemy
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x < 192 and enemy.alive:
                        return enemy

        if self.name == 'priest':
            self.best_target = None
            for tower in towers_group:
                if tower.hp < tower.max_hp and -10 <= tower.rect.y - self.rect.y <= 10 and tower.rect.x >= self.rect.x and tower.hp > 0:
                    self.best_target = tower
                    for tower in towers_group:
                        if self.best_target.rect.x < tower.rect.x and tower.hp < tower.max_hp and -10 <= tower.rect.y - self.rect.y <= 10 and tower.rect.x >= self.rect.x and tower.hp > 0:
                            self.best_target = tower
                    return self.best_target

        return None

    def check_target_alive(self):
        if targets[id(self)]:
            if targets[id(self)].rect.x < self.rect.x:
                targets[id(self)] = None
            elif (self.name == 'thunder' and self.target_phase == 'center') or (self.name == 'electric' and self.target_phase == 'far') or (self.name == 'oruzhik_daggers' and self.target_phase == 'far') or (self.name == 'kar_mag' and self.target_phase == 'far') or self.name == 'urag_anus' or self.name == 'priest' or self.name == 'uvelir' or self.name == 'kirka':
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
            else:                                       # если баг, то убрать это
                self.add_anim_task("wait", lambda: ...)

    def dealing_damage(self, enemy):
        self.damage = self.atk
        if enemy.vulnerabled > 0:
            self.damage *= 2
        for k, v in enemy.vulnerables_and_resists.items():
            if k == self.damage_type:
                self.damage *= (100 + v)/100
        if hasattr(enemy, 'armor') and enemy.armor > 0:
            if self.damage <= enemy.armor:
                enemy.armor -= self.damage
            else:
                enemy.hp -= (self.damage - enemy.armor)
                enemy.armor = 0
        else:
            enemy.hp -= self.damage
        enemy.damaged = True
        if enemy.alive:
            enemy.check_hp()

    def shoot(self):
        if self.name == "fire_mag":
            if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                self.atk_big = self.atk*2
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
            if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                if self.attack_count < 2:
                    Bullet("yellow_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'boom', self)
                    self.attack_count += 1
                else:
                    Bullet("red_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'big_boom', self)
                    self.attack_count = 0
            else:
                Bullet("yellow_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'boom', self)

        if self.name == "holodilnik":
            Bullet("blue_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'razrivnaya', self)

        if self.name == "gribnik":
            Bullet("grib_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'spore', self)

        if self.name == "chorniy":
            Bullet("onyx", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'chorniy_bullet', self)

        if self.name == "ded_moroz":
            if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                if not self.ice_form:
                    if self.attack_count < 1:
                        Bullet("snejok", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'snejok', self)
                        self.attack_count += 1
                        if self.upgrade_level == '3a':
                            self.ice_form_cooldown -= 1
                    else:
                        Bullet("blue_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'snejok_big', self)
                        self.attack_count = 0
                        if self.upgrade_level == '3a':
                            self.ice_form_cooldown -= 1
                else:
                    Bullet("blue_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'snejok_big', self)
                    self.ice_form_duration -= 1
            else:
                Bullet("snejok", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'snejok', self)
            
        if self.name == "sliz":
            Bullet("sliz_bul", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'sliz_bul', self)

        if self.name == "furry_zayac":
            for i in range(3):
                Bullet("zayac_krol", self.rect.centerx+(i*32), self.rect.centery+randint(-32, 32), self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'zayac_krol', self)

        if self.name == "oruzhik_bow":
            Bullet(self.arrows[self.arrow], self.rect.centerx, self.rect.centery, self.arrows_damage_type[self.arrow], self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)
            self.arrow += 1
            if self.arrow >= len(self.arrows):
                self.arrow = 0
                
        if self.name == "chistiy":
            for i in range(15):
                Bullet("chistiy_bullet", self.rect.centerx-16*(1+(i//4)), self.rect.centery+18-(12*(i%4)), self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'chistiy_bullet', self)
            for tower in towers_group:
                if self.rect_chistiy.collidepoint(tower.rect.centerx, tower.rect.centery) and tower.name == self.name and tower != self:
                    for i in range(3):
                        Bullet("chistiy_bullet", tower.rect.centerx-16*(1+(i%3)), tower.rect.centery, tower.damage_type, tower.atk, tower.bullet_speed_x, tower.bullet_speed_y, 'chistiy_bullet', self)

        if self.name == "elf":
            Bullet("emerald", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)

        if self.name == "kopitel":
            for bullet in self.spawned_things:
                bullet.speed_x = 7
                bullet.add(bullets_group)
                self.nakopleno = 0
            self.spawned_things.clear()

        if self.name == "uvelir":
            self.gem_bul.target = targets[id(self)]
            self.gem = ''
            self.gem_bul.add(bullets_group)

        if self.name == "parasitelniy":
            self.parasix = randint(0, 32)
            self.parasiy = randint(-32, 32)
            Parasite('sosun', targets[id(self)].rect.centerx+self.parasix, targets[id(self)].rect.centery+self.parasiy, '', self.atk, targets[id(self)], self)  # bug? no, juk.
            targets[id(self)].parasite_parents.add(self)
            targets[id(self)] = None

        if self.name == "inquisitor":
            self.parasix = randint(-9, 9)
            self.parasiy = randint(-64, -46)
            Parasite('metka_inq', targets[id(self)].rect.centerx+self.parasix, targets[id(self)].rect.centery+self.parasiy, '', self.atk, targets[id(self)], self)
            targets[id(self)].parasite_parents.add(self)
            targets[id(self)] = None

        if self.name == "nekr":
            if self.upgrade_level == "2a":
                if self.rect.y+128 <= 704:
                    if self.cr4 not in self.creeps:
                        self.cr4 = Creep('nekr_skelet', (self.rect.x, self.rect.y + 128), self)
                if self.rect.y-128 >= 192:
                    if self.cr5 not in self.creeps:
                        self.cr5 = Creep('nekr_skelet', (self.rect.x , self.rect.y - 128), self)
                if self.cr1 not in self.creeps:
                    self.cr1 = Creep('nekr_skelet', (self.rect.x, self.rect.y), self)
                if self.cr2 not in self.creeps:
                    self.cr2 = Creep('nekr_skelet', (self.rect.x + 45, self.rect.y), self)
                if self.cr3 not in self.creeps:
                    self.cr3 = Creep('nekr_skelet', (self.rect.x + 90, self.rect.y), self)
            elif self.upgrade_level == "3a":
                if self.rect.y+128 <= 704:
                    if self.cr4 not in self.creeps:
                        self.cr4 = Creep('nekr_skelet_strelok', (self.rect.x, self.rect.y + 128), self)
                if self.rect.y-128 >= 192:
                    if self.cr5 not in self.creeps:
                        self.cr5 = Creep('nekr_skelet_strelok', (self.rect.x, self.rect.y - 128), self)
                if self.cr1 not in self.creeps:
                    self.cr1 = Creep('nekr_skelet_strelok', (self.rect.x, self.rect.y), self)
                if self.cr2 not in self.creeps:
                    self.cr2 = Creep('nekr_skelet', (self.rect.x + 45, self.rect.y), self)
                if self.cr3 not in self.creeps:
                    self.cr3 = Creep('nekr_skelet', (self.rect.x + 90, self.rect.y), self)
            elif self.upgrade_level == "2b":
                if self.cr1 not in self.creeps:
                    self.cr1 = Creep('nekr_zombie', (self.rect.x, self.rect.y), self)
                if self.cr2 not in self.creeps:
                    self.cr2 = Creep('nekr_zombie', (self.rect.x + 45, self.rect.y), self)
                if self.cr3 not in self.creeps:
                    self.cr3 = Creep('nekr_zombie', (self.rect.x + 90, self.rect.y), self)
            elif self.upgrade_level == "3b":
                if self.cr1 not in self.creeps:
                    self.cr1 = Creep('nekr_zombie', (self.rect.x, self.rect.y), self)
                if self.cr2 not in self.creeps:
                    self.cr2 = Creep('nekr_zombie', (self.rect.x + 45, self.rect.y), self)
                if self.cr3 not in self.creeps:
                    self.cr3 = Creep('nekr_zombie_jirny', (self.rect.x + 90, self.rect.y), self)
            else:
                if self.cr1 not in self.creeps:
                    self.cr1 = Creep('nekr_skelet', (self.rect.x, self.rect.y), self)
                if self.cr2 not in self.creeps:
                    self.cr2 = Creep('nekr_skelet', (self.rect.x + 45, self.rect.y), self)
                if self.cr3 not in self.creeps:
                    self.cr3 = Creep('nekr_skelet', (self.rect.x + 90, self.rect.y), self)

        if self.name == "kokol":
            Bullet("ab_kokol", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kok', self)

        if self.name == "thunder":
            if self.upgrade_level == '2b' and self.golem_cooldown <= 0:
                if self.target_phase == 'side':
                    Bullet("mini_kamen_golem", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk*2, self.bullet_speed_x, 0, 'hrom', self)
                    if self.rect.centery+138 <= 832:
                        Bullet("mini_kamen_golem", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk*2, self.bullet_speed_x, self.bullet_speed_y, 'hrom', self)
                    if self.rect.centery-138 >= 192:
                        Bullet("mini_kamen_golem", self.rect.centerx - 8, self.rect.centery - 8,  self.damage_type, self.atk*2, self.bullet_speed_x, self.bullet_speed_y * -1, 'hrom', self)
                elif self.target_phase == 'center':  # я мог бы просто написать else, но пусть лучше так
                    Bullet("big_kamen_golem", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk*6, self.bullet_speed_x, 0, 'hrom', self)
                self.golem_cooldown = self.basic_golem_cooldown
            elif self.upgrade_level == '3b' and self.golem_cooldown <= 0:
                if self.target_phase == 'side':
                    Bullet("big_kamen_golem", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk*3, self.bullet_speed_x, 0, 'hrom', self)
                    if self.rect.centery+138 <= 832:
                        Bullet("big_kamen_golem", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk*3, self.bullet_speed_x, self.bullet_speed_y, 'hrom', self)
                    if self.rect.centery-138 >= 192:
                        Bullet("big_kamen_golem", self.rect.centerx - 8, self.rect.centery - 8,  self.damage_type, self.atk*3, self.bullet_speed_x, self.bullet_speed_y * -1, 'hrom', self)
                elif self.target_phase == 'center':  # я мог бы просто написать else, но пусть лучше так
                    Bullet("mega_kamen_golem", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk*9, self.bullet_speed_x, 0, 'hrom', self)
                self.golem_cooldown = self.basic_golem_cooldown
            else:
                if self.target_phase == 'side':
                    Bullet("mini_kamen", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk, self.bullet_speed_x, 0, 'hrom', self)
                    if self.rect.centery+138 <= 832:
                        Bullet("mini_kamen", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'hrom', self)
                    if self.rect.centery-138 >= 192:
                        Bullet("mini_kamen", self.rect.centerx - 8, self.rect.centery - 8,  self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y * -1, 'hrom', self)
                elif self.target_phase == 'center':  # я мог бы просто написать else, но пусть лучше так
                    Bullet("big_kamen", self.rect.centerx - 8, self.rect.centery - 8, self.damage_type, self.atk*3, self.bullet_speed_x, 0, 'hrom', self)

        if self.name == 'kar_mag':
            if self.target_phase == 'close':
                for bullet in self.spawned_things:
                    bullet.speed_x = 4
                    bullet.add(bullets_group)
                    self.v_falange = 0
                self.spawned_things.clear()
            if self.target_phase == 'far':
                Bullet('karm', self.rect.centerx, self.rect.centery-10, self.damage_type, self.atk,
                                self.bullet_speed_x+4, self.bullet_speed_y, 'default', self)
                
        if self.name == 'shabriri':
            if 25 > self.bezumie:
                Bullet("pubez", self.rect.right - 10, self.rect.y + 45, self.damage_type, self.atk, self.bullet_speed_x,
                    self.bullet_speed_y, 'default', self)
                self.bezumie += 1
            elif self.bezumie >= 25:
                Bullet("big_pubez", self.rect.right - 10, self.rect.y + 45, self.damage_type, self.atk_big, self.bullet_speed_x,
                       self.bullet_speed_y, 'default', self)
                self.bezumie += 1
            if self.bezumie == 25:
                self.vulnerables_and_resists['piercing'] = -10
                self.vulnerables_and_resists['slashing'] = -10
                self.vulnerables_and_resists['bludgeoning'] = -10
                self.vulnerables_and_resists['fire'] = -25
            elif self.bezumie == 50:
                self.basic_attack_cooldown //= 2
                self.time_indicator *= 2
                self.vulnerables_and_resists['piercing'] = -25
                self.vulnerables_and_resists['slashing'] = -25
                self.vulnerables_and_resists['bludgeoning'] = -25
                self.vulnerables_and_resists['fire'] = -50

        if self.name == "pulelom":
            Bullet("pulelomka", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'pulelomka', self)

        if self.name == "electric":
            if self.target_phase == 'close':
                self.atk2 = self.atk*15
                Bullet("electric_kulak", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk2, 0, 0, 'drachun_gulag', self)
            elif self.target_phase == 'far':  # я мог бы просто написать else, но пусть лучше так
                self.bursting = True

        if self.name == "oruzhik_daggers":
            if self.target_phase == 'close':
                Bullet("ice_dagger_slash", self.rect.right + 64, self.rect.centery, 'ice', self.atk, 0, 0, 'drachun_gulag', self)
                Bullet("fire_dagger_slash", self.rect.right + 64, self.rect.centery, 'fire', self.atk, 0, 0, 'drachun_gulag', self)
            elif self.target_phase == 'far':  # я мог бы просто написать else, но пусть лучше так
                Bullet(self.daggers[self.dagger], self.rect.centerx, self.rect.centery, self.daggers_damage_type[self.dagger], self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)
                self.dagger += 1
                if self.dagger >= len(self.daggers):
                    self.dagger = 0

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
            if self.blackik.summon == "baza":
                self.blackik.summon = "ready"
                targets[id(self)] = None

        if self.name == "krovnyak":
            for krov in self.krovs:
                if krov.summon == "baza":
                    krov.summon = "ready"
            targets[id(self)] = None

        if self.name == "gnome_cannon1" or self.name == "gnome_cannon2" or self.name == "gnome_cannon3":
            Bullet("red_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'default', self)

        if self.name == "pukish":
            Bullet("gas", self.rect.centerx + 38, self.rect.centery + 8, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'gas', self)

        if self.name == 'spike':    # fix?
            if self.upgrade_level == '3b' and self.great_form:
                for enemy in enemies_group:
                    if enemy.rect.colliderect(self.great_rect):
                        self.dealing_damage(enemy)
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if enemy.rect.colliderect(self.great_rect):
                            self.dealing_damage(enemy)
            else:
                for enemy in enemies_group:
                    if enemy.rect.colliderect(self.rect):
                        self.dealing_damage(enemy)
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if enemy.rect.colliderect(self.rect):
                            self.dealing_damage(enemy)
                if self.upgrade_level == '3a':
                    self.dengi_cooldown -= self.dengi_cooldown_reducing
                if self.upgrade_level == '3b' and not self.great_form:
                    self.great_form_cooldown -= 1
                    if self.great_form_cooldown <= 0:
                        self.great_form = True
                        self.great_form_cooldown = self.basic_great_form_cooldown
            targets[id(self)] = None

        if self.name == "big_mechman":
            if self.upgrade_level == '2b' or self.upgrade_level == '3b':
                if self.big_mech_cooldown > 0:
                    Bullet("mech_vzux", self.rect.right, self.rect.centery, self.damage_type, self.atk, 0, 0, 'mech', self)
                else:
                    Bullet("big_mech_vzux", self.rect.right+64, self.rect.centery, self.damage_type, self.atk*2, 0, 0, 'mech', self)
                    self.big_mech_cooldown = self.basic_big_mech_cooldown
            else:
                Bullet("mech_vzux", self.rect.right, self.rect.centery, self.damage_type, self.atk, 0, 0, 'mech', self)
                
        if self.name == "sekirshik":
            enemies_in_area_count = 0
            for enemy in enemies_group:
                if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256 and enemy.alive:
                    enemies_in_area_count += 1
                if (self.upgrade_level == '2b' and self.spin_attack_cooldown <= 0) or self.upgrade_level == '3b':
                    if (-138 <= enemy.rect.y - self.rect.y <= 138 and enemy.rect.right >= self.rect.x - 128 and enemy.alive and enemy.rect.x - self.rect.x <= 256) and not ((enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256 and enemy.alive):
                        enemies_in_area_count += 0.5
            if enemies_in_area_count > 16:
                enemies_in_area_count = 16
            if enemies_in_area_count < 1:
                enemies_in_area_count = 1
            if (self.upgrade_level == '2b' and self.spin_attack_cooldown <= 0) or self.upgrade_level == '3b':
                Bullet("drachun_gulag", self.rect.right + 64, self.rect.centery, self.damage_type, (self.atk+((enemies_in_area_count-1)*(self.atk/3)))/2, 0, 0, 'drachun_gulag_splash', self)
                Bullet("joltiy_explosion", self.rect.centerx, self.rect.centery, self.damage_type, (self.atk+((enemies_in_area_count-1)*(self.atk/3)))/2, 0, 0, 'drachun_gulag_splash', self)
                if self.upgrade_level == '2b':
                    self.spin_attack_cooldown = self.basic_spin_attack_cooldown
            else:
                Bullet("drachun_gulag", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk+((enemies_in_area_count-1)*(self.atk/3)), 0, 0, 'drachun_gulag_splash', self)
            
        if self.name == "drachun":
            Bullet("drachun_gulag", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag', self)

        if self.name == "kirka":
            Bullet("drachun_gulag", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag', self)

        if self.name == 'tolkan':
            self.za_towerom = False
            Bullet("tolkan_bux", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'tolkan_bux', self)
            for tower in towers_group:
                if tower.rect.y == self.rect.y and tower.rect.x > self.rect.x and tower.rect.x - self.rect.x <= 128 and tower.name != 'pukish' and tower != self:
                    self.za_towerom = True
            for tower in neutral_objects_group:
                if tower.height == 'high':
                    if tower.rect.y == self.rect.y and tower.rect.x > self.rect.x and tower.rect.x - self.rect.x <= 128 and tower.name != 'pukish' and tower != self:
                        self.za_towerom = True
            if self.za_towerom:
                self.push = self.ottalkivanie_ne_solo
            else:
                self.push = self.ottalkivanie_solo

        if self.name == "knight_on_horse":
            Bullet("big_pike", self.rect.centerx + 192, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag_splash', self)

        if self.name == "knight":
            Bullet("pike", self.rect.centerx + 128, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag_splash', self)

        if self.name == 'ares':
            Bullet("contrsword", self.rect.centerx + 128, self.rect.centery, self.damage_type, self.atk*(1+(self.vpitano_damaged*200//100)), 0, 0, 'drachun_gulag_splash', self)
            self.vpitano_damaged = 0

        if self.name == 'oruzhik_claymore':
            Bullet("earth_claymore", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag_splash', self)

        if self.name == "furry_medved":
            Bullet("medved_lapa", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag_splash', self)

        if self.name == "furry_volk":
            self.atk = self.basic_atk
            self.plus_atk = self.atk/8
            for tower in towers_group:
                if self.rect_furry_volk.collidepoint(tower.rect.centerx, tower.rect.centery) and tower != self:
                    self.atk += self.plus_atk
            for nekusaemiy in nekusaemie_group:
                if self.rect_furry_volk.collidepoint(nekusaemiy.rect.centerx, nekusaemiy.rect.centery) and nekusaemiy != self:
                    self.atk += self.plus_atk
            Bullet("volk_lapa", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag', self)

        if self.name == "kot":
            if self.upgrade_level == '2b':
                if self.lives <= 5:  # можно убрать но я оставил для подстраховки
                    Bullet("kot_scratch0", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag_splash', self)
            elif self.upgrade_level == '3b':
                attack_amount = 3 - ((self.lives - 1) // 3)
                for i in range(attack_amount):
                    Bullet("kot_scratch"+str(i), self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, 'drachun_gulag_splash', self)

        if self.name == "klonys":
            self.illusions = self.basic_illusions
            klonys_pose = randint(1, 5)
            Bullet("klonys_punch" + str(klonys_pose), self.rect.centerx + 128, self.rect.centery, self.damage_type, self.atk, 0, 0, 'klonys_punch', self)
        
        if self.name == "prokach":
            self.leveled_atk = self.atk
            if self.mech_level <= 2:
                self.leveled_atk = self.atk*(self.mech_level+1)
            else:
                self.leveled_atk = self.atk*3 + (self.atk/2)*(self.mech_level-2)
            Bullet("pike", self.rect.centerx + 128, self.rect.centery, self.damage_type, self.leveled_atk, 0, 0, 'drachun_gulag_splash', self).add(self.attack_areas)
            if self.mech_level >= 3:
                Bullet("pike", self.rect.centerx + 128, self.rect.centery-128, self.damage_type, self.leveled_atk, 0, 0, 'drachun_gulag_splash', self).add(self.attack_areas)
                Bullet("pike", self.rect.centerx + 128, self.rect.centery+128, self.damage_type, self.leveled_atk, 0, 0, 'drachun_gulag_splash', self).add(self.attack_areas)
            if self.mech_level >= 4:
                Bullet("pike", self.rect.centerx + 256, self.rect.centery, self.damage_type, self.leveled_atk, 0, 0, 'drachun_gulag_splash', self).add(self.attack_areas)
            if self.mech_level >= 5:
                Bullet("pike", self.rect.centerx + 256, self.rect.centery-128, self.damage_type, self.leveled_atk, 0, 0, 'drachun_gulag_splash', self).add(self.attack_areas)
                Bullet("pike", self.rect.centerx + 256, self.rect.centery+128, self.damage_type, self.leveled_atk, 0, 0, 'drachun_gulag_splash', self).add(self.attack_areas)
            if self.mech_level >= 6:
                Bullet("pike", self.rect.centerx + 384, self.rect.centery, self.damage_type, self.leveled_atk, 0, 0, 'drachun_gulag_splash', self).add(self.attack_areas)
            if self.mech_level >= 7:
                Bullet("pike", self.rect.centerx + 384, self.rect.centery-128, self.damage_type, self.leveled_atk, 0, 0, 'drachun_gulag_splash', self).add(self.attack_areas)
                Bullet("pike", self.rect.centerx + 384, self.rect.centery+128, self.damage_type, self.leveled_atk, 0, 0, 'drachun_gulag_splash', self).add(self.attack_areas)
            self.mech_level = 0

        if self.name == "gnome_flamethrower":
            self.fire = Bullet("fire", self.rect.right + 64, self.rect.centery, self.damage_type, self.atk, 0, 0, "fire", self)

        if self.name == "bolotnik":
            targets[id(self)].hp = 0  # можно чтобы сразу килл и посмертные приколы не случались(по желанию)
            if self.upgrade_level == '2b':
                self.dead()
            elif self.upgrade_level == '3b':
                self.attack_cooldown = self.basic_attack_cooldown

        if self.name == "priest":
            self.heal = self.atk
            if targets[id(self)]:
                if targets[id(self)].name == 'krovnyak':
                    self.heal //= 2
                if targets[id(self)].rect.x - self.rect.x <= 128:
                    if targets[id(self)].max_hp - targets[id(self)].hp > self.heal:
                        targets[id(self)].hp += self.heal
                    else:
                        targets[id(self)].hp = targets[id(self)].max_hp
                else:
                    if targets[id(self)].max_hp - targets[id(self)].hp > self.heal//2:
                        targets[id(self)].hp += self.heal//2
                    else:
                        targets[id(self)].hp = targets[id(self)].max_hp
                targets[id(self)] = None

        # self.sound('shoot')

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
            self.atk2 = self.atk/10
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
                    self.atk_big = self.atk*3
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
                        if self.upgrade_level == "2b":
                            for i in range(2): # тут менять сколько пуль будет сначала спавниться
                                joska_schitayu_y = 16 * self.nakopleno + 16
                                spear_or_sword = choice(["light_spear", "light_sword"])
                                self.nakopleno += 1
                                bullet = Bullet(spear_or_sword, self.rect.centerx-28, self.rect.y+joska_schitayu_y, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, 'kopilka', self)
                                if i < 1:
                                    bullet.remove(bullets_group)
                                    self.spawned_things.append(bullet)
                        elif self.upgrade_level == "3b":
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

        if self.name == 'kar_mag':
            if self.v_falange <= 0:
                self.atkf = (self.atk/4)*3
                bullet = Bullet('karm', self.rect.centerx, self.rect.centery-48, self.damage_type, self.atkf,
                                self.bullet_speed_x, self.bullet_speed_y, 'kar_fal', self)
                self.spawned_things.append(bullet)
                bullet.remove(bullets_group)
                bullet = Bullet('karm', self.rect.centerx-24, self.rect.centery-24, self.damage_type, self.atkf,
                                self.bullet_speed_x, self.bullet_speed_y, 'kar_fal', self)
                self.spawned_things.append(bullet)
                bullet.remove(bullets_group)
                bullet = Bullet('karm', self.rect.centerx+24, self.rect.centery-24, self.damage_type, self.atkf,
                                self.bullet_speed_x, self.bullet_speed_y, 'kar_fal', self)
                self.spawned_things.append(bullet)
                bullet.remove(bullets_group)
                bullet = Bullet('karm', self.rect.centerx-32, self.rect.centery, self.damage_type, self.atkf,
                                self.bullet_speed_x, self.bullet_speed_y, 'kar_fal', self)
                self.spawned_things.append(bullet)
                bullet.remove(bullets_group)
                bullet = Bullet('karm', self.rect.centerx+32, self.rect.centery, self.damage_type, self.atkf,
                                self.bullet_speed_x, self.bullet_speed_y, 'kar_fal', self)
                self.spawned_things.append(bullet)
                bullet.remove(bullets_group)
                self.v_falange = 5

        if self.name == 'shabriri':
            if self.bezumie >= 75:
                self.kill()
                Creep('shiha', (self.rect.x, self.rect.y), self)

        if self.name == 'uvelir':
            self.gem = choice(self.gems)
            self.gems.remove(self.gem)
            if len(self.gems) <= 0:
                self.gems += self.basic_gems
            self.gem_bul = Bullet(self.gem, self.rect.centerx-32, self.rect.centery, self.damage_type, 0, self.bullet_speed_x, self.bullet_speed_y, self.gem, self)
            self.gem_bul.remove(bullets_group)

        if self.name == 'barrier_mag':
            if self.best_x.barrier:
                self.best_x.barrier.owner.have_barrier = False
                self.best_x.barrier.kill()
                # self.best_x.barrier.hp -= self.barrier_hp
                # if self.best_x.barrier.hp < 0:
                #     self.best_x.barrier.hp = 0
                # self.best_x.barrier.hp += self.barrier_hp
            if self.best_x.barrier not in all_sprites_group:
                self.best_x = self
                self.best_x = sorted(towers_group, key=self.sort_by_x)[-1]
                self.best_x.have_barrier = True
                self.best_x.barrier = Parasite('barrier', self.best_x.rect.centerx, self.best_x.rect.centery, '', 0, self.best_x, self)
                # if self.best_x.have_barrier:
                #     self.best_x.barrier.hp += self.barrier_hp
                #     self.best_x.barrier.parent = self
                # else:
                #     self.best_x.have_barrier = True
                #     self.best_x.barrier = Parasite('barrier', self.best_x.rect.centerx, self.best_x.rect.centery, '', 0, self.best_x, self)

        if self.name == 'vozmezdik':
            if self.col_vo_poglash > 0:
                self.col_vo_poglash = 0
                if self.col_vo_poglash < 3:
                    self.vulnerables_and_resists['piercing'] = -20
                    self.vulnerables_and_resists['slashing'] = -20
                    self.vulnerables_and_resists['bludgeoning'] = -20
                    self.vulnerables_and_resists['fire'] = -20
                    self.vulnerables_and_resists['water'] = -20
                    self.vulnerables_and_resists['ice'] = -20
                    self.vulnerables_and_resists['electric'] = -20
                    self.vulnerables_and_resists['poison'] = -20
                    self.vulnerables_and_resists['light'] = -20
                    self.vulnerables_and_resists['dark'] = -20
                elif 3 <= self.col_vo_poglash < 6:
                    self.vulnerables_and_resists['piercing'] = -40
                    self.vulnerables_and_resists['slashing'] = -40
                    self.vulnerables_and_resists['bludgeoning'] = -40
                    self.vulnerables_and_resists['fire'] = -40
                    self.vulnerables_and_resists['water'] = -40
                    self.vulnerables_and_resists['ice'] = -40
                    self.vulnerables_and_resists['electric'] = -40
                    self.vulnerables_and_resists['poison'] = -40
                    self.vulnerables_and_resists['light'] = -40
                    self.vulnerables_and_resists['dark'] = -40
                elif 6 <= self.col_vo_poglash < 9:
                    self.vulnerables_and_resists['piercing'] = -60
                    self.vulnerables_and_resists['slashing'] = -60
                    self.vulnerables_and_resists['bludgeoning'] = -60
                    self.vulnerables_and_resists['fire'] = -60
                    self.vulnerables_and_resists['water'] = -60
                    self.vulnerables_and_resists['ice'] = -60
                    self.vulnerables_and_resists['electric'] = -60
                    self.vulnerables_and_resists['poison'] = -60
                    self.vulnerables_and_resists['light'] = -60
                    self.vulnerables_and_resists['dark'] = -60
                elif 9 <= self.col_vo_poglash:
                    self.vulnerables_and_resists['piercing'] = -90
                    self.vulnerables_and_resists['slashing'] = -90
                    self.vulnerables_and_resists['bludgeoning'] = -90
                    self.vulnerables_and_resists['fire'] = -90
                    self.vulnerables_and_resists['water'] = -90
                    self.vulnerables_and_resists['ice'] = -90
                    self.vulnerables_and_resists['electric'] = -90
                    self.vulnerables_and_resists['poison'] = -90
                    self.vulnerables_and_resists['light'] = -90
                    self.vulnerables_and_resists['dark'] = -90

        if self.name == 'davalka':
            if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                casino = randint(1, 1000)
                if casino <= self.chance*10:
                    level.money += self.skolko_deneg_dast * self.multiplier
                    Alert('+'+str(self.skolko_deneg_dast * self.multiplier), (self.rect.centerx-15, self.rect.centery-55), 50, font30, (0, 70, 200))
                    self.chance = self.basic_chance
                else:
                    level.money += self.skolko_deneg_dast
                    Alert('+'+str(self.skolko_deneg_dast), (self.rect.centerx-15, self.rect.centery-55), 50, font30, (0, 70, 200))
                    self.chance += self.basic_chance
            else:
                level.money += self.skolko_deneg_dast
                Alert('+'+str(self.skolko_deneg_dast), (self.rect.centerx-15, self.rect.centery-55), 50, font30, (0, 70, 200))

    def sort_by_x(self, t):
        if t.rect.y == self.rect.y and (t.have_barrier is False or not t.barrier.parent or t.barrier.parent.name != 'barrier_mag'):
            return t.rect.x
        return 0

    def stop_hiding(self):
        self.hiding = True

    def animation(self):
        count_anim_frames = self.get_count_anim_frames()
        if 0 <= self.anim_count < self.anim_duration * count_anim_frames:
            if int(self.anim_count//self.anim_duration) != self.last_anim_frame:
                self.last_anim_frame = int(self.anim_count//self.anim_duration)
                if self.state == "wait":
                    self.image = towers_wait[self.name][int(self.anim_count//self.anim_duration)]
                if self.state == "attack":
                    if self.name in towers_attack:
                        self.image = towers_attack[self.name][int(self.anim_count//self.anim_duration)]
                if self.state == "give":
                    self.image = towers_give[self.name][int(self.anim_count//self.anim_duration)]
                if self.state == "hide":
                    self.image = towers_hide[self.name][int(self.anim_count//self.anim_duration)]
                if self.state == "death":
                    self.image = towers_death[self.name][int(self.anim_count//self.anim_duration)]

        if self.anim_count >= count_anim_frames * self.anim_duration:
            self.anim_count = 0
        else:
            self.anim_count += self.time_indicator

    def get_count_anim_frames(self):
        if self.state == "wait":
            return len(towers_wait[self.name])
        if self.state == "attack":
            return len(towers_attack[self.name])
        if self.state == "give":
            return len(towers_give[self.name])
        if self.state == "hide":
            return len(towers_hide[self.name])
        if self.state == "death":
            return len(towers_death[self.name])

    def move(self, change_pos):
        self.pos = self.pos[0], self.pos[1] + change_pos
        self.rect = self.image.get_rect(topleft=self.pos)

    def cooldown(self):                           # есть баг с перезарядкой, но там много всего должно сойтись и я пока забью
        if hasattr(self, "attack_cooldown"):      # там буквально 3 тика раз в 100 тиков голимые
            if self.attack_cooldown > 0:          # на определённой башне    !!!=
                self.attack_cooldown -= 1         # если я вам не скажу, вы и не заметите    ЗАМЕТИМ(наверн)
            else:
                # self.check_target_alive()         # если баг, то откоментить
                pass

        if self.anim_tasks:                          # порядок анимации
            if self.anim_tasks[0][1] > 0:            # -> self.anim_sequence = [("attack", 60, shoot), ("give", 50, spawn_something), ...]
                self.state = self.anim_tasks[0][0]   # -> какая анимация, время анимации, функция после анимации
                self.anim_tasks[0][1] -= 1
            elif self.anim_tasks[0][1] == 0:        # баг?
                self.anim_tasks[0][2]()
                self.anim_tasks[0][1] -= 1
                self.anim_tasks.pop(0)
        else:
            if hasattr(self, "attack_cooldown"):                    # если баг, то закоментить
                if self.attack_cooldown <= 0:                       #
                    self.check_target_alive()                       #
                else:                                               #
                    self.add_anim_task("wait", lambda: ...)         #
            else:                                                   #
                self.add_anim_task("wait", lambda: ...)             #
            # self.state = "wait"                                   # а это откоментить
            # self.add_anim_task("wait", lambda: print(1+1))        # не трогать

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
                elif self.name == 'uvelir':
                    if self.gem == '':
                        self.spawn_something_cooldown = self.basic_spawn_something_cooldown
                        self.add_anim_task("give", self.spawn_something)
                elif self.name == 'kar_mag':
                    if self.v_falange <= 0:
                        self.spawn_something_cooldown = self.basic_spawn_something_cooldown
                        self.add_anim_task("give", self.spawn_something)
                elif self.name == 'shabriri':
                    if self.bezumie >= 75:
                        self.add_anim_task("give", self.spawn_something)
                elif self.name == 'vozmezdik':
                    for enemy in enemies_group:
                        if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive and enemy.attack_range > 0:
                            self.vulnerables_and_resists['piercing'] = 0
                            self.vulnerables_and_resists['slashing'] = 0
                            self.vulnerables_and_resists['bludgeoning'] = 0
                            self.vulnerables_and_resists['fire'] = 0
                            self.vulnerables_and_resists['water'] = 0
                            self.vulnerables_and_resists['ice'] = 0
                            self.vulnerables_and_resists['electric'] = 0
                            self.vulnerables_and_resists['poison'] = 0
                            self.vulnerables_and_resists['light'] = 0
                            self.vulnerables_and_resists['dark'] = 0
                            self.vremya_casta = self.basic_vremya_casta
                            self.spawn_something_cooldown = self.basic_spawn_something_cooldown
                            self.add_anim_task("give", self.spawn_something)
                            break
                else:
                    self.spawn_something_cooldown = self.basic_spawn_something_cooldown
                    self.add_anim_task("give", self.spawn_something)

        if hasattr(self, "self_healing_cooldown"):
            if self.self_healing_cooldown >= 0:
                self.self_healing_cooldown -= 1
            else:
                self.self_healing_cooldown = self.basic_healing_cooldown

        if self.unvulnerable > 0:
            self.unvulnerable -= 1
            screen.blit(unvulnerable, (self.rect.centerx, self.rect.centery))  # noqa

        if self.name == 'ares':
            if self.cooldown_contratack > 0:
                if self.contrudar == 0:
                    self.cooldown_contratack -= 1
                    self.vulnerables_and_resists['piercing'] = 0
                    self.vulnerables_and_resists['slashing'] = 0
                    self.vulnerables_and_resists['bludgeoning'] = 0
                    self.vulnerables_and_resists['fire'] = 0
                    self.vulnerables_and_resists['water'] = 0
                    self.vulnerables_and_resists['ice'] = 0
                    self.vulnerables_and_resists['electric'] = 0
                    self.vulnerables_and_resists['poison'] = 0
                    self.vulnerables_and_resists['light'] = 0
                    self.vulnerables_and_resists['dark'] = 0
            else:
                if self.contrudar == 0:
                    self.contrudar = 1
                    self.time_contratack = 300
                    self.vulnerables_and_resists['piercing'] = -95
                    self.vulnerables_and_resists['slashing'] = -95
                    self.vulnerables_and_resists['bludgeoning'] = -95
                    self.vulnerables_and_resists['fire'] = -95
                    self.vulnerables_and_resists['water'] = -95
                    self.vulnerables_and_resists['ice'] = -95
                    self.vulnerables_and_resists['electric'] = -95
                    self.vulnerables_and_resists['poison'] = -95
                    self.vulnerables_and_resists['light'] = -95
                    self.vulnerables_and_resists['dark'] = -95
                if self.contrudar == 2 and self.time_contratack > 0:
                    self.time_contratack -= 1
                    self.add_anim_task("attack", self.shoot)
                    if self.time_contratack <= 0:
                        self.contrudar = 0
                        self.cooldown_contratack = 300

        if self.name == 'nekr':
            for creep in self.creeps:
                creep.krutaya_shtuka()

        if self.name == 'vozmezdik':
            if self.vremya_casta >= 0:
                self.vremya_casta -= 1

        if self.name == 'big_mechman' and (self.upgrade_level == '2b' or self.upgrade_level == '3b'):
            if self.big_mech_cooldown > 0:
                self.big_mech_cooldown -= 1

        if self.name == 'sekirshik' and self.upgrade_level == '2b':
            if self.spin_attack_cooldown > 0:
                self.spin_attack_cooldown -= 1

        if self.name == 'spike':
            if self.upgrade_level == '2a' or self.upgrade_level == '3a':
                if self.dengi_cooldown > 0:
                    self.dengi_cooldown -= 1
                else:
                    level.money += self.skolko_deneg_dast
                    Alert(str(self.skolko_deneg_dast), (self.rect.centerx-15, self.rect.centery-55), 50, font30, (0, 70, 200))
                    self.dengi_cooldown = self.basic_dengi_cooldown
            elif self.upgrade_level == '2b' or self.upgrade_level == '3b':
                for enemy in enemies_group:
                    if enemy in self.slowed_group:
                        if not self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                            if self.upgrade_level == '2b':
                                enemy.speed *= 1.25
                            elif self.upgrade_level == '3b':
                                enemy.speed *= 1.5
                            enemy.remove(self.slowed_group)
                    else:
                        if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):  # проблема в том что дамажит по ректу, а замедляет по поинту, но это самый адекватный вариант, так что эта проблема для нас не проблема
                            if self.upgrade_level == '2b':
                                enemy.speed /= 1.25
                            elif self.upgrade_level == '3b':
                                enemy.speed /= 1.5
                            enemy.add(self.slowed_group)
                    if self.upgrade_level == '3b':
                        if enemy in self.slowed_group2:
                            if not (self.great_rect.collidepoint(enemy.rect.centerx, enemy.rect.centery) and self.great_form) or self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                                enemy.speed *= 1.25
                                enemy.remove(self.slowed_group2)
                        else:
                            if self.great_rect.collidepoint(enemy.rect.centerx, enemy.rect.centery) and self.great_form and not self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                                enemy.speed /= 1.25
                                enemy.add(self.slowed_group2)
            if self.upgrade_level == '3b':
                if self.great_form:
                    if self.great_form_duration > 0:
                        self.great_form_duration -= 1
                        screen.blit(great_spike_form, (self.rect.centerx-192, self.rect.centery-192))
                    else:
                        self.great_form = False
                        self.great_form_duration = self.basic_great_form_duration

        if self.name == 'kot':
            if self.chill_time > 0:
                self.prime_anim("hide", self.stop_hiding)
                self.chill_time -= 1
                if self.upgrade_level == '3a':
                    for enemy in enemies_group:
                        if enemy not in self.slowed_group:
                            if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                                enemy.speed /= 2
                                enemy.add(self.slowed_group)
                        else:
                            if not self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                                enemy.speed *= 2
                                enemy.remove(self.slowed_group)
                if self.chill_time <= 0 and self.hiding:
                    towers_group.add(self)
                    nekusaemie_group.remove(self)
                    self.hiding = False

        if self.name == 'thunder' and (self.upgrade_level == '2b' or self.upgrade_level == '3b'):
            if self.golem_cooldown > 0:
                self.golem_cooldown -= 1
        
        if self.name == 'thunder_kamen' and self.upgrade_level == '3a':
            if self.revive_cooldown > 0:
                self.revive_cooldown -= 1
            else:
                self.new_tower = Tower('thunder', (self.rect.x, self.rect.y))
                self.new_tower.kamen_hp = self.hp
                self.kill()  # мб на деад надо поменять

        if hasattr(self, 'not_damaged_time'):
            if self.not_damaged_time > 0:
                self.not_damaged_time -= 1
                if self.not_damaged_time <= 0:
                    if self.name == 'krovnyak':
                        for krov in self.krovs:
                            if len(self.krovs) > 2:
                                self.hp += 35
                                krov.kill()
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp

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
                screen.blit(rage, (self.rect.centerx-24, self.rect.centery-48))

        if self.name == 'ded_moroz' and self.upgrade_level == '3a':  # надо чтобы миша сюда ещё и анимацию привязал, а то мне страшно туда лезть
            if not self.ice_form:
                if self.ice_form_cooldown <= 0:
                    self.ice_form_duration = self.basic_ice_form_duration
                    self.ice_form = True
                    self.time_indicator *= 2
                    self.basic_attack_cooldown //= 2
            else:
                if self.ice_form_duration <= 0:
                    self.ice_form_cooldown = self.basic_ice_form_cooldown
                    self.ice_form = False
                    self.time_indicator //= 2
                    self.basic_attack_cooldown *= 2
                screen.blit(rage, (self.rect.centerx-24, self.rect.centery-48))

        if self.name == 'drachun' and (self.upgrade_level == "2a" or self.upgrade_level == '3a'):
            if self.rage_cooldown <= 0:
                if not self.rage:
                    for enemy in enemies_group:
                        if (enemy.rect.y - self.rect.y <= 10 and self.rect.y - enemy.rect.y <= 10) and enemy.rect.x >= self.rect.x and enemy.rect.x - self.rect.x <= 256 and enemy.alive:
                            self.rage_duration = self.basic_rage_duration
                            self.rage = True
                            self.atk *= self.rage_amp
            else: 
                self.rage_cooldown -= 1

            if self.rage_duration > 0:
                self.rage_duration -= 1
            else:
                if self.rage:
                    self.rage_cooldown = self.basic_rage_cooldown
                    self.rage = False
                    self.atk = self.basic_atk
            if self.rage:
                screen.blit(rage, (self.rect.centerx-24, self.rect.centery-48))

    def draw2(self, surf):
        surf.blit(self.image2, self.rect2)
    
    def draw3(self, surf):
        surf.blit(self.image3, self.rect3)

    def sound(self, reason):
        # if reason == 'shoot':
        #     self.shoot_sound.set_volume(sound_effects_volume * general_volume)
        #     self.shoot_sound.play()
        # el
        if reason == 'death':
            # self.death_sound.set_volume(sound_effects_volume * general_volume)
            # self.death_sound.play()
            pass
            # sound = mixer.Sound(f"sounds/sound_effects/towers/death/{self.name}.ogg")
            # sound.set_volume(sound_effects_volume * general_volume)
            # sound.play()

    def update(self):
        if self.onyx_barrier:
            self.image3 = font30.render(str(self.onyx_barrier.hp), True, (0, 0, 200))
            self.rect3 = self.image.get_rect(topleft=(self.rect.x + 32, self.rect.y - 64))
        if self.hp <= 0:
            if not level.no_death_animation:
                self.alive = False
                self.prime_anim("death", self.dead)
            else:
                self.dead()
            # self.hp = 0
        if self.name == 'knight_on_horse':
            if self.horse_hp <= 0 or self.knight_hp <= 0:
                if not level.no_death_animation:
                    self.alive = False
                    self.prime_anim("death", self.dead)
                else:
                    self.dead()
        if self.name == 'prokach':
            for i in range(self.mech_level):
                screen.blit(rage, (self.rect.right-(24*i), self.rect.centery-48))

        if not self.stunned:
            self.cooldown()
            self.animation()
            self.image2 = font30.render(str(self.hp), True, (0, 0, 0))
            self.rect2 = self.image.get_rect(topleft=(self.rect.x + 32, self.rect.y - 32))

            if hasattr(self, "bursting"):
                if self.bursting:   # == True
                    if self.attack_cooldown_burst > 0:
                        self.attack_cooldown_burst -= 1
                    else:
                        self.attack_cooldown_burst = self.basic_attack_cooldown_burst
                        self.burst_attack()

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
        self.image = image.load(f"images/enemies/{name}/wait/{name}1.png").convert_alpha()
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
        self.parasites = set()
        self.only_one_hit_bullets = set()

        self.pushed = False
        self.damaged = False
        self.gribs = 0
        self.snegs = 0
        self.sliz = None
        self.not_oneshot = sprite.Group()  # для секирщика
        self.slowed = False
        self.slowed_time = 0
        self.stunned = False
        self.stunned_time = 0
        self.banished = False
        self.vulnerabled = 0  # x2
        self.vulnerables_and_resists = {}  # dict()  # 'damage_type' : resist%
        self.heavy = False

        targets[id(self)] = None
        self.time_indicator = 1
        self.anim_tasks = []
        self.anim_count = 0
        self.anim_duration = 15     # сколько кадров будет оставаться 1 спрайт
        self.state = "wait"
        self.anim_stage = "default"
        self.last_anim_frame = -1

        # СТАТЫ начало

        if self.name == 'popusk':
            self.hp = self.max_hp = 250
            self.atk = 10
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'bludgeoning'

        if self.name == 'josky':
            self.hp = self.max_hp = 500
            self.atk = 10
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'bludgeoning'

        if self.name == 'sigma':
            self.hp = self.max_hp = 1000
            self.atk = 20
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'bludgeoning'

        if self.name == 'armorik':
            self.hp = self.max_hp = 375
            self.armor = 375
            self.have_armor = True
            self.atk = 10
            self.atk2 = self.atk * 1.5  # 150
            self.speed = 0.5
            self.speed2 = 1
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'bludgeoning'
            self.vulnerables_and_resists['piercing'] = -25
            self.vulnerables_and_resists['slashing'] = -25
            self.vulnerables_and_resists['bludgeoning'] = -25

        if self.name == 'slabiy':
            self.hp = self.max_hp = 125
            self.atk = 5
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'slashing'
            self.back_to_line()

        if self.name == 'rojatel':
            self.hp = self.max_hp = 625
            self.atk = 5
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'slashing'

        if self.name == 'tyazhik':
            self.hp = self.max_hp = 1000
            self.atk = 5
            self.speed = 0.25
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.heavy = True
            self.damage_type = 'bludgeoning'

        if self.name == 'sportik':  # надо пофиксить таргеты у пукиша
            self.hp = self.max_hp = 250
            self.atk = 14
            self.speed = 1
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'slashing'

        if self.name == 'klonik':
            self.hp = self.max_hp = 250
            self.atk = 10
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.klonirovanie_cooldown = self.basic_klonirovanie_cooldown = 900
            self.attack_range = 0
            self.damage_type = 'slashing'

        if self.name == 'teleportik':
            self.hp = self.max_hp = 250
            self.atk = 10
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.tp_cooldown = self.basic_tp_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'piercing'

        if self.name == 'fire_res':
            self.hp = self.max_hp = 100
            self.atk = 5
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'fire'
            self.vulnerables_and_resists['fire'] = -100

        if self.name == 'ice_res':
            self.hp = self.max_hp = 100
            self.atk = 5
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'ice'
            self.vulnerables_and_resists['ice'] = -100

        if self.name == 'water_res':
            self.hp = self.max_hp = 100
            self.atk = 5
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'water'
            self.vulnerables_and_resists['water'] = -100

        if self.name == 'poison_res':
            self.hp = self.max_hp = 100
            self.atk = 5
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'poison'
            self.vulnerables_and_resists['poison'] = -100

        if self.name == 'light_res':
            self.hp = self.max_hp = 100
            self.atk = 5
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'light'
            self.vulnerables_and_resists['light'] = -100

        if self.name == "zeleniy_strelok":
            self.hp = self.max_hp = 250
            self.atk = 7.5
            self.bullet_speed_x = -5
            self.bullet_speed_y = 0
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 700
            self.bullets = 1
            self.damage_type = 'piercing'

        if self.name == "telezhnik":
            self.hp = self.max_hp = 460
            self.armor = 40
            self.have_armor = True
            self.atk = 8
            self.atk2 = self.atk * 1.25  # 100
            self.bullet_speed_x = -5
            self.bullet_speed_y = 0
            self.speed = 0.5
            self.speed2 = 1
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 768
            self.attack_range2 = 0
            self.bullets = 1
            self.damage_type = 'piercing'

        if self.name == "drobik":
            self.hp = self.max_hp = 550
            self.atk = 7
            self.bullet_speed_x = -5
            self.bullet_speed_y = 4
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.attack_range = 128
            self.bullets = 3
            self.damage_type = 'piercing'

        if self.name == 'mega_strelok':
            self.hp = self.max_hp = 750
            self.atk = 10
            self.bullet_speed_x = -5
            self.bullet_speed_y = 0
            self.speed = 0.25
            self.attack_cooldown_burst = self.basic_attack_cooldown_burst = 4
            self.attack_cooldown = self.basic_attack_cooldown = 600
            self.ammo = self.basic_ammo = 30
            self.attack_range = 640
            self.bullets = 1
            self.bursting = False
            self.damage_type = 'piercing'

        # СТАТЫ конец
        self.image2 = font30.render(str(self.hp), True, (0, 0, 0))

    def shoot(self):
        if targets[id(self)] == self.sliz:  # с мегастрелком разберусь позже
            targets[id(self)].hp -= self.atk * self.bullets
        else:
            if self.name == "zeleniy_strelok" or self.name == 'telezhnik':
                Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, "zeleniy_strelok_bullet", self)

            if self.name == 'drobik':
                Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, 0, "anti_hrom", self)
                if self.rect.centery-138 >= 192:
                    Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y*-1, "anti_hrom", self)
                if self.rect.centery+138 <= 832:
                    Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, "anti_hrom", self)

        if self.name == 'mega_strelok':
            self.bursting = True

    def burst_attack(self):
        if self.name == 'mega_strelok':
            if self.ammo > 0:
                Bullet(self.name + "_bullet", self.rect.centerx, self.rect.centery+randint(-16, 16), self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, "zeleniy_strelok_bullet", self)
                self.ammo -= 1
            else:
                self.ammo = self.basic_ammo
                self.attack_cooldown = self.basic_attack_cooldown
                self.bursting = False

    def melee_attack(self):
        # if self.name == "popusk":
        #     targets[id(self)].hp -= self.atk
        if targets[id(self)].alive:
            if targets[id(self)] == self.sliz:
                targets[id(self)].hp -= self.atk
            elif targets[id(self)]:
                if hasattr(targets[id(self)], 'barrier') and targets[id(self)].barrier:                     # проверка барьера
                    targets[id(self)].barrier.hp -= self.atk
                elif hasattr(targets[id(self)], 'onyx_barrier') and targets[id(self)].onyx_barrier:                     # проверка барьера
                    targets[id(self)].onyx_barrier.hp -= self.atk
                elif targets[id(self)].name == 'knight_on_horse':      # проверка на коня
                    targets[id(self)].horse_hp -= self.atk
                else:
                    self.damage = self.atk
                    if targets[id(self)].unvulnerable > 0:
                        self.damage = 0
                    for k, v in targets[id(self)].vulnerables_and_resists.items():
                        if k == self.damage_type:
                            self.damage *= (100 + v)/100
                    if targets[id(self)].name == 'ares' and targets[id(self)].contrudar == 1:
                        targets[id(self)].contrudar = 2
                        if self.damage_type == 'clean':
                            targets[id(self)].vpitano_damaged += self.damage//20
                        else:
                            targets[id(self)].vpitano_damaged += self.damage
                    elif targets[id(self)].name == 'ares' and targets[id(self)].contrudar == 2:  # проверка на контратаку
                        targets[id(self)].vpitano_damaged += self.damage
                    targets[id(self)].hp -= self.damage
                    targets[id(self)].damaged = True
                    # if targets[id(self)].name == 'terpila' and (targets[id(self)].upgrade_level == '2b' or targets[id(self)].upgrade_level == '3b' or targets[id(self)].upgrade_level == '3a'):
                    #     targets[id(self)].received_damage += self.damage
                    if hasattr(targets[id(self)], 'received_damage'):
                        targets[id(self)].received_damage += self.damage
                    targets[id(self)].check_hp()
                for parasite in self.parasites:
                    if parasite.name == 'metka_inq':
                        parasite.cashback_list.append(225)
        else:
            targets[id(self)] = None

    def movement(self):
        if not self.stunned:
            if not self.stop:
                self.real_x -= self.speed
                if self.sliz:
                    self.stop = True

            if not self.slowed and self.snegs >= 3:
                self.speed /= 2
                self.slowed = True
            if self.slowed and self.snegs >= 7:
                self.snegs -= 7
                for i in range(7):
                    for parasite in parasites_group:
                        if parasite.owner == self and parasite.name == 'sneg_parasite':
                            parasite.kill()
                            break
                self.stunned = True
                self.stunned_time += 225
                self.slowed_time = 150
            if self.slowed_time > 0 and self.slowed:
                self.slowed_time -= 1
                if self.slowed_time <= 0:
                    self.speed *= 2
                    self.slowed = False

        self.rect.x = int(self.real_x)
        self.rect.y = int(self.real_y)

    def back_to_line(self):
        if (self.real_y-192) % 128 < 64:
            self.real_y -= (self.real_y-192) % 128
        else:
            self.real_y += 128 - ((self.real_y-192) % 128)
        if self.real_y > 704:
            self.real_y -= 128
        elif self.real_y < 192:
            self.real_y += 128

    def add_anim_task(self, anim, func):
        if len(self.anim_tasks) == 0:
            self.anim_tasks.append([anim, (self.get_count_anim_frames() * self.anim_duration) // self.time_indicator - 1, func])
            self.anim_count = 0
        else:
            already_in = [anim[0] for anim in self.anim_tasks]
            if anim not in already_in:
                self.anim_tasks.append([anim, (self.get_count_anim_frames() * self.anim_duration) // self.time_indicator - 1, func])

    def prime_anim(self, anim, func):
        if anim not in [an[0] for an in self.anim_tasks]:
            self.anim_tasks.clear()
            self.add_anim_task(anim, func)

    def animation(self):
        count_anim_frames = self.get_count_anim_frames()
        if 0 <= self.anim_count < self.anim_duration * count_anim_frames:
            if int(self.anim_count//self.anim_duration) != self.last_anim_frame:
                self.last_anim_frame = int(self.anim_count//self.anim_duration)
                if self.state == "wait":
                    self.image = enemies_wait[self.name][int(self.anim_count // self.anim_duration)]
                if self.state == "attack":
                    self.image = enemies_attack[self.name][int(self.anim_count//self.anim_duration)]
                if self.state == "move":
                    self.image = enemies_move[self.name][int(self.anim_count//self.anim_duration)]
                if self.state == "death":
                    self.image = enemies_death[self.name][int(self.anim_count//self.anim_duration)]

                if self.state == "rage_wait":
                    self.image = enemies_rage_wait[self.name][int(self.anim_count // self.anim_duration)]
                if self.state == "rage_attack":
                    self.image = enemies_rage_attack[self.name][int(self.anim_count//self.anim_duration)]
                if self.state == "rage_move":
                    self.image = enemies_rage_move[self.name][int(self.anim_count//self.anim_duration)]

        if self.anim_count >= count_anim_frames * self.anim_duration:   # 4 -- так как в анимации 4 кадра
            self.anim_count = 0
        else:
            self.anim_count += self.time_indicator
            # , zeleniy_strelok, sportik, rojatel, mega_strelok, slabiy, armorik, telezhnik, drobik

    def get_count_anim_frames(self):
        if self.state == "wait":
            return len(enemies_wait[self.name])
        if self.state == "attack":
            return len(enemies_attack[self.name])
        if self.state == "move":
            return len(enemies_move[self.name])
        if self.state == "rage_wait":
            return len(enemies_rage_wait[self.name])
        if self.state == "rage_attack":
            return len(enemies_rage_attack[self.name])
        if self.state == "rage_move":
            return len(enemies_rage_move[self.name])
        if self.state == "death":
            return len(enemies_death[self.name])

    def armor_check(self):
        if hasattr(self, "armor") and self.have_armor:
            if self.armor <= 0:
                if self.name == 'armorik':
                    self.atk *= 1.5
                    self.speed = self.speed2
                    del self.vulnerables_and_resists['piercing']
                    del self.vulnerables_and_resists['slashing']
                    del self.vulnerables_and_resists['bludgeoning']
                    self.have_armor = False
                    self.anim_stage = "rage"

                elif self.name == 'telezhnik':
                    self.atk *= 1.25
                    self.speed = self.speed2
                    self.have_armor = False
                    self.attack_range = self.attack_range2
                    self.anim_stage = "rage"

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

        self.kill()

    def check_hp(self):
        if self.hp <= 0:
            self.alive = False
            self.stunned = False
            self.stunned_time = 0
            if not level.no_death_animation:
                self.stop = True
                self.prime_anim("death", self.dead)
            else:
                self.dead()

        if not self.stunned:
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
                    for tower in towers_group:
                        targets[id(tower)] = None  # если будет лагать закомментить

        self.damaged = False

    def find_target(self):
        for entity in [*towers_group, *creeps_group]:
            if -64 < entity.rect.centery - self.rect.centery < 64 and -64 < self.rect.centerx - entity.rect.centerx < self.attack_range + 64 and self.rect.x < 1472 and entity.alive:
                self.stop = True
                return entity
        
        for entity in neutral_objects_group:
            if entity.height == 'high':
                if -64 < entity.rect.centery - self.rect.centery < 64 and -64 < self.rect.centerx - entity.rect.centerx < self.attack_range + 64 and self.rect.x < 1472 and entity.alive:
                    self.stop = True
                    return entity

        self.stop = False
        return None

    def check_target_alive(self):
        if targets[id(self)]:
            if targets[id(self)].rect.x < self.rect.centerx or targets[id(self)].name == 'sliz_luja_parasite' or targets[id(self)].name == 'kot':
                targets[id(self)] = None

        if self.sliz:
            targets[id(self)] = self.sliz

        if targets[id(self)]:
            if targets[id(self)].alive:
                self.attack_cooldown = self.basic_attack_cooldown
                if self.attack_range == 0:
                    if self.anim_stage == "default":
                        self.add_anim_task("attack", self.melee_attack)
                    if self.anim_stage == "rage":
                        self.add_anim_task("rage_attack", self.melee_attack)
                if self.attack_range > 0:
                    if self.anim_stage == "default":
                        self.add_anim_task("attack", self.shoot)
                    if self.anim_stage == "rage":
                        self.add_anim_task("rage_attack", self.shoot)
            else:
                targets[id(self)] = self.find_target()
                if targets[id(self)]:
                    if targets[id(self)].alive:
                        self.attack_cooldown = self.basic_attack_cooldown
                        if self.attack_range == 0:
                            if self.anim_stage == "default":
                                self.add_anim_task("attack", self.melee_attack)
                            if self.anim_stage == "rage":
                                self.add_anim_task("rage_attack", self.melee_attack)
                        if self.attack_range > 0:
                            if self.anim_stage == "default":
                                self.add_anim_task("attack", self.shoot)
                            if self.anim_stage == "rage":
                                self.add_anim_task("rage_attack", self.shoot)
                else:
                    if self.anim_stage == "default":
                        if self.stop:
                            self.add_anim_task("wait", lambda: ...)
                        else:
                            self.add_anim_task("move", lambda: ...)
                    if self.anim_stage == "rage":
                        if self.stop:
                            self.add_anim_task("rage_wait", lambda: ...)
                        else:
                            self.add_anim_task("rage_move", lambda: ...)

        else:
            targets[id(self)] = self.find_target()
            if targets[id(self)]:
                if targets[id(self)].alive:
                    self.attack_cooldown = self.basic_attack_cooldown
                    if self.attack_range == 0:
                        if self.anim_stage == "default":
                            self.add_anim_task("attack", self.melee_attack)
                        if self.anim_stage == "rage":
                            self.add_anim_task("rage_attack", self.melee_attack)
                    if self.attack_range > 0:
                        if self.anim_stage == "default":
                            self.add_anim_task("attack", self.shoot)
                        if self.anim_stage == "rage":
                            self.add_anim_task("rage_attack", self.shoot)
            else:
                if self.anim_stage == "default":
                    if self.stop:
                        self.add_anim_task("wait", lambda: ...)
                    else:
                        self.add_anim_task("move", lambda: ...)
                if self.anim_stage == "rage":
                    if self.stop:
                        self.add_anim_task("rage_wait", lambda: ...)
                    else:
                        self.add_anim_task("rage_move", lambda: ...)

    def in_stun(self):
        if self.stunned_time > 0:
            self.stunned_time -= 1
            if self.stunned_time <= 0:
                self.stunned = False

    def cooldown(self):
        if hasattr(self, "attack_cooldown"):      # там буквально 3 тика раз в 100 тиков голимые
            if self.attack_cooldown > 0:          # на определённой башне    !!!=
                self.attack_cooldown -= 1         # если я вам не скажу, вы и не заметите    ЗАМЕТИМ(наверн)

        if hasattr(self, "bursting"):
            if self.bursting:   # == True
                if self.attack_cooldown_burst > 0:
                    self.attack_cooldown_burst -= 1
                else:
                    self.attack_cooldown_burst = self.basic_attack_cooldown_burst
                    self.burst_attack()

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

        if self.vulnerabled > 0:
            self.vulnerabled -= 1

        if self.anim_tasks:                          # порядок анимации
            if self.anim_tasks[0][1] > 0:            # -> self.anim_tasks = [("attack", 60, shoot), ("give", 50, spawn_something), ...]
                self.state = self.anim_tasks[0][0]   # -> какая анимация, время анимации, функция после анимации
                self.anim_tasks[0][1] -= 1
            elif self.anim_tasks[0][1] == 0:        # баг?
                self.anim_tasks[0][2]()
                self.anim_tasks[0][1] -= 1
                self.anim_tasks.pop(0)
        else:
            if hasattr(self, "attack_cooldown"):                            # если баг, то закоментить
                if self.attack_cooldown <= 0:                               #
                    self.check_target_alive()                               #
                else:                                                       #
                    if self.anim_stage == "default":                        #
                        if self.stop:                                       #
                            self.add_anim_task("wait", lambda: ...)         #
                        else:                                               #
                            self.add_anim_task("move", lambda: ...)         #
                    if self.anim_stage == "rage":                           #
                        if self.stop:                                       #
                            self.add_anim_task("rage_wait", lambda: ...)    #
                        else:                                               #
                            self.add_anim_task("rage_move", lambda: ...)    #

    def update(self):
        if not self.stunned:
            self.cooldown()
            self.animation()
            self.armor_check()
        else:
            self.in_stun()

        self.movement()
        self.image2 = font30.render(str(self.hp), True, (0, 0, 0))
        self.rect2 = self.image.get_rect(topleft=(self.rect.x + 32, self.rect.y - 32))

        if self.alive:
            self.check_hp()


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
        self.onyx_barrier = None
        self.target = None
        if hasattr(self.parent, 'creeps'):
            self.parent.creeps.add(self)
            self.summon_cooldown = self.parent.basic_attack_cooldown  # решил сюда табнуть тк это вроде тожу чисто некрская тема
        self.stunned = False
        self.banished = False
        self.vulnerabled = 0
        self.vulnerables_and_resists = {}  # dict()  # 'damage_type' : resist%  # fake
        self.unvulnerable = 0

        if self.name == 'nekr_skelet':
            self.hp = self.max_hp = 10
            self.atk = 40
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            if self.parent.upgrade_level == '2a':
                self.speed = 1
            if self.parent.upgrade_level == '3a':
                self.speed = 1.5
            self.damage_type = 'piercing'

        if self.name == 'nekr_zombie':
            self.hp = self.max_hp = 20
            self.atk = 50
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'slashing'

        if self.name == 'nekr_zombie_jirny':
            self.hp = self.max_hp = 50
            self.atk = 130
            self.speed = 0.5
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.attack_range = 0
            self.damage_type = 'bludgeoning'

        if self.name == 'mini_golem':
            self.hp = self.max_hp = 15
            self.atk = 0
            self.speed = 0.25
            self.attack_cooldown = self.basic_attack_cooldown = 0
            self.attack_range = 0
            self.damage_type = 'bludgeoning'
            self.vulnerables_and_resists['poison'] = -100
            self.vulnerables_and_resists['piercing'] = -25
            self.vulnerables_and_resists['slashing'] = -25
            self.vulnerables_and_resists['bludgeoning'] = 50

        if self.name == 'big_golem':
            self.hp = self.max_hp = 45
            self.atk = 0
            self.speed = 0.25
            self.attack_cooldown = self.basic_attack_cooldown = 0
            self.attack_range = 0
            self.damage_type = 'bludgeoning'
            self.vulnerables_and_resists['poison'] = -100
            self.vulnerables_and_resists['piercing'] = -25
            self.vulnerables_and_resists['slashing'] = -25
            self.vulnerables_and_resists['bludgeoning'] = 50

        if self.name == 'mega_golem':
            self.hp = self.max_hp = 135
            self.atk = 0
            self.speed = 0.25
            self.attack_cooldown = self.basic_attack_cooldown = 0
            self.attack_range = 0
            self.damage_type = 'bludgeoning'
            self.vulnerables_and_resists['poison'] = -100
            self.vulnerables_and_resists['piercing'] = -25
            self.vulnerables_and_resists['slashing'] = -25
            self.vulnerables_and_resists['bludgeoning'] = 50

        if self.name == 'nekr_skelet_strelok':
            self.hp = self.max_hp = 10
            self.atk = 70
            self.speed = 0.5
            self.bullet_speed_x = 5
            self.bullet_speed_y = 0
            self.attack_cooldown = self.basic_attack_cooldown = 120
            self.attack_range = 256
            if self.parent.upgrade_level == '2a':
                self.speed = 1
            if self.parent.upgrade_level == '3a':
                self.speed = 1.5
            self.damage_type = 'piercing'

        if self.name == 'shiha':
            self.hp = parent.hp
            self.atk = 80
            self.speed = 1
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.attack_range = 0
            self.damage_type = 'fire'
            self.vulnerables_and_resists['piercing'] = -50
            self.vulnerables_and_resists['slashing'] = -50
            self.vulnerables_and_resists['bludgeoning'] = -50
            self.vulnerables_and_resists['fire'] = -75

        self.back_to_line()

    def is_should_stop_to_attack(self):
        for enemy in enemies_group:
            if -64 < enemy.rect.centery - self.rect.centery < 64 and -64 < enemy.rect.centerx - self.rect.centerx < self.attack_range + 64 and self.rect.centerx > 384:
                return True, enemy
        for enemy in neutral_objects_group:
            if enemy.height == 'high':
                if -64 < enemy.rect.centery - self.rect.centery < 64 and -64 < enemy.rect.centerx - self.rect.centerx < self.attack_range + 64 and self.rect.centerx > 384:
                    return True, enemy
        return False, None

    def preparing_to_attack(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.attack_cooldown = self.basic_attack_cooldown
            if self.stop and not(self.name == 'mini_golem' or self.name == 'big_golem' or self.name == 'mega_golem'):
                if self.attack_range == 0:
                    self.melee_attack()
                if self.attack_range > 0:
                    self.shoot()

    def melee_attack(self):
        if self.target:
            self.dealing_damage(self.target)

    def shoot(self):
        if self.name == 'nekr_skelet_strelok':
            Bullet('bone_arrow', self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, self.bullet_speed_y, "default", self)

    def dealing_damage(self, enemy):
        self.damage = self.atk
        if enemy.vulnerabled > 0:
            self.damage *= 2
        for k, v in enemy.vulnerables_and_resists.items():
            if k == self.damage_type:
                self.damage *= (100 + v)/100
        if hasattr(enemy, 'armor') and enemy.armor > 0:
            if self.damage <= enemy.armor:
                enemy.armor -= self.damage
            else:
                enemy.hp -= (self.damage - enemy.armor)
                enemy.armor = 0
        else:
            enemy.hp -= self.damage
        enemy.damaged = True
        if enemy.alive:
            enemy.check_hp()

    def movement(self):
        if not self.stop:
            self.real_x += self.speed
        self.rect.x = int(self.real_x)
        self.rect.y = int(self.real_y)

    def check_hp(self):
        if self.hp <= 0 or self.rect.x > 1700 or (self.parent not in all_sprites_group and not(self.name == 'mini_golem' or self.name == 'big_golem' or self.name == 'mega_golem' or self.name == 'shiha')):
            self.alive = False
            self.kill()
            if hasattr(self.parent, 'creeps'):
                self.parent.creeps.add(self)

    def back_to_line(self):
        if (self.real_y-192) % 128 < 64:
            # self.rect.y -= (self.rect.y-192) % 128
            self.real_y -= (self.real_y-192) % 128
        else:
            # self.rect.y += 128 - ((self.rect.y-192) % 128)
            self.real_y += 128 - ((self.real_y-192) % 128)
        if self.real_y > 704:
            self.real_y -= 128
        elif self.real_y < 192:
            self.real_y += 128

    def krutaya_shtuka(self):  # её не надо в апдейт потому что я сигма  # чисто некрская тема
        if self.summon_cooldown > 0:
            self.summon_cooldown -= 1
        else:
            if self not in all_sprites_group:
                self.parent.creeps.remove(self)
                self.parent.check_target_alive()

    def update(self):
        self.stop, self.target = self.is_should_stop_to_attack()

        self.preparing_to_attack()
        self.movement()
        if self.alive:
            self.check_hp()


class NeutralObject(sprite.Sprite):
    def __init__(self, unit, pos):
        super().__init__(neutral_objects_group, all_sprites_group)
        self.image = image.load(f"images/neutral_objects/{unit}.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.rect2 = self.image.get_rect(topleft=(self.rect.x + 32, self.rect.y - 32))
        self.pos = pos
        self.name = unit
        self.render_layer = 4

        self.target = None
        self.parasite_parents = set()
        self.parasites = set()
        self.only_one_hit_bullets = set()

        self.is_dead = False
        self.alive = True
        self.damaged = False
        self.pushed = False
        self.gribs = 0
        self.snegs = 0
        self.sliz = None
        self.not_oneshot = sprite.Group()  # для секирщика
        self.slowed = False
        self.slowed_time = 0
        self.stunned = False
        self.stunned_time = 0
        self.banished = False
        self.unvulnerable = 0
        self.vulnerabled = 0
        self.vulnerables_and_resists = {}  # dict()  # 'damage_type' : resist%
        self.heavy = True
        self.speed = 0
        self.atk = 0

        # self.time_indicator = 1
        # self.anim_tasks = []
        # self.anim_count = 0
        # self.last_anim_frame = -1
        # self.anim_duration = 15     # сколько кадров будет оставаться 1 спрайт
        # self.state = "wait"         # потом будет "attack", "death" и какие придумаете


        # СТАТЫ начало

        if self.name == 'block':
            self.hp = self.max_hp = 500
            self.height = 'high'

        if self.name == 'block_mana':
            self.hp = self.max_hp = 500
            self.skolko_deneg_dast = 50
            self.height = 'high'

        if self.name == 'block_bomb':
            self.hp = self.max_hp = 500
            self.atk = 150
            self.rect_bomb = Rect(self.rect.left-128, self.rect.top-128, 384, 384)
            self.height = 'high'
            self.damage_type = 'fire'

        if self.name == 'luja':
            self.hp = self.max_hp = 1
            self.luja_capacity = 3
            self.height = 'low'

        if self.name == 'strelka_up' or self.name == 'strelka_down':
            self.hp = self.max_hp = 1
            self.height = 'low'

        # СТАТЫ конец

        self.image2 = font30.render(str(self.hp), True, (0, 0, 0))

    def dead(self):
        if self.name == 'block_mana':
            level.money += self.skolko_deneg_dast
        if self.name == 'block_bomb':
            Bullet('explosion', self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'visual_effect', self)
            for enemy in enemies_group:
                if self.rect_bomb.colliderect(enemy.rect):
                    self.dealing_damage(enemy)
            for creep in creeps_group:
                if self.rect_bomb.colliderect(creep.rect):
                    self.dealing_damage(creep)
            for tower in towers_group:
                if self.rect_bomb.colliderect(tower.rect):
                    self.dealing_damage(tower)
            for neutral_object in neutral_objects_group:
                if self.rect_bomb.colliderect(neutral_object.rect):
                    self.dealing_damage(neutral_object)
        self.kill()

    def check_hp(self):
        if self.hp <= 0 :
            self.alive = False
            self.dead()
        self.image2 = font30.render(str(self.hp), True, (0, 0, 0))

    def omagad(self):
        if self.name == 'luja':
            if self.luja_capacity > 0:
                for enemy in enemies_group:
                    if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                        enemy.hp = 0
                        self.luja_capacity -= 1
                for creep in creeps_group:
                    if self.rect.collidepoint(creep.rect.centerx, creep.rect.centery):
                        creep.hp = 0
                        self.luja_capacity -= 1
            else:
                self.alive = False
                self.dead()

        if self.name == 'strelka_up':
            for enemy in enemies_group:
                if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.bottom-1):
                    enemy.angle = atan2(self.rect.centery-128 - enemy.rect.centery, 0)
                    enemy.y_vel = sin(enemy.angle) * enemy.speed * 6
                    enemy.real_y += enemy.y_vel
                if self.rect.centery-138 <= enemy.rect.centery <= self.rect.centery-118:
                    enemy.back_to_line()
            for creep in creeps_group:
                if self.rect.collidepoint(creep.rect.centerx, creep.rect.bottom-1):
                    creep.angle = atan2(self.rect.centery-128 - creep.rect.centery, 0)
                    creep.y_vel = sin(creep.angle) * creep.speed * 6
                    creep.real_y += creep.y_vel
                if self.rect.centery-138 <= creep.rect.centery <= self.rect.centery-118:
                    creep.back_to_line()

        if self.name == 'strelka_down':
            for enemy in enemies_group:
                if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.top+1):
                    enemy.angle = atan2(self.rect.centery+128 - enemy.rect.centery, 0)
                    enemy.y_vel = sin(enemy.angle) * enemy.speed * 6
                    enemy.real_y += enemy.y_vel
                if self.rect.centery+118 <= enemy.rect.centery <= self.rect.centery+138:
                    enemy.back_to_line()
            for creep in creeps_group:
                if self.rect.collidepoint(creep.rect.centerx, creep.rect.top+1):
                    creep.angle = atan2(self.rect.centery+128 - creep.rect.centery, 0)
                    creep.y_vel = sin(creep.angle) * creep.speed * 6
                    creep.real_y += creep.y_vel
                if self.rect.centery+118 <= creep.rect.centery <= self.rect.centery+138:
                    creep.back_to_line()
            
    def dealing_damage(self, enemy):
        self.damage = self.atk
        if enemy.vulnerabled > 0:
            self.damage *= 2
        for k, v in enemy.vulnerables_and_resists.items():
            if k == self.damage_type:
                self.damage *= (100 + v)/100
        if hasattr(enemy, 'armor') and enemy.armor > 0:
            if self.damage <= enemy.armor:
                enemy.armor -= self.damage
            else:
                enemy.hp -= (self.damage - enemy.armor)
                enemy.armor = 0
        else:
            enemy.hp -= self.damage
        enemy.damaged = True
        if enemy.alive:
            enemy.check_hp()

    def cooldown(self):
        pass

    def update(self):
        self.omagad()
        self.cooldown()
        self.check_hp()


class Bullet(sprite.Sprite):
    def __init__(self, bullet_sprite, x, y, damage_type, atk, speed_x, speed_y, name, parent):
        super().__init__(all_sprites_group, bullets_group)
        self.image = image.load(f"images/bullets/{bullet_sprite}/move/{bullet_sprite}1.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.render_layer = 7
        self.bullet_sprite = bullet_sprite  # так надо
        self.damage_type = damage_type
        self.atk = self.basic_atk = atk
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.name = name
        self.parent = parent
        self.penned = False
        self.target = None
        self.zloy = False

        self.time_indicator = 1
        self.anim_tasks = []
        self.anim_count = 0
        self.last_anim_frame = -1
        self.anim_duration = 15     # сколько кадров будет оставаться 1 спрайт
        self.state = "move"         # потом будет "attack", "death" и какие придумаете

        self.death_sound = mixer.Sound(f"sounds/sound_effects/bullets/death/fireball.ogg")
        # ^^^ потом поменять на self.death_sound = mixer.Sound(f"sounds/sound_effects/bullets/death/{bullet_sprite}.ogg")

        if self.name == "zeleniy_strelok_bullet" or self.name == 'anti_hrom':
            self.zloy = True

        if self.name == 'ls':
            self.off = 30
        if self.name == 'visual_effect' or self.name == 'explosion' or self.name == 'joltiy_explosion' or self.name == 'opal_explosion' or self.name == "mech" or self.name == 'razlet' or self.name == 'holod_row'  or self.name == 'razriv':
            self.off = 20
            if self.name == 'razlet':
                self.pushl = 128
        if self.name == "drachun_gulag" or self.name == "drachun_gulag_splash" or self.name == "tolkan_bux":
            self.off = 15
        if self.name == "klonys_punch":
            self.mimo = True
            self.off = self.parent.illusions * 15
            self.klonys_off = 15
        if self.name == "fire":
            self.off = 61

        if self.name == 'drachun_gulag' or self.name == "klonys_punch":
            self.udar = False

        if self.name == 'yas' or self.name == 'krov_bul':
            self.summon = 'baza'     # ready
            self.default_pos = (self.rect.x, self.rect.y)
            self.rect.centerx = self.default_pos[0]
            if self.name == 'yas':
                self.parent.attack_cooldown = 300  # wnwn
                if self.parent.upgrade_level == '2b' or self.parent.upgrade_level == '3b':
                    self.stomach_capacity = self.basic_stomach_capacity = self.parent.bullet_stomach_capacity
                if self.parent.upgrade_level == '3a':
                    self.atk = 25

        if self.name == 'krov_bul':
            self.add(self.parent.krovs)

        if self.name == 'gas' or self.name == 'horse' or self.name == 'diamond':
            self.gazirovannie_group = sprite.Group()
            self.enemies_in_group = 0

        if (self.bullet_sprite == 'light_sword' or self.bullet_sprite == 'light_spear') and self.parent.upgrade_level == '3b':
            if self.bullet_sprite == 'light_sword':
                self.atk *= 1.5
            else:
                self.probitie_group = sprite.Group()
                self.enemies_in_group = 0

        if self.name == 'sapphire':
            self.sapphired = False
        elif self.name == 'ruby':
            self.rubied = False
        elif self.name == 'stone':
            self.atk = self.parent.atk * 10
        elif self.name == 'obsidian':
            self.atk = self.parent.atk * 40
        elif self.name == 'diamond':
            self.atk = self.parent.atk * 30
        elif self.name == 'emerald':
            self.heal = 100
        elif self.name == 'onyx':
            self.barrier_hp = 100

        if self.bullet_sprite == 'big_mech_vzux' and self.parent.name == 'big_mechman' and self.parent.upgrade_level == '3b':
            self.dop_rect_top = Rect(self.rect.left, self.rect.top, 384, 128)
            self.dop_rect_mid = Rect(self.rect.right-128, self.rect.top, 128, 640)
            self.dop_rect_bot = Rect(self.rect.left, self.rect.bottom-128, 384, 128)

        if self.name == 'pulelomka':
            self.hp = self.parent.pulelomka_hp

    def bullet_movement(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.name == 'hrom' or self.name == 'anti_hrom':
            if (self.parent.rect.centery - self.rect.centery) >= 128 or (self.rect.centery - self.parent.rect.centery) >= 128:
                self.speed_y = 0
        
        if self.name == 'chistiy_bullet':
            if self.rect.centery < self.parent.rect.centery-20:
                self.speed_y = 5
            elif self.rect.centery > self.parent.rect.centery+20:
                self.speed_y = -5
            else:
                self.speed_y = 0

        if self.name == 'yas' or self.name == 'krov_bul':
            if self.summon == 'ready':
                if self.name == 'yas':
                    if self.parent.upgrade_level == '2a' or self.parent.upgrade_level == '3a':
                        if self.parent.upgrade_level == '2a':
                            self.speed_x = 4
                        else:
                            self.speed_x = 6
                            self.atk = 25
                        self.summon = 'go'
                        self.add(bullets_group)
                    else:
                        self.speed_x = 2
                        self.summon = 'go'
                        self.add(bullets_group)
                elif self.name == 'krov_bul':
                    self.speed_x = 7
                    self.summon = 'go'
                    self.add(bullets_group)

            elif self.rect.centerx >= 1520 and self.summon == 'go':
                self.speed_x *= -1
                self.summon = 'back'
                if self.name == 'yas':
                    if self.parent.upgrade_level == '3a':
                        for enemy in enemies_group:
                            if self in enemy.only_one_hit_bullets:
                                enemy.only_one_hit_bullets.remove(self)

            elif self.rect.centerx <= self.default_pos[0] and self.summon == 'back':
                self.speed_x = 0
                self.rect.centerx = self.default_pos[0]
                self.summon = 'baza'
                self.penned = False
                if self in bullets_group:  # наверное это надо, если не надо то круто, но проверять мне лень(это для корректной работы веток 2а и 3а если по пути нет врагов)
                    self.remove(bullets_group)

        if self.target is not None:
            if self.name == 'stone':
                self.speed_x = 5
            elif self.name == 'obsidian':
                self.speed_x = 7
            elif self.name == 'diamond':
                self.speed_x = 10
            elif self.name == 'opal':
                self.speed_x = 5
            elif self.name == 'onyx':
                self.speed_x = 5
            elif self.name == 'amethyst':
                self.speed_x = 5
            elif self.name == 'emerald':
                if self.target.rect.x < self.rect.x:
                    self.speed_x = -5
                else:
                    self.speed_x = 5
            elif self.name == 'ruby':
                if self.target.rect.x < self.rect.x:
                    self.speed_x = -5
                else:
                    self.speed_x = 5
            elif self.name == 'nephrite':
                level.money += 5
                self.kill()
            elif self.name == 'sapphire':
                if self.sapphired <= 0:
                    self.rect.x += 48
                    self.parent.basic_attack_cooldown //= 2
                    self.parent.basic_spawn_something_cooldown //= 2
                    self.parent.time_indicator *= 2
                    self.sapphired = 300
                else:
                    self.sapphired -= 1
                    if self.sapphired <= 0:
                        self.parent.basic_attack_cooldown *= 2
                        self.parent.basic_spawn_something_cooldown *= 2
                        self.parent.time_indicator //= 2
                        self.kill()

        if self.rect.x >= 1700 or self.rect.x <= -128:
            self.kill()

    def dealing_damage(self, enemy):
        self.damage = self.atk
        if self.parent.name == 'big_mechman':
            if self.parent.upgrade_level == '2a':
                if enemy.hp > (enemy.max_hp/3)*2:
                    self.damage *= 2
            elif self.parent.upgrade_level == '3a':
                if enemy.hp > (enemy.max_hp/4)*3:
                    self.damage *= 3
                elif enemy.hp > enemy.max_hp/2:
                    self.damage *= 2
            elif self.parent.upgrade_level == '3b':
                if self.bullet_sprite == 'big_mech_vzux' and (self.dop_rect_top.collidepoint(enemy.rect.centerx, enemy.rect.centery) or self.dop_rect_mid.collidepoint(enemy.rect.centerx, enemy.rect.centery) or self.dop_rect_bot.collidepoint(enemy.rect.centerx, enemy.rect.centery)):
                    self.damage *= 1.25
        if self.parent.name == 'sekirshik':
            if self.parent.upgrade_level == "2a" or self.parent.upgrade_level == "3a":
                if self.parent not in enemy.not_oneshot:
                    self.damage *= 1.5
        if enemy.vulnerabled > 0:
            self.damage *= 2
        for k, v in enemy.vulnerables_and_resists.items():
            if k == self.damage_type:
                self.damage *= (100 + v)/100
        if self.parent.name == 'pukish' and self.parent.upgrade_level == '3a':
            enemy.hp -= self.damage
        else:
            if hasattr(enemy, 'armor') and enemy.armor > 0:
                if self.parent.name == 'kirka':
                    self.damage *= self.parent.damage_multiplier
                if self.damage <= enemy.armor:
                    enemy.armor -= self.damage
                else:
                    enemy.hp -= (self.damage - enemy.armor)
                    enemy.armor = 0
            else:
                enemy.hp -= self.damage
        enemy.damaged = True
        if enemy.alive:
            enemy.check_hp()
            if self.parent.name == 'sekirshik' and (self.parent.upgrade_level == "2a" or self.parent.upgrade_level == "3a"):
                if self.parent.upgrade_level == "3a" and enemy.hp <= 0:
                    if self.parent not in enemy.not_oneshot:
                        self.parent.hp += 10
                        if self.parent.hp > self.parent.max_hp:
                            self.parent.hp = self.parent.max_hp
                enemy.not_oneshot.add(self.parent)

    def check_collision(self):
        if self.name != "zeleniy_strelok_bullet" and self.name != 'anti_hrom' and self.name != 'explosion' and self.name != 'joltiy_explosion' and self.name != 'opal_explosion' and self.name != 'razlet' and self.name != 'horse':
            if not self.penned:
                for tower in towers_group:
                    if tower.name == 'pen' and self.rect.colliderect(tower.rect_pen):
                        self.speed_x *= 1.5
                        self.atk *= 1.5
                        self.penned = True
        if (self.name == "zeleniy_strelok_bullet" or self.name == 'anti_hrom') and not self.penned:
            for tower in towers_group:
                if tower.name == 'pen' and self.rect.colliderect(tower.rect_pen):
                    self.speed_x /= 1.5
                    self.atk /= 1.5
                    self.penned = True
        if self.name == "zeleniy_strelok_bullet" or self.name == 'anti_hrom':
            for tower in towers_group:
                if tower.name != "pukish":
                    if self.rect.colliderect(tower.rect):
                        if tower.barrier:
                            tower.barrier.hp -= self.atk
                            self.dead()         # тут был кил
                        elif tower.onyx_barrier:
                            tower.onyx_barrier.hp -= self.atk
                            self.dead()         # тут был кил
                        elif tower.name == "knight_on_horse":
                            tower.knight_hp -= self.atk
                            self.dead()         # тут был кил
                        else:
                            self.damage = self.atk
                            if tower.unvulnerable > 0:
                                self.damage = 0
                            for k, v in tower.vulnerables_and_resists.items():
                                if k == self.damage_type:
                                    self.damage *= (100 + v)/100
                            if tower.name == 'kar_mag' and tower.v_falange > 0:
                                self.damage = 0
                                tower.v_falange -= 1
                                tower.spawned_things[tower.v_falange].kill()
                                tower.spawned_things.remove(tower.spawned_things[tower.v_falange])
                            if tower.name == 'ares' and tower.contrudar == 1:
                                tower.contrudar = 2
                                if self.damage_type == 'clean':
                                    tower.vpitano_damaged += self.damage // 20
                                else:
                                    tower.vpitano_damaged += self.damage
                            elif tower.name == 'ares' and tower.contrudar == 2:  # проверка на контратаку
                                tower.vpitano_damaged += self.damage
                            if tower.name == 'vozmezdik' and tower.vremya_casta > 0:
                                self.damage = 0
                                tower.col_vo_poglash += 1
                            tower.hp -= self.damage
                            tower.damaged = True
                            if hasattr(tower, 'received_damage'):
                                tower.received_damage += self.damage
                            tower.check_hp()
                            self.dead()         # тут был кил
                        for parasite in self.parent.parasites:
                            if parasite.name == 'metka_inq':
                                parasite.cashback_list.append(225)
            for creep in creeps_group:
                if self.rect.colliderect(creep.rect):
                    self.damage = self.atk
                    if creep.unvulnerable > 0:
                        self.damage = 0
                    for k, v in creep.vulnerables_and_resists.items():
                        if k == self.damage_type:
                            self.damage *= (100 + v)/100
                    if creep.barrier:
                        creep.barrier.hp -= self.damage
                        self.dead()         # тут был кил
                    else:
                        creep.hp -= self.damage
                        creep.check_hp()
                        self.dead()         # тут был кил
                    for parasite in self.parent.parasites:
                        if parasite.name == 'metka_inq':
                            parasite.cashback_list.append(225)
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if self.rect.colliderect(enemy.rect):
                        self.damage = self.atk
                        if enemy.unvulnerable > 0:
                            self.damage = 0
                        for k, v in enemy.vulnerables_and_resists.items():
                            if k == self.damage_type:
                                self.damage *= (100 + v)/100
                        enemy.hp -= self.damage
                        enemy.check_hp()
                        self.dead()         # тут был кил
                        for parasite in self.parent.parasites:
                            if parasite.name == 'metka_inq':
                                parasite.cashback_list.append(225)
    
        if self.name == "yas":
            if self.summon != "baza":
                for enemy in enemies_group:
                    if enemy.rect.colliderect(self.rect):
                        if self.summon == 'go':
                            if self.parent.upgrade_level == '2b' or self.parent.upgrade_level == '3b':
                                self.stomach_capacity -= 1
                                enemy.hp -= enemy.hp
                                if self.stomach_capacity <= 0:
                                    self.speed_x *= -1
                                    self.summon = 'back'
                                    self.remove(bullets_group)
                                    break
                            elif self.parent.upgrade_level == '3a' and self not in enemy.only_one_hit_bullets:
                                self.dealing_damage(enemy)
                                enemy.only_one_hit_bullets.add(self)
                            elif self.parent.upgrade_level == '1':
                                self.speed_x *= -1
                                self.summon = 'back'
                                enemy.hp -= enemy.hp
                                self.remove(bullets_group)
                                self.parent.attack_cooldown = self.parent.basic_attack_cooldown
                                break
                        elif self.summon == 'back' and (self.parent.upgrade_level == '2a' or self.parent.upgrade_level == '3a'):
                            if self.parent.upgrade_level == '3a' and self not in enemy.only_one_hit_bullets:
                                self.dealing_damage(enemy)
                                enemy.only_one_hit_bullets.add(self)
                            if self in bullets_group:
                                enemy.hp -= enemy.hp
                                self.remove(bullets_group)
                                break
                if self.summon == 'back' and (self.parent.upgrade_level == '2b' or self.parent.upgrade_level == '3b') and self.stomach_capacity != self.basic_stomach_capacity:
                    self.parent.attack_cooldown = (self.parent.basic_attack_cooldown // self.basic_stomach_capacity) * (self.basic_stomach_capacity - self.stomach_capacity)
                    self.stomach_capacity = self.basic_stomach_capacity
        
        if self.name == "krov_bul":
            if self.summon != "baza":
                for enemy in enemies_group:
                    if enemy.rect.colliderect(self.rect):
                        if self.summon == 'go':
                            Bullet("krov_explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.parent.atk, 0, 0, 'explosion', self.parent)
                            self.speed_x *= -1
                            self.summon = 'back'
                            self.remove(bullets_group)
                            break
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if self.rect.colliderect(enemy.rect):
                            if self.summon == 'go':
                                Bullet("krov_explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.parent.atk, 0, 0, 'explosion', self.parent)
                                self.speed_x *= -1
                                self.summon = 'back'
                                self.remove(bullets_group)
                                break

        if self.name == 'gas' or self.name == 'horse' or self.name == 'diamond':
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, self) and enemy.hp > 0:
                    if enemy not in self.gazirovannie_group:
                        self.dealing_damage(enemy)
                        enemy.add(self.gazirovannie_group)
                        if self.name == 'gas':
                            self.enemies_in_group += 1
                            if self.atk > self.basic_atk // 4:
                                if self.parent.upgrade_level == '3b':
                                    pass
                                elif self.parent.upgrade_level == '2b':
                                    self.atk -= (self.atk//3)
                                else:
                                    self.atk //= 2
                            if self.parent.upgrade_level == '2a' or self.parent.upgrade_level == '3a':
                                if self.enemies_in_group >= 5:
                                    self.dead()         # тут был кил
                                    break
                            else:
                                if self.enemies_in_group >= 3:
                                    self.dead()         # тут был кил
                                    break
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if sprite.collide_rect(enemy, self) and enemy.hp > 0:
                        if enemy not in self.gazirovannie_group:
                            self.dealing_damage(enemy)
                            enemy.add(self.gazirovannie_group)
                            if self.name == 'gas':
                                self.enemies_in_group += 1
                                if self.atk > self.basic_atk // 4:
                                    if self.parent.upgrade_level == '3b':
                                        pass
                                    elif self.parent.upgrade_level == '2b':
                                        self.atk -= (self.atk//3)
                                    else:
                                        self.atk //= 2
                                if self.parent.upgrade_level == '2a' or self.parent.upgrade_level == '3a':
                                    if self.enemies_in_group >= 5:
                                        self.dead()         # тут был кил
                                        break
                                else:
                                    if self.enemies_in_group >= 3:
                                        self.dead()         # тут был кил
                                        break

        if self.name == 'pulelomka':
            for bullet in bullets_group:
                if (bullet.name == "zeleniy_strelok_bullet" or bullet.name == 'anti_hrom') and self.rect.colliderect(bullet.rect):
                    bullet.kill()
                    self.hp -= 1
                    if self.hp <= 0:
                        self.kill()

        if self.name == 'razriv':
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, self) and enemy.hp > 0 and self not in enemy.only_one_hit_bullets:
                    if self.vrag != enemy:
                        self.dealing_damage(enemy)
                        enemy.only_one_hit_bullets.add(self)
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if sprite.collide_rect(enemy, self) and enemy.hp > 0 and self not in enemy.only_one_hit_bullets:
                        if self.vrag != enemy:
                            self.dealing_damage(enemy)
                            enemy.only_one_hit_bullets.add(self)

        if self.name == 'ls' or self.name == 'explosion' or self.name == 'joltiy_explosion' or self.name == 'opal_explosion' or self.name == "mech" or self.name == "drachun_gulag_splash" or self.name == "tolkan_bux" or self.name == 'razlet' or self.name == 'holod_row':
            for enemy in enemies_group:
                if sprite.collide_rect(enemy, self) and enemy.hp > 0 and self not in enemy.only_one_hit_bullets:
                    if self.name != 'joltiy_explosion' and self.name != 'holod_row':
                        self.dealing_damage(enemy)
                    if self.name == "tolkan_bux" and not enemy.heavy:
                        enemy.real_x += self.parent.push
                    if self.name == 'razlet' and not enemy.heavy:
                        if (enemy.rect.x >= self.rect.x and enemy.rect.centery == self.rect.centery) or enemy.rect.centery == 768 or enemy.rect.centery == 256:  #  тут же
                            enemy.real_x += self.pushl
                        elif enemy.rect.centery > self.rect.centery and enemy.rect.centery != 768:  # ниже
                            enemy.real_y += self.pushl
                        elif enemy.rect.centery < self.rect.centery and enemy.rect.centery != 256:  # выше
                            enemy.real_y -= self.pushl
                    if self.name == 'joltiy_explosion':
                        level.money += self.parent.money_per_enemy
                        enemy.stunned = True
                        enemy.stunned_time += self.parent.enemy_stunned_time
                    if self.name == 'opal_explosion':
                        enemy.vulnerabled += 300
                    if self.name == 'holod_row':
                        for i in range(14):
                            self.parent.parasix = randint(-32, 32)
                            self.parent.parasiy = randint(-48, 48)
                            Parasite('sneg_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                    if self.parent.name == 'prokach':
                        for bullet in self.parent.attack_areas:
                            enemy.only_one_hit_bullets.add(bullet)
                    else:
                        enemy.only_one_hit_bullets.add(self)
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if sprite.collide_rect(enemy, self) and enemy.hp > 0 and self not in enemy.only_one_hit_bullets:
                        if self.name != 'joltiy_explosion' and self.name != 'holod_row':
                            self.dealing_damage(enemy)
                        if self.name == "tolkan_bux" and not enemy.heavy:
                            enemy.real_x += self.parent.push
                        if self.name == 'razlet' and not enemy.heavy:
                            if (enemy.rect.x >= self.rect.x and enemy.rect.centery == self.rect.centery) or enemy.rect.centery == 768 or enemy.rect.centery == 256:  #  тут же
                                enemy.real_x += self.pushl
                            elif enemy.rect.centery > self.rect.centery and enemy.rect.centery != 768:  # ниже
                                enemy.real_y += self.pushl
                            elif enemy.rect.centery < self.rect.centery and enemy.rect.centery != 256:  # выше
                                enemy.real_y -= self.pushl
                        if self.name == 'opal_explosion':
                            enemy.vulnerabled += 300
                        if self.name == 'holod_row':
                            for i in range(14):
                                self.parent.parasix = randint(-32, 32)
                                self.parent.parasiy = randint(-48, 48)
                                Parasite('sneg_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                        if self.parent.name == 'prokach':
                            for bullet in self.parent.attack_areas:
                                enemy.only_one_hit_bullets.add(bullet)
                        else:
                            enemy.only_one_hit_bullets.add(self)
            if self.name == "mech" or self.name == "drachun_gulag_splash" or self.name == "tolkan_bux" or self.name == "klonys_punch":
                targets[id(self.parent)] = None

        if self.name == 'drachun_gulag' or self.name == "klonys_punch":
            if targets[id(self.parent)] and targets[id(self.parent)].hp > 0 and hasattr(targets[id(self.parent)], 'only_one_hit_bullets'):
                if sprite.collide_rect(targets[id(self.parent)], self) and self not in targets[id(self.parent)].only_one_hit_bullets:
                    targets[id(self.parent)].only_one_hit_bullets.add(self)
                    self.udar = True
                    self.dealing_damage(targets[id(self.parent)])
                    if self.name == "klonys_punch":
                        self.mimo = False
                    if self.parent.name == 'drachun' and (self.parent.upgrade_level == "2a" or self.parent.upgrade_level == "3a") and self.parent.rage:
                        if targets[id(self.parent)]:
                            if not targets[id(self.parent)].alive:
                                if self.parent.upgrade_level == "2a":
                                    if self.parent.max_hp - self.parent.hp <= self.parent.max_hp//2:
                                        self.parent.hp = self.parent.max_hp
                                    else:
                                        self.parent.hp += self.parent.max_hp//2
                                else:
                                    self.parent.hp = self.parent.max_hp
                                    self.parent.rage_duration += 60
                                
            else:  # я хз надо это или нет + я не уверен что это корректно работает тк проверить сложно и лень
                for enemy in enemies_group:
                    if not self.udar:
                        if sprite.collide_rect(enemy, self) and enemy.hp > 0 and self not in enemy.only_one_hit_bullets:
                            self.dealing_damage(enemy)
                            self.udar = True
                            if self.name == "klonys_punch":
                                self.mimo = False
                for enemy in neutral_objects_group:
                    if enemy.height == "high":
                        if not self.udar:
                            if sprite.collide_rect(enemy, self) and enemy.hp > 0 and self not in enemy.only_one_hit_bullets:
                                self.dealing_damage(enemy)
                                self.udar = True
                                if self.name == "klonys_punch":
                                    self.mimo = False

        if self.name == 'emerald' or self.name == 'ruby' or self.name == 'amethyst' or self.name == 'onyx':
            if self.target is not None:
                if sprite.collide_rect(self.target, self):
                    if self.name == 'emerald':
                        if self.target.max_hp - self.target.hp > self.heal:
                            self.target.hp += self.heal
                        else:
                            self.target.hp = self.target.max_hp
                        self.dead()         # тут был кил
                    elif self.name == 'ruby':
                        self.rect.x = self.target.rect.centerx
                        self.speed_x *= -1
                        if self.rubied <= 0:
                            self.target.atk *= 2
                            self.rubied = 900
                        else:
                            self.rubied -= 1
                            if self.rubied <= 0:
                                self.target.atk //= 2
                                self.dead()         # тут был кил
                    elif self.name == 'amethyst':
                        self.target.unvulnerable += 120
                        self.dead()         # тут был кил
                    elif self.name == 'onyx':
                        if self.target.onyx_barrier:
                            self.target.onyx_barrier.hp += self.barrier_hp
                        if self.target.onyx_barrier not in all_sprites_group:
                            self.target.onyx_barrier = Parasite('onyx_barrier', self.target.rect.centerx, self.target.rect.centery, '', 0, self.target, self)
                        self.dead()         # тут был кил

        for enemy in enemies_group:
            if enemy.rect.collidepoint(self.rect.right, self.rect.centery):
                if self.name == 'kopilka':
                    if hasattr(self, 'probitie_group'):
                        if not enemy in self.probitie_group:
                            self.dealing_damage(enemy)
                            enemy.add(self.probitie_group)
                            self.enemies_in_group += 1
                            self.atk /= 2
                            if self.enemies_in_group >= 2:  # через len() нельзя тк там кое какие неприятные нюансы
                                self.dead()         # тут был кил
                                break
                    else:
                        self.dealing_damage(enemy)
                        self.dead()         # тут был кил
                        break
                elif self.name == 'kar_fal':
                    self.dealing_damage(enemy)
                    self.kill()
                    break
        for enemy in neutral_objects_group:
            if enemy.height == "high":
                if enemy.rect.collidepoint(self.rect.right, self.rect.centery):
                    if self.name == 'kopilka':
                        if hasattr(self, 'probitie_group'):
                            if not enemy in self.probitie_group:
                                self.dealing_damage(enemy)
                                enemy.add(self.probitie_group)
                                self.enemies_in_group += 1
                                self.atk /= 2
                                if self.enemies_in_group >= 2:  # через len() нельзя тк там кое какие неприятные нюансы
                                    self.dead()         # тут был кил
                                    break
                        else:
                            self.dealing_damage(enemy)
                            self.dead()         # тут был кил
                            break
                    elif self.name == 'kar_fal':
                        self.dealing_damage(enemy)
                        self.kill()
                        break
        for enemy in enemies_group:
            if sprite.collide_rect(enemy, self) and enemy.hp > 0:
                if self.name == 'default' or self.name == 'hrom' or self.name == 'boom' or self.name == 'big_boom' or self.name == 'struya' or self.name == 'spore' or self.name == 'snejok' or self.name == 'snejok_big' or self.name == 'sliz_bul' or self.name == 'stone' or self.name == 'obsidian' or self.name == 'opal' or self.name == 'es' or self.name == 'kok' or self.name == 'zayac_krol' or self.name == 'chistiy_bullet' or self.name == 'razrivnaya' or self.name == 'chorniy_bullet':
                    self.dealing_damage(enemy)
                    if self.bullet_sprite == 'mini_kamen_golem':
                        Creep('mini_golem', (self.rect.x-64, self.rect.y-64), self.parent)
                    elif self.bullet_sprite == 'big_kamen_golem':
                        Creep('big_golem', (self.rect.x-64, self.rect.y-64), self.parent)
                    elif self.bullet_sprite == 'mega_kamen_golem':
                        Creep('mega_golem', (self.rect.x-64, self.rect.y-64), self.parent)
                    if self.name == 'boom':
                        Bullet("explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'explosion', self.parent)
                    elif self.name == 'big_boom':
                        Bullet("mega_explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'explosion', self.parent)
                    elif self.name == 'razrivnaya':
                        bul = Bullet("drachun_gulag", enemy.rect.right+64, self.rect.centery, 'fire', self.atk*3, 0, 0, 'razriv', self.parent)
                        bul.vrag = enemy
                    elif self.name == 'opal':
                        Bullet("opal_explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'opal_explosion', self.parent)
                    elif self.name == 'struya' and not enemy.heavy:
                        if self.parent.upgrade_level == '3a':
                            enemy.real_x += 64
                        else:
                            enemy.real_x += 32
                    elif self.name == 'zayac_krol':
                        enemy.stunned = True
                        enemy.stunned_time += self.parent.bullet_stun_time
                    elif self.name == 'spore' or self.name == 'snejok' or self.name == 'snejok_big' or self.name == 'chorniy_bullet':
                        self.parent.parasix = randint(-32, 32)
                        self.parent.parasiy = randint(-48, 48)
                        if self.name == 'spore':
                            Parasite('grib_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                        elif self.name == 'snejok':
                            Parasite('sneg_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                        elif self.name == 'snejok_big':
                            Parasite('sneg_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                            self.parent.parasix = randint(-32, 32)
                            self.parent.parasiy = randint(-48, 48)
                            Parasite('sneg_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                        elif self.name == 'chorniy_bullet':
                            Parasite('dark_mark', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, self.damage_type, 0, enemy, self.parent)
                    elif self.name == 'sliz_bul':
                        if enemy.sliz:
                            enemy.sliz.hp += self.parent.sliz_hp
                        else:
                            Parasite('sliz_luja_parasite', enemy.rect.centerx, enemy.rect.centery+32, self.parent.damage_type, 0, enemy, self.parent)
                    elif self.name == 'es':
                        Bullet('electro_maga_explosion', self.rect.centerx, self.rect.centery, self.damage_type, 0, 0, 0, 'razlet', self.parent)
                    if self.bullet_sprite == 'fireball' and (self.parent.upgrade_level == '2b' or self.parent.upgrade_level == '3b') and self.parent.name == 'fire_mag' :
                        self.parent.parasix = randint(-32, 32)
                        self.parent.parasiy = randint(-48, 48)
                        Parasite('ogonek_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', self.parent.atk/10, enemy, self.parent)
                    if self.parent.name == 'elf':
                        self.parent.parasix = randint(-64, 64)
                        self.parent.parasiy = randint(-64, 64)
                        Parasite('poison_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', self.parent.atk/5, enemy, self.parent)
                    self.dead()         # тут был кил

                break

        for enemy in neutral_objects_group:
            if enemy.height == "high":
                if sprite.collide_rect(enemy, self) and enemy.hp > 0:
                    if self.name == 'default' or self.name == 'hrom' or self.name == 'boom' or self.name == 'big_boom' or self.name == 'struya' or self.name == 'spore' or self.name == 'snejok' or self.name == 'snejok_big' or self.name == 'sliz_bul' or self.name == 'stone' or self.name == 'obsidian' or self.name == 'opal' or self.name == 'es' or self.name == 'kok' or self.name == 'zayac_krol' or self.name == 'chistiy_bullet' or self.name == 'razrivnaya' or self.name == 'chorniy_bullet':
                        self.dealing_damage(enemy)
                        if self.bullet_sprite == 'mini_kamen_golem':
                            Creep('mini_golem', (self.rect.x-64, self.rect.y-64), self.parent)
                        elif self.bullet_sprite == 'big_kamen_golem':
                            Creep('big_golem', (self.rect.x-64, self.rect.y-64), self.parent)
                        elif self.bullet_sprite == 'mega_kamen_golem':
                            Creep('mega_golem', (self.rect.x-64, self.rect.y-64), self.parent)
                        if self.name == 'boom':
                            Bullet("explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'explosion', self.parent)
                        elif self.name == 'big_boom':
                            Bullet("mega_explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'explosion', self.parent)
                        elif self.name == 'razrivnaya':
                            bul = Bullet("drachun_gulag", enemy.rect.right+64, self.rect.centery, 'fire', self.atk*3, 0, 0, 'razriv', self.parent)
                            bul.vrag = enemy
                        elif self.name == 'opal':
                            Bullet("opal_explosion", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, 0, 0, 'opal_explosion', self.parent)
                        elif self.name == 'struya' and not enemy.heavy:
                            if self.parent.upgrade_level == '3a':
                                enemy.real_x += 64
                            else:
                                enemy.real_x += 32
                        elif self.name == 'zayac_krol':
                            enemy.stunned = True
                            enemy.stunned_time += self.parent.bullet_stun_time
                        elif self.name == 'spore' or self.name == 'snejok' or self.name == 'snejok_big' or self.name == 'chorniy_bullet':
                            self.parent.parasix = randint(-32, 32)
                            self.parent.parasiy = randint(-48, 48)
                            if self.name == 'spore':
                                Parasite('grib_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                            elif self.name == 'snejok':
                                Parasite('sneg_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                            elif self.name == 'snejok_big':
                                Parasite('sneg_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                                self.parent.parasix = randint(-32, 32)
                                self.parent.parasiy = randint(-48, 48)
                                Parasite('sneg_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', 0, enemy, self.parent)
                            elif self.name == 'chorniy_bullet':
                                Parasite('dark_mark', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, self.damage_type, 0, enemy, self.parent)
                        elif self.name == 'sliz_bul':
                            if enemy.sliz:
                                enemy.sliz.hp += self.parent.sliz_hp
                            else:
                                Parasite('sliz_luja_parasite', enemy.rect.centerx, enemy.rect.centery+32, self.parent.damage_type, 0, enemy, self.parent)
                        elif self.name == 'es':
                            Bullet('electro_maga_explosion', self.rect.centerx, self.rect.centery, self.damage_type, 0, 0, 0, 'razlet', self.parent)
                        if self.bullet_sprite == 'fireball' and (self.parent.upgrade_level == '2b' or self.parent.upgrade_level == '3b') and self.parent.name == 'fire_mag' :
                            self.parent.parasix = randint(-32, 32)
                            self.parent.parasiy = randint(-48, 48)
                            Parasite('ogonek_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', self.parent.atk/10, enemy, self.parent)
                        if self.parent.name == 'elf':
                            self.parent.parasix = randint(-64, 64)
                            self.parent.parasiy = randint(-64, 64)
                            Parasite('poison_parasite', enemy.rect.centerx+self.parent.parasix, enemy.rect.centery+self.parent.parasiy, '', self.parent.atk/5, enemy, self.parent)
                        self.dead()         # тут был кил

                    break

    def check_parent(self):
        if self.name == 'kopilka' or self.name == 'stone' or self.name == 'obsidian' or self.name == 'diamond' or self.name == 'opal' or self.name == 'sapphire' or self.name == 'emerald' or self.name == 'amethyst' or self.name == 'onyx' or self.name == 'ruby' or self.name == 'nephrite' or self.name == 'kar_fal':
            if self.parent not in all_sprites_group and self.speed_x == 0:
                self.dead()         # тут был кил
        if self.name == 'yas' or self.name == 'krov_bul':
            if self.parent not in all_sprites_group:
                self.dead()         # тут был кил

    def cooldowns(self):
        if self.anim_tasks:                          # порядок анимации
            if self.anim_tasks[0][1] > 0:            # -> self.anim_sequence = [("attack", 60, shoot), ("give", 50, spawn_something), ...]
                self.state = self.anim_tasks[0][0]   # -> какая анимация, время анимации, функция после анимации
                self.anim_tasks[0][1] -= 1
            elif self.anim_tasks[0][1] == 0:        # баг?
                self.anim_tasks[0][2]()
                self.anim_tasks[0][1] -= 1
                self.anim_tasks.pop(0)
        else:
            self.state = "move"

        if hasattr(self, 'off'):
            if self.off <= 0:
                self.kill()
            else:
                self.off -= 1

        if hasattr(self, 'klonys_off'):
            if self.klonys_off > 0:
                self.klonys_off -= 1
                if self.klonys_off <= 0:
                    self.parent.illusions -= 1
                    if self.parent.illusions > 0:
                        klonys_pose = randint(1, 5)
                        Bullet("klonys_punch" + str(klonys_pose), self.rect.centerx + self.mimo*128, self.rect.centery, self.parent.damage_type, self.parent.atk, 0, 0, 'klonys_punch', self.parent)

    def add_anim_task(self, anim, func):
        if len(self.anim_tasks) == 0:
            self.state = anim
            self.anim_tasks.append([anim, (self.get_count_anim_frames() * self.anim_duration) // self.time_indicator - 1, func])
            self.anim_count = 0
        else:
            already_in = [anim[0] for anim in self.anim_tasks]
            if anim not in already_in:
                self.state = anim
                self.anim_tasks.append([anim, (self.get_count_anim_frames() * self.anim_duration) // self.time_indicator - 1, func])

    def get_count_anim_frames(self):
        if self.state == "move":
            return len(bullets_move[self.bullet_sprite])     # переделать на name  # НЕТ!!! не будим
        if self.state == "death":
            return len(bullets_death[self.bullet_sprite])     # переделать на name  # НЕТ!!! не будим

    def animation(self):
        count_anim_frames = self.get_count_anim_frames()
        if 0 <= self.anim_count < self.anim_duration * count_anim_frames:
            if int(self.anim_count//self.anim_duration) != self.last_anim_frame:
                self.last_anim_frame = int(self.anim_count//self.anim_duration)
                if self.state == "move":
                    self.image = bullets_move[self.bullet_sprite][int(self.anim_count//self.anim_duration)]     # переделать на name  # НЕТ!!! не будим
                if self.state == "death":
                    self.image = bullets_death[self.bullet_sprite][int(self.anim_count//self.anim_duration)]     # переделать на name  # НЕТ!!! не будим

        if self.anim_count >= count_anim_frames * self.anim_duration:
            self.anim_count = 0
        else:
            self.anim_count += self.time_indicator

    def sound(self, reason):
        if reason == 'death':
            self.death_sound.set_volume(sound_effects_volume * general_volume)
            self.death_sound.play()
            # mixer.Sound(f"sounds/sound_effects/bullets/death/{self.bullet_sprite}.ogg").play()

    def dead(self):
        if not level.no_death_animation:
            # bullets_group.remove(self)  # фича прикол шок жесть блин омг
            self.atk = 0
            self.speed_x = 0
            self.add_anim_task("death", self.kill)
            self.sound('death')
        else:
            self.kill()
            self.sound('death')

        # можно будет сделать чтобы если копитель умирал, то его мечи вниз падали прикольно. А при попадании меча во врага другая анимация

    def update(self):
        self.cooldowns()
        self.bullet_movement()
        self.animation()
        self.check_collision()
        self.check_parent()


class Parasite(sprite.Sprite):
    def __init__(self, name, x, y, damage_type, atk, owner, parent):
        super().__init__(all_sprites_group, parasites_group)
        self.image = image.load(f"images/buffs/{name}.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.render_layer = 6
        self.is_dead = False
        self.damage_type = damage_type
        self.atk = atk
        self.name = name
        self.owner = owner  # это враг к которому привязан паразит
        self.parent = parent

        if self.name == 'sosun' or self.name == 'grib_parasite' or self.name == 'sneg_parasite' or self.name == 'ogonek_parasite' or self.name == 'poison_parasite' or self.name == 'metka_inq' or self.name == 'dark_mark':
            self.parasix = self.parent.parasix
            self.parasiy = self.parent.parasiy
            if self.name == 'sosun' or self.name == 'ogonek_parasite' or self.name == 'poison_parasite':
                self.attack_cooldown = 60
            elif self.name == 'grib_parasite':
                self.owner.gribs += 1
                self.lifetime = 300
                for parasite in parasites_group:
                    if parasite != self and parasite.owner == self.owner and self.parent == parasite.parent and self.name == parasite.name:
                        parasite.kill()
                        self.owner.gribs -= 1
            elif self.name == 'sneg_parasite':
                self.owner.snegs += 1
                self.lifetime = 300
                for parasite in parasites_group:
                    if parasite != self and parasite.owner == self.owner and self.parent == parasite.parent and self.name == parasite.name:
                        parasite.lifetime = 300
            if self.name == 'ogonek_parasite':
                self.lifetime = 300
            elif self.name == 'poison_parasite':
                self.lifetime = 1020
            elif self.name == 'dark_mark':
                self.lifetime = 600
                self.parent.marks.add(self)
                for parasite in parasites_group:
                    if parasite.name == self.name and parasite.owner == self.owner and parasite != self:
                        parasite.kill()
                for mark in self.parent.marks:
                    if mark != self:
                        mark.kill()

        if self.name == 'barrier' or self.name == 'onyx_barrier':
            self.hp = self.parent.barrier_hp
            if self.name == 'barrier':
                self.life_time = self.parent.basic_spawn_something_cooldown

        if self.name == 'sliz_luja_parasite':
                self.hp = self.parent.sliz_hp
                self.owner.sliz = self

        if self.name == 'metka_inq':
            self.atk = self.owner.atk // 5
            self.owner.parasites.add(self)
            # if self.parent in self.owner.parasites:
            self.owner.parasites.remove(self.parent)
            self.cashback_list = []
            self.lifetime = 600

        if self.name == 'uragan' or self.name == 'potok_y':
            self.duration = self.parent.uragan_duration
            self.render_layer = 3
            if self.name == 'uragan':
                self.attack_cooldown = 12
                if self.parent.upgrade_level == '2a' or self.parent.upgrade_level == '3a':
                    self.speed = self.parent.uragan_speed
                    self.start_x = self.rect.centerx
                    self.real_x = self.rect.x
                elif self.parent.upgrade_level == '3b':
                    self.rect_vulnerable = Rect(self.rect.left+128, self.rect.top+128, 128, 128)

        if self.name == 'raven':
            self.home_x = self.rect.centerx
            self.home_y = self.rect.centery
            self.speed = 5
            self.kluving_time = self.basic_kluving_time = 900
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.rest_time = 0
            self.basic_rest_time = 300
            if self.parent not in all_sprites_group:
                self.lifetime = 300

        if self.name == 'mol':
            if self.owner != self.parent:
                self.dealing_damage(self.owner)
            self.lifetime = 60

        if self.name == 'terpila_debuff':
            self.lifetime = 600
            self.owner.speed /= 2
            self.owner.basic_attack_cooldown *= 2

    def dead(self):
        self.kill()
        if self.name == 'uragan' or self.name == 'potok_y':
            for enemy in enemies_group:
                enemy.back_to_line()
        if self.name == 'sosun' or self.name == 'metka_inq':
            self.parent.have_parasite.remove(self.owner)
            if self.parent in self.owner.parasite_parents:
                self.owner.parasite_parents.remove(self.parent)
        if self.name == 'barrier':
            self.owner.have_barrier = False
        if self.name == 'sliz_luja_parasite':
            self.owner.sliz = None
        if self.name == 'raven':
            if self.owner != self.parent and self.parent in self.owner.parasite_parents:
                self.owner.parasite_parents.remove(self.parent)
        if self.name == 'terpila_debuff':
            self.owner.speed *= 2
            self.owner.basic_attack_cooldown //= 2
        if self.name == 'metka_inq':
            for i in range(len(self.cashback_list)):
                self.dealing_damage(self.owner)
            self.cashback_list.clear()

    def prisasivanie(self):  # если честно то это по сути delat_chtoto но для паразитов, когда-нибудь сделаем по-человечески
        if self.parent and self.name != 'ogonek_parasite' and self.name != 'poison_parasite' and self.name != 'sneg_parasite'  and self.name != 'grib_parasite' and self.name != 'sliz_luja_parasite' and self.name != 'mol' and self.name != 'terpila_debuff' and self.name != 'onyx_barrier' and self.name != 'potok_y':
            if self.parent not in all_sprites_group: 
                if self.name == 'raven' and (self.owner != self.parent or (hasattr(self, 'lifetime') and self.lifetime > 0)):
                    pass
                else:
                    self.dead()
        if self.name != 'mol' and self.name != 'potok_y':
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
            self.owner.barrier = None
        elif self.name == 'onyx_barrier' and self.hp <= 0:
            self.kill()
            self.owner.onyx_barrier = None
        elif self.name == 'sliz_luja_parasite' and self.hp <= 0:
            self.dead()

        if self.name == 'sosun' or self.name == 'grib_parasite' or self.name == 'sneg_parasite' or self.name == 'ogonek_parasite' or self.name == 'poison_parasite' or self.name == 'metka_inq' or self.name == 'dark_mark':
            self.rect.centerx = self.owner.rect.centerx+self.parasix
            self.rect.centery = self.owner.rect.centery+self.parasiy
            if self.name == 'sosun' or self.name == 'ogonek_parasite' or self.name == 'poison_parasite':
                if self.attack_cooldown <= 0:
                    self.attack_cooldown = 60
                    self.dealing_damage(self.owner)
                    if self.name == 'sosun':
                        if self.parent.hp < self.parent.max_hp - self.atk:
                            self.parent.hp += self.atk
                        else:
                            self.parent.hp = self.parent.max_hp

        if self.name == 'terpila_debuff':
            self.rect.centerx = self.owner.rect.centerx
            self.rect.centery = self.owner.rect.centery

        if self.name == 'dark_mark':
            if self.owner.vulnerabled:
                self.owner.vulnerabled += 1
            else:
                self.owner.vulnerabled += 2

        if self.name == 'grib_parasite':
            if self.owner.gribs > 3:
                self.kill()
                self.owner.gribs -= 1

        if self.name == 'uragan':
            for enemy in enemies_group:
                if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                    if not enemy.heavy:
                        enemy.angle = atan2(self.rect.centery - enemy.rect.centery, self.rect.centerx - enemy.rect.centerx)
                        enemy.x_vel = cos(enemy.angle) * enemy.speed * 12
                        enemy.y_vel = sin(enemy.angle) * enemy.speed * 12
                        enemy.real_x += enemy.x_vel
                        enemy.real_y += enemy.y_vel

                    if self.attack_cooldown <= 0:
                        self.attack_cooldown = 12
                        self.dealing_damage(enemy)
                        if self.parent.upgrade_level == '3b':
                            if not self.rect_vulnerable.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                                self.dealing_damage(enemy)

                if self.parent.upgrade_level == '3b':
                    if self.rect_vulnerable.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                        if enemy.vulnerabled:
                            enemy.vulnerabled += 1
                        else:
                            enemy.vulnerabled += 2
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                        if not enemy.heavy:
                            enemy.angle = atan2(self.rect.centery - enemy.rect.centery, self.rect.centerx - enemy.rect.centerx)
                            enemy.x_vel = cos(enemy.angle) * enemy.speed * 12
                            enemy.y_vel = sin(enemy.angle) * enemy.speed * 12
                            enemy.real_x += enemy.x_vel
                            enemy.real_y += enemy.y_vel

                        if self.attack_cooldown <= 0:
                            self.attack_cooldown = 12
                            self.dealing_damage(enemy)
                            if self.parent.upgrade_level == '3b':
                                if not self.rect_vulnerable.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                                    self.dealing_damage(enemy)

                    if self.parent.upgrade_level == '3b':
                        if self.rect_vulnerable.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                            if enemy.vulnerabled:
                                enemy.vulnerabled += 1
                            else:
                                enemy.vulnerabled += 2
            if self.parent.upgrade_level == '2a':
                if self.rect.centerx - self.start_x < 256 and self.rect.centerx < 1472:
                    self.real_x += self.speed
                    self.rect.x = int(self.real_x)
            elif self.parent.upgrade_level == '3a':
                if self.rect.centerx - self.start_x < 512 and self.rect.centerx < 1472:
                    self.real_x += self.speed
                    self.rect.x = int(self.real_x)

        if self.name == 'potok_y':
            for enemy in enemies_group:
                if self.rect.colliderect(enemy.rect) and not enemy.heavy:
                    enemy.angle = atan2(self.rect.centery - enemy.rect.centery, 0)
                    enemy.y_vel = sin(enemy.angle) * enemy.speed * 12
                    enemy.real_y += enemy.y_vel

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
                    for enemy in neutral_objects_group:
                        if enemy.height == "high":
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

        if self.name == 'metka_inq':
            for i in self.cashback_list:
                ii = self.cashback_list.index(i)
                if i > 0:
                    i -= 1
                    self.cashback_list[ii] = i
                else:
                    self.dealing_damage(self.owner)
                    self.cashback_list.remove(i)

    def dealing_damage(self, enemy):
        self.damage = self.atk
        if enemy.vulnerabled > 0:
            self.damage *= 2
        for k, v in enemy.vulnerables_and_resists.items():
            if k == self.damage_type:
                self.damage *= (100 + v)/100
        if hasattr(enemy, 'armor') and enemy.armor > 0:
            if self.damage <= enemy.armor:
                enemy.armor -= self.damage
            else:
                enemy.hp -= (self.damage - enemy.armor)
                enemy.armor = 0
        else:
            enemy.hp -= self.damage
        enemy.damaged = True
        if enemy.alive:
            enemy.check_hp()

    def update(self):
        self.prisasivanie()

        if self.name == 'sosun' or self.name == 'uragan' or self.name == 'ogonek_parasite' or self.name == 'poison_parasite' or self.name == 'raven':
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

        if self.name == 'uragan' or self.name == 'potok_y':
            if self.duration > 0:
                self.duration -= 1
            else:
                self.dead()

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
                    elif self.name == 'sneg_parasite':
                        self.owner.snegs -= 1
                        if self.owner.snegs < 3 and self.owner.slowed:
                            self.owner.speed *= 2
                            self.owner.slowed = False


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
        if self.name == 'mat' or self.name == 'cvetok':
            self.rect2 = Rect(self.rect.x - 128, self.rect.y - 128, 384, 384)
        elif self.name == 'boloto':
            self.rect2 = Rect(self.rect.x - ((self.parent.bolotos-1)*128), self.rect.y, self.parent.bolotos*128, 128)
        elif self.name == 'mana':
            if self.parent.upgrade_level == '2b':
                self.rect2 = Rect(self.rect.x - 128, self.rect.y, 128, 128)
            elif self.parent.upgrade_level == '3b':
                self.rect2 = Rect(self.rect.x - 128, self.rect.y, 384, 128)
                self.rect3 = Rect(self.rect.x, self.rect.y-128, 128, 384)

        self.max_buff = None

        if self.name == 'mat' or self.name == 'vodkamat' or self.name == 'kuklo' or self.name == 'mana':
            self.gender = 'tower_buff'
            self.buffed_towers = sprite.Group()
        else:
            self.gender = 'field_debuff'

        if self.name == 'mat' or self.name == 'kuklo' or self.name == 'mana' or self.name == 'cvetok':
            self.mozhet_zhit = False
        else:
            self.mozhet_zhit = True

        if self.rect.x <= 383 or self.rect.x >= 1536 or self.rect.y < 192 or self.rect.y >= 832:  # по хорошему надо не >= 832, а > 704, но похуй
            self.kill()

        if self.name == 'vodkamat':
            self.lifetime = 600
        elif self.name == 'fire_luja':
            self.atk = 20
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.lifetime = 300
            self.damage_type = 'fire'
        elif self.name == 'grib_gas':
            self.atk = self.parent.atk
            self.attack_cooldown = self.basic_attack_cooldown = self.parent.gas_attack_cooldown
            self.lifetime = self.parent.gas_duration
            self.debuffed_enemies = sprite.Group()
            self.damage_type = 'poison'

        if self.name == 'kuklo':
            self.atk = 10
            self.attack_cooldown = self.basic_attack_cooldown = 60
            self.damage_type = 'poison'
            self.bullet_speed_x = 5

        if self.name == 'boloto' or self.name == 'cvetok':
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

        if self.name == 'kuklo':
            for buff in buffs_group:
                if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff and (buff.name == 'kuklo'):
                    self.kill()

        elif self.name == 'mana':
            for buff in buffs_group:
                if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff and buff.name == self.name:
                    self.kill()

        elif self.name == 'cvetok':
            for buff in buffs_group:
                if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff and buff.name == self.name:
                    for enemy in buff.debuffed_enemies:
                        enemy.atk *= 1.5
                    buff.kill()

        elif self.name == 'boloto':
            for buff in buffs_group:
                if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff and self.name == buff.name:
                    for enemy in buff.debuffed_enemies:
                        if buff.parent.upgrade_level == '3a':
                            enemy.speed *= 4
                        else:
                            enemy.speed *= 2
                    buff.kill()

        elif self.name == 'fire_luja':
            for buff in buffs_group:
                if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff and self.name == buff.name:
                    buff.lifetime += self.lifetime
                    self.kill()
        
        elif self.name == 'grib_gas':
            for buff in buffs_group:
                if self.rect.collidepoint(buff.rect.centerx, buff.rect.centery) and self != buff and self.name == buff.name:
                    buff.lifetime += self.lifetime
                    buff.atk = (buff.atk + self.atk) - ((buff.atk + self.atk) // 2)  # чтобы округлялось в большую сторону
                    self.kill()

    def delat_buff(self):
        for tower in towers_group:
            if tower not in self.buffed_towers:
                if self.rect.collidepoint(tower.rect.centerx, tower.rect.centery):
                    if self.name == 'kuklo':
                        if self.attack_cooldown <= 0:
                            for enemy in enemies_group:
                                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                                    Bullet("ab_kokol", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, 0, 'kok', self)
                    elif self.name == 'mana':
                        if hasattr(tower, 'atk') and tower.rarity != 'spell':
                            if self.parent.upgrade_level == '2b':
                                tower.atk *= 1.5
                            elif self.parent.upgrade_level == '3b':
                                tower.atk *= 2
                            tower.add(self.buffed_towers)
                    else:
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
                                or tower.name == "inquisitor"\
                                or tower.name == "priest"\
                                or tower.name == "ded_moroz"\
                                or tower.name == "uvelir"\
                                or tower.name == "krovnyak"\
                                or tower.name == "kokol"\
                                or tower.name == "sliz"\
                                or tower.name == "klonys"\
                                or tower.name == "furry_medved"\
                                or tower.name == "furry_volk"\
                                or tower.name == "furry_zayac"\
                                or tower.name == "oruzhik_daggers"\
                                or tower.name == "oruzhik_bow"\
                                or tower.name == "kar_mag"\
                                or tower.name == "shabriri"\
                                or tower.name == "prokach"\
                                or tower.name == "pulelom"\
                                or tower.name == "chistiy"\
                                or tower.name == "sekirshik"\
                                or tower.name == "kirka"\
                                or tower.name == "elf"\
                                or tower.name == "holodilnik"\
                                or tower.name == "chorniy"\
                                or tower.name == 'electro_maga':

                            if tower.basic_attack_cooldown // 1.5 <= 180:
                                tower.basic_attack_cooldown //= 1.5
                                self.max_buff = False
                            else:
                                tower.basic_attack_cooldown -= 180
                                self.max_buff = True
                            tower.time_indicator *= 1.5
                            if tower.name == 'kopitel' or tower.name == "uvelir" or tower.name == "kar_mag":
                                tower.basic_spawn_something_cooldown //= 1.5
                            tower.add(self.buffed_towers)

        for nekusaemiy in nekusaemie_group:
            if nekusaemiy not in self.buffed_towers:
                if self.rect.collidepoint(nekusaemiy.rect.centerx, nekusaemiy.rect.centery):
                    if self.name == 'kuklo':
                        if self.attack_cooldown <= 0:
                            for enemy in enemies_group:
                                if -10 <= enemy.rect.y - self.rect.y <= 10 and enemy.rect.x >= self.rect.x and enemy.alive:
                                    Bullet("ab_kokol", self.rect.centerx, self.rect.centery, self.damage_type, self.atk, self.bullet_speed_x, 0, 'kok', self)
                    elif self.name == 'mana':
                        if hasattr(nekusaemiy, 'atk'):
                            if self.parent.upgrade_level == '2b':
                                nekusaemiy.atk *= 1.5
                            elif self.parent.upgrade_level == '3b':
                                nekusaemiy.atk *= 2
                            nekusaemiy.add(self.buffed_towers)
                    else:
                        if nekusaemiy.name == 'spike' or nekusaemiy.name == 'pukish':
                            if nekusaemiy.basic_attack_cooldown // 1.5 <= 180:
                                nekusaemiy.basic_attack_cooldown //= 1.5
                                self.max_buff = False
                            else:
                                nekusaemiy.basic_attack_cooldown -= 180
                                self.max_buff = True
                            nekusaemiy.time_indicator *= 1.5
                            nekusaemiy.add(self.buffed_towers)

    def delat_debuff(self):
        if self.name == 'boloto':
            for enemy in enemies_group:
                if enemy not in self.debuffed_enemies:
                    if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                        if self.parent.upgrade_level == '3a':
                            enemy.speed /= 4
                        else:
                            enemy.speed /= 2
                        enemy.add(self.debuffed_enemies)
                else:
                    if not self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                        if self.parent.upgrade_level == '3a':
                            enemy.speed *= 4
                        else:
                            enemy.speed *= 2
                        enemy.remove(self.debuffed_enemies)
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if enemy not in self.debuffed_enemies:
                        if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                            if self.parent.upgrade_level == '3a':
                                enemy.speed /= 4
                            else:
                                enemy.speed /= 2
                            enemy.add(self.debuffed_enemies)
                    else:
                        if not self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                            if self.parent.upgrade_level == '3a':
                                enemy.speed *= 4
                            else:
                                enemy.speed *= 2
                            enemy.remove(self.debuffed_enemies)
            self.mozhet_zhit = False

        if self.name == 'grib_gas':
            for enemy in enemies_group:
                if enemy not in self.debuffed_enemies:
                    if self.rect.colliderect(enemy.rect):
                        if self.parent.upgrade_level == '2a':
                            enemy.speed /= 1.25
                        elif self.parent.upgrade_level == '3a':
                            enemy.speed /= 2
                        enemy.add(self.debuffed_enemies)
                else:
                    if not self.rect.colliderect(enemy.rect):
                        if self.parent.upgrade_level == '2a':
                            enemy.speed *= 1.25
                        elif self.parent.upgrade_level == '3a':
                            enemy.speed *= 2
                        enemy.remove(self.debuffed_enemies)
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if enemy not in self.debuffed_enemies:
                        if self.rect.colliderect(enemy.rect):
                            if self.parent.upgrade_level == '2a':
                                enemy.speed /= 1.25
                            elif self.parent.upgrade_level == '3a':
                                enemy.speed /= 2
                            enemy.add(self.debuffed_enemies)
                    else:
                        if not self.rect.colliderect(enemy.rect):
                            if self.parent.upgrade_level == '2a':
                                enemy.speed *= 1.25
                            elif self.parent.upgrade_level == '3a':
                                enemy.speed *= 2
                            enemy.remove(self.debuffed_enemies)

        if self.name == 'cvetok':
            for enemy in enemies_group:
                if enemy not in self.debuffed_enemies:
                    if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                        enemy.atk /= 1.5
                        enemy.add(self.debuffed_enemies)
                else:
                    if not self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                        enemy.atk *= 1.5
                        enemy.remove(self.debuffed_enemies)
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if enemy not in self.debuffed_enemies:
                        if self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                            enemy.atk /= 1.5
                            enemy.add(self.debuffed_enemies)
                    else:
                        if not self.rect.collidepoint(enemy.rect.centerx, enemy.rect.centery):
                            enemy.atk *= 1.5
                            enemy.remove(self.debuffed_enemies)
            self.mozhet_zhit = False

    def check_life(self):
        if self.name == 'mat':
            for tower in towers_group:
                if tower.name == 'matricayshon':
                    if self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery):
                        self.mozhet_zhit = True

        if self.name == 'cvetok':
            for tower in towers_group:
                if tower.name == 'cvetochnica':
                    if self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery):
                        self.mozhet_zhit = True
            if not self.mozhet_zhit:
                for enemy in self.debuffed_enemies:
                    enemy.atk *= 1.5
                    enemy.remove(self.debuffed_enemies)

        if self.name == 'mana':
            for tower in towers_group:
                if tower.name == 'davalka':
                    if self.parent.upgrade_level == '2b':
                        if self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery):
                            self.mozhet_zhit = True
                    elif self.parent.upgrade_level == '3b':
                        if (self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery) or self.rect3.collidepoint(tower.rect.centerx, tower.rect.centery)) and not (self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery) and self.rect3.collidepoint(tower.rect.centerx, tower.rect.centery)):
                            self.mozhet_zhit = True

        if self.name == 'vodkamat' or self.name == 'fire_luja':
            if self.lifetime > 0:
                self.lifetime -= 1
            else:
                self.mozhet_zhit = False

        if self.name == 'grib_gas':
            if self.lifetime > 0:
                self.lifetime -= 1
            else:
                self.mozhet_zhit = False
                for enemy in self.debuffed_enemies:
                    if self.parent.upgrade_level == '2a':
                        enemy.speed *= 1.25
                    elif self.parent.upgrade_level == '3a':
                        enemy.speed *= 2

        if self.name == 'boloto':
            for tower in towers_group:
                if tower.name == 'bolotnik':
                    if self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery):
                        self.mozhet_zhit = True
            for tower in nekusaemie_group:
                if tower.name == 'bolotnik':
                    if self.rect2.collidepoint(tower.rect.centerx, tower.rect.centery):
                        self.mozhet_zhit = True
            if self.mozhet_zhit == False:
                if not hasattr(self, 'lifetime'):
                    self.lifetime = 180
                self.mozhet_zhit = True
            if hasattr(self, 'lifetime'):
                if self.lifetime > 0:
                    self.lifetime -= 1
                else:
                    self.mozhet_zhit = False
                    for enemy in self.debuffed_enemies:
                        if self.parent.upgrade_level == '3a':
                            enemy.speed *= 4
                        else:
                            enemy.speed *= 2

        if self.name == 'kuklo':
            for tower in towers_group:
                if tower.name == 'kokol':
                    if (self.rect.centery == tower.rect.centery - 127 and self.rect.centerx-1 == tower.rect.centerx) or (self.rect.centery == tower.rect.centery + 129 and self.rect.centerx-1 == tower.rect.centerx):
                        self.mozhet_zhit = True

    def check_tower(self):
        if not self.mozhet_zhit:
            self.kill()
            for tower in self.buffed_towers:
                if self.name == 'mat' or self.name == 'vodkamat':
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
                            or tower.name == "inquisitor"\
                            or tower.name == "priest"\
                            or tower.name == "ded_moroz"\
                            or tower.name == "uvelir"\
                            or tower.name == "krovnyak"\
                            or tower.name == "kokol"\
                            or tower.name == "sliz"\
                            or tower.name == "klonys"\
                            or tower.name == "furry_medved"\
                            or tower.name == "furry_volk"\
                            or tower.name == "furry_zayac"\
                            or tower.name == "kar_mag"\
                            or tower.name == "shabriri"\
                            or tower.name == "prokach"\
                            or tower.name == "pulelom"\
                            or tower.name == "chistiy"\
                            or tower.name == "sekirshik"\
                            or tower.name == "kirka"\
                            or tower.name == "elf"\
                            or tower.name == "holodilnik"\
                            or tower.name == "chorniy"\
                            or tower.name == 'electro_maga':
                        if not self.max_buff:
                            tower.basic_attack_cooldown *= 1.5
                        else:
                            tower.basic_attack_cooldown += 180
                        tower.time_indicator //= 1.5
                        if tower.name == 'kopitel' or tower.name == "uvelir" or tower.name == "kar_mag":
                            tower.basic_spawn_something_cooldown *= 1.5

                elif self.name == 'mana':
                    if hasattr(tower, 'atk'):
                        if self.parent.upgrade_level == '2b':
                            tower.atk /= 1.5
                        elif self.parent.upgrade_level == '3b':
                            tower.atk /= 2

            if self.name == 'vodkamat':
                Buff('mat', self.rect.x, self.rect.y, self)

        if self.name == 'mat' or self.name == 'kuklo' or self.name == 'mana':
            self.mozhet_zhit = False

    def attack(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        else:
            self.attack_cooldown = self.basic_attack_cooldown
            for enemy in enemies_group:
                if self.rect.colliderect(enemy.rect):
                    self.dealing_damage(enemy)
            for enemy in neutral_objects_group:
                if enemy.height == "high":
                    if self.rect.colliderect(enemy.rect):
                        self.dealing_damage(enemy)
            self.attack_cooldown -= 1  # так надо тк иначе будет просираться 1 тик кулдауна и будут ошибки в подсчётах

    def dealing_damage(self, enemy):
        self.damage = self.atk
        if enemy.vulnerabled > 0:
            self.damage *= 2
        for k, v in enemy.vulnerables_and_resists.items():
            if k == self.damage_type:
                self.damage *= (100 + v)/100
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
        if self.gender == 'tower_buff':
            self.delat_buff()
            self.check_life()
            self.check_tower()
            if hasattr(self, 'atk'):
                self.attack()
        else:
            self.delat_debuff()
            if hasattr(self, 'atk'):
                self.attack()
            self.check_life()
            if not self.mozhet_zhit:
                self.kill()

    def __repr__(self):
        return f"Я {self.name}"


class Slot:
    def __init__(self, pos):    # allowed_rarity=("common",)
        self.pos = pos
        self.blocked = False
        self.free_placement = False
        self.allowed_rarity = None
        self.image = image.load("images/slots_rarity/default_slot.png").convert_alpha()

        self.rect = self.image.get_rect(topleft=self.pos)
        self.render_layer = 3
        self.is_move = False

        self.unit_inside = None
        self.unit_image = image.load("images/other/nothing.png").convert_alpha()    # пока так
        self.unit_rect = self.unit_image.get_rect()
        self.unit_default_rect = self.unit_rect
        self.unit_cost = 0
        self.kd_time = 0
        self.default_kd_time = 0
        slots_group.add(self)

    def repaint(self):
        if self.unit_inside:
            if self.unit_inside.rarity == "legendary":
                self.image = image.load("images/slots_rarity/legendary_slot.png").convert_alpha()
            if self.unit_inside.rarity == "common":
                self.image = image.load("images/slots_rarity/common_slot.png").convert_alpha()
            if self.unit_inside.rarity == "spell":
                self.image = image.load("images/slots_rarity/spell_slot.png").convert_alpha()
        else:
            self.image = image.load("images/slots_rarity/default_slot.png").convert_alpha()

    def add_unit(self, unit):
        self.unit_inside = Tower(unit.name, (self.unit_rect.x - 100, self.unit_rect.y))   # x - 100 == нет всяких блакиков и ворон
        self.unit_inside.image = image.load(f"images/towers/{self.unit_inside.name}/{self.unit_inside.name}_preview.png").convert_alpha()
        self.unit_inside.rect = self.unit_inside.image.get_rect(topleft=(self.pos[0] + 62, self.pos[1]))
        self.unit_default_rect = self.unit_inside.rect
        self.unit_cost = tower_costs[unit.name]   # можно прям в тавер записать
        self.kd_time = -1                            # можно прям в тавер записать
        self.default_kd_time = towers_kd[unit.name]
        self.free_placement = unit.free_placement
        self.repaint()

    def remove_unit(self):
        self.unit_inside.kill()
        self.unit_inside.rect = self.unit_inside.image.get_rect()
        self.unit_default_rect = self.unit_inside.rect
        self.unit_cost = 0
        self.kd_time = 0
        self.default_kd_time = 0
        self.unit_inside = None
        self.repaint()

    def move_unit(self):
        self.unit_inside.rect = self.unit_inside.image.get_rect(center=mouse.get_pos())
        self.unit_inside.render_layer = 9
        self.unit_inside.image = towers_wait[self.unit_inside.name][0]

    def back_to_default(self):
        self.unit_inside.image = image.load(f"images/towers/{self.unit_inside.name}/{self.unit_inside.name}_preview.png").convert_alpha()

        self.unit_inside.rect = self.unit_default_rect
        self.unit_inside.render_layer = 3

    def magic_cooldown(self):
        pass

    def update(self):
        if self.unit_inside:
            self.magic_cooldown()
            if self.kd_time > 0:                                                        # уменьшает кд с каждым циклом
                self.kd_time -= 1

            if self.is_move and self.kd_time == -1:                                     # если нажал кнопку и кд откатилось
                self.unit_inside.image = image.load(f"images/towers/{self.unit_inside.name}/wait/{self.unit_inside.name}1.png").convert_alpha()
                self.move_unit()
            if self.is_move and self.kd_time != -1:                                     # если нажал кнопку и кд не откатилось
                self.is_move = False
            if self.is_move is not True and self.unit_inside.rect != self.unit_default_rect:               # если отжал кнопку и не на дефолтной позиции.
                self.back_to_default()

            if self.kd_time == 0:                                                       # когда кд дошло до нуля, загрузить картину юнита
                self.kd_time = -1

    def __repr__(self):
        return f"I am at {self.pos[1]}. I has {self.unit_inside} inside"


class Shovel(sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites_group)
        self.pos = pos
        self.image = image.load("images/shovel/lopata.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.default_rect = self.rect
        self.is_move = False
        self.name = "shovel"
        self.render_layer = 3

    def move(self):
        self.rect = self.image.get_rect(center=mouse.get_pos())

    def back_to_default(self):
        self.rect = self.default_rect

    def update(self):
        if self.is_move:
            self.move()
        if not self.is_move and self.rect != self.default_rect:
            self.back_to_default()


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
        self.pos = (0, 0)
        self.color_manage = False
        self.new_color = (0, 0, 0)
        buttons_group.append(self)

    def click(self, surf, pos, col=(255, 255, 255), offset_pos=(0, 0)):  # offset_pos нужно только где есть скрол
        if self.data_type == "text":
            if not self.color_manage:
                self.image = self.font.render(self.text, font, col)   # По дефолту цвет текста белый. Я ебал по 50 раз писать одно и тоже
            else:
                self.image = self.font.render(self.text, font, self.new_color)
        self.rect = self.image.get_rect(topleft=(pos[0] + offset_pos[0], pos[1] + offset_pos[1]))

        self.pos = pos
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

    def on_hover(self, offset_pos=(0, 0)):
        if hasattr(self, "image"):
            if self.image.get_rect(topleft=(self.pos[0] + offset_pos[0], self.pos[1] + offset_pos[1])).collidepoint(mouse_pos):
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


class UpgradeTowerButton:
    def __init__(self, number: str, pos):
        self.pushed = False
        self.activate = False
        self.number = number
        self.pos = pos
        self.image = upgrade_tower_red
        self.rect = self.image.get_rect(topleft=self.pos)
        self.repainted = False
        tower_upgrades_group.add(self)

    def set_active(self, state):

        if self.activate != state:
            if state:
                self.image = upgrade_tower_green
            if not state:
                self.image = upgrade_tower_red
            self.activate = state

    def repaint_to_hovered(self):
        if not self.repainted:
            new_img = self.image.__copy__()
            for i in range(new_img.get_width()):
                for j in range(new_img.get_height()):
                    pixel = new_img.get_at((i, j))
                    if pixel == (200, 0, 0, 255):
                        new_img.set_at((i, j), (255, 0, 0))
                    if pixel == (0, 200, 0, 255):
                        new_img.set_at((i, j), (0, 255, 0))

            self.image = new_img
            self.repainted = True

    def repaint_to_default(self):
        if self.repainted:
            new_img = self.image.__copy__()
            for i in range(new_img.get_width()):
                for j in range(new_img.get_height()):
                    pixel = new_img.get_at((i, j))
                    if pixel[0] == 255:
                        new_img.set_at((i, j), (200, 0, 0))
                    if pixel[1] == 255:
                        new_img.set_at((i, j), (0, 200, 0))
            self.image = new_img
            self.repainted = False


class Scroller:
    def __init__(self):
        self.scroll_offset_x = 0
        self.scroll_offset_y = 0
        self.target_scroll_offset_x = 0
        self.target_scroll_offset_y = 0
        self.rules = {
            "manual_menu": {
                "x": {"min": 0, "max": 0},
                "y": {"min": -2740, "max": 0}
            },
            "global_map": {
                "x": {"min": -3838, "max": 0},  # -2
                "y": {"min": -2302, "max": 0}   # -2
            },
            "reward_second_stage": {
                "x": {"min": 0, "max": 0},
                "y": {"min": 0, "max": 0}
            },
            "tower_select": {
                "x": {"min": 0, "max": 0},
                "y": {"min": -1110, "max": 0}
            }
        }
        self.remembered_scroll_offsets = {
            "global_map": (0, 0),
        }

    def set_scroll_offset(self, offset):
        self.scroll_offset_x = offset[0]
        self.scroll_offset_y = offset[1]
        self.target_scroll_offset_x = offset[0]
        self.target_scroll_offset_y = offset[1]

    def set_target_scroll_offset(self, offset):
        self.target_scroll_offset_x = offset[0]
        self.target_scroll_offset_y = offset[1]

    def check_possible_scrolling(self):
        if game_state in self.rules:
            if self.scroll_offset_x < self.rules[game_state]["x"]["min"]:
                self.scroll_offset_x = self.rules[game_state]["x"]["min"]
            if self.scroll_offset_x > self.rules[game_state]["x"]["max"]:
                self.scroll_offset_x = self.rules[game_state]["x"]["max"]

            if self.scroll_offset_y < self.rules[game_state]["y"]["min"]:
                self.scroll_offset_y = self.rules[game_state]["y"]["min"]
            if self.scroll_offset_y > self.rules[game_state]["y"]["max"]:
                self.scroll_offset_y = self.rules[game_state]["y"]["max"]

    def smooth_movement(self):
        if self.target_scroll_offset_x - self.scroll_offset_x > 40:
            self.scroll_offset_x += 6
        elif self.target_scroll_offset_x - self.scroll_offset_x > 20:
            self.scroll_offset_x += 3
        elif self.target_scroll_offset_x - self.scroll_offset_x > 1:
            self.scroll_offset_x += 1

        if self.target_scroll_offset_x - self.scroll_offset_x < -40:
            self.scroll_offset_x -= 6
        elif self.target_scroll_offset_x - self.scroll_offset_x < -20:
            self.scroll_offset_x -= 3
        elif self.target_scroll_offset_x - self.scroll_offset_x < -1:
            self.scroll_offset_x -= 1

        if self.target_scroll_offset_y - self.scroll_offset_y > 40:
            self.scroll_offset_y += 6
        elif self.target_scroll_offset_y - self.scroll_offset_y > 20:
            self.scroll_offset_y += 3
        elif self.target_scroll_offset_y - self.scroll_offset_y > 1:
            self.scroll_offset_y += 1

        if self.target_scroll_offset_y - self.scroll_offset_y < -40:
            self.scroll_offset_y -= 6
        elif self.target_scroll_offset_y - self.scroll_offset_y < -20:
            self.scroll_offset_y -= 3
        elif self.target_scroll_offset_y - self.scroll_offset_y < -1:
            self.scroll_offset_y -= 1

    def current_scroll_offset(self) -> tuple:
        return self.scroll_offset_x, self.scroll_offset_y

    def current_target_scroll_offset(self) -> tuple:
        return self.target_scroll_offset_x, self.target_scroll_offset_y


class TextField:
    def __init__(self, text, topleft_pos, max_width, color_=(0, 0, 0), font_=font25, text_speed=2, enable_animation=True, alignment="left"):
        if enable_animation:
            self.default_text = self.not_shown_text = text
            self.text = ""
        else:
            self.text = self.default_text = text
            self.not_shown_text = ""
        self.topleft_pos = topleft_pos
        self.max_width = max_width
        self.color = color_
        self.font = font_
        self.anim_count = 0
        self.text_speed = text_speed
        self.alignment = alignment  # right, center     in dev
        text_fields_group.add(self)

    def render_text(self, surf):
        def get_whitespace_width():
            return self.font.render(" ", True, self.color).get_width()

        def get_word_width(word_):
            return self.font.render("".join(word_), True, self.color).get_width()

        lines = 1

        if self.alignment == "left":
            word_pos = self.topleft_pos
            for word in self.text.split():
                word_width = get_word_width(word)
                if word_pos[0] + word_width > self.max_width + self.topleft_pos[0]:
                    word_pos = self.topleft_pos[0], word_pos[1] + self.get_font_height()
                    lines += 1
                surf.blit(self.font.render(word, True, self.color), word_pos)
                if level.rect_visible:
                    draw.rect(screen, (0, 200, 0), self.font.render(word, True, self.color).get_rect(topleft=word_pos), 5)  # отображение границы слова
                word_pos = word_pos[0] + word_width + get_whitespace_width(), word_pos[1]

        if self.alignment == "center":      # works only with 1 word
            if len(self.text.split()) == 1:
                word = str(self.text)
                word_pos = (self.max_width - get_word_width(word)) // 2 + self.topleft_pos[0], self.topleft_pos[1]
                surf.blit(self.font.render(word, True, self.color), word_pos)

        if level.rect_visible:
            draw.rect(screen, (200, 0, 0), Rect(self.topleft_pos[0], self.topleft_pos[1], self.max_width, self.get_font_height() * lines), 5)   # отображение границы текста

    def get_font_height(self):
        return self.font.render(" ", True, self.color).get_height()

    def update(self) -> bool:
        if self.anim_count < self.text_speed:
            self.anim_count += 1
        else:
            self.anim_count = 0
            if self.not_shown_text != "":
                self.text += self.not_shown_text[0]
                self.not_shown_text = self.not_shown_text[1:]

        if self.not_shown_text != "":
            return False
        else:
            return True


def render_bg_decorator(func):
    @functools.wraps(func)  # нужно для func.__name__
    def wrapper():
        screen.blit(global_map.event.bg_image, (0, 0))

        if global_map.event.has_event_stages:
            screen.blit(dialog_menu, (100, 550))

        func()

    return wrapper


def is_free(new_tower):
    is_free_list = []           # Проверка свободна ли клетка
    for tower in towers_group:
        if tower != new_tower:
            is_free_list.append(tower.rect.collidepoint(new_tower.rect.centerx, new_tower.rect.centery) is False)
    for nekusaemiy in nekusaemie_group:
        if nekusaemiy != new_tower:
            is_free_list.append(nekusaemiy.rect.collidepoint(new_tower.rect.centerx, new_tower.rect.centery) is False)
    for neutral_object in neutral_objects_group:
        if neutral_object != new_tower:
            is_free_list.append(neutral_object.rect.collidepoint(new_tower.rect.centerx, new_tower.rect.centery) is False)
    if all(is_free_list) or new_tower.free_placement:
        is_free_list.clear()
        return True


def uniq_is_free(new_tower):
    if new_tower.name == "gnome_cannon1":
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


def tower_placement(slot_):
    if is_free(slot_.unit_inside):
        if level.money - tower_costs[slot_.unit_inside.name] >= 0 or level.cheat:
            Tower(slot_.unit_inside.name, unit_pos)
            if not level.cheat:
                level.money -= tower_costs[slot_.unit_inside.name]
                slot_.kd_time = slot_.default_kd_time

    elif slot_.unit_inside.name == "gnome_cannon1" or slot_.unit_inside.name == "go_bleen1":
        ok_, tower_name = uniq_is_free(slot_.unit_inside)
        if ok_:
            if level.money - tower_costs[slot_.unit_inside.name] >= 0:
                Tower(tower_name, unit_pos)
                if not level.cheat:
                    level.money -= tower_costs[slot_.unit_inside.name]
                    slot_.kd_time = slot_.default_kd_time


def upload_data(default=False):
    global passed_levels, \
        received_towers, \
        not_received_towers, \
        encountered_enemies, \
        not_encountered_enemies, \
        city_coins, \
        forest_coins, \
        evil_coins, \
        mountain_coins, \
        snow_coins, \
        completed_events, \
        temp_hero_pos, \
        temp_scroll_offset, \
        enemy_levels

    load_file = "saves/current_save.save"
    if default:
        load_file = "saves/default_save.save"

    with open(load_file, "r", encoding="utf-8") as file:
        row = list(map(int, str(*file.readline().strip().split(" = ")[1:]).replace("(", "").replace(")", "").split(",")))
        passed_levels = []
        for i in range(len(row)):
            if i % 2 == 0:
                pos = row[i], row[i+1]
                passed_levels.append(pos)

        row = list(map(int, str(*file.readline().strip().split(" = ")[1:]).replace("(", "").replace(")", "").split(",")))
        enemy_levels = []
        for i in range(len(row)):
            if i % 2 == 0:
                pos = row[i], row[i+1]
                enemy_levels.append(pos)

        received_towers = str(*file.readline().strip().split(" = ")[1:]).split(", ")       # считать список
        not_received_towers = str(*file.readline().strip().split(" = ")[1:]).split(", ")
        if not_received_towers[0] == "[]":
            not_received_towers = []
        encountered_enemies = str(*file.readline().strip().split(" = ")[1:]).split(", ")
        not_encountered_enemies = str(*file.readline().strip().split(" = ")[1:]).split(", ")
        if not_encountered_enemies[0] == "[]":
            not_encountered_enemies = []

        completed_events = str(*file.readline().strip().split(" = ")[1:]).split(", ")
        if completed_events[0] == "[]":
            completed_events = []

        line = str(*file.readline().strip().split(" = ")[1:]).split(",")
        temp_hero_pos = tuple(map(int, line))

        line = str(*file.readline().strip().split(" = ")[1:]).split(",")
        temp_scroll_offset = tuple(map(int, line))

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
        file.write(f"passed_levels = " + str(passed_levels).replace("[", "").replace("]", "").replace("'", "") + "\n")
        file.write(f"enemy_levels = " + str(enemy_levels).replace("[", "").replace("]", "").replace("'", "") + "\n")
        file.write(f"received_towers = " + str(received_towers).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"not_received_towers = " + str(not_received_towers).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"encountered_enemies = " + str(encountered_enemies).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"not_encountered_enemies = " + str(not_encountered_enemies).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"completed_events = " + str(completed_events).replace("['", "").replace("']", "").replace("'", "") + "\n")
        file.write(f"hero_pos = {str(global_map.hero_pos[0])}, {str(global_map.hero_pos[1])}" + "\n")
        file.write(f"global_map_scroll_offset = {str(scroller.remembered_scroll_offsets['global_map'][0])}, {str(scroller.remembered_scroll_offsets['global_map'][1])}" + "\n")
        file.write(f"-----\n")
        for k, v in your_coins.items():
            file.write(f"{k} = {v}\n")
        file.write(f"-----\n")
        for k, v in upgrades.items():
            file.write(f"{k} = " + str(v).replace("['", "").replace("']", "").replace("'", "") + "\n")


def draw_info(pos, current_value, max_value, reversed_=False):       # (196, 380)
    draw.rect(modification_preview_menu, (200, 0, 0), (*pos, 300, 35))
    if current_value != 0:
        current_value *= 10
        max_value *= 10
        if reversed_:
            w = 60 * (6 - max(int(current_value / (max_value / 5)), 1))
        else:
            w = 60 * max(int(current_value / (max_value / 5)), 1)       # int, max и 1 убрать и будут не целые квадраты
        draw.rect(modification_preview_menu, (0, 200, 0), (*pos, w, 35))
        for i in range(1, 5):
            draw.line(modification_preview_menu, (0, 0, 0), (pos[0] + (60 * i), pos[1]), (pos[0] + (60 * i), pos[1] + 34), 5)
    else:
        draw.rect(modification_preview_menu, (128, 128, 128), (*pos, 300, 35))
    draw.rect(modification_preview_menu, (0, 0, 0), (*pos, 300, 35), 5)


# пример
@render_bg_decorator
def new_event_with_chest():
    select_menu.blit(font60.render("Болото", True, (0, 0, 0)), (352, 10))

    if first_event_button.click(screen, (370, 300)):
        global_map.chest = Chest((5, 5), chests_rewards[(5, 5)], bg_image="bg_image_(2, 3)")
        global_map.event.finish_event(next_game_state="reward_first_stage")


# ивент для начала уровня   !!! написать action_args=Level(...) !!!
def start_level_event(level_: Level):
    global game_state, last_game_state, level
    scroller.remembered_scroll_offsets["global_map"] = scroller.current_scroll_offset()
    last_game_state = game_state
    level = level_
    game_state = "tower_select"


def cant_step_event():
    global game_state
    global_map.hero_pos, global_map.next_hero_pos = global_map.last_hero_pos, global_map.hero_pos
    scroller.set_scroll_offset((scroller.scroll_offset_x, scroller.scroll_offset_y))    # чтобы камера не фокусировалась на чела
    game_state = "global_map"


# доделать
@render_bg_decorator
def hello_game_event():
    global event_stage
    if event_stage == 1:
        TextField("Главный герой", (130, 580), 400, font_=font40, enable_animation=False)
        TextField("Где это я?", (150, 650), 1300)
        event_stage += 1

    if event_stage == 2:
        screen.blit(gg_dialog, (100, 100))

    if event_stage == 3:
        TextField("Фаермаг", (1100, 580), 400, font_=font40, enable_animation=False)
        TextField("Я нашёл тебя тут.  ...(Сюжет будет потом)... Тебе нужно в деревню", (150, 650), 1300)
        event_stage += 1

    if event_stage == 4:
        screen.blit(fire_mag, (1000, 100))

    if event_stage == 5:
        TextField("Фаермаг", (1100, 580), 400, font_=font40, enable_animation=False)
        TextField("PS: карту можно двигать зажав колёсико мыши", (150, 650), 1300)
        event_stage += 1

    if event_stage == 6:
        screen.blit(fire_mag, (1000, 100))

    if event_stage == 7:
        global_map.event.finish_event()


@render_bg_decorator
def village_event():
    global event_stage
    if event_stage == 1:
        TextField("Жители деревни", (1100, 580), 400, font_=font40, enable_animation=False)
        TextField("О нет, на нас напали", (150, 650), 1300)
        event_stage += 1

    if event_stage == 2:
        screen.blit(villager, (1000, 100))

    if event_stage == 3:
        global_map.event.finish_event()
        global_map.event = Event(start_level_event, on_map_image="None", bg_image="None", action_args=Level((13, 8), 22500, 500, 50, level_waves["3"], level_allowed_enemies["3"], level_image="2"))
        global_map.event.do()


@render_bg_decorator
def lost_in_forest_event():
    global event_stage
    if event_stage == 1:
        TextField("Главный герой", (130, 580), 400, font_=font40, enable_animation=False)
        TextField("О нет, там я потеряюсь. Нужно вернуться на тропинку", (150, 650), 1300)
        global_map.hero_pos, global_map.next_hero_pos = global_map.last_hero_pos, global_map.hero_pos
        event_stage += 1

    if event_stage == 2:
        screen.blit(gg_dialog, (100, 100))

        global_map.focus_on_hero()

    if event_stage == 3:
        global_map.event.finish_event(can_repeat=True)


def menu_positioning():
    global game_state,\
            running,\
            last_game_state,\
            passed_levels, \
            level,\
            scroll_offset, \
            coin_indent_x, \
            count_of_reward_coins, \
            general_volume, \
            music_volume, \
            sound_effects_volume, \
            developer_mode, \
            current_scroll_offset_state, \
            event_stage

    if game_state == "main_menu":
        text_fields_group.clear()   # на всякий
        screen.blit(main_menu, (0, 0))
        screen.blit(game_name, (416, 10))

        if new_game_button.click(screen, (30, 460)):    # 380
            if developer_mode:
                last_game_state = game_state
                game_state = "yes_no_window"  # новая игра
            else:
                Alert("Анжела Вячеславовна, Вам сюда нельзя", (200, 400), 150, font60, (0, 255, 255))

        if to_map_button.click(screen, (30, 540)):
            if developer_mode:
                last_game_state = game_state
                scroller.set_scroll_offset(scroller.remembered_scroll_offsets["global_map"])
                game_state = "global_map"
            else:
                Alert("Анжела Вячеславовна, Вам сюда нельзя", (200, 400), 150, font60, (0, 255, 255))
        if manual_menu_button.click(screen, (30, 620)):
            last_game_state = game_state
            scroller.set_scroll_offset((0, 0))
            game_state = "manual_menu"
        if settings_button.click(screen, (30, 700)):
            last_game_state = game_state
            game_state = "settings_menu"
        if quit_button.click(screen, (30, 780)):
            running = False

        if level1_button.click(screen, (600, 620), col=(255, 0, 0)):
            level = Level((3, 0), 22500, 500, 50, level_waves["3"], level_allowed_enemies["3"], level_image="2")
            scroller.scroll_offset_y = 0
            level.refresh()
            last_game_state = game_state
            game_state = "tower_select"

    if game_state == "yes_no_window":
        text_fields_group.clear()
        screen.blit(main_menu, (0, 0))
        screen.blit(pause_menu, (480, 250))
        screen.blit(font60.render("Начать новую игру?", True, (255, 255, 255)), (507, 280))

        if accept_button.click(screen, (620, 485)):
            upload_data(default=True)
            preview_group.refresh(3)
            global_map.refresh()

            last_game_state = game_state

            global_map.event = Event(hello_game_event, on_map_image="None")    # стартовый ивент
            game_state = "event"
            event_stage = 1

            scroller.set_scroll_offset(scroller.remembered_scroll_offsets["global_map"])
            global_map.tiles.clear()
            global_map.build_tiles(default=True)

        if accept_button.on_hover():
            screen.blit(font30.render("!!! Весь прогресс сотрётся !!!", True, (200, 0, 0)), (598, 580))

        if deny_button.click(screen, (870, 485)):
            last_game_state, game_state = game_state, last_game_state

    if game_state == "manual_menu":
        text_fields_group.clear()   # если есть text_field не в ивенте, то нужно использовать clear в начале game_state | анимация работает только в ивентах
        screen.blit(preview_menu, (0, 0))
        preview_menu.blit(entity_preview_menu, (250, 120))      # 50 100 пофиксить/вырезать нафиг
        entity_preview_menu.blit(entity_preview_menu_copy, (0, 0))
        screen.blit(font50.render("Справочник", True, (0, 0, 0)), (370, 60))
        screen.blit(modification_preview_menu, (830, 120))
        modification_preview_menu.blit(modification_preview_menu_copy, (0, 0))
        modification_preview_menu.blit(line_, (0, 275))
        scroller.check_possible_scrolling()

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
            tower_upgrades_group.check_hover(entity_preview_menu, offset_pos=(830, 120))
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
            modification_preview_menu.blit(line_, (0, 600))
            if preview_group.pushed_entity.name in upgrade_costs:
                up_cost = upgrade_costs[preview_group.pushed_entity.name][tower_upgrades_group.pushed_entity.number].split()
                upgrade_cost = int(up_cost[0])
                upgrade_coin_name = up_cost[1]

                if tower_upgrades_group.pushed_entity.number not in upgrades[preview_group.pushed_entity.name] and tower_upgrades_group.possible_upgrade_path():
                    modification_preview_menu.blit(font60.render(str(f"{your_coins[upgrade_coin_name]}/{upgrade_cost}"), True, (0, 0, 0)), (270, 510))
                    offset = font60.render(str(f"{your_coins[upgrade_coin_name]}/{upgrade_cost}"), True, (0, 0, 0)).get_width()
                    modification_preview_menu.blit(coins[upgrade_coin_name], (280 + offset, 520))    # 355

                    if buy_upgrade_button.click(screen, (870, 630), col=(0, 0, 0)) and your_coins[upgrade_coin_name] >= upgrade_cost:
                        upgrades[preview_group.pushed_entity.name].append(tower_upgrades_group.pushed_entity.number)
                        your_coins[upgrade_coin_name] -= upgrade_cost

                if tower_upgrades_group.pushed_entity.number not in upgrades[preview_group.pushed_entity.name] and not tower_upgrades_group.possible_upgrade_path():
                    TextField("Нужен предыдущий навык", (875, 660), 450, (255, 0, 0), font_=font30, enable_animation=False)

                if tower_upgrades_group.pushed_entity.number in upgrades[preview_group.pushed_entity.name] and preview_group.pushed_entity.upgrade_level == tower_upgrades_group.pushed_entity.number:
                    TextField("Выбрано", (960, 630), 300, (255, 0, 0), font_=font60, enable_animation=False)

                if tower_upgrades_group.pushed_entity.number in upgrades[preview_group.pushed_entity.name] and preview_group.pushed_entity.upgrade_level != tower_upgrades_group.pushed_entity.number:
                    if choice_button.click(screen, (960, 630), col=(0, 0, 0)):
                        preview_group.pushed_entity.upgrade_level = tower_upgrades_group.pushed_entity.number
                        selected_upgrade_level = upgrades[preview_group.pushed_entity.name].pop(upgrades[preview_group.pushed_entity.name].index(tower_upgrades_group.pushed_entity.number))
                        upgrades[preview_group.pushed_entity.name].append(selected_upgrade_level)

            TextField(upgrade_descriptions[preview_group.pushed_entity.name][tower_upgrades_group.pushed_entity.number], (850, 420), 450, font_=font25, enable_animation=False)

        if back_button.click(screen, (1000, 750), col=(0, 0, 0)):
            game_state, last_game_state = last_game_state, game_state
            scroller.set_scroll_offset(scroller.remembered_scroll_offsets["global_map"])

        if change_preview_turn_button.click(screen, (1280, 90)):
            if preview_group.turn == Enemy:
                preview_group.turn = Tower
                change_preview_turn_button.image = image.load("images/coins/city_coin.png").convert_alpha()
            else:
                preview_group.turn = Enemy
                change_preview_turn_button.image = image.load("images/coins/evil_coin.png").convert_alpha()
            scroller.set_scroll_offset((0, 0))
            preview_group.pushed_entity = list(filter(preview_group.filter_by_turn, preview_group.entities))[0]

    if game_state != "main_menu"\
            and game_state != "main_settings_menu"\
            and game_state != "level_select"\
            and game_state != "manual_menu"\
            and game_state != "yes_no_window"\
            and game_state != "global_map"\
            and game_state != "reward"\
            and game_state != "event"\
            and game_state != "global_map_paused":
        screen.blit(level.image, (0, 0))
        if not level.cheat:
            level.draw_level_time()

        text_fields_group.clear()
        TextField(str(level.money), (88, 53), 100, font_=font40, enable_animation=False)
        if level.cheat:
            TextField("CHEAT MODE", (853, 110), 300, (255, 0, 0), font_=font40, enable_animation=False)

        all_sprites_group.custom_draw(screen)
        all_sprites_group.draw_other(screen)

        slots_group.custom_draw(screen)

    if game_state == "global_map":
        text_fields_group.clear()   # на всякий
        scroller.check_possible_scrolling()
        screen.blit(game_map, (66 + scroller.scroll_offset_x, 66 + scroller.scroll_offset_y))
        global_map.actions()
        global_map.render_overlay()
        scroller.smooth_movement()
        scroller.check_possible_scrolling()     # 2 раза, чтобы картинка не дёргалась

        if pause_button.click(screen, (1515, 58)):
            last_game_state = game_state
            game_state = "global_map_paused"

        if manual_menu_img_button.click(screen, (1445, 58)):
            last_game_state = game_state
            scroller.remembered_scroll_offsets["global_map"] = scroller.current_scroll_offset()
            scroller.set_scroll_offset((0, 0))
            game_state = "manual_menu"

        if settings_button_img.click(screen, (1375, 58)):
            last_game_state = game_state
            scroller.remembered_scroll_offsets["global_map"] = scroller.current_scroll_offset()
            game_state = "global_map_settings_menu"

    if game_state == "run":
        game_state = level.update()
        if pause_button.click(screen, (1515, 58)):  # 1550 30
            last_game_state = game_state
            Alert("Пауза", (700, 200), 75)
            game_state = "paused"

        if level.cheat:
            if kill_enemy_on_click_button.click(screen, (1400, 800)):
                if level.kill_enemy_on_click:
                    kill_enemy_on_click_button.ok = False
                    level.kill_enemy_on_click = False
                else:
                    kill_enemy_on_click_button.ok = True
                    level.kill_enemy_on_click = True
        else:
            level.kill_enemy_on_click = False

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
                level.refresh(slots_group)
                game_state = "tower_select"
                level.state = "not_run"
        else:
            if restart_button.click(screen, (582, 440), col=(130, 130, 130)):  # 2 кнопка серая
                pass
        if main_menu_button.click(screen, (567, 520)):
            level.refresh()
            last_game_state = game_state
            game_state = "main_menu"

            global_map.hero_pos, global_map.next_hero_pos = global_map.last_hero_pos, global_map.hero_pos
            global_map.focus_on_hero()
        if pause_button.click(screen, (1515, 58)):
            Alert("Пауза", (700, 200), 75)
            if level.state == "run":
                last_game_state = game_state
                game_state = "run"
            else:
                game_state, last_game_state = last_game_state, game_state

    if game_state == "global_map_paused":
        text_fields_group.clear()
        screen.blit(game_map, (66 + scroller.scroll_offset_x, 66 + scroller.scroll_offset_y))
        global_map.render_overlay()
        screen.blit(pause_menu, (480, 250))

        if resume_button.click(screen, (614, 280)):
            last_game_state = game_state
            game_state = "global_map"

        if settings_button.click(screen, (642, 360)):
            last_game_state = game_state
            game_state = "global_map_settings_menu"

        if manual_menu_button.click(screen, (621, 440)):
            scroller.remembered_scroll_offsets["global_map"] = scroller.current_scroll_offset()
            last_game_state = game_state
            game_state = "manual_menu"

        if main_menu_button.click(screen, (567, 520)):
            level.refresh()
            last_game_state = game_state
            game_state = "main_menu"

        if pause_button.click(screen, (1515, 58)):
            game_state, last_game_state = last_game_state, game_state

        if manual_menu_img_button.click(screen, (1445, 58)):
            pass

        if settings_button_img.click(screen, (1375, 58)):
            pass

    if game_state == "level_complited":
        screen.blit(pause_menu, (480, 250))
        screen.blit(font60.render("Уровень пройден", True, (193, 8, 42)), (544, 280))

        if to_map_button.click(screen, (669, 360)):     # 449
            if developer_mode:
                game_state = "global_map"
                scroller.set_scroll_offset(scroller.remembered_scroll_offsets["global_map"])
            else:
                Alert("Анжела Вячеславовна, Вам сюда нельзя", (200, 400), 150, font60, (0, 255, 255))
        if restart_button.click(screen, (582, 440)):
            last_game_state = game_state
            level.refresh()
            game_state = "tower_select"
        if main_menu_button.click(screen, (567, 520)):
            last_game_state = game_state
            game_state = "main_menu"

        if level.action_after_complete:
            level.action_after_complete.do()

    if game_state == "tower_select":
        text_fields_group.clear()
        screen.blit(select_menu, (250, 150))
        select_menu.blit(select_menu_copy, (0, 0))
        screen.blit(additional_menu, (1210, 150))
        screen.blit(botton_select_menu, (250, 750))
        scroller.check_possible_scrolling()

        select_towers_preview_group.move_element_by_scroll()
        select_towers_preview_group.check_hover(select_menu, offset_pos=(250, 150))
        if select_towers_preview_group.check_click(select_menu, offset_pos=(250, 150)):
            if select_towers_preview_group.pushed_entity.name in received_towers:
                slots_group.add_to_slots(select_towers_preview_group.pushed_entity)

        if select_towers_preview_group.check_hover(select_menu, offset_pos=(250, 150)):
            if select_towers_preview_group.hovered_entity.name in received_towers:
                TextField(select_towers_preview_group.hovered_entity.name, (1215, 160), 310, enable_animation=False, font_=font40, alignment="center")
                TextField(upgrade_descriptions[select_towers_preview_group.hovered_entity.name]["1"], (1230, 220), 280, enable_animation=False)     # [upgrades[select_towers_preview_group.hovered_entity.name][-1]] (1230, 160)
            else:
                TextField("???", (1215, 160), 310, enable_animation=False, font_=font40, alignment="center")
        else:
            TextField("???", (1215, 160), 310, enable_animation=False, font_=font40, alignment="center")

        select_towers_preview_group.go_animation()
        select_towers_preview_group.custom_draw(select_menu)

        if clear_button.click(screen, (321, 770), col=(0, 0, 0)):  # 1250, 470
            slots_group.clear_units()

        if random_choice_button.click(screen, (620, 770), col=(0, 0, 0)):  # 1248, 550
            slots_group.random_add_to_slots()

        if start_level_button.click(screen, (929, 760), col=(0, 0, 0)):    # 1265, 630
            if len(select_towers_preview_group.remember_entities) == 7 - len(level.blocked_slots):
                scroller.scroll_offset_y = 0
                game_state = "run"
                level.clear(ui_group, slots_group)
                level.state = "not_run"
                for obj_ in [*towers_group, *nekusaemie_group]:
                    if not obj_.name == 'krest':
                        if hasattr(obj_, "bullet"):
                            obj_.bullet.kill()
                        obj_.alive = False
                        obj_.kill()
            else:
                Alert("Остались свободные слоты", (400, 60), 75)
        if pause_button.click(screen, (1515, 58)):
            last_game_state = game_state
            Alert("Пауза", (700, 200), 75)
            game_state = "paused"
        ui_group.draw(screen)

    if game_state == "settings_menu":
        if last_game_state == "main_menu" or last_game_state == "level_select":
            screen.blit(main_menu, (0, 0))
            screen.blit(game_name, (416, 10))
        screen.blit(pause_menu, (480, 250))
        for i in range(int(general_volume*10//1)):
            screen.blit(red_32x32, (622+(i*36), 602))
        for i in range(int(music_volume*10//1)):
            screen.blit(nota, (622+(i*36), 652))
        for i in range(int(sound_effects_volume*10//1)):
            screen.blit(unvulnerable, (622+(i*36), 702))

        if back_button.click(screen, (709, 520)):
            game_state = last_game_state

        if cheat_button.click(screen, (550, 280)):
            if level.cheat:
                cheat_button.ok = False
                level.cheat = False
            else:
                cheat_button.ok = True
                level.cheat = True

        if rect_visible_button.click(screen, (735, 280)):
            if level.rect_visible:
                rect_visible_button.ok = False
                level.rect_visible = False
            else:
                rect_visible_button.ok = True
                level.rect_visible = True

        if no_death_animation.click(screen, (930, 280)):
            if level.no_death_animation:
                no_death_animation.ok = False
                level.no_death_animation = False
            else:
                no_death_animation.ok = True
                level.no_death_animation = True
                Alert("Анимации смерти выключена", (100, 450), 150)

        if unlock_all_button.click(screen, (600, 420)):
            unlock_all_button.ok = True

            for tower in not_received_towers:
                received_towers.append(tower)
            not_received_towers.clear()

            for enemy_ in not_encountered_enemies:
                encountered_enemies.append(enemy_)
            not_encountered_enemies.clear()

            passed_levels = [(0, 0), (0, 1), (0, 2)]
            preview_group.refresh(3)
            print("all_unlocked")

        if general_volume_button.click(screen, (619, 600)):
            pass
        if general_volume_up_button.click(screen, (989, 600)):
            if general_volume*10//1 < 10:
                general_volume = ((general_volume*10//1)+1)/10
        if general_volume_down_button.click(screen, (580, 600)):
            if general_volume*10//1 > 0:
                general_volume = ((general_volume*10//1)-1)/10
        if general_volume_mute_button.click(screen, (1030, 604)): 
            general_volume = 0.0

        if music_volume_button.click(screen, (619, 650)):
            pass
        if music_volume_up_button.click(screen, (989, 650)):
            if music_volume*10//1 < 10:
                music_volume = ((music_volume*10//1)+1)/10
        if music_volume_down_button.click(screen, (580, 650)):
            if music_volume*10//1 > 0:
                music_volume = ((music_volume*10//1)-1)/10
        if music_volume_mute_button.click(screen, (1030, 654)): 
            music_volume = 0.0

        if sound_effects_volume_button.click(screen, (619, 700)):
            pass
        if sound_effects_volume_up_button.click(screen, (989, 700)):
            if sound_effects_volume*10//1 < 10:
                sound_effects_volume = ((sound_effects_volume*10//1)+1)/10
        if sound_effects_volume_down_button.click(screen, (580, 700)):
            sound_effects_volume = ((sound_effects_volume*10//1)-1)/10
        if sound_effects_volume_mute_button.click(screen, (1030, 704)): 
            sound_effects_volume = 0.0

    if game_state == "global_map_settings_menu":
        text_fields_group.clear()
        screen.blit(game_map, (66 + scroller.scroll_offset_x, 66 + scroller.scroll_offset_y))
        global_map.render_overlay()
        screen.blit(pause_menu, (480, 250))
        for i in range(int(general_volume*10//1)):
            screen.blit(red_32x32, (622+(i*36), 602))
        for i in range(int(music_volume*10//1)):
            screen.blit(nota, (622+(i*36), 652))
        for i in range(int(sound_effects_volume*10//1)):
            screen.blit(unvulnerable, (622+(i*36), 702))

        if back_button.click(screen, (709, 520)):
            game_state, last_game_state = last_game_state, game_state

        if pause_button.click(screen, (1515, 58)):  # чтобы не пропадала кнопка паузы
            pass

        if manual_menu_img_button.click(screen, (1445, 58)):
            pass

        if settings_button_img.click(screen, (1375, 58)):
            pass

        if cheat_button.click(screen, (550, 280)):
            if level.cheat:
                cheat_button.ok = False
                level.cheat = False
            else:
                cheat_button.ok = True
                level.cheat = True

        if rect_visible_button.click(screen, (735, 280)):
            if level.rect_visible:
                rect_visible_button.ok = False
                level.rect_visible = False
            else:
                rect_visible_button.ok = True
                level.rect_visible = True

        if no_death_animation.click(screen, (930, 280)):
            if level.no_death_animation:
                no_death_animation.ok = False
                level.no_death_animation = False
            else:
                no_death_animation.ok = True
                level.no_death_animation = True
                Alert("Анимации смерти выключена", (100, 450), 150)

        if unlock_all_button.click(screen, (600, 420)):
            unlock_all_button.ok = True

            for tower in not_received_towers:
                received_towers.append(tower)
            not_received_towers.clear()

            for enemy_ in not_encountered_enemies:
                encountered_enemies.append(enemy_)
            not_encountered_enemies.clear()

            passed_levels = [(0, 0), (0, 1), (0, 2)]
            preview_group.refresh(3)
            print("all_unlocked")

        if general_volume_button.click(screen, (619, 600)):
            pass
        if general_volume_up_button.click(screen, (989, 600)):
            if general_volume*10//1 < 10:
                general_volume = ((general_volume*10//1)+1)/10
        if general_volume_down_button.click(screen, (580, 600)):
            if general_volume*10//1 > 0:
                general_volume = ((general_volume*10//1)-1)/10
        if general_volume_mute_button.click(screen, (1030, 604)):
            general_volume = 0.0

        if music_volume_button.click(screen, (619, 650)):
            pass
        if music_volume_up_button.click(screen, (989, 650)):
            if music_volume*10//1 < 10:
                music_volume = ((music_volume*10//1)+1)/10
        if music_volume_down_button.click(screen, (580, 650)):
            if music_volume*10//1 > 0:
                music_volume = ((music_volume*10//1)-1)/10
        if music_volume_mute_button.click(screen, (1030, 654)):
            music_volume = 0.0

        if sound_effects_volume_button.click(screen, (619, 700)):
            pass
        if sound_effects_volume_up_button.click(screen, (989, 700)):
            if sound_effects_volume*10//1 < 10:
                sound_effects_volume = ((sound_effects_volume*10//1)+1)/10
        if sound_effects_volume_down_button.click(screen, (580, 700)):
            sound_effects_volume = ((sound_effects_volume*10//1)-1)/10
        if sound_effects_volume_mute_button.click(screen, (1030, 704)):
            sound_effects_volume = 0.0

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
        text_fields_group.clear()
        scroller.remembered_scroll_offsets["global_map"] = scroller.current_scroll_offset()
        screen.blit(global_map.chest.bg_image, (0, 0))

        global_map.chest.bg_image.blit(font60.render("Награда", True, (0, 0, 0)), (195 + 480, 0 + 250))

        for i, (k, v) in enumerate(global_map.chest.rewards.items()):
            if k in coins:
                column = (i % count_of_reward_coins)
                global_map.chest.bg_image.blit(coins[k], (coin_indent_x + (column * (64 + coin_indent_x)) + (column * 22.5) + 480, 230 + 250))
                global_map.chest.bg_image.blit(font60.render(str(v), True, (0, 0, 0)), (coin_indent_x + (column * (64 + coin_indent_x)) - ((2 - column) * 22.5) + 480, 225 + 250))

        rewards_preview_group.custom_draw(global_map.chest.bg_image)   # , offset_pos=(480, 250)
        rewards_preview_group.check_hover(global_map.chest.bg_image)   # , offset_pos=(480, 250)
        rewards_preview_group.go_animation()

        if rewards_preview_group.check_click(global_map.chest.bg_image):   # , offset_pos=(480, 250)
            last_game_state = game_state
            game_state = "manual_menu"

            preview_group.refresh(3)
            for entity in preview_group.entities:
                if entity.name == rewards_preview_group.pushed_entity.name:
                    preview_group.pushed_entity = entity
                    scroller.set_scroll_offset((-preview_group.pushed_entity.pos[0], -preview_group.pushed_entity.pos[1]))

        if take_button.click(screen, (680, 540), col=(0, 0, 0)):
            if not global_map.chest.action_after_open:
                last_game_state = game_state
                game_state = "global_map"
                rewards_preview_group.clear_rewards()
                scroller.set_scroll_offset(scroller.remembered_scroll_offsets["global_map"])
            else:
                last_game_state = game_state
                event_stage = 1
                global_map.chest.action_after_open.do()

    if game_state == "event":
        if global_map.event:
            global_map.event.do()
        else:
            last_game_state = game_state
            game_state = "global_map"

    # -------


# --- from save
passed_levels = []  # должно быть тут
enemy_levels = []
received_towers = []
not_received_towers = []
encountered_enemies = []
not_encountered_enemies = []
completed_events = []
city_coins = 0
forest_coins = 0
evil_coins = 0
mountain_coins = 0
snow_coins = 0
upload_data()
# ---


bullets_group = sprite.Group()
parasites_group = sprite.Group()
buffs_group = sprite.Group()
creeps_group = sprite.Group()
enemies_group = sprite.Group()
towers_group = sprite.Group()
nekusaemie_group = sprite.Group()
neutral_objects_group = sprite.Group()
ui_group = sprite.Group()
all_sprites_group = ExtendedGroup()
clouds_group = sprite.Group()
alert_group = sprite.Group()
level_group = sprite.Group()
krests_group = sprite.Group()
preview_group = PreviewGroup(Tower, Enemy)
select_towers_preview_group = PreviewGroup(Tower)
tower_upgrades_group = TowerUpgradesGroup()
rewards_preview_group = RewardsPreviewGroup()
slots_group = SlotsGroup(slots_rarity={"common": 5, "spell": 2})  # "common": 2, "spell": 2, "legendary/common": 2, "spell/common": 1
global_map = GlobalMap()
global_map.hero_pos = global_map.last_hero_pos = global_map.next_hero_pos = temp_hero_pos
text_fields_group = TextFieldsGroup()

pause_button = Button("img", "other", "pause_button")
restart_button = Button("text", font60, "Перезапустить")
resume_button = Button("text", font60, "Продолжить")
settings_button = Button("text", font60, "Настройки")
settings_button_img = Button("img", "other", "settings_button")
main_menu_button = Button("text", font60, "В главное меню")
back_button = Button("text", font60, "Назад")
quit_button = Button("text", font60, "Выход")
new_game_button = Button("text", font60, "Новая игра",)
level_select_button = Button("text", font60, "Выбрать уровень")
to_map_button = Button("text", font60, "На карту")
cheat_button = Button("img", "menu", "cheat")
rect_visible_button = Button("img", "other", "rect_visible")
no_death_animation = Button("img", "other", "no_death_animation")
no_death_animation.ok = True
start_level_button = Button("text", font60, "Начать")
random_choice_button = Button("text", font50, "Случайно")
manual_menu_button = Button("text", font60, "Справочник")
manual_menu_img_button = Button("img", "other", "manual_menu_button")
change_preview_turn_button = Button("img", "coins", "city_coin")
accept_button = Button("text", font60, "Да")
deny_button = Button("text", font60, "Нет")
unlock_all_button = Button("text", font60, "Открыть всё")
buy_upgrade_button = Button("text", font60, "Купить")
clear_button = Button("text", font50, "Очистить")
take_button = Button("text", font60, "Забрать")
first_event_button = Button("img", "buffs", "boloto")
kust_event_button = Button("img", "creeps", "nekr_zombie_jirny")
choice_button = Button("text", font60, "Выбрать")
kill_enemy_on_click_button = Button("img", "other", "kill_enemy_onclick")
general_volume_button = Button("img", "other", "volume_bar")
general_volume_up_button = Button("img", "other", "up")
general_volume_down_button = Button("img", "other", "down")
general_volume_mute_button = Button("img", "other", "mute")
music_volume_button = Button("img", "other", "volume_bar")
music_volume_up_button = Button("img", "other", "up")
music_volume_down_button = Button("img", "other", "down")
music_volume_mute_button = Button("img", "other", "mute")
sound_effects_volume_button = Button("img", "other", "volume_bar")
sound_effects_volume_up_button = Button("img", "other", "up")
sound_effects_volume_down_button = Button("img", "other", "down")
sound_effects_volume_mute_button = Button("img", "other", "mute")
level1_button = Button("text", font60, "Нажать чтобы играть!")

global_map.build_tiles()
# global_map_levels_builder()
# GlobalMapLevelButton("1", "0", (118, 668), level=Level("1", 6750, 1500, 20, level_waves["1"], level_allowed_enemies["1"], allowed_cords=(448, 448), level_image="2"))    # !!! все буквы русские !!!
# GlobalMapLevelButton("2", "1", (295, 570), level=Level("2", 13500, 13501, 20, level_waves["2"], level_allowed_enemies["2"], allowed_cords=(320, 448, 576), level_image="2"))
# GlobalMapLevelButton("2а", "2", (409, 700), required_done_events=("spike_chest_allow",), level=Level("2а", 10, 13501, 20, level_waves["2"], level_allowed_enemies["2"], level_image="2"))
# GlobalMapLevelButton("2б", "2а", (723, 791), event=Event(found_spike_chest_event, "boloto_event", "2б"))
# GlobalMapLevelButton("3", "2", (472, 508), level=Level("3", 22500, 500, 50, level_waves["3"], level_allowed_enemies["3"], level_image="2"))
# GlobalMapLevelButton("3а", "3", (945, 753), chest=Chest(parent_number="3а", rewards=chests_rewards["3а"]))
# GlobalMapLevelButton("4", "3", (671, 507), level=Level("4", 22500, 225, 50, level_waves["4"], level_allowed_enemies["4"], level_image="2"))
# GlobalMapLevelButton("5", "4", (824, 462), level=Level("5", 31500, 225, 50, level_waves["5"], level_allowed_enemies["5"], level_image="2"))
# GlobalMapLevelButton("6", "5", (1374, 304), event=Event(village_event, image_="village", parent_number="6", repeat=True))    # на 6 поменять

level = Level((0, 0), 6750, 1500, 20, level_waves["1"], level_allowed_enemies["1"], allowed_cords=(448, 448), level_image="2")

UpgradeTowerButton("1", (50, 104))
UpgradeTowerButton("2a", (216, 36))
UpgradeTowerButton("3a", (384, 36))
UpgradeTowerButton("2b", (216, 172))
UpgradeTowerButton("3b", (384, 172))

scroller = Scroller()
scroller.remembered_scroll_offsets["global_map"] = temp_scroll_offset

preview_group.entity_create(3)
select_towers_preview_group.entity_create(6)

# {160, 256, 352, 448, 544, 640, 736}
Slot((32, 160))
Slot((32, 256))
Slot((32, 352))
Slot((32, 448))
Slot((32, 544))
Slot((32, 640))
Slot((32, 736))

Cloud((1000, 100))
Cloud((600, 60))
Cloud((300, 70))
Cloud((720, 20))
Cloud((1400, 50))
Cloud((1200, 30))
Cloud((1800, 90))

shovel = Shovel((1500, 800))


running = True
while running:

    mouse_pos = mouse.get_pos()
    global_map.update()
    menu_positioning()
    text_anim_over = text_fields_group.update()

    for button in buttons_group:
        if button.on_hover():
            button.color_manage = True
            button.new_color = (230, 160, 35)
        else:
            button.color_manage = False

    if level:
        if level.state == 'run' and game_state == 'run':
            if free_money > 0:
                free_money -= 1
            else:
                free_money = default_free_money
                level.money += 1
                Alert('+1', (200, 30), 75, col=(0, 0, 0))

    alert_group.update()
    alert_group.draw(screen)
    if mouse.get_focused():
        screen.blit(cursor, mouse_pos)
        # screen.blit(font30.render(str(f"{mouse_pos[0]}, {mouse_pos[1]}"), True, (255, 0, 0)), (mouse_pos[0] - 60, mouse_pos[1] - 40))
        # for ii in range(10):
        #     draw.line(screen, (0, 0, 0), (ii * 160, 0), (ii * 160, 900), 5)
        #     draw.line(screen, (0, 0, 0), (0, ii * 90), (1600, ii * 90), 5)

    for enemy in enemies_group:
        if enemy.rect.x <= 150:
            if not level.cheat:
                game_state = "death"
            enemy.kill()

    clock.tick(75)
    display.update()
    for e in event.get():
        if e.type == MOUSEWHEEL and (game_state == "level_select"
                                     or game_state == "tower_select"
                                     or game_state == "manual_menu"):
            scroller.scroll_offset_y += e.y * 50
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE and (game_state == "run"
                                      or game_state == "paused"
                                      or game_state == "settings_menu"
                                      or game_state == "tower_select"
                                      or game_state == "global_map"
                                      or game_state == "manual_menu"
                                      or game_state == "global_map_paused"
                                      or game_state == "global_map_settings_menu"):
                if game_state == "run":
                    last_game_state = game_state
                    Alert("Пауза", (700, 200), 75)
                    game_state = "paused"
                elif game_state == "global_map":
                    scroller.remembered_scroll_offsets["global_map"] = scroller.current_scroll_offset()
                    last_game_state = game_state
                    game_state = "global_map_paused"
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
                elif game_state == "manual_menu":
                    last_game_state, game_state = game_state, last_game_state
                    scroller.set_scroll_offset(scroller.remembered_scroll_offsets["global_map"])
                elif game_state == "reward_second_stage":
                    last_game_state = game_state
                    game_state = "global_map"
                    rewards_preview_group.clear_rewards()
                    scroller.set_scroll_offset(scroller.remembered_scroll_offsets["global_map"])
                elif game_state == "global_map_paused":
                    last_game_state = game_state
                    game_state = "global_map"
                elif game_state == "global_map_settings_menu":
                    last_game_state = game_state
                    game_state = "global_map_paused"

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
                Enemy("tyazhik", (1508, 704))
            if e.key == K_KP_3:
                Enemy("klonik", (1508, 704))
            if e.key == K_KP_0:
                Enemy("fire_res", (1508, 192))
                Enemy("ice_res", (1508, 320))
                Enemy("water_res", (1508, 448))
                Enemy("poison_res", (1508, 576))
                Enemy("light_res", (1508, 704))

            if e.key == K_a:
                level.rect_visible = False
            if e.key == K_d:
                level.rect_visible = True

            if e.key == K_r:
                level.give_reward()
            if e.key == K_o:
                developer_mode = True
            if e.key == K_w:
                game_state = "level_complited"
            if e.key == K_q:
                running = False
            if e.key == K_s:
                for o in range(41):
                    for p in range(25):
                        global_map.level_completed((o, p), detect_smoke=False)
                global_map.where_is_smoke()
            
            if e.key == K_m:
                NeutralObject('block', (1024, 448))
            if e.key == K_n:
                NeutralObject('luja', (1024, 576))
            if e.key == K_l:
                NeutralObject('strelka_up', (1152, 704))
                NeutralObject('strelka_down', (1152, 192))
            if e.key == K_j:
                NeutralObject('block_mana', (1024, 448))
            if e.key == K_k:
                NeutralObject('block_bomb', (1024, 448))

        if e.type == QUIT:
            running = False

        if e.type == MOUSEMOTION and game_state == "global_map":
            if global_map.on_map and mouse.get_pressed() == (0, 1, 0):
                scroller.set_scroll_offset((scroller.scroll_offset_x + e.rel[0], scroller.scroll_offset_y + e.rel[1]))

        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            mouse_pos = mouse.get_pos()

            if shovel.rect.collidepoint(mouse_pos):
                shovel.is_move = True
            for slot in slots_group.entities:
                if slot.unit_inside:
                    if slot.unit_inside.rect.collidepoint(mouse_pos):                                          # если элемент отпущен
                        slot.is_move = True
        if e.type == MOUSEBUTTONUP and e.button == 1:                                                          # При отжатии кнопки мыши
            if game_state == "event":
                if text_anim_over:
                    event_stage += 1
                    text_fields_group.clear()
                else:
                    text_fields_group.finish_text_animation()
            mouse_pos = mouse.get_pos()
            unit_pos = (384 + ((mouse_pos[0] - 384) // 128) * 128), (192 + ((mouse_pos[1] - 192) // 128) * 128)

            if level.kill_enemy_on_click:
                for enemy in enemies_group:
                    if enemy.rect.collidepoint(mouse_pos):
                        enemy.alive = False
                        enemy.kill()

            if shovel.rect.collidepoint(mouse_pos):
                shovel.is_move = False
                for obj in [*towers_group, *nekusaemie_group]:                  # Сразу по 2 группам
                    if not obj.name == 'krest':
                        if obj.rect.collidepoint(shovel.rect.centerx, shovel.rect.centery):
                            if not level.cheat:
                                level.money += tower_costs[obj.name] // 2
                            if hasattr(obj, "bullet"):
                                obj.bullet.kill()
                            obj.alive = False
                            obj.kill()

            for slot in slots_group.entities:
                if slot.unit_inside:
                    if slot.unit_inside.rect.collidepoint(mouse_pos):                                          # если элемент отпущен
                        slot.is_move = False

                        if 1536 > unit_pos[0] >= 384 and 832 > unit_pos[1] >= 192:
                            tower_placement(slot)
save_data()  # 1
