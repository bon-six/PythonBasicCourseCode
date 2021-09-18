


####################################################################
# internal communicate event data structure
# [event_type, event_value]
####################################################################

FPS = 60
SCREEN_WIDTH = 600
SCREEN_HEIGHT=900
BLOCK_SIZE = 40
GAME_ONE_STEP_COUNTS = 30

I_EVENT_SOUND = 1
MUSIC_ON = 1
MUSIC_OFF = 2
SOUND_BLOCK_DOWN = 4
SOUND_BLOCK_REMOVE = 8

I_EVENT_GAMESTART = 2
I_EVENT_GAMEPAUSE = 4
I_EVENT_GAMESTOP = 8
I_EVENT_GAMEOVER = 16
I_EVENT_EXIT = 32

class event_queue():
    def __init__(self):
        self.internal_events =[]

    def get(self):
        events = self.internal_events
        self.internal_events = []
        return events

    def add(self,event):
        self.internal_events.append(event)


color_white = (255,255,255)
color_black = (0,0,0)
color_red = (255,0,0)
color_green = (0,255,255)
color_blue = (0,0,255)
color_grey = (128,128,128)
color_silver = (192,192,192)
color_cyan = (0,255,255)
color_yellow = (255,255,0)
color_fuchsia = (255,0,255)
color_purple = (128,0,128)
color_pink = (255,192,203)
color_brown = (165,42,42)
color_orange = (255,165,0)


def init():
    global i_queue
    i_queue = event_queue()
    global game_state
    game_state = 'menu'
    global game_level
    game_level = 0
    global game_score
    game_score = 0
