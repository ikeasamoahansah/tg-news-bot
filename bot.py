import telegram.ext
import config


class BotMethods:

    def __init__(self):
        self.token = config.api_key
        self.updater = telegram.ext._updater(self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

    
    def start(self, update, context):
        update.message.reply_text("Hello")

    def help(self, update, context):
        pass