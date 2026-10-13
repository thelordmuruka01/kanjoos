import asyncio
import os
import threading
from flask import Flask
from pyrogram import Client, idle
from modules.clientbot import run as run_client
import modules.config as config 

# 1. Flask setup with multi-method support for Render health checks
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def health_check():
    return "Bot is alive!", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    # host='0.0.0.0' is mandatory for Render/Koyeb/Heroku
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

# 2. Pyrogram Client setup
bot = Client(
    "kanjoos_bot", # Changed from ":memory:" to a string
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

async def main():
    try:
        threading.Thread(target=run_flask, daemon=True).start()
        print("Flask Health Check started!")

        await asyncio.sleep(1)

        await config.get_session()
        print("Aiohttp session initialized!")

        try:
            await bot.start()
        except Exception as e:
            if "[16]" in str(e) or "msg_id too low" in str(e).lower():
                print("Time sync error detected. Waiting 5 seconds to retry...")
                await asyncio.sleep(5)
                await bot.start()
            else:
                raise

        print("Bot is online!")

        await run_client()
        print("ClientBot logic running!")

        await idle()

    except Exception:
        import traceback
        print("CRITICAL ERROR during startup:")
        traceback.print_exc()
        raise

    finally:
        if hasattr(config, "aiohttpsession") and config.aiohttpsession:
            await config.aiohttpsession.close()
            print("Aiohttp session closed.")

        if bot.is_connected:
            await bot.stop()
            print("Bot disconnected gracefully.")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    finally:
        try:
            pending = asyncio.all_tasks(loop)
            if pending:
                loop.run_until_complete(
                    asyncio.gather(*pending, return_exceptions=True)
                )
        except Exception:
            pass

        try:
            loop.close()
            print("Loop closed.")
        except Exception:
            pass
