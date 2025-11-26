import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
TOKEN = os.getenv('DISCORD_TOKEN', 'your_token_here')
PREFIX = os.getenv('PREFIX', '!')
OWNER_ID = int(os.getenv('OWNER_ID', '0'))
DEBUG_GUILD = int(os.getenv('DEBUG_GUILD', '0'))

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot.db')

# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', '')

# Bot Settings
COLOR_SUCCESS = 0x2ecc71
COLOR_ERROR = 0xe74c3c
COLOR_INFO = 0x3498db
COLOR_WARNING = 0xf39c12

# Command Settings
COMMAND_TIMEOUT = 60
MAX_EMBED_FIELDS = 25
