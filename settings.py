# GAME OPTIONS/SETTINGS

# constants for our window
TITLE = "Jumpy!"
WIDTH =  480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "hightscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 20
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POWERUP_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# game properties
BOOST_POWER = 60
POWERUP_SPAWN_PCT = 7
MOB_FREQUENCY = 5000

# Starting Platforms
PLATFORM_LIST = [(0, HEIGHT - 60),
				 (WIDTH / 2 - 50, HEIGHT * 3 / 4),
				 (125, HEIGHT - 350),
				 (350, 200),
				 (175, 100)]

# defining some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE