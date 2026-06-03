# TurtleBot Vier-Ecke (4-Corners)

## Beschreibung
Dieses Projekt steuert einen physischen **TurtleBot Burger 3** so, dass er eine quadratische Strecke von 1m x 1m abfährt. Der Robot bewegt sich in vier Ecken (Vier-Ecke) und kann bei Bedarf angepasst werden.

## Hardware-Anforderungen
- **TurtleBot Burger 3**
- ROS/ROS2 kompatibles System
- Python 3.x

## Installation

### Voraussetzungen
```bash
pip install turtle
pip install rospy  # Für ROS-Integration
```

### Setup
1. Repository klonen:
```bash
git clone https://github.com/Hoinkkoma/Turtelbot_Vier-ecke-.git
cd Turtelbot_Vier-ecke-
```

2. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

## Verwendung

Starten Sie das Programm:
```bash
python turtelbot_vier_ecke.py
```

## Projektstruktur
```
Turtelbot_Vier-ecke-/
├── README.md
├── requirements.txt
├── turtelbot_vier_ecke.py
└── docs/
    └── anleitung.md
```

## Funktionalität
- Der Robot fährt automatisch ein Quadrat von 1m x 1m ab
- Bewegung in vier Ecken mit präzisen Drehungen
- Anpassbar für unterschiedliche Geschwindigkeiten und Abstände

## Anpassungen
Sie können folgende Parameter ändern:
- **Strecke**: Seitenlänge des Quadrats
- **Geschwindigkeit**: Bewegungsgeschwindigkeit
- **Drehwinkel**: 90° für Rechtecke

## Lizenz
MIT License

## Autor
Hoinkkoma
