# Pinterest Image Bot 🖼️

Ein Discord Bot, der Bilder von Pinterest sucht und herunterlädt. Der Bot nutzt Web-Scraping, um Bilder basierend auf Suchbegriffen zu finden und direkt in Discord-Kanäle zu senden.

## ✨ Features

- 🔍 **Bildsuche**: Suche nach Bildern auf Pinterest mit Stichwörtern
- 📥 **Automatischer Download**: Lädt bis zu 10 Bilder gleichzeitig herunter
- ⏰ **Cooldown-System**: Konfigurierbarer Cooldown zwischen Anfragen (Standard: 30 Sekunden)
- 🎨 **Anpassbare Embeds**: Konfigurierbare Farben für Bot-Nachrichten
- 🧹 **Automatische Bereinigung**: Temporäre Dateien werden automatisch gelöscht
- 🛡️ **Fehlerbehandlung**: Robuste Behandlung von Netzwerk- und Dateifehlern

## 🛠️ Verwendete Technologien

- **Python 3.8+**
- **discord.py** - Discord Bot Framework
- **pinscrape** - Pinterest Web-Scraping Library
- **python-dotenv** - Umgebungsvariablen Management

## 📋 Voraussetzungen

- Python 3.8 oder höher
- Discord Bot Token
- Internetverbindung

## 🚀 Installation

### 1. Repository klonen
```bash
git clone https://github.com/yourusername/pinterest-discord-bot.git
cd pinterest-discord-bot
```

### 2. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 3. Umgebungsvariablen konfigurieren
Erstelle eine `.env` Datei im Projektverzeichnis:

```env
BOT_TOKEN=dein_discord_bot_token_hier
EMBED_COLOR=0xe0dade
COOLDOWN_DURATION=30
DEFAULT_SLEEP_TIME=1
MAX_WORKERS=5
MAX_IMAGES_PER_REQUEST=10
```

### 4. Discord Bot erstellen

1. Gehe zu [Discord Developer Portal](https://discord.com/developers/applications)
2. Erstelle eine neue Application
3. Gehe zu "Bot" und erstelle einen Bot
4. Kopiere den Bot Token in deine `.env` Datei
5. Aktiviere "Message Content Intent" unter "Privileged Gateway Intents"

### 5. Bot zu Server einladen

Generiere einen Einladungslink mit folgenden Berechtigungen:
- `Send Messages`
- `Attach Files`
- `Use Slash Commands`
- `Embed Links`

## 🎮 Verwendung

### Bot starten
```bash
python bot.py
```

### Slash Commands

#### `/pull`
Sucht und lädt Bilder von Pinterest herunter.

**Parameter:**
- `keyword` (erforderlich): Suchbegriff für die Bildsuche
- `amount` (optional): Anzahl der Bilder (1-10, Standard: 5)
- `ephemeral` (optional): Ob die Antwort nur für dich sichtbar ist (Standard: False)

**Beispiele:**
```
/pull keyword:cats amount:5
/pull keyword:nature amount:3 ephemeral:True
/pull keyword:cars
```

## ⚙️ Konfiguration

### Umgebungsvariablen

| Variable | Beschreibung | Standard | Beispiel |
|----------|--------------|----------|----------|
| `BOT_TOKEN` | Discord Bot Token | - | `MTQ0NzI2...` |
| `EMBED_COLOR` | Farbe der Bot Embeds (Hex) | `0x323337` | `0xe0dade` |
| `COOLDOWN_DURATION` | Cooldown zwischen Anfragen (Sekunden) | `30` | `60` |
| `DEFAULT_SLEEP_TIME` | Wartezeit zwischen Downloads | `1` | `2` |
| `MAX_WORKERS` | Maximale Download-Threads | `5` | `3` |
| `MAX_IMAGES_PER_REQUEST` | Maximale Bilder pro Anfrage | `10` | `8` |

### Cooldown anpassen
```env
COOLDOWN_DURATION=60  # 1 Minute Cooldown
COOLDOWN_DURATION=120 # 2 Minuten Cooldown
```

### Embed-Farbe ändern
```env
EMBED_COLOR=0xff0000  # Rot
EMBED_COLOR=0x00ff00  # Grün
EMBED_COLOR=0x0099ff  # Blau
```

## 🔧 Troubleshooting

### Häufige Probleme

**Bot reagiert nicht auf Slash Commands:**
- Überprüfe, ob der Bot die richtigen Berechtigungen hat
- Stelle sicher, dass "Message Content Intent" aktiviert ist
- Warte bis zu 1 Stunde nach Änderungen an Slash Commands

**"Database Error" Meldungen:**
- Überprüfe deine Internetverbindung
- Versuche andere Suchbegriffe
- Pinterest könnte temporär nicht verfügbar sein

**Dateien können nicht gelöscht werden:**
- Der Bot bereinigt Dateien automatisch beim nächsten Start
- Stelle sicher, dass keine anderen Programme die Dateien verwenden

**UTF-8 Dekodierungsfehler:**
- Der Bot behandelt diese automatisch und überspringt problematische Dateien
- Versuche andere Suchbegriffe

### Logs überprüfen
Der Bot gibt detaillierte Logs in der Konsole aus:
```
nyxify dev#8447 is online!
Cleaned up folder: temp_123456789
Error in pull command: [Fehlerdetails]
```

## 📁 Projektstruktur

```
pinterest-discord-bot/
├── bot.py              # Haupt-Bot Code
├── requirements.txt    # Python Abhängigkeiten
├── .env               # Umgebungsvariablen (nicht in Git)
├── .gitignore         # Git Ignore Datei
├── data/              # Datenordner
│   └── time_epoch.json
└── temp_*/            # Temporäre Download-Ordner (automatisch bereinigt)
```

## 🤝 Beitragen

1. Fork das Repository
2. Erstelle einen Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Committe deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

## 📝 Lizenz

Dieses Projekt steht unter der MIT Lizenz. Siehe `LICENSE` Datei für Details.

## ⚠️ Haftungsausschluss

Dieser Bot ist nur für Bildungszwecke gedacht. Stelle sicher, dass du die Nutzungsbedingungen von Pinterest und Discord einhältst. Der Bot-Betreiber ist nicht verantwortlich für Missbrauch oder Verstöße gegen Plattform-Richtlinien.

## 🔗 Links

- [Discord.py Dokumentation](https://discordpy.readthedocs.io/)
- [Pinterest API](https://developers.pinterest.com/)
- [Discord Developer Portal](https://discord.com/developers/applications)

## 📞 Support

Bei Problemen oder Fragen:
1. Überprüfe die Troubleshooting Sektion
2. Öffne ein Issue auf GitHub
3. Kontaktiere den Entwickler

---

**Made with ❤️ for the Discord Community**
