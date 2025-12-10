# Pinterest Image Bot 🖼️

A Discord bot that searches and downloads images from Pinterest using web scraping. The bot finds images based on keywords and sends them directly to Discord channels.

## ✨ Features

- 🔍 **Image Search**: Search for images on Pinterest using keywords
- 📥 **Automatic Download**: Downloads up to 10 images simultaneously
- ⏰ **Cooldown System**: Configurable cooldown between requests (default: 30 seconds)
- 🎨 **Customizable Embeds**: Configurable colors for bot messages
- 🧹 **Automatic Cleanup**: Temporary files are automatically deleted
- 🛡️ **Error Handling**: Robust handling of network and file errors

## 🛠️ Technologies Used

- **Python 3.8+**
- **discord.py** - Discord Bot Framework
- **pinscrape** - Pinterest Web-Scraping Library
- **python-dotenv** - Environment Variables Management

## 📋 Prerequisites

- Python 3.8 or higher
- Discord Bot Token
- Internet connection

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/pinterest-discord-bot.git
cd pinterest-discord-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project directory:

```env
BOT_TOKEN=your_discord_bot_token_here
EMBED_COLOR=0xe0dade
COOLDOWN_DURATION=30
DEFAULT_SLEEP_TIME=1
MAX_WORKERS=5
MAX_IMAGES_PER_REQUEST=10
```

### 4. Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new Application
3. Go to "Bot" and create a Bot
4. Copy the Bot Token to your `.env` file
5. Enable "Message Content Intent" under "Privileged Gateway Intents"

### 5. Invite Bot to Server

Generate an invitation link with the following permissions:
- `Send Messages`
- `Attach Files`
- `Use Slash Commands`
- `Embed Links`

## 🎮 Usage

### Start the Bot
```bash
python bot.py
```

### Slash Commands

#### `/pull`
Searches and downloads images from Pinterest.

**Parameters:**
- `keyword` (required): Search term for image search
- `amount` (optional): Number of images (1-10, default: 5)
- `ephemeral` (optional): Whether the response is only visible to you (default: False)

**Examples:**
```
/pull keyword:cats amount:5
/pull keyword:nature amount:3 ephemeral:True
/pull keyword:cars
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `BOT_TOKEN` | Discord Bot Token | - | `MTQ0NzI2...` |
| `EMBED_COLOR` | Bot Embed Color (Hex) | `0x323337` | `0xe0dade` |
| `COOLDOWN_DURATION` | Cooldown between requests (seconds) | `30` | `60` |
| `DEFAULT_SLEEP_TIME` | Wait time between downloads | `1` | `2` |
| `MAX_WORKERS` | Maximum download threads | `5` | `3` |
| `MAX_IMAGES_PER_REQUEST` | Maximum images per request | `10` | `8` |

### Adjust Cooldown
```env
COOLDOWN_DURATION=60  # 1 minute cooldown
COOLDOWN_DURATION=120 # 2 minutes cooldown
```

### Change Embed Color
```env
EMBED_COLOR=0xff0000  # Red
EMBED_COLOR=0x00ff00  # Green
EMBED_COLOR=0x0099ff  # Blue
```

## 🔧 Troubleshooting

### Common Issues

**Bot doesn't respond to Slash Commands:**
- Check if the bot has the correct permissions
- Make sure "Message Content Intent" is enabled
- Wait up to 1 hour after making changes to Slash Commands

**"Database Error" messages:**
- Check your internet connection
- Try different search terms
- Pinterest might be temporarily unavailable

**Files cannot be deleted:**
- The bot automatically cleans up files on next startup
- Make sure no other programs are using the files

**UTF-8 decoding errors:**
- The bot handles these automatically and skips problematic files
- Try different search terms

### Check Logs
The bot outputs detailed logs to the console:
```
nyxify dev#8447 is online!
Cleaned up folder: temp_123456789
Error in pull command: [Error details]
```

## 📁 Project Structure

```
pinterest-discord-bot/
├── bot.py              # Main bot code
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not in Git)
├── .gitignore         # Git ignore file
├── data/              # Data folder
│   └── time_epoch.json
└── temp_*/            # Temporary download folders (auto-cleaned)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See `LICENSE` file for details.

## ⚠️ Disclaimer

This bot is intended for educational purposes only. Make sure to comply with Pinterest's and Discord's terms of service. The bot operator is not responsible for misuse or violations of platform policies.

## 🔗 Links

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Pinscrape Library](https://github.com/iamatulsingh/pinscrape)
- [Discord Developer Portal](https://discord.com/developers/applications)

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Open an issue on GitHub
3. Contact me

---

**Made with ❤️ for the Discord Community**
