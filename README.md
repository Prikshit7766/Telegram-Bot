# Telegram Bot

This is a Telegram bot 

## Installation

### Prerequisites

- Python 3.10
- Conda (optional but recommended)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Prikshit7766/Telegram-Bot.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Telegram-Bot
   ```

3. **Create a new Conda environment:**
   ```bash
   conda create --name <env_name> python=3.10
   ```

4. **Activate the Conda environment:**
   ```bash
   conda activate <env_name>
   ```

5. **Install dependencies from `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root directory.
2. Add the required environment variables to the `.env` file. Example:
   ```
   HUGGINGFACEHUB_API_TOKEN="your_huggingface_api_token"
   TELEGRAM_TOKEN="your_telegram_bot_token"
   ```

## Usage

Run the bot using the following command:
```bash
python bot.py
```

Once the bot is running, it will listen for messages on your Telegram bot and respond accordingly.

## Features

- `/start`: Start the conversation.
- `/clear`: Clear the previous conversation and context.
- `/help`: Display the help menu.
