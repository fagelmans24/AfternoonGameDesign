#Susie Fagelman
#Cross the Road

#imports
from itertools import count
import pygame 
import time, sys, random, datetime

#VARIABLES (declaring constants)
WIDTH = 640
HEIGHT = 480
pygame.init() #helps initialize all the modules in pygame. Gives access to many functions 
background = pygame.image.load(r'pygameFiles\\images\\Pygame Crossy Road\\road background.jpg')
background = pygame.transform.scale (background, (WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #setting up screen/window
pygame.display.set_caption("Crossy Road") #setting a caption on top of the window    
clock = pygame.time.Clock() #helps regulate the flow of the main loop 

SCORE = 0
score_font = pygame.font.SysFont('comicsans', 80, True)
MENU_FONT=pygame.font.SysFont('comicsans',20)



colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),


"RED" : (255, 0, 0),
"GREEN" : (0, 255, 0),
"BLUE" : (0, 0,255),
# SHADES,
"BLACK" : (0, 0, 0),
"DARK_GREY" : (60, 60, 60),
"DARK_SLATE_GREY" : (47, 79, 79),
"DIM_GREY" : (105, 105, 105),
"FREE_SPEECH_GREY" : (99, 86, 136),
"GREY" : (190, 190, 190),
"GREY0" : (0, 0, 0),
"GREY1" : (3, 3, 3),
"GREY2" : (5, 5, 5),
"GREY3" : (8, 8, 8),
"GREY4" : (10, 10, 10),
"GREY5" : (13, 13, 13),
"GREY6" : (15, 15, 15),
"GREY7" : (18, 18, 18),
"GREY8" : (20, 20, 20),
"GREY9" : (23, 23, 23),
"GREY10" : (26, 26, 26),
"GREY11" : (28, 28, 28),
"GREY12" : (31, 31, 31),
"GREY13" : (33, 33, 33),
"GREY14" : (36, 36, 36),
"GREY15" : (38, 38, 38),
"GREY16" : (41, 41, 41),
"GREY17" : (43, 43, 43),
"GREY18" : (46, 46, 46),
"GREY19" : (48, 48, 48),
"GREY20" : (51, 51, 51),
"GREY21" : (54, 54, 54),
"GREY22" : (56, 56, 56),
"GREY23" : (59, 59, 59),
"GREY24" : (61, 61, 61),
"GREY25" : (64, 64, 64),
"GREY26" : (66, 66, 66),
"GREY27" : (69, 69, 69),
"GREY28" : (71, 71, 71),
"GREY29" : (74, 74, 74),
"GREY30" : (77, 77, 77),
"GREY31" : (79, 79, 79),
"GREY32" : (82, 82, 82),
"GREY33" : (84, 84, 84),
"GREY34" : (87, 87, 87),
"GREY35" : (89, 89, 89),
"GREY36" : (92, 92, 92),
"GREY37" : (94, 94, 94),
"GREY38" : (97, 97, 97),
"GREY39" : (99, 99, 99),
"GREY40" : (102, 102, 102),
"GREY41" : (105, 105, 105),
"GREY42" : (107, 107, 107),
"GREY43" : (110, 110, 110),
"GREY44" : (112, 112, 112),
"GREY45" : (115, 115, 115),
"GREY46" : (117, 117, 117),
"GREY47" : (120, 120, 120),
"GREY48" : (122, 122, 122),
"GREY49" : (125, 125, 125),
"GREY50" : (127, 127, 127),
"GREY51" : (130, 130, 130),
"GREY52" : (133, 133, 133),
"GREY53" : (135, 135, 135),
"GREY54" : (138, 138, 138),
"GREY55" : (140, 140, 140),
"GREY56" : (143, 143, 143),
"GREY57" : (145, 145, 145),
"GREY58" : (148, 148, 148),
"GREY59" : (150, 150, 150),
"GREY60" : (153, 153, 153),
"GREY61" : (156, 156, 156),
"GREY62" : (158, 158, 158),
"GREY63" : (161, 161, 161),
"GREY64" : (163, 163, 163),
"GREY65" : (166, 166, 166),
"GREY66" : (168, 168, 168),
"GREY67" : (171, 171, 171),
"GREY68" : (173, 173, 173),
"GREY69" : (176, 176, 176),
"GREY70" : (179, 179, 179),
"GREY71" : (181, 181, 181),
"GREY72" : (184, 184, 184),
"GREY73" : (186, 186, 186),
"GREY74" : (189, 189, 189),
"GREY75" : (191, 191, 191),
"GREY76" : (194, 194, 194),
"GREY77" : (196, 196, 196),
"GREY78" : (199, 199, 199),
"GREY79" : (201, 201, 201),
"GREY80" : (204, 204, 204),
"GREY81" : (207, 207, 207),
"GREY82" : (209, 209, 209),
"GREY83" : (212, 212, 212),
"GREY84" : (214, 214, 214),
"GREY85" : (217, 217, 217),
"GREY86" : (219, 219, 219),
"GREY87" : (222, 222, 222),
"GREY88" : (224, 224, 224),
"GREY89" : (227, 227, 227),
"GREY90" : (229, 229, 229),
"GREY91" : (232, 232, 232),
"GREY92" : (235, 235, 235),
"GREY93" : (237, 237, 237),
"GREY94" : (240, 240, 240),
"GREY95" : (242, 242, 242),
"GREY96" : (245, 245, 245),
"GREY97" : (247, 247, 247),
"GREY98" : (250, 250, 250),
"GREY99" : (252, 252, 252),
"LIGHT_GREY" : (211, 211, 211),
"SLATE_GREY" : (112, 128, 144),
"SLATE_GREY_1" : (198, 226, 255),
"SLATE_GREY_2" : (185, 211, 238),
"SLATE_GREY_3" : (159, 182, 205),
"SLATE_GREY_4" : (108, 123, 139),
"VERY_LIGHT_GREY" : (205, 205, 205),
"WHITE" : (255, 255,255),
 
 
"ALICE_BLUE" : (240, 248, 255),
"AQUA" : (0, 255, 255),
"AQUAMARINE" : (127, 255, 212),
"AQUAMARINE_1" : (127, 255, 212),
"AQUAMARINE_2" : (118, 238, 198),
"AQUAMARINE_3" : (102, 205, 170),
"AQUAMARINE_4" : (69, 139, 116),
"AZURE" : (240, 255, 255),
"AZURE_1" : (240, 255, 255),
"AZURE_2" : (224, 238, 238),
"AZURE_3" : (193, 205, 205),
"AZURE_4" : (131, 139, 139),
"BLUE_1" : (0, 0, 255),
"BLUE_2" : (0, 0, 238),
"BLUE_3" : (0, 0, 205),
"BLUE_4" : (0, 0, 139),
"BLUE_VIOLET" : (138, 43, 226),
"CADET_BLUE" : (95, 159, 159),
"CADET_BLUE_1" : (1152, 245, 255),
"CADET_BLUE_2" : (142, 229, 238),
"CADET_BLUE_3" : (122, 197, 205),
"CADET_BLUE_4" : (83, 134, 139),
"CORN_FLOWER_BLUE" : (66, 66, 111),
"CYAN" : (0, 255, 255),
"CYAN_1" : (0, 255, 255),
"CYAN_2" : (0, 238, 238),
"CYAN_3" : (0, 205, 205),
"CYAN_4" : (0, 139, 139),
"DARK_SLATE_BLUE" : (36, 24, 130),
"DARK_TURQUOISE" : (112, 147, 219),
"DEEP_SKY_BLUE" : (0, 191, 255),
"DEEP_SKY_BLUE_1" : (0, 191, 255),
"DEEP_SKY_BLUE_2" : (0, 178, 238),
"DEEP_SKY_BLUE_3" : (0, 154, 205),
"DEEP_SKY_BLUE_4" : (0, 104, 139),
"DODGER_BLUE" : (30, 144, 255),
"DODGER_BLUE_1" : (30, 144, 255),
"DODGER_BLUE_2" : (28, 134, 238),
"DODGER_BLUE_3" : (24, 116, 205),
"DODGER_BLUE_4" : (16, 78, 139),
"FREE_SPEECH_BLUE" : (65, 86, 197),
"LIGHT_BLUE" : (173, 216, 230),
"LIGHT_BLUE_1" : (191, 239, 255),
"LIGHT_BLUE_2" : (178, 223, 238),
"LIGHT_BLUE_3" : (154, 192, 205),
"LIGHT_BLUE_4" : (104, 131, 139),
"LIGHT_CYAN" : (224, 255, 255),
"LIGHT_CYAN_1" : (224, 255, 255),
"LIGHT_CYAN_2" : (209, 238, 238),
"LIGHT_CYAN_3" : (180, 205, 205),
"LIGHT_CYAN_4" : (122, 139, 139),
"LIGHT_SKY_BLUE" : (135, 206, 250),
"LIGHT_SKY_BLUE_1" : (176, 226, 255),
"LIGHT_SKY_BLUE_2" : (164, 211, 238),
"LIGHT_SKY_BLUE_3" : (141, 182, 205),
"LIGHT_SKY_BLUE_4" : (96, 123, 139),
"LIGHT_SLATE_BLUE" : (132, 112, 255),
"LIGHT_STEEL_BLUE" : (176, 196, 222),
"LIGHT_STEEL_BLUE_1" : (202, 225, 255),
"LIGHT_STEEL_BLUE_2" : (188, 210, 238),
"LIGHT_STEEL_BLUE_3" : (162, 181, 205),
"LIGHT_STEEL_BLUE_4" : (110, 123, 139),
"MEDIUM_BLUE" : (0, 0, 205),
"MEDIUM_SLATE_BLUE" : (123, 104, 238),
"MEDIUM_TURQUOISE" : (72, 209, 204),
"MIDNIGHT_BLUE" : (25, 25, 112),
"NAVY" : (0, 0, 128),
"NAVY_BLUE" : (0, 0, 128),
"NEON_BLUE" : (77, 77, 255),
"NEW_MIDNIGHT_BLUE" : (0, 0, 156),
"PALE_TURQUOISE" : (187, 255, 255),
"PALE_TURQUOISE_1" : (187, 255, 255),
"PALE_TURQUOISE_2" : (174, 238, 238),
"PALE_TURQUOISE_3" : (150, 205, 205),
"PALE_TURQUOISE_4" : (102, 139, 139),
"POWDER_BLUE" : (176, 224, 230),
"RICH_BLUE" : (89, 89, 171),
"ROYAL_BLUE" : (65, 105, 225),
"ROYAL_BLUE_1" : (72, 118, 255),
"ROYAL_BLUE_2" : (67, 110, 238),
"ROYAL_BLUE_3" : (58, 95, 205),
"ROYAL_BLUE_4" : (39, 64, 139),
"ROYAL_BLUE_5" : (0, 34, 102),
"SKY_BLUE" : (135, 206, 235),
"SKY_BLUE_1" : (135, 206, 255),
"SKY_BLUE_2" : (126, 192, 238),
"SKY_BLUE_3" : (108, 166, 205),
"SKY_BLUE_4" : (74, 112, 139),
"SLATE_BLUE" : (131, 111, 255),
"SLATE_BLUE_1" : (122, 103, 238),
"SLATE_BLUE_2" : (122, 103, 238),
"SLATE_BLUE_3" : (105, 89, 205),
"SLATE_BLUE_4" : (71, 60, 139),
"STEEL_BLUE" : (70, 130, 180),
"STEEL_BLUE_1" : (99, 184, 255),
"STEEL_BLUE_2" : (92, 172, 238),
"STEEL_BLUE_3" : (79, 148, 205),
"STEEL_BLUE_4" : (54, 100, 139),
"SUMMER_SKY" : (56, 176, 222),
"TEAL" : (0, 128, 128),
"TRUE_IRIS_BLUE" : (3, 180, 204),
"TURQUOISE" : (64, 224, 208),
"TURQUOISE_1" : (0, 245, 255),
"TURQUOISE_2" : (0, 229, 238),
"TURQUOISE_3" : (0, 197, 205),
"TURQUOISE_4" : (0, 134,139),
 
 
"BAKERS_CHOCOLATE" : (92, 51, 23),
"BEIGE" : (245, 245, 220),
"BROWN" : (166, 42, 42),
"BROWN_1" : (255, 64, 64),
"BROWN_2" : (238, 59, 59),
"BROWN_3" : (205, 51, 51),
"BROWN_4" : (139, 35, 35),
"BURLYWOOD" : (222, 184, 135),
"BURLYWOOD_1" : (255, 211, 155),
"BURLYWOOD_2" : (238, 197, 145),
"BURLYWOOD_3" : (205, 170, 125),
"BURLYWOOD_4" : (139, 115, 85),
"CHOCOLATE" : (210, 105, 30),
"CHOCOLATE_1" : (255, 127, 36),
"CHOCOLATE_2" : (238, 118, 33),
"CHOCOLATE_3" : (205, 102, 29),
"CHOCOLATE_4" : (139, 69, 19),
"DARK_BROWN" : (92, 64, 51),
"DARK_TAN" : (151, 105, 79),
"DARK_WOOD" : (133, 94, 66),
"LIGHT_WOOD" : (133, 99, 99),
"MEDIUM_WOOD" : (166, 128, 100),
"NEW_TAN" : (235, 199, 158),
"PERU" : (205, 133, 63),
"ROSY_BROWN" : (188, 143, 143),
"ROSY_BROWN_1" : (255, 193, 193),
"ROSY_BROWN_2" : (238, 180, 180),
"ROSY_BROWN_3" : (205, 155, 155),
"ROSY_BROWN_4" : (139, 105, 105),
"SADDLE_BROWN" : (139, 69, 19),
"SANDY_BROWN" : (244, 164, 96),
"SEMI_SWEET_CHOCOLATE" : (107, 66, 38),
"SIENNA" : (142, 107, 35),
"TAN" : (219, 147, 112),
"TAN_1" : (255, 165, 79),
"TAN_2" : (238, 154, 73),
"TAN_3" : (205, 133, 63),
"TAN_4" : (139, 90, 43),
"VERY_DARK_BROWN" : (92, 64,51),
 
"CHARTREUSE" : (127, 255, 0),
"CHARTREUSE_1" : (127, 255, 0),
"CHARTREUSE_2" : (118, 238, 0),
"CHARTREUSE_3" : (102, 205, 0),
"CHARTREUSE_4" : (69, 139, 0),
"DARK_GREEN" : (47, 79, 47),
"DARK_GREEN_COPPER" : (74, 118, 110),
"DARK_KHAKI" : (189, 183, 107),
"DARK_OLIVE_GREEN" : (85, 107, 47),
"DARK_OLIVE_GREEN_1" : (202, 255, 112),
"DARK_OLIVE_GREEN_2" : (188, 238, 104),
"DARK_OLIVE_GREEN_3" : (162, 205, 90),
"DARK_OLIVE_GREEN_4" : (110, 139, 61),
"DARK_SEA_GREEN" : (143, 188, 143),
"DARK_SEA_GREEN_1" : (193, 255, 193),
"DARK_SEA_GREEN_2" : (180, 238, 180),
"DARK_SEA_GREEN_3" : (155, 205, 155),
"DARK_SEA_GREEN_4" : (105, 139, 105),
"FOREST_GREEN" : (34, 139, 34),
"FREE_SPEECH_GREEN" : (9, 249, 17),
"GREEN_1" : (0, 255, 0),
"GREEN_2" : (0, 238, 0),
"GREEN_3" : (0, 205, 0),
"GREEN_4" : (0, 139, 0),
"GREEN_YELLOW" : (173, 255, 47),
"KHAKI" : (240, 230, 140),
"KHAKI_1" : (255, 246, 143),
"KHAKI_2" : (238, 230, 133),
"KHAKI_3" : (205, 198, 115),
"KHAKI_4" : (139, 134, 78),
"LAWN_GREEN" : (124, 252, 0),
"LIGHT_SEA_GREEN" : (32, 178, 170),
"LIME" : (0, 255, 0),
"MEDIUM_SEA_GREEN" : (60, 179, 113),
"MEDIUM_SPRING_GREEN" : (0, 250, 154),
"MINT_CREAM" : (245, 255, 250),
"OLIVE" : (128, 128, 0),
"OLIVE_DRAB" : (107, 142, 35),
"OLIVE_DRAB_1" : (192, 255, 62),
"OLIVE_DRAB_2" : (179, 238, 58),
"OLIVE_DRAB_3" : (154, 205, 50),
"OLIVE_DRAB_4" : (105, 139, 34),
"PALE_GREEN" : (152, 251, 152),
"PALE_GREEN_1" : (154, 255, 154),
"PALE_GREEN_2" : (144, 238, 144),
"PALE_GREEN_3" : (124, 205, 124),
"PALE_GREEN_4" : (84, 139, 84),
"SEA_GREEN" : (46, 139, 87),
"SEA_GREEN_1" : (84, 255, 159),
"SEA_GREEN_2" : (78, 238, 148),
"SEA_GREEN_3" : (67, 205, 128),
"SEA_GREEN_4" : (46, 139, 87),
"SPRING_GREEN" : (0, 255, 127),
"SPRING_GREEN_1" : (0, 255, 127),
"SPRING_GREEN_2" : (0, 238, 118),
"SPRING_GREEN_3" : (0, 205, 102),
"SPRING_GREEN_4" : (0, 139, 69),
"YELLOW_GREEN" : (154, 205,50),
"BISQUE" : (255, 228, 196),
"BISQUE_1" : (255, 228, 196),
"BISQUE_2" : (238, 213, 183),
"BISQUE_3" : (205, 183, 158),
"BISQUE_4" : (139, 125, 107),
"CORAL" : (255, 127, 0),
"CORAL_1" : (255, 114, 86),
"CORAL_2" : (238, 106, 80),
"CORAL_3" : (205, 91, 69),
"CORAL_4" : (139, 62, 47),
"DARK_ORANGE" : (255, 140, 0),
"DARK_ORANGE_1" : (255, 127, 0),
"DARK_ORANGE_2" : (238, 118, 0),
"DARK_ORANGE_3" : (205, 102, 0),
"DARK_ORANGE_4" : (139, 69, 0),
"DARK_SALMON" : (233, 150, 122),
"HONEYDEW" : (240, 255, 240),
"HONEYDEW_1" : (240, 255, 240),
"HONEYDEW_2" : (224, 238, 224),
"HONEYDEW_3" : (193, 205, 193),
"HONEYDEW_4" : (131, 139, 131),
"LIGHT_CORAL" : (240, 128, 128),
"LIGHT_SALMON" : (255, 160, 122),
"LIGHT_SALMON_1" : (255, 160, 122),
"LIGHT_SALMON_2" : (238, 149, 114),
"LIGHT_SALMON_3" : (205, 129, 98),
"LIGHT_SALMON_4" : (139, 87, 66),
"MANDARIN_ORANGE" : (142, 35, 35),
"ORANGE" : (255, 165, 0),
"ORANGE_1" : (255, 165, 0),
"ORANGE_2" : (238, 154, 0),
"ORANGE_3" : (205, 133, 0),
"ORANGE_4" : (139, 90, 0),
"ORANGE_RED" : (255, 36, 0),
"PEACH_PUFF" : (255, 218, 185),
"PEACH_PUFF_1" : (255, 218, 185),
"PEACH_PUFF_2" : (238, 203, 173),
"PEACH_PUFF_3" : (205, 175, 149),
"PEACH_PUFF_4" : (139, 119, 101),
"SALMON" : (250, 128, 114),
"SALMON_1" : (255, 140, 105),
"SALMON_2" : (238, 130, 98),
"SALMON_3" : (205, 112, 84),
"SALMON_4" : (139, 76, 57),
"SIENNA_1" : (255, 130, 71),
"SIENNA_2" : (238, 121, 66),
"SIENNA_3" : (205, 104, 57),
"SIENNA_4" : (139, 71, 38),
"DEEP_PINK," : (255, 20, 147),
"DEEP_PINK_1" : (255, 20, 147),
"DEEP_PINK_2" : (238, 18, 137),
"DEEP_PINK_3" : (205, 16, 118),
"DEEP_PINK_4" : (139, 10, 80),
"DUSTY_ROSE" : (133, 99, 99),
"FIREBRICK" : (178, 34, 34),
"FIREBRICK_1" : (255, 48, 48),
"FIREBRICK_2" : (238, 44, 44),
"FIREBRICK_3" : (205, 38, 38),
"FIREBRICK_4" : (139, 26, 26),
"FELDSPAR" : (209, 146, 117),
"FLESH" : (245, 204, 176),
"FREE_SPEECH_MAGENTA" : (227, 91, 216),
"FREE_SPEECH_RED" : (192, 0, 0),
"HOT_PINK" : (255, 105, 180),
"HOT_PINK_1" : (255, 110, 180),
"HOT_PINK_2" : (238, 106, 167),
"HOT_PINK_3" : (205, 96, 144),
"HOT_PINK_4" : (139, 58, 98),
"INDIAN_RED" : (205, 92, 92),
"INDIAN_RED_1" : (255, 106, 106),
"INDIAN_RED_2" : (238, 99, 99),
"INDIAN_RED_3" : (205, 85, 85),
"INDIAN_RED_4" : (139, 58, 58),
"LIGHT_PINK" : (255, 182, 193),
"LIGHT_PINK_1" : (255, 174, 185),
"LIGHT_PINK_2" : (238, 162, 173),
"LIGHT_PINK_3" : (205, 140, 149),
"LIGHT_PINK_4" : (139, 95, 101),
"MEDIUM_VIOLET_RED" : (199, 21, 133),
"MISTY_ROSE" : (255, 228, 225),
"MISTY_ROSE_1" : (255, 228, 225),
"MISTY_ROSE_2" : (238, 213, 210),
"MISTY_ROSE_3" : (205, 183, 181),
"MISTY_ROSE_4" : (139, 125, 123),
"ORANGE_RED_1" : (255, 69, 0),
"ORANGE_RED_2" : (238, 64, 0),
"ORANGE_RED_3" : (205, 55, 0),
"ORANGE_RED_4" : (139, 37, 0),
"PALE_VIOLET_RED" : (219, 112, 147),
"PALE_VIOLET_RED_1" : (255, 130, 171),
"PALE_VIOLET_RED_2" : (238, 121, 159),
"PALE_VIOLET_RED_3" : (205, 104, 137),
"PALE_VIOLET_RED_4" : (139, 71, 93),
"PINK" : (255, 192, 203),
"PINK_1" : (255, 181, 197),
"PINK_2" : (238, 169, 184),
"PINK_3" : (205, 145, 158),
"PINK_4" : (139, 99, 108),
"RED_1" : (255, 0, 0),
"RED_2" : (238, 0, 0),
"RED_3" : (205, 0, 0),
"RED_4" : (139, 0, 0),
"SCARLET" : (140, 23, 23),
"SPICY_PINK" : (255, 28, 174),
"TOMATO" : (255, 99, 71),
"TOMATO_1" : (255, 99, 71),
"TOMATO_2" : (238, 92, 66),
"TOMATO_3" : (205, 79, 57),
"TOMATO_4" : (139, 54, 38),
"VIOLET_RED" : (208, 32, 144),
"VIOLET_RED_1" : (255, 62, 150),
"VIOLET_RED_2" : (238, 58, 140),
"VIOLET_RED_3" : (205, 50, 120),
"VIOLET_RED_4" : (139, 34, 82),
 
"DARK_ORCHID," : (153, 50, 204),
"DARK_ORCHID_1" : (191, 62, 255),
"DARK_ORCHID_2" : (178, 58, 238),
"DARK_ORCHID_3" : (154, 50, 205),
"DARK_ORCHID_4" : (104, 34, 139),
"DARK_PURPLE" : (135, 31, 120),
"DARK_VIOLET" : (148, 0, 211),
"FUCHSIA" : (255, 0, 255),
"LAVENDER" : (230, 230, 250),
"LAVENDER_BLUSH" : (255, 240, 245),
"LAVENDER_BLUSH_1" : (255, 240, 245),
"LAVENDER_BLUSH_2" : (238, 224, 229),
"LAVENDER_BLUSH_3" : (205, 193, 197),
"LAVENDER_BLUSH_4" : (139, 131, 134),
"MAGENTA" : (255, 0, 255),
"MAGENTA_1" : (255, 0, 255),
"MAGENTA_2" : (238, 0, 238),
"MAGENTA_3" : (205, 0, 205),
"MAGENTA_4" : (139, 0, 139),
"MAROON" : (176, 48, 96),
"MAROON_1" : (255, 52, 179),
"MAROON_2" : (238, 48, 167),
"MAROON_3" : (205, 41, 144),
"MAROON_4" : (139, 28, 98),
"MEDIUM_ORCHID" : (186, 85, 211),
"MEDIUM_ORCHID_1" : (224, 102, 255),
"MEDIUM_ORCHID_2" : (209, 95, 238),
"MEDIUM_ORCHID_3" : (180, 82, 205),
"MEDIUM_ORCHID_4" : (122, 55, 139),
"MEDIUM_PURPLE" : (147, 112, 219),
"MEDIUM_PURPLE_1" : (171, 130, 255),
"MEDIUM_PURPLE_2" : (159, 121, 238),
"MEDIUM_PURPLE_3" : (137, 104, 205),
"MEDIUM_PURPLE_4" : (93, 71, 139),
"NEON_PINK" : (255, 110, 199),
"ORCHID" : (218, 112, 214),
"ORCHID_1" : (219, 112, 219),
"ORCHID_2" : (238, 122, 233),
"ORCHID_3" : (205, 105, 201),
"ORCHID_4" : (139, 71, 137),
"PLUM" : (221, 160, 221),
"PLUM_1" : (255, 187, 255),
"PLUM_2" : (238, 174, 238),
"PLUM_3" : (205, 150, 205),
"PLUM_4" : (139, 102, 139),
"PURPLE" : (160, 32, 240),
"PURPLE_1" : (155, 48, 255),
"PURPLE_2" : (145, 44, 238),
"PURPLE_3" : (125, 38, 205),
"PURPLE_4" : (85, 26, 139),
"THISTLE" : (216, 191, 216),
"THISTLE_1" : (255, 225, 255),
"THISTLE_2" : (238, 210, 238),
"THISTLE_3" : (205, 181, 205),
"THISTLE_4" : (139, 123, 139),
"VIOLET" : (238, 130, 238),
"VIOLET_BLUE" : (159, 95, 159),
 
"BLANCHED_ALMOND," : (255, 235, 205),
"DARK_GOLDENROD" : (184, 134, 11),
"DARK_GOLDENROD_1" : (255, 185, 15),
"DARK_GOLDENROD_2" : (238, 173, 14),
"DARK_GOLDENROD_3" : (205, 149, 12),
"DARK_GOLDENROD_4" : (139, 101, 8),
"LEMON_CHIFFON" : (255, 250, 205),
"LEMON_CHIFFON_1" : (255, 250, 205),
"LEMON_CHIFFON_2" : (238, 233, 191),
"LEMON_CHIFFON_3" : (205, 201, 165),
"LEMON_CHIFFON_4" : (139, 137, 112),
"LIGHT_GOLDENROD" : (238, 221, 130),
"LIGHT_GOLDENROD_1" : (255, 236, 139),
"LIGHT_GOLDENROD_2" : (238, 220, 130),
"LIGHT_GOLDENROD_3" : (205, 190, 112),
"LIGHT_GOLDENROD_4" : (139, 129, 76),
"LIGHT_GOLDENROD_YELLOW" : (250, 250, 210),
"LIGHT_YELLOW" : (255, 255, 224),
"LIGHT_YELLOW_1" : (255, 255, 224),
"LIGHT_YELLOW_2" : (238, 238, 209),
"LIGHT_YELLOW_3" : (205, 205, 180),
"LIGHT_YELLOW_4" : (139, 139, 122),
"PALE_GOLDENROD" : (238, 232, 170),
"PAPAYA_WHIP" : (255, 239, 213),
"CORNSILK" : (255, 248, 220),
"CORNSILK_1" : (255, 248, 220),
"CORNSILK_2" : (238, 232, 205),
"CORNSILK_3" : (205, 200, 177),
"CORNSILK_4" : (139, 236, 120),
"GOLDENROD" : (218, 165, 32),
"GOLDENROD_1" : (255, 193, 37),
"GOLDENROD_2" : (238, 180, 34),
"GOLDENROD_3" : (205, 155, 29),
"GOLDENROD_4" : (139, 105, 20),
"MOCCASIN" : (255, 228, 181),
"YELLOW" : (255, 255, 0),
"YELLOW_1" : (255, 255, 0),
"YELLOW_2" : (238, 238, 0),
"YELLOW_3" : (205, 205, 0),
"YELLOW_4" : (139, 139, 0),
"GOLD" : (255, 215, 0),
"GOLD_1" : (255, 215, 0),
"GOLD_2" : (238, 201, 0),
"GOLD_3" : (205, 173, 0),
"GOLD_4" : (139, 117, 0),
"MEDIUM_GOLDENROD" : (234, 234, 174),
"ANTIQUE_WHITE" : (250, 235, 215),
"ANTIQUE_WHITE_1" : (255, 239, 219),
"ANTIQUE_WHITE_2" : (238, 223, 204),
"ANTIQUE_WHITE_3" : (205, 192, 176),
"ANTIQUE_WHITE_4" : (139, 131, 120),
"FLORAL_WHITE" : (255, 250, 240),
"GHOST_WHITE" : (248, 248, 255),
"NAVAJO_WHITE" : (255, 222, 173),
"NAVAJO_WHITE_1" : (255, 222, 173),
"NAVAJO_WHITE_2" : (238, 207, 161),
"NAVAJO_WHITE_3" : (205, 179, 139),
"NAVAJO_WHITE_4" : (139, 121, 94),
"OLD_LACE" : (253, 245, 230),
"WHITE_SMOKE" : (245, 245, 245),
"GAINSBORO" : (220, 220, 220),
"IVORY" : (255, 255, 240),
"IVORY_1" : (255, 255, 240),
"IVORY_2" : (238, 238, 224),
"IVORY_3" : (205, 205, 193),
"IVORY_4" : (139, 139, 131),
"LINEN" : (250, 240, 230),
"SEASHELL" : (255, 245, 238),
"SEASHELL_1" : (255, 245, 238),
"SEASHELL_2" : (238, 229, 222),
"SEASHELL_3" : (205, 197, 191),
"SEASHELL_4" : (139, 134, 130),
"SNOW" : (255, 250, 250),
"SNOW_1" : (255, 250, 250),
"SNOW_2" : (238, 233, 233),
"SNOW_3" : (205, 201, 201),
"SNOW_4" : (139, 137, 137),
"WHEAT" : (245, 222, 179),
"WHEAT_1" : (255, 231, 186),
"WHEAT_2" : (238, 216, 174),
"WHEAT_3" : (205, 186, 150),
"WHEAT_4" : (139, 126, 102),
"QUARTZ" : (217, 217, 243),
}
gameOn = True


class Duck(pygame.sprite.Sprite):   #these are the inheretants #the object is a sprite meaning it has certain things like images
    def __init__(self): 
        super().__init__()  #this makes sure that the sprites work properly
        #duck attributes:
        self.x = 50     #where duck starts off at beginning of game
        self.y = HEIGHT / 2     #centering the duck
        self.vel = 4    #setting velocity of duck   
        self.width = 90    #width of the duck
        self.height = 50    #height of the duck

        # IMAGES #two duck images (one for moving right, one for moving left)
        self.duckright = pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct duck1.png')
        self.duckleft = pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct duck2.png')
        self.duckright = pygame.transform.scale(self.duckright, (self.width, self.height))  #scaling images to change dimensions of the image to a particular width or height
        self.duckleft = pygame.transform.scale(self.duckleft, (self.width, self.height))

        #duck is a sprite so it needs an image and a rectangle
        self.image = self.duckright #starts of facing the right
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):   #main update function of sprite
        self.move() #calling movement function
        self.correction()   #calling correction method
        self.checkCollision()
        self.rect.center = (self.x, self.y)

    def move(self):     #function to move the duck with keys
        keys = pygame.key.get_pressed()     #this gets whatver key has been pressed
        if keys[pygame.K_LEFT]: #using left arrow on keyboard
            self.x -= self.vel  #changing x position by the velocity
            self.image = self.duckleft

        elif keys[pygame.K_RIGHT]:  #using right arrow on keyboard
            self.x += self.vel
            self.image = self.duckright

        if keys[pygame.K_UP]: #using up arrow on the keyboard
            self.y -= self.vel  #up is negative velocity 

        elif keys[pygame.K_DOWN]: #using the down arrow on the keyboard
            self.y += self.vel  #down is positive velocity

    def correction(self):   #this function makes sure that the duck is always on the screen
        if self.x - self.width / 2 < 0: #if the cat is off of the screen
            self.x = self.width / 2

        elif self.x + self.width / 2 > WIDTH:
            self.x = WIDTH - self.width / 2

        if self.y - self.height / 2 < 0:
            self.y = self.height / 2

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2

    def checkCollision(self):
        car_check = pygame.sprite.spritecollide(self, car_group, False, pygame.sprite.collide_mask)
        if car_check:   #if collision takes place, call explosion fcuntions
            boom.explode(self.x, self.y)


class Car(pygame.sprite.Sprite): 
    def __init__(self, number):
        super().__init__()
        if number == 1: #correspodning to the slow car
            self.x = 190
            self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct blue slow car.png')
            self.vel = -4   #making velocity slower and puts the car facing in a different direction

        else:   #if the number==2
            self.x = 460
            self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\\red fast car.png')
            self.vel = 5    #making car faster

        self.y = HEIGHT / 2 #starting both cars off in middle of the screen
        self.width = 100
        self.height = 150
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  #resizing image
        self.rect = self.image.get_rect()   #getting a rectangle to move image around
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.move() #calling movement
        self.rect.center = (self.x, self.y)

    def move(self):
        self.y += self.vel
        #making sure car doesnt go off the screen
        if self.y - self.height / 2 < 0:
            self.y = self.height / 2
            self.vel *= -1  #making the cars go up or down

        elif self.y + self.height / 2 > HEIGHT:
            self.y = HEIGHT - self.height / 2
            self.vel *= -1  #determines direction of car


class Screen(pygame.sprite.Sprite): #creating class screen
    def __init__(self):
        super().__init__()
        #setting up images
        self.img1 = pygame.image.load('pygameFiles\images\Pygame Crossy Road\\road background.jpg') #background
        self.img2 = pygame.image.load('pygameFiles\images\Pygame Crossy Road\You Win.png')  #you win screen
        self.img3 = pygame.image.load('pygameFiles\images\Pygame Crossy Road\You lose.png') #you lose screen

        self.img1 = pygame.transform.scale(self.img1, (WIDTH, HEIGHT))
        self.img2 = pygame.transform.scale(self.img2, (WIDTH, HEIGHT))
        self.img3 = pygame.transform.scale(self.img3, (WIDTH, HEIGHT))

        self.image = self.img1
        #starting background at top left corner of the screen:
        self.x = 0
        self.y = 0

        self.rect = self.image.get_rect()   #to move sprite around

    def update(self):
        self.rect.topleft = (self.x, self.y)    #top left corner


class Flag(pygame.sprite.Sprite):   #creating flag class
    def __init__(self, number): 
        super().__init__()
        self.number = number    #setting up attribute

        if self.number == 1:    #freen flag
            self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\green flag.png')
            self.visible = False    #green flag is hidden until white flag is touched
            self.x = 50     #going to left of screen

        else:   #white flag
            self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\white flag.png')
            self.visible = True
            self.x = 580    #opposite end of screen to the green flag

        self.y = HEIGHT / 2 #centering flags
        self.image = pygame.transform.scale2x(self.image)   #double existing width and height
        self.rect = self.image.get_rect()   #to move them around
        self.mask = pygame.mask.from_surface(self.image)    #masks ensure sure the collisions work for irregular shapes

    def update(self):
        if self.visible:    #checking if sprite is visible
            self.collision()    #calling collision
            self.rect.center = (self.x, self.y)

    def collision(self):
        global SCORE, duck

        flag_hit = pygame.sprite.spritecollide(self, duck_group, False, pygame.sprite.collide_mask) #need 4 perameters
        if flag_hit:    #detect whether flag ahs collided with duck or not
            self.visible = False

            if self.number == 1:    #green flag
                white_flag.visible = True
                if SCORE < 5:   #if the score it less than 5, the flags switch
                    SwitchLevel()   #calling function if score is less than 5

                else:   #white flag
                    duck_group.empty()  #removing duck from group if player won
                    DeleteOtherItems()

                    EndScreen(1)    #end screen for winner

            else:   #showing the opposite flag
                green_flag.visible = True   #setting visisble


class Boom(object): #object for when car and duck hit each other
    def __init__(self):
        self.costume = 1    #represents costume of particular image we use
        self.width = 140
        self.height = 140
        self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct boom image.png')  #uploading explosion when duck hits car
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  #resizing image

    def explode(self, x, y):   
        #two perameters use has to enter in: 
        x = x - self.width / 2  #x coordinate of duck
        y = y - self.height / 2 #y coordinate of duck
        DeleteDuck()    #calling function

        while self.costume < 9: #while loop to make sure costume is under 9
            self.image = pygame.image.load('pygameFiles\images\Pygame Crossy Road\correct boom image.png')  #importing explode image
            self.image = pygame.transform.scale(self.image, (self.width, self.height))  
            screen.blit(self.image, (x, y))
            pygame.display.update()

            self.costume += 1  #making sure annimation works properly 
            time.sleep(0.1) #delaying the time

        DeleteOtherItems()  #calling this function to clear screen
        EndScreen(0)    #calling this function so that after explosion is complete, player has lost


def ScoreDisplay(): #displays score
    global gameOn   #make sure it isnt a local variable

    if gameOn:
        score_text = score_font.render(str(SCORE) + ' / 5', True, ('BLACK'))    #varible to show what level user is on
        screen.blit(score_text, (255, 10))  #making sure that none of this will show if the game or varibale is set to false


def checkFlags():   #checking whetehr to hide or show the flag
    for flag in flags:  
        if not flag.visible:
            flag.kill() #flag removed from specific group

        else:   #making sure flag visislve is not hidden forever
            if not flag.alive():    #checks if flag is part of group
                flag_group.add(flag)    #if it isnt part of group, we add it


def SwitchLevel():  #applies when going up 1 level
    global SCORE

    if slow_car.vel < 0:
        slow_car.vel -= 1

    else:
        slow_car.vel += 1

    if fast_car.vel < 0:
        fast_car.vel -= 1

    else:
        fast_car.vel += 1

    SCORE += 1  #changing score by 1


def DeleteDuck():   #function to delete the duck
    global duck 

    duck.kill() #removing duck object from groups
    screen_group.draw(screen)
    car_group.draw(screen)
    flag_group.draw(screen)

    screen_group.update()
    car_group.update()
    flag_group.update()

    pygame.display.update()


def DeleteOtherItems(): #deleting the other items from the groups, not just the duck
    car_group.empty()
    flag_group.empty()
    flags.clear()   #in case of errors


def EndScreen(number):
    global gameOn

    gameOn = False  
    lose = pygame.image.load('pygameFiles\images\Pygame Crossy Road\you lost screen.png')   #loser screen 
    lose = pygame.transform.scale(lose, (WIDTH,HEIGHT))

    win = pygame.image.load('pygameFiles\images\Pygame Crossy Road\you won gif.gif')   #winner screen
    win = pygame.transform.scale(win, (WIDTH,HEIGHT))

    if number == 0: #if number is 0 they lost
        screen.blit(lose, (0,0))    #blitting screen
        
    elif number == 1:   #if number is 1 they won
        screen.blit(win, (0,0)) #blitting screen
        
    pygame.display.update()
    pygame.time.delay(3000)
    GameOver(number)

def GameOver(num):
    screen.fill((255,255,255))
    if num == 0:
        text = "You lost the Game 😞 Do you want to play again?"
    if num == 1:
        text = "Congradulations, you won the Game 😃🦆!! Do you want to play again"
    
    text = MENU_FONT.render(text, 1, (0,0,0))
    xd = WIDTH//2 - (text.get_width()//2)
    screen.blit(text, (xd, 50))
    #creating buttons
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    pygame.draw.rect(screen, (255,180,0), Button_1)
    pygame.draw.rect(screen, (255,180,0), Button_2)

    text1 = MENU_FONT.render("Yes", 1, (0,0,0)) #yes buttons
    text2 = MENU_FONT.render("No", 1, (0,0,0))  #no button
    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))
    pygame.display.update() 

    date = datetime.datetime.now()
    scoreLn=str(SCORE) +"    " + user_name +"    " +date.strftime("%m/%d/%y") + "\n"    #adds an enter
    myFile = open("scoreFile.txt", "a")
    myFile.write (scoreLn)
    myFile.close()
    while True:
        for event in pygame.event.get():    #if player hits x on screen it leaves program
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()   #position 
                mx = mousePos[0]    
                my = mousePos[1]
                if Button_1.collidepoint(mx, my):
                    crossyRoad()    #if user presses yes it restarts game
                if Button_2.collidepoint(mx, my):   #if user presses no, go back to main menu
                    screen.fill("GREEN") # fills the screen with green
                    goodbye_text = MENU_FONT.render("Thanks for playing", 1, colors.get("BLACK")) # says thank you for playing
                    goodbye_text_X = WIDTH//2 - (goodbye_text.get_width()//2)
                    screen.blit(goodbye_text, (goodbye_text_X, 350))
                    menu()

#Need these varibales here to reference them before crossyRoad() if not there the variables wont be defined for the classes 
bg = Screen()   #background screen
screen_group = pygame.sprite.Group()
screen_group.add(bg)    #adding bg to screen gorup

#duck objects
duck = Duck()
duck_group = pygame.sprite.Group() #to hold both in place
duck_group.add(duck)

#car objects
slow_car = Car(1)
fast_car = Car(2)
car_group = pygame.sprite.Group()
car_group.add(slow_car, fast_car)

green_flag = Flag(1)
white_flag = Flag(2)
flag_group = pygame.sprite.Group()
flag_group.add(green_flag, white_flag)
flags = [green_flag, white_flag]    #creating a list to help hiding and showing flags
boom = Boom()
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
message = ["Instructions", "Setting", "Game 1", "Scoreboard", "Exit"]

backgrnd = (255,255,255)

def input_name():
    global user_name
    # name variable
    user_name = ""

    #rendering text objects

    Title = TITLE_FONT.render("Input your name:", 1, colors.get("MANDARIN_ORANGE"))
    text1 = MENU_FONT.render("(Enter in the pink box)", 1, colors.get("SALMON"))
    user_text = MENU_FONT.render(user_name,1, colors.get("BLACK"))

    #fills screen with white
    screen.fill(colors.get("white"))


    # renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    xb = WIDTH//2 - (text1.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text1, (xb,100))
    # text1_x = WIDTH//2 - (text1.get_width()//2)
    # screen.blit(text1, (text1_x, 350))

    # creats the box for typing
    botton1 = WIDTH//2 - WIDTH//4
    button2 = pygame.Rect(botton1, 400, WIDTH//2, 50)
    pygame.draw.rect(screen, colors.get("DEEP_PINK,"), button2)

    pygame.display.update()
        
    run = True    
    while run:
            for event in pygame.event.get(): #if they exit game ends
                if event.type==pygame.QUIT:
                    print(user_name)
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    mx = mousePos[0] #variables
                    my = mousePos[1]
                    

                if event.type == pygame.KEYDOWN:
                    if event.key ==  pygame.K_RETURN: # Entering the users name 
                        run = False #ends the loop
                        print(user_name) 
                    if event.key == pygame.K_BACKSPACE: # Removing th elast leter o their name by subtracting 1 from the length of the word
                        user_name = user_name[0:len(user_name)-1]
                    elif event.key != pygame.K_RETURN: # Adding the romoved character to the end of the string
                        user_name += event.unicode 

                    pygame.draw.rect(screen, colors.get("DEEP_PINK,"), button2)
                    user_text = MENU_FONT.render(user_name,1, colors.get("BLACK"))
                    screen.blit(user_text, (botton1 + 20, 410))
                    pygame.display.update()       # Must always update the screen

Bx= WIDTH//3
#setting buttons
Button_Color = pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_Background = pygame.Rect(Bx, 200, WIDTH//4, 40)
Button_Sizeincrease= pygame.Rect(Bx, 250, WIDTH//4, 40)
Button_Sizedecrease= pygame.Rect(Bx, 300, WIDTH//4, 40)
buttoncolor= colors.get ("BLACK")

#menu function
def menu():
    Title = TITLE_FONT.render("Crossy Road", 1, colors.get(""))
    screen.fill(backgrnd)
    ymenu = 155
    xd = WIDTH//2 - (Title.get_width()//2) #centering title
    screen.blit(Title, (xd, 75))
    #setting where the buttons will be displayed on the screen
    Button_Instructions = pygame.Rect(30, 145, 150, 50) 
    Button_Settings = pygame.Rect(30, 195, 150, 50)
    Button_Game_1 = pygame.Rect(30, 245, 150, 50)
    Button_Score = pygame.Rect(30, 295, 150, 50)
    Button_Exit = pygame.Rect(30, 345, 150, 50)
    #drawing the buttons
    pygame.draw.rect(screen, buttoncolor, Button_Instructions)
    pygame.draw.rect(screen, buttoncolor, Button_Settings)
    pygame.draw.rect(screen, buttoncolor, Button_Game_1)
    pygame.draw.rect(screen, buttoncolor, Button_Score)
    pygame.draw.rect(screen, buttoncolor, Button_Exit)

    for item in message: #for the words in the buttons
        text = MENU_FONT.render(item, 1, colors.get('DARK_VIOLET'))
        screen.blit(text, (40, ymenu))
        pygame.display.update()
        pygame.time.delay(50) #very short delay
        ymenu += 50
    
    while True: #loop for buttons
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False #making run = false to end the game
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]    #variables
                my = mousePos[1]
                if Button_Instructions.collidepoint((mx, my)): #if user presses instructions it displays instructions txt
                    Instructions("Instructions" , "pygameFiles\instructions.txt")
                if Button_Settings.collidepoint((mx, my)):
                    settings () #calling settings function
                if Button_Game_1.collidepoint((mx, my)):
                    crossyRoad () #calling game function
                if Button_Score.collidepoint((mx, my)):
                    Instructions ("Highscores", "pygameFiles\images\Pygame Crossy Road\scoreFile.txt") #showing the score txt
                if Button_Exit.collidepoint((mx, my)):
                    pygame.quit () #to leave the program
                    sys.exit ()
                    

def Instructions(TITLE, FILE):
    #rendering text objects
    Title = TITLE_FONT.render(TITLE, 1, colors.get("blue"))
    
    #fills screen with white
    screen.fill(backgrnd)

    #Instructions
    myFile = open(FILE, "r")    #reading lines
    content = myFile.readlines()

    #variable to control change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu ()
        
                      
def settings ():    #settings funtion
    global WIDTH, HEIGHT, backgrnd, screen, buttoncolor #setting global so they apply to all
    Title = TITLE_FONT.render("Crossy Road", 1, colors.get("MINT_CREAM"))
    screen.fill(backgrnd)
    ymenu = 155
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 100))
    
    Bx= WIDTH//3
    #setting buttons
    Button_Color = pygame.Rect(Bx, 150, WIDTH//4, 40)
    Button_Background = pygame.Rect(Bx, 200, WIDTH//4, 40)
    Button_Sizeincrease= pygame.Rect(Bx, 250, WIDTH//4, 40)
    Button_Sizedecrease= pygame.Rect(Bx, 300, WIDTH//4, 40)
    
    #drawinf the settings buttons
    pygame.draw.rect(screen, buttoncolor, Button_Color)
    pygame.draw.rect(screen, buttoncolor, Button_Background)
    pygame.draw.rect(screen, buttoncolor, Button_Sizeincrease)
    pygame.draw.rect(screen, buttoncolor, Button_Sizedecrease)
    
    #variables for the different settings
    color = MENU_FONT.render("Randomize button color", 1, colors.get("blue"))
    bgcolor = MENU_FONT.render("Randomize background color", 1, colors.get("blue"))
    sizeincrease = MENU_FONT.render("Increase screen size",1, colors.get ("blue"))
    sizedecrease = MENU_FONT.render("Decrease screen size",1, colors.get ("blue"))

    screen.blit(color, (WIDTH//2 - (color.get_width()//2), 160))
    screen.blit(bgcolor, (WIDTH//2 - (bgcolor.get_width()//2), 210))
    screen.blit(sizeincrease, (WIDTH//2 - (sizeincrease.get_width()//2), 260))
    screen.blit(sizedecrease, (WIDTH//2 - (sizedecrease.get_width()//2), 310))

    while True: #start loop in settings 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu ()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                mx=mousepos[0]
                my=mousepos[1]
                if Button_Color.collidepoint(mx,my):
                    buttoncolor=(random.randint(0,255),random.randint(0,255), random.randint(0,255)) #changes color                   
                if Button_Background.collidepoint(mx,my):
                    backgrnd=(random.randint(0,255),random.randint(0,255), random.randint(0,255))   #changes background color
                if Button_Sizeincrease.collidepoint(mx, my):
                    WIDTH+=100  #increasing size by 100 
                    screen= pygame.display.set_mode((WIDTH,HEIGHT))
                if Button_Sizedecrease.collidepoint(mx, my) and WIDTH >500:
                    WIDTH -=100 #decreases size by 100
                    screen= pygame.display.set_mode((WIDTH,HEIGHT))
            pygame.display.update()
            settings()  #calling function
                
                
def crossyRoad ():  #calling game function
    global flags, boom, gameOn, bg, screen_group, duck, duck_group, slow_car, fast_car, car_group, green_flag, white_flag, flag_group, flags, boom    #making all variables global so they apply everywhere
    gameOn = True   #control whether the player has finished the game or if it still going on
    bg = Screen()   #background screen
    screen_group = pygame.sprite.Group()
    screen_group.add(bg)    #adding bg to screen gorup

    #duck objects
    duck = Duck()
    duck_group = pygame.sprite.Group() #to hold both in place
    duck_group.add(duck)

    #car objects
    slow_car = Car(1)
    fast_car = Car(2)
    car_group = pygame.sprite.Group()
    car_group.add(slow_car, fast_car)

    green_flag = Flag(1)
    white_flag = Flag(2)
    flag_group = pygame.sprite.Group()
    flag_group.add(green_flag, white_flag)
    flags = [green_flag, white_flag]    #creating a list to help hiding and showing flags

    boom = Boom()
    

    #MAIN LOOP
    run = True 
    while run:
        clock.tick(60)  #entering a framerate of 60 frames per second 
        for event in pygame.event.get():    #when player wanst to close window the game ends
            if event.type == pygame.QUIT:
                run = False     #exiting main loop
        # screen.fill(0,225,0) #filling screen with green background
        screen_group.draw(screen)
        #calling fucntions
        ScoreDisplay()
        checkFlags()

        car_group.draw(screen)
        duck_group.draw(screen)
        flag_group.draw(screen)
        #need these to be constantly updating 
        car_group.update()
        duck_group.update()
        flag_group.update()

        screen_group.update()

        pygame.display.update() #updating screen so user can see changes added
input_name()
menu()


