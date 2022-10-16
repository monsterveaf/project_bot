import telegram as tg
import telegram.ext as tge


updater = tge.Updater(token='5780766591:AAFyzLIU3DGshE5kHsOYJro5O3Je-yF09Fg')
dispatcher = updater.dispatcher


def start(update: tg.Update, context: tge.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I can tell the weather today. "
                                                                    "Please, send me your location bistro blyat!")


start_handler = tge.CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

