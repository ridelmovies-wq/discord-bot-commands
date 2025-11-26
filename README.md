# Discord Bot - 50+ Commands

A comprehensive Discord bot with 50+ commands built using discord.py.

## Features

- **Moderation Commands** (10): kick, ban, unban, mute, unmute, warn, clear, slowmode, lock, unlock
- **Utility Commands** (8): help, userinfo, serverinfo, avatar, invite, latency, uptime, membercount  
- **Fun Commands** (10): roll, coinflip, joke, 8ball, choose, rps, reverse, ascii, hug, slap
- **Admin Commands** (12): setprefix, reload, load, unload, shutdown, restart, announce, broadcast, setstatus, eval, guildconfig
- **Info Commands** (11): about, version, credits, roleinfo, channelinfo, time, ping, stats, source, perms, prefix

**Total: 51 Commands**

## Installation

1. Clone the repository
```bash
git clone https://github.com/ridelmovies-wq/discord-bot-commands
cd discord-bot-commands
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up configuration
- Create a `.env` file
- Add your Discord bot token: `DISCORD_TOKEN=your_token_here`
- Add prefix: `PREFIX=!`

4. Run the bot
```bash
python main.py
```

## Project Structure

```
discord-bot-commands/
├── main.py           # Main bot file
├── config.py         # Configuration file
├── requirements.txt  # Dependencies
├── cogs/            # Command modules
│   ├── __init__.py
│   ├── moderation.py
│   ├── utility.py
│   ├── fun.py
│   ├── admin.py
│   └── info.py
└── README.md
```

## Requirements

- Python 3.8+
- discord.py 2.3.2
- python-dotenv 1.0.0

## License

MIT License
