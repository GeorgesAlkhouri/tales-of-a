# Discord RPG Bot

This Discord bot provides a simple tile-based RPG game that can be played within a Discord server. Players can move their hero on a 10x10 grid, exploring different terrains and managing their health, energy and inventory.

## Prerequisites

- Python 3.8+
- `pip` (Python package manager)
- A Discord account with a registered bot

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/discord-rpg-bot.git
cd discord-rpg-bot
```

Replace `yourusername` with your actual GitHub username and the repository URL.

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project directory with the following content:

```
TOKEN=your_bot_token_here
PREFIX=>
```

Replace `your_bot_token_here` with your actual Discord bot token.

5. Run the bot:

```bash
python bot.py
```

The bot should now be running and connected to your Discord server. Use the `>` prefix (or any other prefix you've set in the `.env` file) to issue commands.

## Commands

- `>startgame`: Starts a new game.
- `>move [direction]`: Moves the hero in the specified direction (up, down, left, or right).
- `>inventory`: Displays the hero's inventory
- `>map`: Responds with the current map state without moving the hero
- `>version`: Get the current version of the bot

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

[MIT License](LICENSE)
