import cv2
import mediapipe as mp
import pyautogui

cap= cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils= mp.soloutions.drawing_utils
screen_width, screen_height