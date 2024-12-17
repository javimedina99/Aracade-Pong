import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class pong_movement(ABC):
    @abstractmethod
    def movement():
        pass

class up(pong_movement):
    def movement():
        pass #movimiento del pong arriba

class down(pong_movement):
    def movement():
        pass #movimiento del pong hacia abajo

class game():
    pass #definir la funcionalidad del juego

class app():
    pass #definir la interfaz grafica del juego