from keyboard import is_pressed
from detecto import core,visualize
core.FastRCNNPredictor()
import cv2

model = core.Model()
visualize.detect_live(model,score_filter=0.6)

