from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

import os

TOKEN = os.getenv("BOT_TOKEN")

async def group_listener(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    text = update.message.text

    if "کیر" in text:
        await update.message.reply_text("کیر رضا پهلوی 💦💦💦")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            group_listener
        )
    )

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()