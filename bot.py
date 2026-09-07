import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Welcome to CartoonForge AI!\n\n"
        "Turn your ideas and stories into animated cartoon videos. ✨\n\n"
        "Use /create to start creating a video."
    )


async def create(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎭 Great! Send me your cartoon story or video idea.\n\n"
        "Example:\n"
        "A funny little robot gets lost in a magical forest "
        "and meets a talking cat."
    )


async def handle_story(update: Update, context: ContextTypes.DEFAULT_TYPE):
    story = update.message.text

    await update.message.reply_text(
        "📝 Story received!\n\n"
        f"Your idea:\n{story}\n\n"
        "🎬 CartoonForge AI is preparing your cartoon video...\n\n"
        "Video generation will be connected in the next step. 🚀"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 CartoonForge AI Help\n\n"
        "/start - Start the bot\n"
        "/create - Create a cartoon video\n"
        "/help - Show help\n\n"
        "Send me a story or idea to begin."
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not configured.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("create", create))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_story)
    )

    print("CartoonForge AI is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
