import telegram as tg
import telegram.ext as tge
import requests
import datetime


weather_token = '22d38e4b789796c92e6e4fe65846ff67'


# Create a connection with bot
updater = tge.Updater(token='5780766591:AAFyzLIU3DGshE5kHsOYJro5O3Je-yF09Fg')
dispatcher = updater.dispatcher


def get_weather(city, token):

    try:
        request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"
        )
        json_data = request.json()
        weather_desc = json_data["weather"][0]["main"]
        curr_temp = json_data["main"]["temp"]
        max_temp = json_data["main"]["temp_max"]
        min_temp = json_data["main"]["temp_min"]
        fills_temp = json_data["main"]["feels_like"]
        humidity = json_data["main"]["humidity"]
        pressure = json_data["main"]["pressure"]
        wind_speed = json_data["wind"]["speed"]

        return city, weather_desc, curr_temp, max_temp, min_temp, fills_temp, \
            humidity, pressure, wind_speed

    except KeyError:
        return "Please, check name of a city you entered"


def start(update: tg.Update, context: tge.CallbackContext):

    """ Send message, when the bot is started
        or received a /start command"""

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello, {update.effective_chat.first_name}, jan.\n"
                                                                    "I can tell the weather today, ebana.\n"
                                                                    "Please, send me the ciy i tuda priedut bratki."  
                                                                    "Bistro nahui blyat!\n")


def weather(update: tg.Update, context: tge.CallbackContext):

    """ Receive location and sends weather """

    location = update.message.text
    weather_input = get_weather(location, weather_token)
    context.bot.send_message(chat_id=update.effective_chat.id, text=weather_input)


def unknown(update: tg.Update, context: tge.CallbackContext):

    """ Receive unknown command and send warning """

    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, moya tvoya ne ponimat'.")


if __name__ == '__main__':

    # Create a tracker for start command with welcome speech
    start_handler = tge.CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Create a tracker for unknown commands
    unknown_handler = tge.MessageHandler(tge.Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Create a tracker for messages with weather function
    message_handler = tge.MessageHandler(tge.Filters.text, weather)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()

