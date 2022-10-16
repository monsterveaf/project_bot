import telegram as tg
import telegram.ext as tge

# Create a connection with bot
updater = tge.Updater(token='5780766591:AAFyzLIU3DGshE5kHsOYJro5O3Je-yF09Fg')
dispatcher = updater.dispatcher


def start(update: tg.Update, context: tge.CallbackContext):

    """ Send message, when the bot is started
        or received a /start command"""

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello, {update.effective_chat.first_name} "
                                                                    "I can tell the weather today. "
                                                                    "Please, send me the ciy. "  
                                                                    "Bistro nahui blyat!")


def weather(update: tg.Update, context: tge.CallbackContext):

    """ Receive location and sends weather """

    location = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=location)


if __name__ == '__main__':

    # Create a tracker for start command with welcome speech
    start_handler = tge.CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Create a tracker for messages with weather function
    message_handler = tge.MessageHandler(tge.Filters.text, weather)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()

