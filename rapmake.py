import tkinter as tk
import customtkinter as ctk
import os 
import torch
import torchaudio 
from transformers import AutoModelForCausalLM, AutoTokenizer
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice 
import vlc 
from tkVideoPlayer import TkinterVideo
