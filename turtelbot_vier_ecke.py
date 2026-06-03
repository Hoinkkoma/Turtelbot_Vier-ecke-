"""
TurtleBot Vier-Ecke - Square Movement Controller
Steuert einen TurtleBot Burger 3, um ein Quadrat von 1m x 1m abzufahren
"""

import turtle
import time

class TurtleBotSquare:
    """Klasse zum Steuern des Robots in einer quadratischen Bewegung"""
    
    def __init__(self, side_length=100, speed=50):
        """
        Initialisiert den TurtleBot
        
        Args:
            side_length (int): Seitenlänge des Quadrats in Pixeln (default: 100 = ~1m)
            speed (int): Bewegungsgeschwindigkeit (0-10, default: 5)
        """
        self.turtle = turtle.Turtle()
        self.turtle.speed(speed)
        self.side_length = side_length
        
    def draw_square(self):
        """Zeichnet ein Quadrat (Vier-Ecke)"""
        for _ in range(4):
            self.turtle.forward(self.side_length)
            self.turtle.right(90)
            
    def draw_multiple_squares(self, count=1):
        """
        Zeichnet mehrere Quadrate übereinander
        
        Args:
            count (int): Anzahl der Quadrate
        """
        for _ in range(count):
            self.draw_square()
            time.sleep(0.5)  # Pause zwischen den Quadraten
            
    def move_and_return(self):
        """Bewegt den Robot in einem Quadrat und kehrt zum Startpunkt zurück"""
        self.draw_square()
        
    def close(self):
        """Beendet die Turtle-Grafik"""
        turtle.done()


def main():
    """Hauptfunktion zum Ausführen des Programms"""
    print("TurtleBot Vier-Ecke wird gestartet...")
    
    # Konfiguration
    SIDE_LENGTH = 100  # ~1 Meter
    SPEED = 5
    
    # Robot initialisieren
    robot = TurtleBotSquare(side_length=SIDE_LENGTH, speed=SPEED)
    
    print(f"Robot fährt Quadrat ab: {SIDE_LENGTH}px x {SIDE_LENGTH}px")
    
    # Quadrat abfahren
    robot.draw_square()
    
    print("Quadrat abgefahren! Fenster schließen zum Beenden.")
    robot.close()


if __name__ == "__main__":
    main()
