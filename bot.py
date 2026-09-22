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

    if "کیر" in text or "kir" in text:
        await update.message.reply_text("کیر رضا پهلوی 💦💦💦")
    elif "کص" in text or "kos" in text:
        await update.message.reply_text("کص رضا پهلوی 🤓")
    elif "کونی" in text or "koni" in text:
        await update.message.reply_text("جوووون کی اینجا کونیه؟؟؟؟ 🤗")
    elif "مندل" in text or "mendel" in text:
        await update.message.reply_text("بر مندل گویان صلوات🙃")


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
