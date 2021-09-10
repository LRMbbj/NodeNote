from PyQt5.QtWidgets import QGraphicsItem
from Components import attribute


__all__ = ["DEBUG_DRAW_PIPE", "DEBUG_EFFECT_SNOW", "DEBUG_VIEW_CHANGE_SCALE", "DEBUG_TUPLE_NODE_SCALE",
           "DEBUG_CUT_LINE", "DEBUG_HISTORY", "DEBUG_FONT",
           "Z_VAL_PORT", "Z_VAL_NODE", "Z_VAL_PIPE", "Z_VAL_CUTLINE", "Z_VAL_PIPE_DONE",
           "NODE_HEIGHT", "NODE_WIDTH", "NODE_LAYOUT_MARGINS", "NODE_SEL_BORDER_COLOR", "NODE_SEL_COLOR",
           "NODE_ICON_SIZE",
           "ITEM_CACHE_MODE",
           "INPUT_NODE_TYPE", "OUTPUT_NODE_TYPE",
           "MODE_PIPE_DRAG", "MODE_NOOP", "MODE_PIPE_CUT", "MODE_CONTAINER",
           "SCALE_WIDGET",
           "PIPE_STATUS_NEW", "PIPE_STATUS_CHANGE", "PIPE_FIRST", "PIPE_MOVEING", "PIPE_COMMON", "PIPE_UPDATE",
           "INPUT_NODE_START", "OUTPUT_NODE_START",
           "down", "up", "left", "right"]


# === DEBUG ===
DEBUG_EFFECT_SNOW = False
DEBUG_TUPLE_NODE_SCALE = False
DEBUG_VIEW_CHANGE_SCALE = False
DEBUG_DRAW_PIPE = True
DEBUG_TEXT_CHANGED = False
DEBUG_PYTHON_SYNTAXHIGHTLIGHTER = False
DEBUG_RICHTEXT = False
DEBUG_CUT_LINE = False
DEBUG_COLLIDING = False
DEBUG_HISTORY = False
DEBUG_DESERIALIZE = False
DEBUG_FONT = True

# === DRAW STACK ORDER ===
Z_VAL_PIPE = 2
Z_VAL_PIPE_DONE = 4
Z_VAL_NODE = 3
Z_VAL_PORT = 3
Z_VAL_CUTLINE = 5
Z_VAL_CONTAINERS = 6

# === NODE ===
NODE_WIDTH = 150
NODE_HEIGHT = 70
NODE_LAYOUT_MARGINS = 5
NODE_ICON_SIZE = 24
NODE_SEL_COLOR = (255, 255, 255, 30)
NODE_SEL_BORDER_COLOR = (254, 207, 42, 255)

# === ITEM CACHE MODE ===
ITEM_CACHE_MODE = QGraphicsItem.DeviceCoordinateCache

# === NODE TYPE ===
INPUT_NODE_TYPE = 0
OUTPUT_NODE_TYPE = 1

# === DRAW LINE ===
MODE_NOOP = 1
MODE_PIPE_DRAG = 2
MODE_PIPE_CUT = 3
MODE_CONTAINER = 4

# === WIDGET ===
SCALE_WIDGET = (attribute.LogicWidget,)

# === PIPE ===
PIPE_STATUS_NEW = 0
PIPE_STATUS_CHANGE = 1

# === PIPE START STATUS ===
INPUT_NODE_START = 0
OUTPUT_NODE_START = 1

# === COLLIDING ===
COLLIDING_ATTRIBUTE = 0
COLLIDING_PIPE = 1

# === PIPE MOVE ===
PIPE_FIRST = 0
PIPE_MOVEING = 1
PIPE_COMMON = 2
PIPE_UPDATE = 3

# === MOVE ===
down = 0
up = 1
left = 2
right = 3
