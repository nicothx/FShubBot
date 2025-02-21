from flask import Flask, request, jsonify
import asyncio
from main import bot

app = Flask(__name__)

DISCORD_CHANNEL_ID = 1341946215226540075  # Remplace par ton ID de salon

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data and "pilot.pirep" in data.get("event", ""):
        pirep = data["data"]
        flight_info = (
            f"🛫 **{pirep['departure']}** → 🛬 **{pirep['arrival']}**\n"
            f"✈️ Avion : {pirep['aircraft']}\n"
            f"⏳ Durée de vol : {pirep['duration']}\n"
            f"📜 Rapport : {pirep['comments']}\n"
        )

        loop = asyncio.get_event_loop()
        loop.create_task(send_to_discord(flight_info))

    return jsonify({"status": "success"}), 200

async def send_to_discord(message):
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        await channel.send(message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
