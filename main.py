import discord
from discord.ext import commands
import os

# Charger le token depuis les variables d'environnement
TOKEN = os.getenv("https://discord.com/api/webhooks/1342174813929738241/-KRu1ceJFJ0HLU8REAQA8bkvew7d8iQ0vBXUx9ZyOlaRuW0aJV-cLPnj52PmBd-rl2qc")

# Activer les intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Initialisation du bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} est en ligne !")

    channel = bot.get_channel(1341946215226540075)  # Remplace avec l'ID du salon
    if channel:
        await channel.send("🚀 Le bot est bien en ligne et peut envoyer des messages !")
    else:
        print("❌ Erreur : Impossible de récupérer le salon")

@bot.command()
async def test(ctx):
    await ctx.send("✅ Le bot fonctionne !")

# Lancer le bot
bot.run(TOKEN)
