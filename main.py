import pygame # För pygame
import os # För att ändra filsöksvägen
import random
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512) # Konfigurerar ljudfilerna
pygame.init()
mixer.init()

# Ändra arbetskatalogen till den mapp där din Python-fil ligger
os.chdir(os.path.dirname(os.path.abspath(__file__)))
  
# Definera fönsterstorlek och titel
info = pygame.display.Info() 
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Feathers of The Mountain")

# FPS-inställningar
clock = pygame.time.Clock()
FPS = 60

# Typsnitt
font = pygame.font.SysFont("Bauhaus 93", 60)
font_score = pygame.font.SysFont("Bauhaus 93", 35)
font_conversation = pygame.font.SysFont("Bauhaus 93", 28)
font_credits = pygame.font.SysFont("Bauhaus 93", 40)
font_credits_big = pygame.font.SysFont("Bauhaus 93", 80)

# Spel variabler
tile_size = max(min(screen_width // 25, screen_height // 14, 102), 32)
game_over = 0
main_menu = True
music_playing = False
current_music = None
level = 0
max_level = 30
score = 0
hp = 100
if level == 5:
  temp = 500
else:
  temp = 100
is_freezing = False
visa_bild = False
blockTurnAt = 0
snowfall = None
last_level = level
current_frostbite_image = None
kristall_lyser = False
music_1_is_playing = False
music_cave_is_playing = False
music_calm_is_playing = False
music_climb_is_playing = False
music_boss_is_playing = False
iced_fx_is_playing = False
move_egg = False
egg_has_rolled = False
draw_npc_sign = False
player_at_npc_kille = False
player_at_npc_tjej = False
player_at_npc_borgmästare = False
player_at_npc_barman = False
hole_radius = tile_size * 13
hole_speed = 10
size = 0
waiting_for_cutscene = False
player_can_enter = False
cutscene_shown_lvl_12 = False
cutscene_shown_lvl_28 = False
cutscene_shown_lvl_29 = False
by_kit_cutscene_shown = False
show_end_screen = False
mithril_cooldown = 0


# Färger
COLORS = {
  "white": (255, 255, 255),
  "black": (0, 0, 0),
  "green": (0, 255, 0),
  "brown": (150, 75, 0),
  "sky-blue" : (59, 138, 177),
  "cave_gray" : (38, 38, 38),
  "red" : (255, 0, 0)
}

# Bilder
IMAGES = {
  "img/bakgrund_1" : pygame.image.load("bilder/bakgrund_1.png"),
  "img/bakgrund_2" : pygame.image.load("bilder/bakgrund_2.png"),
  "img/bakgrund_3" : pygame.image.load("bilder/bakgrund_3.png"),
  "img/bakgrund_4" : pygame.image.load("bilder/bakgrund_4.png"),
  "img/bakgrund_5" : pygame.image.load("bilder/bakgrund_5.png"),
  "img/bakgrund_6" : pygame.image.load("bilder/bakgrund_6.png"),
  "img/bakgrund_6_upplyst" : pygame.image.load("bilder/bakgrund_6_upplyst.png"),
  "img/bakgrund_7" : pygame.image.load("bilder/bakgrund_7.png"),
  "img/bakgrund_8" : pygame.image.load("bilder/bakgrund_8.png"),
  "img/bakgrund_9" : pygame.image.load("bilder/bakgrund_9.png"),
  "img/bakgrund_10" : pygame.image.load("bilder/bakgrund_10.png"),
  "img/bakgrund_11" : pygame.image.load("bilder/bakgrund_11.png"),
  "img/bakgrund_12" : pygame.image.load("bilder/bakgrund_12.png"),
  "img/jord" : pygame.image.load("bilder/jord.png"),
  "img/jord_snö" : pygame.image.load("bilder/jord_snö.png"),
  "img/grotta" : pygame.image.load("bilder/grotta.png"),
  "img/grotta_grå" : pygame.image.load("bilder/grotta_grå.png"),
  "img/barriär" : pygame.image.load("bilder/barriär.png"),
  "img/äventyrare_1" : pygame.image.load("bilder/äventyrare_1.png"),
  "img/äventyrare_2" : pygame.image.load("bilder/äventyrare_2.png"),
  "img/äventyrare_3" : pygame.image.load("bilder/äventyrare_1.png"),
  "img/äventyrare_4" : pygame.image.load("bilder/äventyrare_3.png"),
  "img/äventyrare_5" : pygame.image.load("bilder/äventyrare_4.png"),
  "img/äventyrare_front_1" : pygame.image.load("bilder/äventyrare_front_1.png"),
  "img/äventyrare_front_2" : pygame.image.load("bilder/äventyrare_front_2.png"),
  "img/äventyrare_front_3" : pygame.image.load("bilder/äventyrare_front_3.png"),
  "img/äventyrare_front_4" : pygame.image.load("bilder/äventyrare_front_1.png"),
  "img/äventyrare_back_1" : pygame.image.load("bilder/äventyrare_back_1.png"),
  "img/äventyrare_back_2" : pygame.image.load("bilder/äventyrare_back_2.png"),
  "img/äventyrare_back_3" : pygame.image.load("bilder/äventyrare_back_3.png"),
  "img/äventyrare_back_4" : pygame.image.load("bilder/äventyrare_back_1.png"),
  "img/äventyrare_climb_1" : pygame.image.load("bilder/äventyrare_climb_2.png"),
  "img/äventyrare_climb_2" : pygame.image.load("bilder/äventyrare_climb_3.png"),
  "img/äventyrare_climb_3" : pygame.image.load("bilder/äventyrare_climb_1.png"),
  "img/npc_kille_1" : pygame.image.load("bilder/npc_kille_1.png"),
  "img/npc_tjej_1" : pygame.image.load("bilder/npc_tjej_1.png"),
  "img/npc_borgmästare" : pygame.image.load("bilder/npc_borgmästare.png"),
  "img/vildsvin_1" : pygame.image.load("bilder/vildsvin_1.png"),
  "img/vildsvin_2" : pygame.image.load("bilder/vildsvin_2.png"),
  "img/vildsvin_3" : pygame.image.load("bilder/vildsvin_3.png"),
  "img/vatten" : pygame.image.load("bilder/vatten.png"),
  "img/restart_knapp" : pygame.image.load("bilder/restart_knapp.png"),
  "img/start_knapp" : pygame.image.load("bilder/start_knapp.png"),
  "img/exit_knapp" : pygame.image.load("bilder/exit_knapp.png"),
  "img/levels_knapp" : pygame.image.load("bilder/levels_knapp.png"),
  "img/level_1_knapp" : pygame.image.load("bilder/level_1_knapp.png"),
  "img/level_2_knapp" : pygame.image.load("bilder/level_2_knapp.png"),
  "img/level_3_knapp" : pygame.image.load("bilder/level_3_knapp.png"),
  "img/level_4_knapp" : pygame.image.load("bilder/level_4_knapp.png"),
  "img/level_5_knapp" : pygame.image.load("bilder/level_5_knapp.png"),
  "img/level_6_knapp" : pygame.image.load("bilder/level_6_knapp.png"),
  "img/level_7_knapp" : pygame.image.load("bilder/level_7_knapp.png"),
  "img/level_8_knapp" : pygame.image.load("bilder/level_8_knapp.png"),
  "img/level_9_knapp" : pygame.image.load("bilder/level_9_knapp.png"),
  "img/osynlig_dörr" : pygame.image.load("bilder/osynlig_dörr.png"),
  "img/mithril" : pygame.image.load("bilder/mithril.png"),
  "img/älg_1" : pygame.image.load("bilder/älg_1.png"),
  "img/älg_2" : pygame.image.load("bilder/älg_2.png"),
  "img/älg_3" : pygame.image.load("bilder/älg_3.png"),
  "img/brasa_1" : pygame.image.load("bilder/brasa1.png"),
  "img/brasa_2" : pygame.image.load("bilder/brasa2.png"),
  "img/brasa_3" : pygame.image.load("bilder/brasa3.png"),
  "img/brasa_4" : pygame.image.load("bilder/brasa4.png"),
  "img/brasa_5" : pygame.image.load("bilder/brasa5.png"),
  "img/skylt" : pygame.image.load("bilder/skylt.png"),
  "img/fladdermus_1" : pygame.image.load("bilder/fladdermus_1.png"),
  "img/fladdermus_2" : pygame.image.load("bilder/fladdermus_2.png"),
  "img/fladdermus_3" : pygame.image.load("bilder/fladdermus_3.png"),
  "img/frostbite_1" : pygame.image.load("bilder/frostbite_1.png"),
  "img/frostbite_2" : pygame.image.load("bilder/frostbite_2.png"),
  "img/frostbite_3" : pygame.image.load("bilder/frostbite_3.png"),
  "img/örn_1" : pygame.image.load("bilder/örn_1.png"),
  "img/örn_2" : pygame.image.load("bilder/örn_2.png"),
  "img/örn_3" : pygame.image.load("bilder/örn_3.png"),
  "img/örn_4" : pygame.image.load("bilder/örn_4.png"),
  "img/stalaktit" : pygame.image.load("bilder/stalaktit.png"),
  "img/höbal" : pygame.image.load("bilder/hö_hög.png"),
  "img/kristall_grön_av" : pygame.image.load("bilder/kristall_grön_av.png"),
  "img/kristall_grön_på" : pygame.image.load("bilder/kristall_grön_på.png"),
  "img/kristall_blå_av" : pygame.image.load("bilder/kristall_blå_av.png"),
  "img/kristall_blå_på" : pygame.image.load("bilder/kristall_blå_på.png"),
  "img/kristall_lila_av" : pygame.image.load("bilder/kristall_lila_av.png"),
  "img/kristall_lila_på" : pygame.image.load("bilder/kristall_lila_på.png"),
  "img/kristall_effekt_1" : pygame.image.load("bilder/kristall_effekt_1.png"),
  "img/kristall_effekt_2" : pygame.image.load("bilder/kristall_effekt_2.png"),
  "img/kristall_effekt_3" : pygame.image.load("bilder/kristall_effekt_3.png"),
  "img/kristall_effekt_4" : pygame.image.load("bilder/kristall_effekt_4.png"),
  "img/kristall_effekt_5" : pygame.image.load("bilder/kristall_effekt_5.png"),
  "img/kristall_effekt_6" : pygame.image.load("bilder/kristall_effekt_6.png"),
  "img/kristall_effekt_7" : pygame.image.load("bilder/kristall_effekt_7.png"),
  "img/kristall_effekt_8" : pygame.image.load("bilder/kristall_effekt_8.png"),
  "img/kristall_effekt_9" : pygame.image.load("bilder/kristall_effekt_9.png"),
  "img/kristall_effekt_10" : pygame.image.load("bilder/kristall_effekt_10.png"),
  "img/kristall_effekt_11" : pygame.image.load("bilder/kristall_effekt_11.png"),
  "img/kristall_effekt_12" : pygame.image.load("bilder/kristall_effekt_12.png"),
  "img/egg_roll1" : pygame.image.load("bilder/egg_roll1.png"),
  "img/egg_roll2" : pygame.image.load("bilder/egg_roll2.png"),
  "img/egg_roll3" : pygame.image.load("bilder/egg_roll3.png"),
  "img/egg_roll4" : pygame.image.load("bilder/egg_roll4.png"),
  "img/npc_skylt" : pygame.image.load("bilder/npc_skylt.png"),
  "img/horn" : pygame.image.load("bilder/horn.png"),
  "img/sten" : pygame.image.load("bilder/sten.png"),
  "danger_1" : pygame.image.load("bilder/danger_1.png"),
  "danger_2" : pygame.image.load("bilder/danger_2.png"),
  "img/örn_boss_1" : pygame.image.load("bilder/örn_boss_1.png"),
  "img/örn_boss_2" : pygame.image.load("bilder/örn_boss_2.png"),
  "img/örn_boss_3" : pygame.image.load("bilder/örn_boss_3.png"),
  "img/örn_boss_jump_1" : pygame.image.load("bilder/örn_boss_jump_1.png"),
  "img/örn_boss_jump_2" : pygame.image.load("bilder/örn_boss_jump_2.png"),
  "img/örn_boss_jump_3" : pygame.image.load("bilder/örn_boss_jump_3.png"),
  "img/örn_boss_jump_4" : pygame.image.load("bilder/örn_boss_jump_4.png"),
  "img/örn_boss_jump_5" : pygame.image.load("bilder/örn_boss_jump_5.png"),
  "img/örn_boss_jump_6" : pygame.image.load("bilder/örn_boss_jump_6.png"),
  "img/örn_boss_jump_7" : pygame.image.load("bilder/örn_boss_jump_7.png"),
  "img/örn_boss_jump_8" : pygame.image.load("bilder/örn_boss_jump_8.png"),
  "img/örn_boss_slash_1" : pygame.image.load("bilder/örn_boss_slash_1.png"),
  "img/örn_boss_slash_2" : pygame.image.load("bilder/örn_boss_slash_2.png"),
  "img/örn_boss_slash_3" : pygame.image.load("bilder/örn_boss_slash_3.png"),
  "img/örn_boss_slash_4" : pygame.image.load("bilder/örn_boss_slash_4.png"),
  "img/örn_boss_slash_5" : pygame.image.load("bilder/örn_boss_slash_5.png"),
  "img/örn_boss_slash_6" : pygame.image.load("bilder/örn_boss_slash_6.png"),
  "img/örn_boss_slash_7" : pygame.image.load("bilder/örn_boss_slash_7.png"),
  "img/örn_boss_slash_8" : pygame.image.load("bilder/örn_boss_slash_8.png"),
  "img/örn_boss_slash_9" : pygame.image.load("bilder/örn_boss_slash_9.png"),
  "img/örn_boss_slash_10" : pygame.image.load("bilder/örn_boss_slash_10.png"),
  "img/by_Kit" : pygame.image.load("bilder/by_Kit.png"),
  "img/cutscene_1" : pygame.image.load("bilder/cutscene_1.png"),
  "img/cutscene_2" : pygame.image.load("bilder/cutscene_2.png"),
  "img/cutscene_3" : pygame.image.load("bilder/cutscene_3.png"),
  "img/cutscene_4" : pygame.image.load("bilder/cutscene_4.png"),
  "img/cutscene_5" : pygame.image.load("bilder/cutscene_5.png"),
  "img/cutscene_6" : pygame.image.load("bilder/cutscene_6.png"),
  "img/cutscene_7" : pygame.image.load("bilder/cutscene_7.png"),
  "img/cutscene_8" : pygame.image.load("bilder/cutscene_8.png"),
  "img/cutscene_9" : pygame.image.load("bilder/cutscene_9.png"),
  "img/cutscene_10" : pygame.image.load("bilder/cutscene_10.png"),
  "img/cutscene_11" : pygame.image.load("bilder/cutscene_11.png"),
  "img/cutscene_12" : pygame.image.load("bilder/cutscene_12.png"),
  "img/cutscene_13" : pygame.image.load("bilder/cutscene_13.png"),
  "img/cutscene_14" : pygame.image.load("bilder/cutscene_14.png"),
  "img/cutscene_15" : pygame.image.load("bilder/cutscene_15.png"),
  "img/cutscene_16" : pygame.image.load("bilder/cutscene_16.png"),
  "img/cutscene_17" : pygame.image.load("bilder/cutscene_17.png"),
  "img/cutscene_18" : pygame.image.load("bilder/cutscene_18.png"),
  "img/cutscene_19" : pygame.image.load("bilder/cutscene_19.png"),
  "img/cutscene_20" : pygame.image.load("bilder/cutscene_20.png"),
  "img/cutscene_21" : pygame.image.load("bilder/cutscene_21.png"),
  "img/cutscene_22" : pygame.image.load("bilder/cutscene_22.png"),
  "img/cutscene_23" : pygame.image.load("bilder/cutscene_23.png"),
  "img/cutscene_24" : pygame.image.load("bilder/cutscene_24.png"),
  "img/cutscene_25" : pygame.image.load("bilder/cutscene_25.png"),
  "img/cutscene_26" : pygame.image.load("bilder/cutscene_26.png"),
  "img/cutscene_27" : pygame.image.load("bilder/cutscene_27.png"),
  "img/cutscene_28" : pygame.image.load("bilder/cutscene_28.png"),
  "img/cutscene_29" : pygame.image.load("bilder/cutscene_29.png"),
  "img/cutscene_30" : pygame.image.load("bilder/cutscene_30.png"),
  "img/cutscene_31" : pygame.image.load("bilder/cutscene_31.png")
}

# Skala bilderna till rätt storlek
IMAGES["img/bakgrund_1"] = pygame.transform.scale(IMAGES["img/bakgrund_1"], (tile_size * 25 + (tile_size / 10), tile_size * 14 + (tile_size / 10)))
IMAGES["img/bakgrund_2"] = pygame.transform.scale(IMAGES["img/bakgrund_2"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_3"] = pygame.transform.scale(IMAGES["img/bakgrund_3"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_4"] = pygame.transform.scale(IMAGES["img/bakgrund_4"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_5"] = pygame.transform.scale(IMAGES["img/bakgrund_5"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_6"] = pygame.transform.scale(IMAGES["img/bakgrund_6"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_6_upplyst"] = pygame.transform.scale(IMAGES["img/bakgrund_6_upplyst"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_7"] = pygame.transform.scale(IMAGES["img/bakgrund_7"], (tile_size * 26, tile_size * 21))
IMAGES["img/bakgrund_8"] = pygame.transform.scale(IMAGES["img/bakgrund_8"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_9"] = pygame.transform.scale(IMAGES["img/bakgrund_9"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_10"] = pygame.transform.scale(IMAGES["img/bakgrund_10"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_11"] = pygame.transform.scale(IMAGES["img/bakgrund_11"], (tile_size * 23, tile_size * 12))
IMAGES["img/bakgrund_12"] = pygame.transform.scale(IMAGES["img/bakgrund_12"], (tile_size * 23, tile_size * 12))
IMAGES["img/frostbite_1"] = pygame.transform.scale(IMAGES["img/frostbite_1"], (tile_size * 23, tile_size * 12))
IMAGES["img/frostbite_2"] = pygame.transform.scale(IMAGES["img/frostbite_2"], (tile_size * 23, tile_size * 12))
IMAGES["img/frostbite_3"] = pygame.transform.scale(IMAGES["img/frostbite_3"], (tile_size * 23, tile_size * 12))
IMAGES["img/jord"] = pygame.transform.scale(IMAGES["img/jord"], (tile_size, tile_size))
IMAGES["img/jord_snö"] = pygame.transform.scale(IMAGES["img/jord_snö"], (tile_size, tile_size))
IMAGES["img/grotta"] = pygame.transform.scale(IMAGES["img/grotta"], (tile_size, tile_size))
IMAGES["img/grotta_grå"] = pygame.transform.scale(IMAGES["img/grotta_grå"], (tile_size, tile_size))
IMAGES["img/barriär"] = pygame.transform.scale(IMAGES["img/barriär"], (tile_size, tile_size))
IMAGES["img/vildsvin_1"] = pygame.transform.scale(IMAGES["img/vildsvin_1"], (tile_size * 2, tile_size * 1))
IMAGES["img/vildsvin_2"] = pygame.transform.scale(IMAGES["img/vildsvin_2"], (tile_size * 2, tile_size * 1))
IMAGES["img/vildsvin_3"] = pygame.transform.scale(IMAGES["img/vildsvin_3"], (tile_size * 2, tile_size * 1))
IMAGES["img/vatten"] = pygame.transform.scale(IMAGES["img/vatten"], (tile_size, tile_size))
IMAGES["img/äventyrare_5"] = pygame.transform.scale(IMAGES["img/äventyrare_5"], (tile_size, tile_size * 2 - (tile_size // 5)))
IMAGES["img/npc_kille_1"] = pygame.transform.scale(IMAGES["img/npc_kille_1"], (tile_size, tile_size * 2))
IMAGES["img/npc_tjej_1"] = pygame.transform.scale(IMAGES["img/npc_tjej_1"], (tile_size, tile_size * 2))
IMAGES["img/npc_borgmästare"] = pygame.transform.scale(IMAGES["img/npc_borgmästare"], (tile_size, tile_size * 2))
IMAGES["img/restart_knapp"] = pygame.transform.scale(IMAGES["img/restart_knapp"], (tile_size * 4, tile_size * 2))
IMAGES["img/start_knapp"] = pygame.transform.scale(IMAGES["img/start_knapp"], (tile_size * 4, tile_size * 2))
IMAGES["img/exit_knapp"] = pygame.transform.scale(IMAGES["img/exit_knapp"], (tile_size * 4, tile_size * 2))
IMAGES["img/levels_knapp"] = pygame.transform.scale(IMAGES["img/levels_knapp"], (tile_size * 4, tile_size * 2))
IMAGES["img/level_1_knapp"] = pygame.transform.scale(IMAGES["img/level_1_knapp"], (tile_size * 2, tile_size))
IMAGES["img/level_2_knapp"] = pygame.transform.scale(IMAGES["img/level_2_knapp"], (tile_size * 2, tile_size))
IMAGES["img/level_3_knapp"] = pygame.transform.scale(IMAGES["img/level_3_knapp"], (tile_size * 2, tile_size))
IMAGES["img/level_4_knapp"] = pygame.transform.scale(IMAGES["img/level_4_knapp"], (tile_size * 2, tile_size))
IMAGES["img/level_5_knapp"] = pygame.transform.scale(IMAGES["img/level_5_knapp"], (tile_size * 2, tile_size))
IMAGES["img/level_6_knapp"] = pygame.transform.scale(IMAGES["img/level_6_knapp"], (tile_size * 2, tile_size))
IMAGES["img/level_7_knapp"] = pygame.transform.scale(IMAGES["img/level_7_knapp"], (tile_size * 2, tile_size))
IMAGES["img/level_8_knapp"] = pygame.transform.scale(IMAGES["img/level_8_knapp"], (tile_size * 2, tile_size))
IMAGES["img/level_9_knapp"] = pygame.transform.scale(IMAGES["img/level_9_knapp"], (tile_size * 2, tile_size))
IMAGES["img/osynlig_dörr"] = pygame.transform.scale(IMAGES["img/osynlig_dörr"], (tile_size, tile_size * 1.5))
IMAGES["img/mithril"] = pygame.transform.scale(IMAGES["img/mithril"], (tile_size // 2 + 10, tile_size // 2 + 10))
IMAGES["img/älg_1"] = pygame.transform.scale(IMAGES["img/älg_1"], (tile_size * 2.5, tile_size * 2.5))
IMAGES["img/älg_2"] = pygame.transform.scale(IMAGES["img/älg_2"], (tile_size * 2.5, tile_size * 2.5))
IMAGES["img/älg_3"] = pygame.transform.scale(IMAGES["img/älg_3"], (tile_size * 2.5, tile_size * 2.5))
IMAGES["img/brasa_1"] = pygame.transform.scale(IMAGES["img/brasa_1"], (tile_size, tile_size))
IMAGES["img/brasa_2"] = pygame.transform.scale(IMAGES["img/brasa_2"], (tile_size, tile_size))
IMAGES["img/brasa_3"] = pygame.transform.scale(IMAGES["img/brasa_3"], (tile_size, tile_size))
IMAGES["img/brasa_4"] = pygame.transform.scale(IMAGES["img/brasa_4"], (tile_size, tile_size))
IMAGES["img/brasa_5"] = pygame.transform.scale(IMAGES["img/brasa_5"], (tile_size, tile_size))
IMAGES["img/skylt"] = pygame.transform.scale(IMAGES["img/skylt"], (tile_size, tile_size))
IMAGES["img/fladdermus_1"] = pygame.transform.scale(IMAGES["img/fladdermus_1"], (tile_size * 1.5, tile_size))
IMAGES["img/fladdermus_2"] = pygame.transform.scale(IMAGES["img/fladdermus_2"], (tile_size * 1.5, tile_size))
IMAGES["img/fladdermus_3"] = pygame.transform.scale(IMAGES["img/fladdermus_3"], (tile_size * 1.5, tile_size))
IMAGES["img/örn_1"] = pygame.transform.scale(IMAGES["img/örn_1"], (tile_size * 1.2, tile_size * 1.2))
IMAGES["img/örn_2"] = pygame.transform.scale(IMAGES["img/örn_2"], (tile_size * 1.2, tile_size * 1.2))
IMAGES["img/örn_3"] = pygame.transform.scale(IMAGES["img/örn_3"], (tile_size * 1.2, tile_size * 1.2))
IMAGES["img/örn_4"] = pygame.transform.scale(IMAGES["img/örn_4"], (tile_size * 1.2, tile_size * 1.2))
IMAGES["img/stalaktit"] = pygame.transform.scale(IMAGES["img/stalaktit"], (tile_size, tile_size * 1.25))
IMAGES["img/höbal"] = pygame.transform.scale(IMAGES["img/höbal"], (tile_size * 4, tile_size * 1.5))
IMAGES["img/kristall_grön_av"] = pygame.transform.scale(IMAGES["img/kristall_grön_av"], (tile_size, tile_size))
IMAGES["img/kristall_grön_på"] = pygame.transform.scale(IMAGES["img/kristall_grön_på"], (tile_size, tile_size))
IMAGES["img/kristall_blå_av"] = pygame.transform.scale(IMAGES["img/kristall_blå_av"], (tile_size, tile_size))
IMAGES["img/kristall_blå_på"] = pygame.transform.scale(IMAGES["img/kristall_blå_på"], (tile_size, tile_size))
IMAGES["img/kristall_lila_av"] = pygame.transform.scale(IMAGES["img/kristall_lila_av"], (tile_size, tile_size))
IMAGES["img/kristall_lila_på"] = pygame.transform.scale(IMAGES["img/kristall_lila_på"], (tile_size, tile_size))
IMAGES["img/egg_roll1"] = pygame.transform.scale(IMAGES["img/egg_roll1"], (tile_size, tile_size))
IMAGES["img/egg_roll2"] = pygame.transform.scale(IMAGES["img/egg_roll2"], (tile_size, tile_size))
IMAGES["img/egg_roll3"] = pygame.transform.scale(IMAGES["img/egg_roll3"], (tile_size, tile_size))
IMAGES["img/egg_roll4"] = pygame.transform.scale(IMAGES["img/egg_roll4"], (tile_size, tile_size))
IMAGES["img/npc_skylt_1"] = pygame.transform.scale(IMAGES["img/npc_skylt"], (tile_size * 6.5, tile_size * 2))
IMAGES["img/npc_skylt_2"] = pygame.transform.scale(IMAGES["img/npc_skylt"], (tile_size * 10.5, tile_size * 3))
IMAGES["img/horn"] = pygame.transform.scale(IMAGES["img/horn"], (tile_size, tile_size))
IMAGES["img/sten"] = pygame.transform.scale(IMAGES["img/sten"], (tile_size * 1.5, tile_size * 1.5))
IMAGES["danger_1"] = pygame.transform.scale(IMAGES["danger_1"], (tile_size * 1.5, tile_size * 1.5))
IMAGES["danger_2"] = pygame.transform.scale(IMAGES["danger_2"], (tile_size * 1.5, tile_size * 1.5))
IMAGES["img/örn_boss_1"] = pygame.transform.scale(IMAGES["img/örn_boss_1"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_2"] = pygame.transform.scale(IMAGES["img/örn_boss_2"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_3"] = pygame.transform.scale(IMAGES["img/örn_boss_3"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_jump_1"] = pygame.transform.scale(IMAGES["img/örn_boss_jump_1"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_jump_2"] = pygame.transform.scale(IMAGES["img/örn_boss_jump_2"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_jump_3"] = pygame.transform.scale(IMAGES["img/örn_boss_jump_3"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_jump_4"] = pygame.transform.scale(IMAGES["img/örn_boss_jump_4"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_jump_5"] = pygame.transform.scale(IMAGES["img/örn_boss_jump_5"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_jump_6"] = pygame.transform.scale(IMAGES["img/örn_boss_jump_6"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_jump_7"] = pygame.transform.scale(IMAGES["img/örn_boss_jump_7"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_jump_8"] = pygame.transform.scale(IMAGES["img/örn_boss_jump_8"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_1"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_1"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_2"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_2"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_3"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_3"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_4"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_4"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_5"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_5"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_6"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_6"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_7"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_7"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_8"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_8"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_9"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_9"], (tile_size * 4, tile_size * 4))
IMAGES["img/örn_boss_slash_10"] = pygame.transform.scale(IMAGES["img/örn_boss_slash_10"], (tile_size * 4, tile_size * 4))
IMAGES["img/by_Kit"] = pygame.transform.scale(IMAGES["img/by_Kit"], (tile_size * 25, tile_size * 14))
for i in range (1, 32):
  IMAGES[f"img/cutscene_{i}"] = pygame.transform.scale(IMAGES[f"img/cutscene_{i}"], (tile_size * 25 + (tile_size / 10), tile_size * 14 + (tile_size / 10)))




# Ladda in ljud
# Bakgrunds musik
music_menu_fx = pygame.mixer.Sound("ljudfiler/music_main_menu.mp3")
music_menu_fx.set_volume(0.5)
music_1_fx = pygame.mixer.Sound("ljudfiler/music_1.mp3")
music_1_fx.set_volume(0.5)
music_2_fx = pygame.mixer.Sound("ljudfiler/music_2.mp3")
music_2_fx.set_volume(0.5)
music_cave_fx = pygame.mixer.Sound("ljudfiler/music_cave.mp3")
music_cave_fx.set_volume(0.5)
music_calm_fx = pygame.mixer.Sound("ljudfiler/music_calm.mp3")
music_calm_fx.set_volume(0.5)
music_saloon_fx = pygame.mixer.Sound("ljudfiler/music_saloon.mp3")
music_saloon_fx.set_volume(0.5)
music_climb_fx = pygame.mixer.Sound("ljudfiler/music_the_climb.mp3")
music_climb_fx.set_volume(0.5)
music_boss_fx = pygame.mixer.Sound("ljudfiler/music_boss.mp3")
music_boss_fx.set_volume(0.5)
music_ending_fx = pygame.mixer.Sound("ljudfiler/music_ending.mp3")
music_ending_fx.set_volume(0.5)
# Ljud effekter
mithril_fx = pygame.mixer.Sound("ljudfiler/money.mp3")
mithril_fx.set_volume(0.5)
hoppar_fx = pygame.mixer.Sound("ljudfiler/jumping.mp3")
hoppar_fx.set_volume(2.0)
vildsvin_fx = pygame.mixer.Sound("ljudfiler/pig_squeal.mp3")
vildsvin_fx.set_volume(0.5)
moose_fx = pygame.mixer.Sound("ljudfiler/moose.mp3")
moose_fx.set_volume(0.5)
iced_fx = pygame.mixer.Sound("ljudfiler/iced.mp3")
iced_fx.set_volume(0.5)
campfire_fx = pygame.mixer.Sound("ljudfiler/campfire.mp3")
iced_fx.set_volume(0.5)
music_cave_fx = pygame.mixer.Sound("ljudfiler/music_cave.mp3")
music_cave_fx.set_volume(0.5)
fladdermus_fx = pygame.mixer.Sound("ljudfiler/fladdermus.mp3")
fladdermus_fx.set_volume(0.5)
crystal_fx = pygame.mixer.Sound("ljudfiler/crystal.mp3")
crystal_fx.set_volume(0.5)
water_dripping_fx = pygame.mixer.Sound("ljudfiler/water_dripping.mp3")
water_dripping_fx.set_volume(0.5)
water_splash_fx = pygame.mixer.Sound("ljudfiler/water_splash.mp3")
water_splash_fx.set_volume(0.5)
damage_w_fx = pygame.mixer.Sound("ljudfiler/damage_w.mp3")
damage_w_fx.set_volume(0.5)
damage_h_fx = pygame.mixer.Sound("ljudfiler/damage_h.mp3")
damage_h_fx.set_volume(0.5)
eagle_fx = pygame.mixer.Sound("ljudfiler/eagle.mp3")
eagle_fx.set_volume(1)
horn_fx = pygame.mixer.Sound("ljudfiler/horn.mp3")
horn_fx.set_volume(0.5)
door_slam_fx = pygame.mixer.Sound("ljudfiler/door_slam.mp3")
door_slam_fx.set_volume(0.5)
silly_trumpet_fx = pygame.mixer.Sound("ljudfiler/silly_trumpet.mp3")
silly_trumpet_fx.set_volume(1)
woosh_fx = pygame.mixer.Sound("ljudfiler/woosh.mp3")
woosh_fx.set_volume(1)

levels = []

# Nivåer
for i in range(1, max_level):
  with open(f"Nivåer/level{i}.txt") as file:
    level_file = file.readlines()
    level_list = []
    for j in level_file:
      level_list.append(j.split())
    levels.append(level_list)

# Funktion för text
text_col = COLORS["white"]
def draw_text(text, font, text_col, x, y, line_spacing = 10):
  text = text.split("\n")
  for i, text in enumerate(text):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y + i * (font.get_height() + line_spacing)))

# Funktion för att starta om nivå
def reset_level(level):
  # Återställer snöfallet
  global snowfall
  snowfall = None
  # Spelarens startposition
  # Starten
  if level in range (0, 4):
    player.reset((tile_size * 2) - 2, tile_size * 11)
  elif level == 4:
    player.reset((tile_size * 1) + 3, tile_size * 11)
  elif level == 5:
    player.reset((tile_size * 2) - 2, tile_size * 3)
  # Grottan
  elif level == 6:
    player.reset((tile_size * 1) + 3, tile_size * 11)
  elif level == 7:
    player.reset((tile_size * 1) + 3, tile_size * 2)
  # Byn
  elif level in range (8, 12):
    player.reset((tile_size * 1) + 3, tile_size * 11)
  elif level == 12:
    player.reset(tile_size * 12, tile_size * 12)
  elif level == 13:
    player.reset(tile_size * 17, tile_size * 11)
  # Den nya skogen
  elif level in range (14, 17):
    player.reset((tile_size * 1) + 3, tile_size * 11)
  elif level == 17:
    player.reset(tile_size * 23, tile_size * 11)
    player.direction = "left"
  elif level in range (18, 20):
    player.reset((tile_size * 2) - 2, tile_size * 11)
  elif level == 20:
    player.reset(tile_size * 22, tile_size)
  # Kristallgrottan
  elif level == 21:
    player.reset(tile_size * 4, tile_size)
  elif level == 22:
    player.reset(tile_size * 2 + 1, tile_size * 7)
  # Branten och slutstriden
  elif level in range (23, 27):
    player.reset((tile_size * 2) - 2, tile_size * 11)
  elif level == 27 or level == 28:
    player.reset((tile_size * 3) - 2, tile_size * 7)
  elif level in range (29, 32):
    player.reset((tile_size * 2) - 2, tile_size * 11)
  
  # Ändrar ljudeffektens storlek
  global size
  if level == 22:
    size = tile_size + (tile_size // 2)
  elif level == 27:
    size = tile_size * 3
  else:
    size = tile_size

  # Återställer alla cutscenes
  global cutscene_shown_lvl_12
  global cutscene_shown_lvl_28
  global cutscene_shown_lvl_29
  cutscene_shown_lvl_12 = False
  cutscene_shown_lvl_28 = False
  cutscene_shown_lvl_29 = False


  vildsvin_group.empty()
  vatten_group.empty()
  plattform_group.empty()
  mithril_group.empty()
  dörr_group.empty()
  älg_group.empty()
  grotta_group.empty()
  volym_group.empty()
  volymG_group.empty()
  brasa_group.empty()
  skylt_group.empty()
  fladdermus_group.empty()
  npc_kille_group.empty()
  npc_tjej_group.empty()
  npc_borgmästare_group.empty()
  npc_barman_group.empty()
  örn_group.empty()
  stalaktit_group.empty()
  höbal_group.empty()
  kristall_group.empty()
  egg_group.empty()
  barriär_group.empty()
  horn_group.empty()
  sten_group.empty()
  örn_boss_group.empty()

  global egg_has_rolled

  # Återställer ägget
  egg_has_rolled = False

  # Definiera fyra horn positionerna på skärmen
  if level == 27:
    horn_positions = [
      (tile_size * 11, tile_size * 3),  # Position 1 mitten toppen
      (tile_size * 4, tile_size * 6),  # Position 2 vänster mitten
      (tile_size * 19, tile_size * 6),  # Position 3 höger mitten
      (tile_size * 4, tile_size * 12),  # Position 4 vänster botten
      (tile_size * 11, tile_size * 12),   # Position 5 mitten botten
      (tile_size * 19, tile_size * 12)   # Position 6 höger botten
    ]
    # Skapa hornet
    horn = Horn(horn_positions)
    horn_group.add(horn)

  # Ladda in nivå data och skapa världen
  world = World(levels[level])
  
  return world

def play_music(music_fx):
  global current_music
  # Spela ny musik om det är en ny låt
  if current_music != music_fx:
    # Stoppa all musik
    music_menu_fx.stop()
    music_1_fx.stop()
    music_2_fx.stop()
    music_cave_fx.stop()
    music_calm_fx.stop()
    music_saloon_fx.stop()
    music_climb_fx.stop()
    music_boss_fx.stop()
    music_ending_fx.stop()
    if music_fx is not None:
      music_fx.play(-1)
      current_music = music_fx
    else:
      current_music = None

class CutsceneManager:
  def __init__(self):
    self.active = False
    self.images = []
    self.music = None
    self.sounds = []
    self.timers = []
    self.current_index = 0
    self.start_time = 0
    self.finished = False

  def start(self, images, timers, music=None, sounds=None):
    self.active = True
    self.images = [img if isinstance(img, pygame.Surface) else pygame.image.load(img) for img in images]
    self.timers = timers
    self.music = music
    self.sounds = sounds if sounds else []
    self.current_index = 0
    self.start_time = pygame.time.get_ticks()
    self.finished = False
    if self.music:
      self.music.play(-1)
    for _, snd in self.sounds:
      snd.stop()  # Stoppa ev. pågående ljud

  def update(self):
    if not self.active:
      return
    now = pygame.time.get_ticks()
    elapsed = (now - self.start_time) / 1000  # sekunder
    # Spela ljud vid rätt tid
    for t, snd in self.sounds:
      if abs(elapsed - t) < 0.05:  # Spela ljudet nära rätt tid
        snd.play()
    # Byt bild om tiden är ute
    if elapsed > sum(self.timers[:self.current_index + 1]):
      self.current_index += 1
      if self.current_index >= len(self.images):
        self.end()

  def draw(self, screen):
    if self.active and self.current_index < len(self.images):
      screen.blit(self.images[self.current_index], (0, 0))

  def end(self):
    self.active = False
    self.finished = True
    if self.music and not (level == 29 and not credits_manager.active):
      self.music.stop()
    for _, snd in self.sounds:
      snd.stop()


cutscene_manager = CutsceneManager()


class CreditsManager:
  def __init__(self, lines, font, font_big, screen, speed = 1):
    self.active = False
    self.lines = lines
    self.font = font
    self.font_big = font_big
    self.screen = screen
    self.speed = speed
    self.y = screen.get_height()
    self.finished = False
    self.credits_height = len(lines) * (font.get_height() + 20)
    self.start_time = 0
    self.stopped = False

  def start(self):
    self.active = True
    self.y = self.screen.get_height()
    self.finished = False
    self.start_time = pygame.time.get_ticks()

  def update(self):
    if not self.active or self.stopped:
      return
    self.y -= self.speed
    # Kolla om sista raden ("Thank you for playing!") är i mitten
    thank_index = len(self.lines) - 1
    thank_text, thank_font, _ = self.lines[thank_index]
    thank_surface = thank_font.render(thank_text, True, (0,0,0))
    thank_y = self.y + thank_index * (self.font.get_height() + 20)
    center_y = (self.screen.get_height() // 2) - (thank_surface.get_height() // 2)
    if thank_y <= center_y:
        self.stopped = True
        self.y = center_y - thank_index * (self.font.get_height() + 20)

  def draw(self):
    if not self.active:
      return
    if self.stopped:
      self.screen.blit(IMAGES["img/cutscene_31"], (0, 0))
      thank_text, thank_font, thank_color = self.lines[-1]
      thank_surface = thank_font.render(thank_text, True, thank_color)
      thank_x = (self.screen.get_width() - thank_surface.get_width()) // 2
      thank_y = (self.screen.get_height() // 2) - (thank_surface.get_height() // 2)
      self.screen.blit(thank_surface, (thank_x, thank_y))
      press_text = "(Press Space to continue)"
      press_surface = self.font.render(press_text, True, COLORS["black"])
      press_x = (self.screen.get_width() - press_surface.get_width()) // 2
      press_y = thank_y + thank_surface.get_height() + 40
      self.screen.blit(press_surface, (press_x, press_y))
    else:
      self.screen.fill((0, 0, 0))
      y_offset = self.y
      for i, (text, font, color) in enumerate(self.lines):
          text_surface = font.render(text, True, color)
          x = (self.screen.get_width() - text_surface.get_width()) // 2
          self.screen.blit(text_surface, (x, y_offset))
          y_offset += font.get_height() + 20

credits_lines = [
  ("FEATHERS OF THE MOUNTAIN", font_credits_big, COLORS["white"]),
  ("", font_credits, COLORS["white"]),
  ("An original game by Kit Fossengen", font_credits, COLORS["white"]),
  ("", font_credits, COLORS["white"]),
  ("Programming & Design", font_credits, COLORS["white"]),
  ("Kit Fossengen, Kit Fossengen", font_credits, COLORS["white"]),
  ("", font_credits, COLORS["white"]),
  ("Music", font_credits, COLORS["white"]),
  ("Free tracks from various online sources", font_credits, COLORS["white"]),
  ("", font_credits, COLORS["white"]),
  ("Special Thanks", font_credits, COLORS["white"]),
  ("My friends and family", font_credits, COLORS["white"]),
  ("", font_credits, COLORS["white"]),
  ("Thank you for playing!", font_credits_big, COLORS["black"])
]
credits_manager = CreditsManager(credits_lines, font_credits, font_credits_big, screen, speed = 1)


class Snowfall:
  def __init__(self, num_flakes, screen_width, screen_height, intensity=1.0, speed_range=(1, 3), size_range=(2, 5), direction='down'):
    self.num_flakes = num_flakes
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.intensity = intensity
    self.speed_range = speed_range
    self.size_range = size_range
    self.direction = direction
    self.snowflakes = self.create_snowflakes()

  def create_snowflakes(self):
    snowflakes = []
    for i in range(int(self.num_flakes * self.intensity)):
      x = random.randint(0, self.screen_width)
      y = random.randint(0, self.screen_height)
      speed = random.uniform(*self.speed_range)
      size = random.randint(*self.size_range)
      snowflakes.append([x, y, speed, size])
    return snowflakes

  def update(self):
    for flake in self.snowflakes:
      if self.direction == 'down':
        flake[1] += flake[2]
      elif self.direction == 'left':
        flake[0] -= flake[2]
      elif self.direction == 'right':
        flake[0] += flake[2]

      # Om snöflingan går utanför skärmen, återställ den till toppen (eller sidorna)
      if flake[1] > self.screen_height:
        flake[0] = random.randint(0, self.screen_width)
        flake[1] = random.randint(-50, -10)

      if flake[0] > self.screen_width:
        flake[0] = random.randint(-50, -10)
        flake[1] = random.randint(0, self.screen_height)

  def draw(self, screen):
    for flake in self.snowflakes:
      pygame.draw.circle(screen, COLORS["white"], (flake[0], flake[1]), flake[3])

# Snöfall för olika nivåer
def create_snowfall_for_level(level, screen_width, screen_height):
  if level in range (0, 3):
    return Snowfall(num_flakes = 100, screen_width = tile_size * 26, screen_height = screen_height, intensity = 0.5, speed_range = (1, 2), size_range = (2, 4), direction = 'down')
  elif level in range (3, 5):
    return Snowfall(num_flakes = 150, screen_width = tile_size * 26, screen_height = screen_height, intensity = 1.0, speed_range = (2, 4), size_range = (2, 5), direction = 'down')
  elif level == 5:
    return Snowfall(num_flakes = 250, screen_width = tile_size * 26, screen_height = screen_height, intensity = 2.0, speed_range = (2, 4), size_range = (2, 6), direction = 'down')

class Button():
  def __init__(self, x, y, image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.clicked = False

  def draw(self):
    action = False
    pos = pygame.mouse.get_pos()

    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        action = True
        self.clicked = True
    
    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False


    screen.blit(self.image, self.rect)

    return action
  
  def is_clicked(self, event):
    return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


class Player():
  def __init__(self, x, y):
    self.reset(x, y)
    self.conversation_step = 0
    self.conversation_cooldown = 0
    self.knockback_x = 0
    self.in_water = False

  def knockback(self, amount):
    self.knockback_x += amount

  def update(self, game_over):
    global is_freezing
    global temp
    global main_menu
    global messages
    global level
    global world
    global move_egg
    global player_at_npc_kille
    global player_at_npc_tjej
    global player_at_npc_borgmästare
    global player_at_npc_barman
    global hp
    global snowfall
    if hp <= 0:
      game_over = -1
    self.dx = 0
    self.dy = 0
    walk_cooldown = 5
    col_thresh = 10
    draw_npc_sign
    if self.conversation_cooldown > 0:
      self.conversation_cooldown -= 1
    else:
      self.conversation_cooldown = 0
    if snowfall != None and level == 27:
      self.dx += tile_size / 25

    if game_over == 0:
      # Hämtar tangent rörelser
      key = pygame.key.get_pressed()
      if (key[pygame.K_w] or key[pygame.K_UP] or key[pygame.K_SPACE]) and self.jumped == False and self.in_air == False:
        hoppar_fx.play()
        self.vel_y = -16
        self.jumped = True

      if (key[pygame.K_w] or key[pygame.K_UP] or key[pygame.K_SPACE]) == False:
        self.jumped = False

      if (key[pygame.K_a] or key[pygame.K_LEFT]):
        self.direction = "left"
        self.counter += 1
        self.dx -= tile_size / 8

      if (key[pygame.K_d] or key[pygame.K_RIGHT]):
        self.direction = "right"
        self.counter += 1
        self.dx += tile_size / 8

      if not (key[pygame.K_a] or key[pygame.K_LEFT]) and not (key[pygame.K_d] or key[pygame.K_RIGHT]) and not (key[pygame.K_w] or key[pygame.K_UP]) and not (key[pygame.K_s] or key[pygame.K_DOWN]):
        self.counter = 0
        self.index = 0
        if self.direction == "right":
          self.image = self.images_right[self.index]
        if self.direction == "left":
          self.image = self.images_left[self.index]
        if self.direction == "up":
          self.image = self.images_up[self.index]
        if self.direction == "down":
          self.image = self.images_down[self.index]

      if (key[pygame.K_ESCAPE]):
        main_menu = True
      
        
      # Hanterar player-animationen
      if self.counter > walk_cooldown:
          self.counter = 0
          self.index += 1

      if level == 28:
          speed = tile_size / 8
          self.dx = 0
          self.dy = 0

          if self.index >= len(self.images_climb):
              self.index = 0
          self.image = self.images_climb[self.index]

          # Ingen gravitation på level 28
          self.vel_y = 0

          # Kolla om spelaren rör sig
          if key[pygame.K_w] or key[pygame.K_UP]:
              self.dy -= 1
              self.counter += 1
          if key[pygame.K_s] or key[pygame.K_DOWN]:
              self.dy += 1
              self.counter += 1
          if key[pygame.K_a] or key[pygame.K_LEFT]:
              self.dx -= 1
              self.counter += 1
          if key[pygame.K_d] or key[pygame.K_RIGHT]:
              self.dx += 1
              self.counter += 1

          if self.dx != 0 or self.dy != 0:
            length = (self.dx ** 2 + self.dy ** 2) ** 0.5
            self.dx = self.dx / length * speed
            self.dy = self.dy / length * speed
          else:
            self.counter = 0
            self.index = 0
            self.image = self.images_climb[0]

      else:
        # Vanlig animation och gravitation för alla andra banor (inklusive level 12)
        if self.direction == "left":
          if self.index >= len(self.images_left):
            self.index = 0
          self.image = self.images_left[self.index]

        if self.direction == "right":
          if self.index >= len(self.images_right):
              self.index = 0
          self.image = self.images_right[self.index]

        if self.direction == "up":
          if self.index >= len(self.images_up):
              self.index = 0
          self.image = self.images_up[self.index]

        if self.direction == "down":
          if self.index >= len(self.images_down):
              self.index = 0
          self.image = self.images_down[self.index]

      # Level 12 och övriga banor: hantera gravitation och rörelse som vanligt
      if level == 12:
        self.vel_y = 0
        speed = tile_size / 8
        self.dx = 0
        self.dy = 0
        if key[pygame.K_w] or key[pygame.K_UP]:
          self.dy -= 1
          self.direction = "up"
          self.counter += 1
        if key[pygame.K_a] or key[pygame.K_LEFT]:
          self.dx -= 1
          self.direction = "left"
          self.counter += 1
        if key[pygame.K_s] or key[pygame.K_DOWN]:
          self.dy += 1
          self.direction = "down"
          self.counter += 1
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
          self.dx += 1
          self.direction = "right"
          self.counter += 1

        # Normalisera rörelsen så att diagonaler inte är snabbare
        if self.dx != 0 or self.dy != 0:
          length = (self.dx ** 2 + self.dy ** 2) ** 0.5
          self.dx = self.dx / length * speed
          self.dy = self.dy / length * speed
        else:
          self.counter = 0
          self.index = 0
          if self.direction == "up":
            self.image = self.images_up[0]
          elif self.direction == "down":
            self.image = self.images_down[0]
          elif self.direction == "left":
            self.image = self.images_left[0]
          elif self.direction == "right":
            self.image = self.images_right[0]
        # Animation (om du vill ha den kvar)
        if self.counter > 5:
          self.counter = 0
          self.index += 1
        if self.index >= 3:
          self.index = 0
        if self.direction == "up":
          self.image = self.images_up[self.index]
        elif self.direction == "down":
          self.image = self.images_down[self.index]
        elif self.direction == "left":
          self.image = self.images_left[self.index]
        elif self.direction == "right":
          self.image = self.images_right[self.index]

      else:
        # Vanlig gravitation på övriga banor
        self.vel_y += 1
        if self.vel_y > tile_size / 3.5:
          self.vel_y = tile_size / 3.5
        self.dy += self.vel_y

      # Kontrollera kollision för en
      self.in_air = True
      for tile in world.tile_list:
          # Skapa en rektangel för spelarens nya position
          player_rect_x = pygame.Rect(self.rect.x + self.dx, self.rect.y, self.width, self.height)
          player_rect_y = pygame.Rect(self.rect.x, self.rect.y + self.dy, self.width, self.height)

          # Hindrar spelaren från att falla ut ur kartan
          # Under eller över kartan
          if self.rect.top <= 0:
            if level == 17:
              game_over = 1
            else:
              self.rect.top = 0
              self.vel_y = 0

          # # Vänster eller höger om kartan
          if self.rect.x > tile_size * 26:
            reset_level(level)
          elif self.rect.y < -20:
            reset_level(level)

          # Ignorera kollisioner med barriär (tile 29) om ägget har rullat
          if egg_has_rolled and tile[0] == IMAGES["img/barriär"]:
            continue

          # Kontrollera kollision i X-axeln
          if tile[1].colliderect(player_rect_x):
            if self.dx > 0:  # Rör sig åt höger
              self.dx = tile[1].left - self.rect.right
            elif self.dx < 0:  # Rör sig åt vänster
              self.dx = tile[1].right - self.rect.left

          # Kontrollera kollision i Y-axeln
          if tile[1].colliderect(player_rect_y):
            if level == 12:
              # Om spelaren går upp och träffar ett block
              if self.dy < 0:
                self.dy = tile[1].bottom - self.rect.top
              # Om spelaren går ner och träffar ett block
              elif self.dy > 0:
                self.dy = tile[1].top - self.rect.bottom
            else:
              # Standard kollisioner på andra nivåer
              if self.vel_y < 0:  # Om spelaren hoppar och träffar ett block
                self.dy = tile[1].bottom - self.rect.top
                self.vel_y = 0
              elif self.vel_y >= 0:  # Om spelaren faller och landar på ett block
                self.dy = tile[1].top - self.rect.bottom
                self.vel_y = 0
                self.in_air = False


      # Kolla efter kollision med vildsvin
      if pygame.sprite.spritecollide(self, vildsvin_group, False):
        vildsvin_fx.play()
        game_over = -1
      
      # Kolla efter kollision med älgar
      if pygame.sprite.spritecollide(self, älg_group, False):
        moose_fx.play()
        game_over = -1

      # Kolla efter kollision med örnar
      if pygame.sprite.spritecollide(self, örn_group, False):
        eagle_fx.play()
        game_over = -1

      # Kolla efter kollision med vatten
      if pygame.sprite.spritecollide(self, vatten_group, False):
        is_freezing = True
        if not self.in_water:
          water_splash_fx.play()
          self.in_water = True
      else:
        self.in_water = False
        if is_freezing and temp == 0:
          iced_fx.play()
          game_over = -1
          if self.direction == "left":
            self.image = pygame.transform.flip(self.frozen_image, True, False)

          else:
            self.image = self.frozen_image

      # Kolla efter kollision med dörr
      if pygame.sprite.spritecollide(self, dörr_group, False):
        draw_text("Press E or Enter to continue", font, COLORS["black"], tile_size * 5.5, tile_size * 5.5)
      if pygame.sprite.spritecollide(self, dörr_group, False) and (key[pygame.K_e] or key[pygame.K_RETURN]):
        game_over = 1

      # Kolla efter kollision med volymer
      if pygame.sprite.spritecollide(self, volym_group, False):
        game_over = 1

      global player_can_enter
      if level == 27:
        for örn_boss in örn_boss_group:
          if örn_boss.hp <= 0:
            player_can_enter = True
            break
          else:
            player_can_enter = False
        for volymG in volymG_group:
          if player_can_enter:
            volymG.image = IMAGES["img/grotta"]
          else:
            volymG.image = IMAGES["img/jord"]
      else:
        player_can_enter = True
        for volymG in volymG_group:
          volymG.image = IMAGES["img/grotta"]
      if pygame.sprite.spritecollide(self, volymG_group, False) and player_can_enter:
        game_over = 1

      # Kolla efter kollision med brasor
      if pygame.sprite.spritecollide(self, brasa_group, False):
        is_freezing = False

      # Kolla efter kollision med fladdermössen
      if pygame.sprite.spritecollide(self, fladdermus_group, False):
        fladdermus_fx.play()
        game_over = -1

      # Kolla efter kollision med stalaktiter
      if pygame.sprite.spritecollide(self, stalaktit_group, False):
        damage_w_fx.play()
        game_over = -1

      # Kolla efter kollision med kristallerna
      for kristall in kristall_group:
        if pygame.sprite.collide_rect(self, kristall):
          if not kristall.effect_done:
            kristall.is_active = True
            kristall.effect_done = False
            crystal_fx.play()
        else:
          kristall.is_active = False
          kristall.reset_effect()

      # Kollision med äggen
      if pygame.sprite.spritecollide(self, egg_group, False):
        move_egg = True
      else:
        move_egg = False

      # Kolla efter kollision med hornen
      for horn in horn_group:
        for örn_boss in örn_boss_group:
          if pygame.sprite.collide_rect(self, horn):  # Kontrollera kollision med ett specifikt horn
            horn.draw_effect(screen)
            if not horn.damage_given:
              örn_boss.hp -= 1
              horn_fx.play()
              if hp <= 80:
                hp += 20
              horn.damage_given = True
            if not horn.is_animating:
              horn.start_animation()

      # Updaterar bossens hp
      for örn_boss in örn_boss_group:
        # Starta attack om bossen är redo och spelaren kolliderar
        if pygame.sprite.collide_rect(self, örn_boss) and not örn_boss.is_slashing and level == 27:
            örn_boss.slash_attack(self)
            eagle_fx.play()
        elif pygame.sprite.collide_rect(self, örn_boss) and not örn_boss.has_damaged and level == 28:
          damage_h_fx.play()
          hp -= 30
          örn_boss.has_damaged = True
        # Ge skada endast på sista bilden och bara en gång per attack
        if (pygame.sprite.collide_rect(player, örn_boss) and örn_boss.is_slashing and örn_boss.slash_index == len(örn_boss.slash_images) - 1 and not örn_boss.damage_given):
          hp -= 30
          damage_h_fx.play()
          if player.rect.x < örn_boss.rect.x:
            self.dx -= tile_size
          else:
            self.dx += tile_size
          örn_boss.damage_given = True
        örn_boss.healthpoints()

      if level == 27:
        for örn_boss in örn_boss_group:
          if örn_boss.hp == 0 and snowfall == None:
            snowfall = Snowfall(
              num_flakes = 250,
              screen_width = tile_size * 26,
              screen_height = tile_size * 14,
              intensity = 4.0,
              speed_range = (2, 4),
              size_range = (4, 8),
              direction = 'right'
            )
      if level == 28:
        for örn_boss in örn_boss_group:
         if not örn_boss.fly_mode:
            örn_boss.start_fly()


      # Gör så att konversationsskylten ritas på rätt plats
      if pygame.sprite.spritecollide(self, npc_kille_group, False):
        player_at_npc_kille = True
      else:
        player_at_npc_kille = False
      
      if pygame.sprite.spritecollide(self, npc_tjej_group, False):
        player_at_npc_tjej = True
      else:
        player_at_npc_tjej = False

      if pygame.sprite.spritecollide(self, npc_borgmästare_group, False):
        player_at_npc_borgmästare = True
      else:
        player_at_npc_borgmästare = False

      if pygame.sprite.spritecollide(self, npc_barman_group, False):
        player_at_npc_barman = True
      else:
        player_at_npc_barman = False

      # Kolla efter kollision med skylt
      if pygame.sprite.spritecollide(self, skylt_group, False) and level == 0:
        draw_text("Press A - D or < - > to go left and right", font, COLORS["black"], tile_size * 3, tile_size * 5 + (tile_size // 5))
      if pygame.sprite.spritecollide(self, skylt_group, False) and level == 1:
        draw_text("Press W or PgUp to jump over obstacles", font, COLORS["black"], tile_size * 3, tile_size * 5 + (tile_size // 5))
      if pygame.sprite.spritecollide(self, skylt_group, False) and level == 2:
        draw_text("Be careful of cold water", font, COLORS["black"], tile_size * 6, tile_size * 5 + (tile_size // 5))
      if pygame.sprite.spritecollide(self, skylt_group, False) and level == 3:
        draw_text("Cozy campfires can warm you up", font, COLORS["black"], tile_size * 3, tile_size * 5 + (tile_size // 5))
      if pygame.sprite.spritecollide(self, skylt_group, False) and level == 5:
        draw_text("Run to the cave before you freeze", font, COLORS["black"], tile_size * 4, tile_size * 5 + (tile_size // 5))
        is_freezing = True
     
      # Kolla efter kollision med plattformar
      for plattform in plattform_group:
        # Kollision i X-axeln
        if plattform.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
          # Rör sig åt höger
          if self.dx > 0:
            self.dx = plattform.rect.left - self.rect.right
          # Rör sig åt vänster
          elif self.dx < 0:
            self.dx = plattform.rect.right - self.rect.left

        # Kollision i Y-axeln
        if plattform.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
          # Kolla om spelaren landar på plattformen
          if self.rect.bottom <= plattform.rect.top + col_thresh and self.vel_y >= 0:
            self.rect.bottom = plattform.rect.top - 1.6
            self.in_air = False
            self.vel_y = 0
            self.dy = 0

          # Kolla om spelaren träffar plattformen underifrån
          elif self.rect.top >= plattform.rect.bottom - col_thresh and self.vel_y <= 0 and self.in_air == True:
            self.rect.top = plattform.rect.bottom 
            self.vel_y = 0
            self.dy = 0

          # Kolla om spelaren träffar plattformen underifrån och spelaren är i marken
          elif self.rect.top >= plattform.rect.bottom - col_thresh and self.vel_y <= 0 and self.in_air == False:
            self.rect.top = plattform.rect.bottom 
            self.vel_y = 0
            self.dy = 0
            damage_w_fx.play()
            game_over = -1
          

          # Spelaren rör sig sida till sida med plattformen
          if plattform.move_x != 0 and self.rect.bottom == plattform.rect.top:
            self.dx += plattform.move_direction * plattform.move_x

      # Updaterar spelar koordinater
      self.rect.x += self.dx
      self.rect.y += self.dy

    # Rita spelaren på skärmen
    screen.blit(self.image, self.rect)

    # Meddelanden från NPC:er (första 3 meddelanden från varje NPC)
    messages = [
      "Welcome stranger,\nto our humble village.",
      "You are free to \nexplore, but don´t...",
      "...Stay outside for  \ntoo long.",
      "Hello mister, what \ndo you think...",
      "...about our little town?",
      "But stay away \nfrom the wildlife.",
      "Welcome to by village,\nI´m the mayor.",
      "Meet me at the bar,I\nhave to tell you something.",
      "I wouldn´t stay outside\n too long.",
      "Hi again, I also work as a bartender.\nWould you like something to drink?",
      "...",
      "I´ll take it as a no then, but anyways,\nwe need your help.",
      "The wild animals are going wild on us,\nand they are stealing our belongings!",
      "Some of us think that they live under\n a mighty eagle that has gone beserk.",
      "We saw them climbing the mountain\nwith our things, do you have what it \ntakes to bring everything back?"
    ]

    global iced_fx_is_playing
    if level != 5:
      if is_freezing == True: # Spelaren tar skada av att nudda vattnet
        if temp > 0:
          temp -= 1
        if temp <= 0 and not iced_fx_is_playing:
          iced_fx.play()
          iced_fx_is_playing = True
          game_over = -1
          if self.direction == "left":  # Om spelaren tittade åt vänster
            self.image = pygame.transform.flip(self.frozen_image, True, False)

          else: # Om spelaren tittade åt höger
            self.image = self.frozen_image
    
      else: # Spelaren värms av att vara nära brasan
        if temp < 100:
          temp += 1
          iced_fx_is_playing = False
    else:
      if is_freezing == True: # Spelaren tar skada av att nudda vattnet
        if temp > 0:
          temp -= 1
        if temp <= 0 and not iced_fx_is_playing:
          iced_fx.play()
          iced_fx_is_playing = True
          game_over = -1
          if self.direction == "left":  # Om spelaren tittade åt vänster
            self.image = pygame.transform.flip(self.frozen_image, True, False)

          else: # Om spelaren tittade åt höger
            self.image = self.frozen_image
    
      else: # Spelaren värms av att vara nära brasan
        is_freezing = False
        if temp < 500:
          temp += 1
        iced_fx_is_playing = False

    
    return game_over
  
  def handle_npc_conversations(self, npc_groups):
    global draw_npc_sign
    key = pygame.key.get_pressed()
    in_conversation = False

    for npc_group, start_index in npc_groups:
      if pygame.sprite.spritecollide(self, npc_group, False):
        in_conversation = True
        draw_npc_sign = True
        if npc_group == npc_barman_group:
          npc_messages = messages[start_index:start_index + 6]
        else:
          npc_messages = messages[start_index:start_index + 3]

        # Visa starttexten om konversationen inte har börjat
        if self.conversation_step == 0:
          if player_at_npc_kille:
            draw_text("Press E or Enter to talk", font_conversation, COLORS["white"], tile_size * 7 + (tile_size // 5) * 2, tile_size * 9 + (tile_size // 5))
          elif player_at_npc_tjej:
            draw_text("Press E or Enter to talk", font_conversation, COLORS["white"], tile_size * 13 + (tile_size // 5) * 2, tile_size * 9 + (tile_size // 5))
          elif player_at_npc_borgmästare:
            draw_text("Press E or Enter to talk", font_conversation, COLORS["white"], tile_size * 17 + (tile_size // 5) * 2, tile_size * 9 + (tile_size // 5))
          elif player_at_npc_barman:
            draw_text("Press E or Enter to talk", font_conversation, COLORS["white"], tile_size * 8 + (tile_size // 5) * 2, tile_size * 11 + (tile_size // 4))
          if (key[pygame.K_e] or key[pygame.K_RETURN]) and self.conversation_cooldown == 0:
            self.conversation_step = 1
            self.conversation_cooldown = 20
            
        else:
          # Visa meddelandet för den aktuella konversationssteget
            if player_at_npc_kille:
              draw_text(npc_messages[self.conversation_step - 1], font_conversation, COLORS["white"], tile_size * 7 + (tile_size // 5) * 2, tile_size * 9 + (tile_size // 5))
            elif player_at_npc_tjej:
              draw_text(npc_messages[self.conversation_step - 1], font_conversation, COLORS["white"], tile_size * 13 + (tile_size // 5) * 2, tile_size * 9 + (tile_size // 5))
            elif player_at_npc_borgmästare:
              draw_text(npc_messages[self.conversation_step - 1], font_conversation, COLORS["white"], tile_size * 17 + (tile_size // 5) * 2, tile_size * 9 + (tile_size // 5))
            elif player_at_npc_barman:
              draw_text(npc_messages[self.conversation_step - 1], font_conversation, COLORS["white"], tile_size * 8 + (tile_size // 5) * 2, tile_size * 11 + (tile_size // 4))
            if (key[pygame.K_e] or key[pygame.K_RETURN]) and self.conversation_cooldown == 0:
              self.conversation_step += 1
              self.conversation_cooldown = 20
              if self.conversation_step > len(npc_messages):
                self.conversation_step = 0

    # Återställ konversationssteget om spelaren inte längre är nära en NPC
    if not in_conversation:
      self.conversation_step = 0
      draw_npc_sign = False

  def reset(self, x , y):
    self.images_right = []
    self.images_left = []
    self.images_up = []
    self.images_down = []
    self.images_climb = []
    self.index = 0
    self.counter = 0
    self.direction = "right"
    for num in range(1, 5):
      img_right = IMAGES[f"img/äventyrare_{num}"]
      img_right = pygame.transform.scale(img_right, (tile_size, (tile_size * 2) - ((tile_size // 5) * 2)))
      img_left = pygame.transform.flip(img_right, True, False)
      img_up = IMAGES[f"img/äventyrare_back_{num}"]
      img_up = pygame.transform.scale(img_up, (tile_size, (tile_size * 2) - ((tile_size // 5) * 2)))
      img_down = IMAGES[f"img/äventyrare_front_{num}"]
      img_down = pygame.transform.scale(img_down, (tile_size, (tile_size * 2) - ((tile_size // 5) * 2)))
      self.images_right.append(img_right)
      self.images_left.append(img_left)
      self.images_up.append(img_up)
      self.images_down.append(img_down)
    for num in range(1, 4):
      img_climb = IMAGES[f"img/äventyrare_climb_{num}"]
      img_climb = pygame.transform.scale(img_climb, (tile_size, (tile_size * 2) - ((tile_size // 5) * 2)))
      self.images_climb.append(img_climb)
    self.image = self.images_right[self.index]
    self.frozen_image = IMAGES["img/äventyrare_5"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_y = 0
    self.jumped = False
    self.in_air = False


# Skapa världen med hjälp av nivån
class World():
  def __init__(self, data):
    self.tile_list = []
    for row_count, row in enumerate(data):
      for col_count, tile in enumerate(row):
        if tile == "1":  # Om det är mark (1), skapa en rektangel för tile
          if level == 6 or level == 7 or level == 21 or level == 22 or level == 28:
            img = pygame.transform.scale(IMAGES["img/grotta_grå"], (tile_size, tile_size))
          elif level == 12:
            img = pygame.transform.scale(IMAGES["img/barriär"], (tile_size, tile_size))
          else:
            img = pygame.transform.scale(IMAGES["img/jord"], (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          self.tile_list.append((img, img_rect))
        elif tile == "2":  # Om det är snö (2), skapa en rektangel för tile
          img = pygame.transform.scale(IMAGES["img/jord_snö"], (tile_size, tile_size))
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          self.tile_list.append((img, img_rect))
        elif tile == "3": # Om det är vildsvin (3), skapa en rektangel för tile
          vildsvin = Vildsvin(col_count * tile_size, row_count * tile_size)
          vildsvin_group.add(vildsvin)
        elif tile == "4": # Om det är vatten (4), skapa en rektangel för tile
          vatten = Vatten(col_count * tile_size, row_count * tile_size)
          vatten_group.add(vatten)
        elif tile == "5": # Om det är mithril (5), skapa en rektangel för tile
          mithril = Mithril(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
          mithril_group.add(mithril)
        elif tile == "6": # Om det är plattform (<->) (6), skapa en rektangel för tile
          plattform = Plattform(col_count * tile_size, row_count * tile_size, 1, 0)
          plattform_group.add(plattform)
        elif tile == "7": # Om det är plattform (V/A) (7), skapa en rektangel för tile
          plattform = Plattform(col_count * tile_size, row_count * tile_size, 0, 1)
          plattform_group.add(plattform)
        elif tile == "8": # Om det är dörr (8), skapa en rektangel för tile
          dörr = Dörr(col_count * tile_size, row_count * tile_size - (tile_size // 2))
          dörr_group.add(dörr)
        elif tile == "9": # Om det är älgar (9), skapa en rektangel för tile
          älg = Älg(col_count * tile_size - tile_size, row_count * tile_size - tile_size * 1.5)
          älg_group.add(älg)
        elif tile == "10": # Om det är grotta (10), skapa en rektangel för tile
          grotta = Grotta(col_count * tile_size, row_count * tile_size)
          grotta_group.add(grotta)
        elif tile == "11": # Om det är volym (11), skapa en rektangel för tile
          volym = Volym(col_count * tile_size, row_count * tile_size)
          volym_group.add(volym)
        elif tile == "12": # Om det är brasa (12), skapa en rektangel för tile
          brasa = Brasa(col_count * tile_size - (tile_size // 2), row_count * tile_size)
          brasa_group.add(brasa)
        elif tile == "13": # Om det är skylt (13), skapa en rektangel för tile
          skylt = Skylt(col_count * tile_size, row_count * tile_size)
          skylt_group.add(skylt)
        elif tile == "14": # Om det är volym i en grotta (14), skapa en rektangel för tile
          volymG = VolymG(col_count * tile_size, row_count * tile_size)
          volymG_group.add(volymG)
        elif tile == "15": # Om det är fladdermöss (<->) (15), skapa en rektangel för tile
          fladdermus = Fladdermus(col_count * tile_size, row_count * tile_size, 1, 0)
          fladdermus_group.add(fladdermus)
        elif tile == "16": # Om det är fladdermöss (V/A) (16), skapa en rektangel för tile
          fladdermus = Fladdermus(col_count * tile_size, row_count * tile_size, 0, 1)
          fladdermus_group.add(fladdermus)
        elif tile == "17": # Om det är bybo (17), skapa en rektangel för tile
          npc_kille = Npc_kille(col_count * tile_size, row_count * tile_size)
          npc_kille_group.add(npc_kille)
        elif tile == "18": # Om det är bybo (18), skapa en rektangel för tile
          npc_tjej = Npc_tjej(col_count * tile_size, row_count * tile_size)
          npc_tjej_group.add(npc_tjej)
        elif tile == "19": # Om det är bybo (19), skapa en rektangel för tile
          npc_borgmästare = Npc_borgmästare(col_count * tile_size, row_count * tile_size)
          npc_borgmästare_group.add(npc_borgmästare)
        elif tile == "20": # Om det är örn (<->) (20), skapa en rektangel för tile
          örn = Örn(col_count * tile_size, row_count * tile_size, 1, 0, False)
          örn_group.add(örn)
        elif tile == "21": # Om det är örn (V/A) (21), skapa en rektangel för tile
          örn = Örn(col_count * tile_size, row_count * tile_size, 0, 1, False)
          örn_group.add(örn)
        elif tile == "22": # Om det är örn inverterad (<->) (22), skapa en rektangel för tile
          örn = Örn(col_count * tile_size, row_count * tile_size, 1, 0, True)
          örn_group.add(örn)
        elif tile == "23": # Om det är stalaktit (23), skapa en rektangel för tile
          stalaktit = Stalaktit(col_count * tile_size, row_count * tile_size)
          stalaktit_group.add(stalaktit)
        elif tile == "24": # Om det är höbal (24), skapa en rektangel för tile
          hö = Höbal(col_count * tile_size - tile_size * 1.5, row_count * tile_size - tile_size // 2)
          höbal_group.add(hö)
        elif tile == "25": # Om det är kristall (grön) (25), skapa en rektangel för tile
          kristall = Kristall(col_count * tile_size, row_count * tile_size, "green")
          kristall_group.add(kristall)
        elif tile == "26": # Om det är kristall (blå) (26), skapa en rektangel för tile
          kristall = Kristall(col_count * tile_size, row_count * tile_size, "blue")
          kristall_group.add(kristall)
        elif tile == "27": # Om det är kristall (lila) (27), skapa en rektangel för tile
          kristall = Kristall(col_count * tile_size, row_count * tile_size, "purple")
          kristall_group.add(kristall)
        elif tile == "28": # Om det är ägg (28), skapa en rektangel för tile
          egg = Egg(col_count * tile_size, row_count * tile_size)
          egg_group.add(egg)
        elif tile == "29": # Om det är barriär (29), skapa en rektangel för tile
          img = IMAGES["img/barriär"]
          img_rect = img.get_rect()
          img_rect.x = col_count * tile_size
          img_rect.y = row_count * tile_size
          self.tile_list.append((img, img_rect))
        elif tile == "s": # Om det är sten (31), skapa en rektangel för tile
          if level == 28:
            for i in range(10):
              x = random.randint(tile_size, tile_size * 22)
              y = random.randint(- tile_size * 2, 0)
              sten = Sten(x, y)
              if not pygame.sprite.spritecollide(sten, sten_group, False):
                sten_group.add(sten)
        elif tile == "b": # Om det är örnbossen (b), skapa en rektangel för tile
          örn_boss = Örn_boss(col_count * tile_size - (tile_size), row_count * tile_size - (tile_size * 3))
          örn_boss_group.add(örn_boss)
        elif tile == "30": # Om det är barman (30), skapa en rektangel för tile
          barman = Npc_barman(col_count * tile_size, row_count * tile_size)
          npc_barman_group.add(barman)


  def draw(self):
    for tile in self.tile_list:
      image, rect = tile
      screen.blit(image, rect)

class Vildsvin(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.images = [
        IMAGES["img/vildsvin_1"],
        IMAGES["img/vildsvin_3"],
        IMAGES["img/vildsvin_2"],
    ]
    self.image = self.images[0]  # Startbild
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_direction = 1
    self.move_counter = 0
    self.animation_index = 0  # Håller reda på vilken bild som visas
    self.animation_speed = 15  # Antal frames mellan varje bildväxling
    self.animation_counter = 0  # Räknare för animationen

  def update(self):
    # Flytta vildsvinet
    self.rect.x += self.move_direction
    self.move_counter += 1

    # Byt riktning om vildsvinet når sitt rörelseintervall
    if abs(self.move_counter) > tile_size * 1:
      self.move_direction *= -1
      self.move_counter *= -1

    # Uppdatera animationen
    self.animation_counter += 1
    if self.animation_counter >= self.animation_speed:
      self.animation_counter = 0
      self.animation_index = (self.animation_index + 1) % len(self.images)  # Växla till nästa bild
      self.image = self.images[self.animation_index]

    # Vänd bilden beroende på rörelseriktningen
    if self.move_direction == -1:
      self.image = self.images[self.animation_index]  # Original bild (går åt vänster)
    else:
      self.image = pygame.transform.flip(self.images[self.animation_index], True, False)  # Spegelvänd bild (går åt höger)

class Älg(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.images = [
        IMAGES["img/älg_1"],
        IMAGES["img/älg_2"],
        IMAGES["img/älg_3"],
    ]
    self.image = self.images[0]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_direction = -1
    self.move_counter = 0
    self.animation_index = 0
    self.animation_speed = 10
    self.animation_counter = 0

  def update(self):
    # Flytta älgen
    self.rect.x += self.move_direction
    self.move_counter += 1

    # Byt riktning om älgen når sitt rörelseintervall
    if abs(self.move_counter) > tile_size * 3:
      self.move_direction *= -1
      self.move_counter *= -1

    # Uppdatera animationen
    self.animation_counter += 1
    if self.animation_counter >= self.animation_speed:
      self.animation_counter = 0
      self.animation_index = (self.animation_index + 1) % len(self.images)
      self.image = self.images[self.animation_index]

    # Vänd bilden beroende på rörelseriktningen
    if self.move_direction == -1:
      self.image = self.images[self.animation_index]
    else:
      self.image = pygame.transform.flip(self.images[self.animation_index], True, False)

class Vatten(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/vatten"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y


class Mithril(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/mithril"]
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)


class Plattform(pygame.sprite.Sprite):
  def __init__(self, x, y, move_x, move_y):
    pygame.sprite.Sprite.__init__(self)
    if level == 21 or level == 22:
      self.image = IMAGES["img/grotta_grå"]
    else:
      self.image = IMAGES["img/jord_snö"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_counter = 0
    self.move_direction = -2
    self.move_x = move_x
    self.move_y = move_y
    self.pause_timer = 0

  def update(self):
    if self.pause_timer > 0:
      self.pause_timer -= 1
      return

    # Kontrollera om plattformen når sitt högsta eller lägsta läge
    if abs(self.move_counter) > blockTurnAt:
      self.move_direction *= -1
      self.move_counter *= -1
      self.pause_timer = FPS // 2
    
    # Flytta på plattformen
    self.rect.x += self.move_direction * self.move_x
    self.rect.y += self.move_direction * self.move_y
    self.move_counter += 1


class Dörr(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/osynlig_dörr"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y


class Grotta(pygame.sprite.Sprite):
    def __init__(self, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.image = IMAGES["img/grotta"]
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y

class Volym(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/osynlig_dörr"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class VolymG(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/grotta"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Brasa(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.images = [
      IMAGES["img/brasa_1"],
      IMAGES["img/brasa_2"],
      IMAGES["img/brasa_3"],
      IMAGES["img/brasa_4"],
      IMAGES["img/brasa_5"],
    ]
    self.image = self.images[0]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.animation_index = 0
    self.animation_speed = 10
    self.animation_counter = 0
  def update(self):
    self.animation_counter += 1
    if self.animation_counter >= self.animation_speed:
      self.animation_counter = 0
      self.animation_index = (self.animation_index + 1) % len(self.images)
      self.image = self.images[self.animation_index]

class Skylt(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/skylt"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Fladdermus(pygame.sprite.Sprite):
  def __init__(self, x, y, move_x, move_y):
    pygame.sprite.Sprite.__init__(self)
    self.images = [
      IMAGES["img/fladdermus_1"],
      IMAGES["img/fladdermus_2"],
      IMAGES["img/fladdermus_3"],
    ]
    self.image = self.images[0]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_direction = -1
    self.move_counter = 0
    self.move_x = move_x
    self.move_y = move_y
    self.animation_index = 0
    self.animation_speed = 10
    self.animation_counter = 0

  def update(self):
    # Flytta fladdermusen
    self.rect.x += self.move_direction * self.move_x
    self.rect.y += self.move_direction * self.move_y
    self.move_counter += 1

    # Byt riktning om fladdermusen når sitt rörelseintervall
    if abs(self.move_counter) > batTurnAt:
      self.move_direction *= -1
      self.move_counter *= -1

    if self.move_y != 0:
      if self.move_direction == -1:
        self.animation_speed = 8
      else:
        self.animation_speed = 12
    else:
      self.animation_speed = 10

    # Uppdatera animationen
    self.animation_counter += 1
    if self.animation_counter >= self.animation_speed:
      self.animation_counter = 0
      self.animation_index = (self.animation_index + 1) % len(self.images)
      self.image = self.images[self.animation_index]

    # Vänd bilden beroende på rörelseriktningen
    if self.move_direction == 1 and self.move_y == 0:
      self.image = self.images[self.animation_index]
    else:
      self.image = pygame.transform.flip(self.images[self.animation_index], True, False)

class Npc_kille(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/npc_kille_1"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Npc_tjej(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/npc_tjej_1"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Npc_borgmästare(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/npc_borgmästare"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Npc_barman(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/barriär"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Örn(pygame.sprite.Sprite):
  def __init__(self, x, y, move_x, move_y, invert):
    pygame.sprite.Sprite.__init__(self)
    self.images = [
      IMAGES["img/örn_1"],
      IMAGES["img/örn_2"],
      IMAGES["img/örn_3"],
      IMAGES["img/örn_4"],
      IMAGES["img/örn_3"],
      IMAGES["img/örn_2"],
    ]
    self.image = self.images[0]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_counter = 0
    self.move_x = move_x
    self.move_y = move_y
    self.animation_index = 0
    self.animation_speed = 10
    self.animation_counter = 0
    if invert:
        self.move_direction = 1
    else:
        self.move_direction = -1

  def update(self):
    # Flytta örnen
    self.rect.x += self.move_direction * self.move_x
    self.rect.y += self.move_direction * self.move_y
    self.move_counter += 1

    # Byt riktning om örnen når sitt rörelseintervall
    if abs(self.move_counter) > tile_size * 2:
      self.move_direction *= -1
      self.move_counter *= -1

    # Justera animationshastigheten baserat på rörelseriktningen
    if self.move_y != 0:
      if self.move_direction == -1:
        self.animation_speed = 8
      else:
        self.animation_speed = 12
    else:
      self.animation_speed = 10

    # Uppdatera animationen
    self.animation_counter += 1
    if self.animation_counter >= self.animation_speed:
      self.animation_counter = 0
      self.animation_index = (self.animation_index + 1) % len(self.images)
      self.image = self.images[self.animation_index]

    # Vänd bilden beroende på rörelseriktningen
    if self.move_direction == 1 and self.move_y == 0:
      self.image = self.images[self.animation_index]
    else:
      self.image = pygame.transform.flip(self.images[self.animation_index], True, False)


class Stalaktit(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/stalaktit"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Höbal(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/höbal"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Kristall(pygame.sprite.Sprite):
  def __init__(self, x, y, color):
    pygame.sprite.Sprite.__init__(self)
    self.color = color
    self.images = {
      "green" : [IMAGES["img/kristall_grön_av"], IMAGES["img/kristall_grön_på"]],
      "blue" : [IMAGES["img/kristall_blå_av"], IMAGES["img/kristall_blå_på"]],
      "purple" : [IMAGES["img/kristall_lila_av"], IMAGES["img/kristall_lila_på"]]
    }
    self.effect_images = [
      pygame.transform.scale(IMAGES["img/kristall_effekt_1"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_2"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_3"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_4"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_5"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_6"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_7"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_8"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_9"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_10"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_11"], (size, size)),
      pygame.transform.scale(IMAGES["img/kristall_effekt_12"], (size, size))
    ]
    self.image = self.images[self.color][0]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.is_active = False
    self.effect_index = 0
    self.effect_speed = 5
    self.effect_counter = 0
    self.effect_done = False

  def update(self):
    if self.is_active:
      self.image = self.images[self.color][1]
    else:
      self.image = self.images[self.color][0]
    
    if self.is_active and not self.effect_done:
      self.effect_counter += 1
      if self.effect_counter >= self.effect_speed:
        self.effect_counter = 0
        self.effect_index += 1
        if self.effect_index >= len(self.effect_images):
          self.effect_index = 0
          self.effect_done = True

  def effect(self, screen):
    if self.is_active and not self.effect_done:
      effect_image = self.effect_images[self.effect_index]
      effect_rect = effect_image.get_rect(center=self.rect.center)
      screen.blit(effect_image, effect_rect)

  def reset_effect(self):
    self.effect_index = 0
    self.effect_counter = 0
    self.effect_done = False

class Egg(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.images = [
      IMAGES["img/egg_roll1"],
      IMAGES["img/egg_roll2"],
      IMAGES["img/egg_roll3"],
      IMAGES["img/egg_roll4"]
    ]
    self.image = self.images[0]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_x = 10
    self.moving_to_center = False
    self.animation_index = 0
    self.animation_speed = 5
    self.animation_counter = 0
    self.stop_rolling = False

  def update(self):
    global move_egg
    global egg_has_rolled

    if move_egg:
      self.moving_to_center = True

    if self.moving_to_center:
      if self.rect.x < tile_size * 13:
        self.rect.x += self.move_x
        if self.rect.x >= tile_size * 13:
          self.rect.x = tile_size * 13
          self.stop_rolling = True
          self.moving_to_center = False
          egg_has_rolled = True

      self.animation_counter += 1
      if self.animation_counter >= self.animation_speed and not self.stop_rolling:
        self.animation_counter = 0
        self.animation_index = (self.animation_index + 1) % len(self.images)
        self.image = self.images[self.animation_index]


      
    if not move_egg:
      self.moving_to_center = False

class Horn(pygame.sprite.Sprite):
    def __init__(self, positions):
        pygame.sprite.Sprite.__init__(self)
        self.positions = positions
        self.current_position = random.choice(self.positions)
        self.image = IMAGES["img/horn"]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.current_position
        self.damage_given = False
        size = tile_size * 3
        self.animation_frames = [
          pygame.transform.scale(IMAGES["img/kristall_effekt_1"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_2"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_3"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_4"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_5"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_6"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_7"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_8"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_9"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_10"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_11"], (size, size)),
          pygame.transform.scale(IMAGES["img/kristall_effekt_12"], (size, size))
        ]
        self.animation_index = 0
        self.animation_speed = 5  # Antal frames mellan varje bildväxling
        self.animation_counter = 0
        self.is_animating = False

    def update(self):
      if self.is_animating:
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
          self.animation_counter = 0
          self.animation_index += 1
          if self.animation_index >= len(self.animation_frames):
            self.is_animating = False
            self.respawn()  # Slumpa ut hornet på en ny position
          else:
            pass

    def respawn(self):
      # Välj en ny position som inte är samma som den nuvarande
      new_position = random.choice([pos for pos in self.positions if pos != self.current_position])
      self.current_position = new_position
      self.rect.topleft = self.current_position
      self.image = IMAGES["img/horn"]
      self.animation_index = 0
      self.animation_counter = 0
      self.damage_given = False
  

    def start_animation(self):
      self.is_animating = True

    def draw_effect(self, screen):
      if self.is_animating:
        effect_image = self.animation_frames[self.animation_index]
        effect_rect = effect_image.get_rect(center = self.rect.center)
        effect_rect.x += 0
        effect_rect.y += 0
        screen.blit(effect_image, effect_rect)


class Sten(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = IMAGES["img/sten"]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.speed = tile_size // 10
  
  def update(self):
    self.rect.y += self.speed
    if self.rect.y > tile_size * 15:
      self.rect.y = - self.rect.height
      self.rect.x = random.randint(0, (tile_size * 22) - self.rect.width)

class Örn_boss(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.idle_images = [
      IMAGES["img/örn_boss_1"],
      IMAGES["img/örn_boss_2"],
      IMAGES["img/örn_boss_3"]
    ]
    self.slash_images = [
    IMAGES["img/örn_boss_slash_1"],
    IMAGES["img/örn_boss_slash_2"],
    IMAGES["img/örn_boss_slash_3"],
    IMAGES["img/örn_boss_slash_4"],
    IMAGES["img/örn_boss_slash_5"],
    IMAGES["img/örn_boss_slash_6"],
    IMAGES["img/örn_boss_slash_7"],
    IMAGES["img/örn_boss_slash_8"],
    IMAGES["img/örn_boss_slash_9"],
    IMAGES["img/örn_boss_slash_10"]
    ]
    self.jump_images = [
      IMAGES["img/örn_boss_jump_1"],
      IMAGES["img/örn_boss_jump_2"],
      IMAGES["img/örn_boss_jump_3"],
      IMAGES["img/örn_boss_jump_4"],
      IMAGES["img/örn_boss_jump_5"],
      IMAGES["img/örn_boss_jump_6"],
      IMAGES["img/örn_boss_jump_7"],
      IMAGES["img/örn_boss_jump_8"],
    ]
    # Idle-animationen
    self.idle_index = 0
    self.idle_counter = 0
    self.idle_speed = 15
    # Slashing-animationen
    self.is_slashing = False
    self.damage_given = False
    self.slash_index = 0
    self.slash_speed = 6
    self.slash_counter = 0
    self.slash_cooldown = 0
    # Jumping-animationen
    self.is_jumping = False
    self.jump_index = 0
    self.jump_counter = 0
    self.jump_speed = 6
    self.is_flying_up = False
    self.is_flying_in = False
    self.fly_speed = 18
    # Initiera sprite
    self.image = self.idle_images[0]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_timer = 0
    self.move_interval = 300
    self.hp = 3
    # Flygningen
    self.fly_mode = False
    self.fly_direction = None  # "down" eller "up"
    self.has_damaged = False
    self.fly_timer = 0
    self.fly_start_time = 0
    self.fly_wait_time = 0
    self.fly_total_time = 0
    self.fly_speed = 18
    self.fly_cooldown = 0
    # Positioner
    self.target_pos = (self.rect.x, self.rect.y)
    self.positions = [
      (tile_size * 10, 0),  # Övre mitten
      (tile_size * 3, tile_size * 3),  # Övre vänstra hörnet
      (tile_size * 17, tile_size * 3),  # Övre högra hörnet
      (tile_size * 2, tile_size * 9),  # Nedre vänstra hörnet
      (tile_size * 3, tile_size * 9),  # Nedre vänstra mitten hörnet
      (tile_size * 10, tile_size * 9),  # Nedre mitten
      (tile_size * 18, tile_size * 9),  # Nedre högra hörnet
      (tile_size * 17, tile_size * 9)  # Nedre högra mitten hörnet
    ]
    self.face_right = False

  def update(self, player):
    self.move_timer += 1

    # Uppdatera cooldown
    if self.slash_cooldown > 0:
      self.slash_cooldown -= 1

    # Bestäm riktning mot spelaren
    if player.rect.x > self.rect.x:
      self.facing_right = True
    else:
      self.facing_right = False

    # Flygning
    if self.fly_mode:
      now = pygame.time.get_ticks()
      # Avsluta efter 20 sekunder
      if now - self.fly_total_time > 10000:
        global game_over
        game_over = 1
        self.fly_mode = False
        return

      # Flyg ner
      if self.fly_direction == "down":
        self.rect.y += self.fly_speed
        self.image = pygame.transform.flip(self.jump_images[-1], False, True)        
        if self.rect.y > screen.get_height():
          # Vänta 1 sekund, sen flyg upp
          if self.fly_cooldown == 0:
            self.fly_cooldown = now
          elif now - self.fly_cooldown > 1000:
            self.start_fly_up()
            eagle_fx.play()
        return  # Hindra annan kod från att köra

      # Flyg upp
      if self.fly_direction == "up":
        self.rect.y -= self.fly_speed
        self.image = self.jump_images[-1]
        if self.rect.y + self.rect.height < 0:
          # Vänta slumpad tid, sen flyg ner igen
          if self.fly_cooldown == 0:
            self.fly_cooldown = now
            self.fly_wait_time = random.randint(1000, 3000)
          elif now - self.fly_cooldown > self.fly_wait_time:
            self.start_fly_down()
            eagle_fx.play()
        return  # Hindra annan kod från att köra

    # Jump-animation
    if self.is_jumping:
      self.jump_counter += 1
      if self.jump_counter >= self.jump_speed:
        self.jump_counter = 0
        self.jump_index += 1
        if self.jump_index >= len(self.jump_images):
          self.jump_index = len(self.jump_images) - 1
          self.is_jumping = False
          self.is_flying_up = True  # Starta flyg uppåt
      current_image = self.jump_images[self.jump_index]
      if self.facing_right:
        self.image = pygame.transform.flip(current_image, True, False)
      else:
        self.image = current_image
      return

    # Flyg uppåt ut ur skärmen
    if self.is_flying_up:
      self.rect.y -= self.fly_speed
      if self.rect.y + self.rect.height < 0:
        self.is_flying_up = False
        self.is_flying_in = True
        # Starta underifrån, men på rätt x
        self.rect.x = self.target_pos[0]
        self.rect.y = screen_height
      current_image = self.jump_images[-1]
      if self.facing_right:
        self.image = pygame.transform.flip(current_image, True, False)
      else:
        self.image = current_image
      return

    # --- NYTT: Flyg in underifrån till target_pos ---
    if self.is_flying_in:
      if self.rect.y > self.target_pos[1]:
        self.rect.y -= self.fly_speed
        if self.rect.y <= self.target_pos[1]:
          self.rect.y = self.target_pos[1]
          self.is_flying_in = False
      current_image = self.jump_images[-1]
      if self.facing_right:
        self.image = pygame.transform.flip(current_image, True, False)
      else:
        self.image = current_image
      return

    # Slash-animation
    if self.is_slashing:
      self.slash_counter += 1
      if self.slash_counter >= self.slash_speed:
        self.slash_counter = 0
        self.slash_index += 1
        if self.slash_index >= len(self.slash_images):
          self.slash_index = 0
          self.is_slashing = False
          self.damage_given = False
      current_image = self.slash_images[self.slash_index]
    else:
      # Idle-animation
      self.idle_counter += 1
      if self.idle_counter >= self.idle_speed:
        self.idle_counter = 0
        self.idle_index = (self.idle_index + 1) % len(self.idle_images)
      current_image = self.idle_images[self.idle_index]

    # Välj rätt bild och vänd om det behövs
    if self.facing_right:
      self.image = pygame.transform.flip(current_image, True, False)
    else:
      self.image = current_image

    if self.move_timer >= self.move_interval:
      self.move_timer = 0
      self.move(player)

  def move(self, player):
    player_pos = (player.rect.x, player.rect.y)
    possible_positions = [pos for pos in self.positions if (pos[0], pos[1]) != (self.rect.x, self.rect.y)]
    self.target_pos = min(possible_positions, key = lambda pos: (pos[0] - player_pos[0]) ** 2 + (pos[1] - player_pos[1]) ** 2)
    self.is_jumping = True
    self.jump_index = 0
    self.jump_counter = 0
    self.is_flying_up = False
    self.is_flying_in = False

  def healthpoints(self):
    global game_over

    if level == 27:
      # Bakgrundsrektangel (svart)
      background_rect = pygame.Rect(tile_size * 6, tile_size, tile_size * 13, tile_size // 2)
      pygame.draw.rect(screen, COLORS["black"], background_rect)

      # Hälsomätare (röd)
      health_width = (tile_size * 13) * (self.hp / 3)
      health_rect = pygame.Rect(tile_size * 6, tile_size, health_width, tile_size // 2)
      pygame.draw.rect(screen, COLORS["red"], health_rect)

  def slash_attack(self, player):
    if not self.is_slashing and self.slash_cooldown == 0 and level == 27:
      self.is_slashing = True
      self.slash_index = 0
      self.slash_counter = 0
      self.slash_cooldown = 120

  def start_fly(self):
    self.fly_mode = True
    self.fly_total_time = pygame.time.get_ticks()
    self.start_fly_down()

  def start_fly_down(self):
    self.fly_direction = "down"
    self.rect.x = random.randint(tile_size, tile_size * 22)
    self.rect.y = -self.rect.height
    self.image = self.jump_images[-1]
    self.fly_timer = pygame.time.get_ticks()
    self.fly_cooldown = 0
    self.has_damaged = False

  def start_fly_up(self):
    self.fly_direction = "up"
    self.rect.x = random.randint(tile_size, tile_size * 22)
    self.rect.y = screen.get_height()
    self.image = pygame.transform.flip(self.jump_images[-1], False, True)
    self.fly_timer = pygame.time.get_ticks()
    self.fly_cooldown = 0
    self.has_damaged = False

# Ritar spelaren
player_start_x = int(screen_width * 0.08)
player_start_y = int(screen_height * 0.85)
player = Player(player_start_x, player_start_y)

# Skapa snöfall beroende på nivån
snowfall = create_snowfall_for_level(level, screen_width, screen_height)


# Skapa prylar
vildsvin_group = pygame.sprite.Group()
vatten_group = pygame.sprite.Group()
mithril_group = pygame.sprite.Group()
plattform_group = pygame.sprite.Group()
dörr_group = pygame.sprite.Group()
älg_group = pygame.sprite.Group()
grotta_group = pygame.sprite.Group()
volym_group = pygame.sprite.Group()
volymG_group = pygame.sprite.Group()
brasa_group = pygame.sprite.Group()
skylt_group = pygame.sprite.Group()
fladdermus_group = pygame.sprite.Group()
npc_kille_group = pygame.sprite.Group()
npc_tjej_group = pygame.sprite.Group()
npc_borgmästare_group = pygame.sprite.Group()
npc_barman_group = pygame.sprite.Group()
örn_group = pygame.sprite.Group()
stalaktit_group = pygame.sprite.Group()
höbal_group =  pygame.sprite.Group()
kristall_group = pygame.sprite.Group()
egg_group = pygame.sprite.Group()
barriär_group = pygame.sprite.Group()
horn_group = pygame.sprite.Group()
sten_group = pygame.sprite.Group()
örn_boss_group = pygame.sprite.Group()

# Hantera konversationer med NPC:er
npc_groups = [
  (npc_kille_group, 0),
  (npc_tjej_group, 3),
  (npc_borgmästare_group, 6),
  (npc_barman_group, 9)
]

# Ladda in nivå data och skapa världen
world = World(levels[level])

# Skapa knappar
exit_button = Button(tile_size * 8, tile_size * 7, IMAGES["img/exit_knapp"])
start_button = Button(tile_size * 14, tile_size * 7, IMAGES["img/start_knapp"])
restart_button = Button(tile_size * 11, tile_size * 8, IMAGES["img/restart_knapp"])
level_button = Button((tile_size // 5), tile_size * 13, IMAGES["img/mithril"])
# Knappar från 1 - 9
level_1_button = Button(tile_size * 4, tile_size * 10, IMAGES["img/level_1_knapp"])
level_2_button = Button(tile_size * 6, tile_size * 10, IMAGES["img/level_2_knapp"])
level_3_button = Button(tile_size * 8, tile_size * 10, IMAGES["img/level_3_knapp"])
level_4_button = Button(tile_size * 10, tile_size * 10, IMAGES["img/level_4_knapp"])
level_5_button = Button(tile_size * 12, tile_size * 10, IMAGES["img/level_5_knapp"])
level_6_button = Button(tile_size * 14, tile_size * 10, IMAGES["img/level_6_knapp"])
level_7_button = Button(tile_size * 16, tile_size * 10, IMAGES["img/level_7_knapp"])
level_8_button = Button(tile_size * 18, tile_size * 10, IMAGES["img/level_8_knapp"])
level_9_button = Button(tile_size * 20, tile_size * 10, IMAGES["img/level_9_knapp"])
# Knappar från 10 - 18
level_10_button = Button(tile_size * 4, tile_size * 11, IMAGES["img/level_1_knapp"])
level_11_button = Button(tile_size * 6, tile_size * 11, IMAGES["img/level_2_knapp"])
level_12_button = Button(tile_size * 8, tile_size * 11, IMAGES["img/level_3_knapp"])
level_13_button = Button(tile_size * 10, tile_size * 11, IMAGES["img/level_4_knapp"])
level_14_button = Button(tile_size * 12, tile_size * 11, IMAGES["img/level_5_knapp"])
level_15_button = Button(tile_size * 14, tile_size * 11, IMAGES["img/level_6_knapp"])
level_16_button = Button(tile_size * 16, tile_size * 11, IMAGES["img/level_7_knapp"])
level_17_button = Button(tile_size * 18, tile_size * 11, IMAGES["img/level_8_knapp"])
level_18_button = Button(tile_size * 20, tile_size * 11, IMAGES["img/level_9_knapp"])
# Knappar från 19 - 27
level_19_button = Button(tile_size * 4, tile_size * 12, IMAGES["img/level_1_knapp"])
level_20_button = Button(tile_size * 6, tile_size * 12, IMAGES["img/level_2_knapp"])
level_21_button = Button(tile_size * 8, tile_size * 12, IMAGES["img/level_3_knapp"])
level_22_button = Button(tile_size * 10, tile_size * 12, IMAGES["img/level_4_knapp"])
level_23_button = Button(tile_size * 12, tile_size * 12, IMAGES["img/level_5_knapp"])
level_24_button = Button(tile_size * 14, tile_size * 12, IMAGES["img/level_6_knapp"])
level_25_button = Button(tile_size * 16, tile_size * 12, IMAGES["img/level_7_knapp"])
level_26_button = Button(tile_size * 18, tile_size * 12, IMAGES["img/level_8_knapp"])
level_27_button = Button(tile_size * 20, tile_size * 12, IMAGES["img/level_9_knapp"])
# Knappar från 28 - 29
level_28_button = Button(tile_size * 4, tile_size * 13, IMAGES["img/level_1_knapp"])

# Definiera nivådata i en lista
levels_data = [
  # Starten
  {"level": 0, "button": level_1_button, "music": music_1_fx, "temp": 100, "is_freezing": False},
  {"level": 1, "button": level_2_button, "music": music_1_fx, "temp": 100, "is_freezing": False},
  {"level": 2, "button": level_3_button, "music": music_1_fx, "temp": 100, "is_freezing": False},
  {"level": 3, "button": level_4_button, "music": music_1_fx, "temp": 100, "is_freezing": False},
  {"level": 4, "button": level_5_button, "music": music_1_fx, "temp": 100, "is_freezing": False},
  {"level": 5, "button": level_6_button, "music": music_1_fx, "temp": 500, "is_freezing": True},
  # Grottan
  {"level": 6, "button": level_7_button, "music": music_cave_fx, "temp": 100, "is_freezing": False},
  {"level": 7, "button": level_8_button, "music": music_cave_fx, "temp": 100, "is_freezing": False},
  # Byn
  {"level": 8, "button": level_9_button, "music": music_calm_fx, "temp": 100, "is_freezing": False},
  {"level": 9, "button": level_10_button, "music": music_calm_fx, "temp": 100, "is_freezing": False},
  {"level": 10, "button": level_11_button, "music": music_calm_fx, "temp": 100, "is_freezing": False},
  {"level": 11, "button": level_12_button, "music": music_calm_fx, "temp": 100, "is_freezing": False},
  {"level": 12, "button": level_13_button, "music": music_saloon_fx, "temp": 100, "is_freezing": False},
  # Den nya skogen
  {"level": 13, "button": level_14_button, "music": music_2_fx, "temp": 100, "is_freezing": False},
  {"level": 14, "button": level_15_button, "music": music_2_fx, "temp": 100, "is_freezing": False},
  {"level": 15, "button": level_16_button, "music": music_2_fx, "temp": 100, "is_freezing": False},
  {"level": 16, "button": level_17_button, "music": music_2_fx, "temp": 100, "is_freezing": False},
  {"level": 17, "button": level_18_button, "music": music_2_fx, "temp": 100, "is_freezing": False},
  {"level": 18, "button": level_19_button, "music": music_2_fx, "temp": 100, "is_freezing": False},
  {"level": 19, "button": level_20_button, "music": music_2_fx, "temp": 100, "is_freezing": False},
  # Kristallgrottan
  {"level": 21, "button": level_21_button, "music": music_cave_fx, "temp": 100, "is_freezing": False},
  {"level": 22, "button": level_22_button, "music": music_cave_fx, "temp": 100, "is_freezing": False},
  # Branten
  {"level": 23, "button": level_23_button, "music": music_climb_fx, "temp": 100, "is_freezing": False},
  {"level": 24, "button": level_24_button, "music": music_climb_fx, "temp": 100, "is_freezing": False},
  {"level": 25, "button": level_25_button, "music": music_climb_fx, "temp": 100, "is_freezing": False},
  {"level": 26, "button": level_26_button, "music": music_climb_fx, "temp": 100, "is_freezing": False},
  # Slutstriden
  {"level": 27, "button": level_27_button, "music": music_boss_fx, "temp": 100, "is_freezing": False},
  {"level": 28, "button": level_28_button, "music": music_boss_fx, "temp": 100, "is_freezing": False}
]

# Ritar ut mithril-bilden i det vänstra hörnet
mithril_img = IMAGES["img/mithril"]
mithril_rect = mithril_img.get_rect()
mithril_rect.topleft = (tile_size // 8, tile_size // 7)

# Ritar ut frostbite-bilden
frostbite_img = IMAGES["img/frostbite_1"]
frostbite_rect = frostbite_img.get_rect()
frostbite_rect.topleft = (tile_size, tile_size)

# Spel-loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if mithril_cooldown > 0:
    mithril_cooldown -= 1

  if not by_kit_cutscene_shown:  
    cutscene_manager.start(
      images = [IMAGES["img/by_Kit"], IMAGES["img/cutscene_1"]],
      timers = [3, 1],  # sekunder per bild
      music = None,
      sounds = [(0, silly_trumpet_fx)]
    )
    by_kit_cutscene_shown = True
    waiting_for_cutscene = True
    continue

  if cutscene_manager.active:
    cutscene_manager.update()
    cutscene_manager.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    continue

  # Efter cutscene är klar, byt nivå
  if waiting_for_cutscene and cutscene_manager.finished and level != 29:
    for level_data in levels_data:
      if level_data["level"] == level:
        play_music(level_data["music"])
        temp = level_data["temp"]
        is_freezing = level_data["is_freezing"]
        break
    world = reset_level(level)
    snowfall = create_snowfall_for_level(level, screen_width, screen_height)
    hp = 100
    waiting_for_cutscene = False
    cutscene_manager.finished = False  # Återställ cutscene-flaggan
    game_over = 0

  # Visa credits om de är aktiva
  if credits_manager.active:
    credits_manager.update()
    credits_manager.draw()
    pygame.display.update()
    clock.tick(FPS)
    # Om credits stannat, kolla på SPACE
    if credits_manager.stopped:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
          running = False
    continue

  # När credits är klar, återställ flaggor (eller avsluta spelet om du vill)
  if credits_manager.finished and waiting_for_cutscene:
    waiting_for_cutscene = False
    cutscene_manager.finished = False

  # Starta credits efter sista cutscenen på level 29
  if waiting_for_cutscene and cutscene_manager.finished and level == 29 and not credits_manager.active and not credits_manager.finished:
    credits_manager.start()
    continue

  # När credits är klar, visa slutskärm
  if credits_manager.finished and not show_end_screen:
    show_end_screen = True

  # Visa slutskärm
  if show_end_screen:
    screen.fill((0, 0, 0))
    # Centrera texten
    thank_text = "Thank you for playing!"
    press_text = "(Press Enter to exit)"
    thank_surface = font_credits_big.render(thank_text, True, COLORS["black"])
    press_surface = font_credits.render(press_text, True, COLORS["black"])
    thank_x = (screen.get_width() - thank_surface.get_width()) // 2
    thank_y = (screen.get_height() // 2) - thank_surface.get_height()
    press_x = (screen.get_width() - press_surface.get_width()) // 2
    press_y = (screen.get_height() // 2) + 20
    screen.blit(thank_surface, (thank_x, thank_y))
    screen.blit(press_surface, (press_x, press_y))
    pygame.display.update()
    # Avsluta om spelaren trycker på Enter
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        running = False
    clock.tick(FPS)

  # Ritar bakgrunden
  if level in range (0, 6):
    screen.fill(COLORS["white"])
    screen.blit(IMAGES["img/bakgrund_1"], (0, 0))
  elif level in range (6, 8):
    screen.fill(COLORS["cave_gray"])
    screen.blit(IMAGES["img/bakgrund_2"], (tile_size, tile_size))
  elif level in range (8, 9):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_3"], (tile_size, tile_size))
  elif level in range (9, 10):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_4"], (tile_size, tile_size))
  elif level in range (10, 11):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_5"], (tile_size, tile_size))
  elif level in range (11, 12):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_6_upplyst"], (tile_size, tile_size))
  elif level in range (12, 13):
    screen.fill(COLORS["black"])
    screen.blit(IMAGES["img/bakgrund_7"], (- tile_size // 2, - tile_size * 3))
  elif level in range (13, 14):
    screen.fill(COLORS["white"])
    screen.blit(IMAGES["img/bakgrund_6"], (tile_size, tile_size))
  elif level in range (14, 17):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_3"], (tile_size, tile_size))
  elif level in range (17, 18):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_3"], (tile_size, tile_size))
  elif level in range (18, 21):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_3"], (tile_size, tile_size))
  elif level in range (21, 23):
    screen.fill(COLORS["cave_gray"])
    screen.blit(IMAGES["img/bakgrund_2"], (tile_size, tile_size))
  elif level in range (23, 24):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_8"], (tile_size, tile_size))
  elif level in range (24, 26):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_9"], (tile_size, tile_size))
  elif level in range (26, 27):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_10"], (tile_size, tile_size))
  elif level in range (27, 28):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_11"], (tile_size, tile_size))
  elif level in range (28, 29):
    screen.fill(COLORS["cave_gray"])
    screen.blit(IMAGES["img/bakgrund_12"], (tile_size, tile_size))
  elif level in range (29, 32):
    screen.fill(COLORS["sky-blue"])
    screen.blit(IMAGES["img/bakgrund_3"], (tile_size, tile_size))    

  if main_menu == True:
    play_music(music_menu_fx)
    screen.fill(COLORS["black"])
    screen.blit(IMAGES["img/bakgrund_1"], (0, 0))
    draw_text("FEATHERS OF THE MOUNTAIN", font, COLORS["black"],tile_size * 5.5, tile_size * 4.5)

    # Avsluta spelet
    if exit_button.draw():
      running = False

    # Starta spelet
    if start_button.draw():
      main_menu = False
      # Starta cutscene innan spelet fortsätter
      cutscene_manager.start(
        images = [IMAGES["img/cutscene_2"], IMAGES["img/cutscene_3"], IMAGES["img/cutscene_4"], IMAGES["img/cutscene_1"], IMAGES["img/cutscene_5"], IMAGES["img/cutscene_6"], IMAGES["img/cutscene_5"], IMAGES["img/cutscene_6"], IMAGES["img/cutscene_5"], IMAGES["img/cutscene_6"], IMAGES["img/cutscene_7"], IMAGES["img/cutscene_8"], IMAGES["img/cutscene_9"], IMAGES["img/cutscene_10"], IMAGES["img/cutscene_11"]],
        timers = [2, 2, 2, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, 1, 1, 1, 3],  # sekunder per bild
        music = None,
        sounds = [(6, eagle_fx)]
      )
      waiting_for_cutscene = True
      continue
      player.reset((tile_size * 2) - 2, tile_size * 11)
      game_over = 0
      for level_data in levels_data:
        if level_data["level"] == 0:
          play_music(level_data["music"])
          break

    level_button.draw()
    if level_button.is_clicked(event) and mithril_cooldown == 0:
      visa_bild = not visa_bild
      mithril_cooldown = 30

    # Hantera nivåknappar
    if visa_bild:
      for level_data in levels_data:
        if level_data["button"].draw():
          level = level_data["level"]
          is_freezing = level_data["is_freezing"]
          temp = level_data["temp"]
          main_menu = False
          play_music(level_data["music"])
          world = reset_level(level)
          hp = 100


  else:
    if level != last_level:  # Om nivån har ändrats
      snowfall = create_snowfall_for_level(level, screen_width, screen_height)
      last_level = level  # Uppdatera nivån så att den inte skapar nytt snöfall varje loop

    # Uppdatera och rita snöfall
    if snowfall:
      snowfall.draw(screen)
      snowfall.update()

    # Ritar frosbite bilden
    if is_freezing and temp > 0:
      if level == 5:
        if temp > 350:
          screen.blit(IMAGES["img/frostbite_1"], frostbite_rect)
        elif temp > 150 and temp < 350:
          screen.blit(IMAGES["img/frostbite_2"], frostbite_rect)
        elif temp < 150:
          screen.blit(IMAGES["img/frostbite_3"], frostbite_rect)
      else:
        if temp > 70:
          screen.blit(IMAGES["img/frostbite_1"], frostbite_rect)
        elif temp > 30 and temp < 70:
          screen.blit(IMAGES["img/frostbite_2"], frostbite_rect)
        elif temp < 30:
          screen.blit(IMAGES["img/frostbite_3"], frostbite_rect)

    # Ritar ut chatt-bakgrunden bakom texten (lös genom att flytta koden till en update funktion)
    npc_skylt_1_img = IMAGES["img/npc_skylt_1"]
    npc_skylt_1_rect = npc_skylt_1_img.get_rect()
    npc_skylt_2_img = IMAGES["img/npc_skylt_2"]
    npc_skylt_2_rect = npc_skylt_2_img.get_rect()
    if player_at_npc_kille:
      npc_skylt_1_rect.topleft = (tile_size * 7, tile_size * 9)
    elif player_at_npc_tjej:
      npc_skylt_1_rect.topleft = (tile_size * 13, tile_size * 9)
    elif player_at_npc_borgmästare:
      npc_skylt_1_rect.topleft = (tile_size * 17, tile_size * 9)
    elif player_at_npc_barman:
      npc_skylt_2_rect.topleft = (tile_size * 7.5, tile_size * 11)

    # Rita världen
    world.draw()

    # Sträckan som plattformerna ska gå på varje bana
    if level == 4 or level == 13 or level == 14 or level == 16 or level == 17 or level == 18 or level == 23 or level == 27:
      blockTurnAt = tile_size
    else:
      blockTurnAt = tile_size // 2

    # Sträckan som fladdermössen ska gå på varje bana
    if level == 21 or level == 7:
      batTurnAt = tile_size * 2
    else:
      batTurnAt = tile_size

    # Om spelet är på
    if game_over == 0:
      # Ritar mithril bilden i det vänstra hörnet
      screen.blit(mithril_img, mithril_rect)

      # Uppdaterar grupperna
      vildsvin_group.update()
      plattform_group.update()
      älg_group.update()
      fladdermus_group.update()
      örn_group.update()
      kristall_group.update()
      egg_group.update()
      horn_group.update()
      sten_group.update()
      brasa_group.update()
      örn_boss_group.update(player)


      # Kolla om mithril har plockats upp
      if pygame.sprite.spritecollide(player, mithril_group, True):
        mithril_fx.play()
        if score < 99:
          score += 1
      
      # Kolla efter kollision med stenarna
      if pygame.sprite.spritecollide(player, sten_group, True):
        sten_group.add(Sten(random.randint(tile_size, tile_size * 22), random.randint(- tile_size * 2, 0)))
        damage_w_fx.play()
        hp -= 20
    
      
      
    # Rita prylar
    vildsvin_group.draw(screen)
    vatten_group.draw(screen)
    mithril_group.draw(screen)
    grotta_group.draw(screen)
    plattform_group.draw(screen)
    dörr_group.draw(screen)
    volym_group.draw(screen)
    volymG_group.draw(screen)
    älg_group.draw(screen)
    brasa_group.draw(screen)
    skylt_group.draw(screen)
    fladdermus_group.draw(screen)
    npc_kille_group.draw(screen)
    npc_tjej_group.draw(screen)
    npc_borgmästare_group.draw(screen)
    npc_barman_group.draw(screen)
    örn_group.draw(screen)
    stalaktit_group.draw(screen)
    kristall_group.draw(screen)
    egg_group.draw(screen)
    barriär_group.draw(screen)
    örn_boss_group.draw(screen)
    horn_group.draw(screen)
    sten_group.draw(screen)

    # Ritar effekterna för kristallerna
    for kristall in kristall_group:
      if kristall.is_active:
        kristall.effect(screen)


    # Ritar bakgrunden bakom npc:sens text
    if draw_npc_sign and not player_at_npc_barman:
      screen.blit(npc_skylt_1_img, npc_skylt_1_rect)
    elif draw_npc_sign and player_at_npc_barman:
      screen.blit(npc_skylt_2_img, npc_skylt_2_rect)

    # Ser till att npc-konversationerna startas
    player.handle_npc_conversations(npc_groups)

    # Ritar UI
    if level == 5:
      new_temp = temp // 5
    else:
      new_temp = temp
    if level == 20:
      new_level = level - 4
    elif level > 20:
      new_level = level - 1
    else:
      new_level = level
    if hp < 0:
      hp = 0
    draw_text("X " + str(score), font_score, COLORS["white"], tile_size + (tile_size // 10), tile_size // 10)
    draw_text("   |   HP " + str(hp), font_score, COLORS["white"], tile_size * 2 + (tile_size // 5), tile_size // 10)
    draw_text("  |  TEMP " + str(new_temp), font_score, COLORS["white"], tile_size * 6, tile_size // 10)
    draw_text("  |  LEVEL " + str(new_level + 1), font_score, COLORS["white"], tile_size * 10, tile_size // 10)

    # Uppdatera och rita spelaren
    game_over = player.update(game_over)

    # Ritar höbalen framför spelaren
    höbal_group.draw(screen)

    # Om spelaren har dött
    if game_over == -1:
      # Ritar den krympande cirkeln
      if hole_radius > 40:
        hole_radius -= hole_speed
      hole = pygame.Surface((tile_size * 26, tile_size * 14), pygame.SRCALPHA)
      hole.fill(COLORS["black"])
      player_head_x = player.rect.centerx + 5
      player_head_y = player.rect.top + 20
      pygame.draw.circle(hole, (0, 0, 0, 0), (player_head_x, player_head_y), max(hole_radius, 0))
      screen.blit(hole, (0, 0))

      draw_text("GAME OVER", font, COLORS["white"], tile_size * 10, tile_size * 6)
      key = pygame.key.get_pressed()
      if restart_button.draw() or key[pygame.K_r]:
        world = []
        world = reset_level(level)
        game_over = 0
        score = 0
        is_freezing = False
        if level == 5:
          temp = 500
        else:
          temp = 100
        hp = 100
        hole_radius = tile_size * 13


    # Om spelaren har klarat nivån
    if game_over == 1:
      # Starta om spelet och gå till nästa nivå
      level += 1
      if level == 12 and not cutscene_shown_lvl_12:
        cutscene_manager.start(
        images = [IMAGES["img/cutscene_12"]],
        timers = [2],
        music = None,
        sounds = [(0, door_slam_fx)]
        )
        cutscene_shown_lvl_12 = True
        waiting_for_cutscene = True
        continue
      if level == 28 and not cutscene_shown_lvl_28:
        cutscene_manager.start(
        images = [IMAGES["img/cutscene_13"]],
        timers = [2],
        music = None,
        sounds = [(0, woosh_fx)]
        )
        cutscene_shown_lvl_28 = True
        waiting_for_cutscene = True
        continue
      if level == 29 and not cutscene_shown_lvl_29:
        play_music(None)
        cutscene_manager.start(
        images = [IMAGES["img/cutscene_14"], IMAGES["img/cutscene_15"], IMAGES["img/cutscene_16"], IMAGES["img/cutscene_17"], IMAGES["img/cutscene_18"], IMAGES["img/cutscene_19"], IMAGES["img/cutscene_20"], IMAGES["img/cutscene_21"], IMAGES["img/cutscene_1"], IMAGES["img/cutscene_1"], IMAGES["img/cutscene_22"], IMAGES["img/cutscene_23"], IMAGES["img/cutscene_24"], IMAGES["img/cutscene_25"], IMAGES["img/cutscene_26"], IMAGES["img/cutscene_27"], IMAGES["img/cutscene_28"], IMAGES["img/cutscene_29"], IMAGES["img/cutscene_30"]],
        timers = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 2, 1, 1, 1, 2, 1 , 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
        music = music_ending_fx,
        sounds = None
        )
        cutscene_shown_lvl_29 = True
        waiting_for_cutscene = True
        continue

      # Hitta rätt level_data för nya banan
      for level_data in levels_data:
        if level_data["level"] == level:
          play_music(level_data["music"])
          temp = level_data["temp"]
          is_freezing = level_data["is_freezing"]
          break
      world = reset_level(level)
      game_over = 0
      hp = 100

  # Uppdatera skärmen
  pygame.display.update()

  # Begränsa FPS
  clock.tick(FPS)

# Avsluta Pygame
pygame.quit()

#Om du ser detta, tack för att du spelade spelet! Fler spel från mig kommer i framtiden
