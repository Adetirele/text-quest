# src/main.py
import sys
import pygame

# ------------------ Config ------------------
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60

LEFT_TEXT_X = 28          # left padding for text
LEFT_TEXT_Y = 40          # top padding for text
LEFT_TEXT_MAX_WIDTH = 380 # keep text on left half (avoid right-side art)

INTRO_IMAGE_PATH = "src/assets/TQ_intro.png"
TEACH_IMAGE_PATH = "src/assets/TQ_teach.png"
END_IMAGE_PATH   = "src/assets/TQ_end.png"
QUEST_FONT_PATH  = "src/assets/quest_font.ttf"

TEXT_COLOR = (0, 0, 0)      # black text
FEEDBACK_GOOD = (40, 150, 60)
FEEDBACK_BAD = (180, 40, 40)