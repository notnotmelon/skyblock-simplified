import os
import bot

if not os.environ.get('DISCORD_TOKEN'):
    import dotenv
    dotenv.load_dotenv()

client = bot.Bot()
client.run(os.getenv('DISCORD_TOKEN'))
