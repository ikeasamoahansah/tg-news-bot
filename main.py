from telegram.ext import Updater, CommandHandler, Application, ContextTypes
from telegram import Update
import config
from scrape import Scrape
        
response = Scrape().zip_soup(link='https://news.ycombinator.com')
    
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, this bot was made with love by User: @Afrocomb ")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
            """
            /start -> Welcome to the channel
            /help -> This is the help center
            /get_news -> Get todays readings
            """
        )

async def get_news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for res in response:
        await update.message.reply_text(res)
        


if __name__ == "__main__":
    print('Application Starting....3...2...1...')

    #Token
    token = config.api_key

    #Start app
    app = Application.builder().token(token=token).build()

    #Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('get_news', get_news))

    #Start the polling
    app.run_polling()
