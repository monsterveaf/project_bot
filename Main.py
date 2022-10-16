import telegram as tg
import telegram.ext as tge
import requests
import datetime

weather_token = '22d38e4b789796c92e6e4fe65846ff67'

# Create a connection with bot
updater = tge.Updater(token='5780766591:AAFyzLIU3DGshE5kHsOYJro5O3Je-yF09Fg')
dispatcher = updater.dispatcher


def get_weather(city, token):
    """ Receive city and return weather information"""

    try:
        request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"
        )
        json_data = request.json()
        weather_desc = json_data["weather"][0]["main"]
        curr_temp = int(json_data["main"]["temp"])
        max_temp = int(json_data["main"]["temp_max"])
        min_temp = int(json_data["main"]["temp_min"])
        feels_temp = int(json_data["main"]["feels_like"])
        humidity = json_data["main"]["humidity"]
        pressure = json_data["main"]["pressure"]
        wind_speed = int(json_data["wind"]["speed"])

        return f"Date and time: {datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n" \
               f"Your location: {city}\n" \
               f"Weather description: {weather_desc}\n" \
               f"Current temperature: {curr_temp}° С\n" \
               f"Minimal temperature: {min_temp}° С\n" \
               f"Maximal temperature: {max_temp}° С\n" \
               f"Temperature feels like: {feels_temp}° С\n" \
               f"Humidity: {humidity}%\n" \
               f"Pressure: {pressure} hPa\n" \
               f"Wind speed: {wind_speed} m/s"

    except KeyError:
        return "Please, check the name of a city you entered"


def start(update: tg.Update, context: tge.CallbackContext):
    """ Send message, when the bot is started
        or received a /start command"""

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello, {update.effective_chat.first_name}, jan.\n"
                                                                    "I can tell you the weather today, ebana.\n"
                                                                    "Please, send me the ciy i tuda priedut bratki.\n"
                                                                    "Bistro nahui blyat!")


def weather(update: tg.Update, context: tge.CallbackContext):
    """ Receive location and sends weather """

    location = update.message.text
    weather_input = get_weather(location, weather_token)
    context.bot.send_message(chat_id=update.effective_chat.id, text=weather_input)


def unknown(update: tg.Update, context: tge.CallbackContext):
    """ Receive unknown command and send warning """

    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, moya tvoya ne ponimat")


def inline_caps(update: tg.Update, context: tge.CallbackContext):
    """ Receive inline_query and send weather info """

    query = update.inline_query.query

    if not query:
        return "Shoto strannoe"

    results = [tg.InlineQueryResultArticle(
        id=query.upper(),
        title='Weather',
        input_message_content=tg.InputTextMessageContent(get_weather(query, weather_token)),
        description=f"Today's weather for {query}"
    )]
    context.bot.answer_inline_query(update.inline_query.id, results)


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

    # Create a inline queries
    inline_caps_handler = tge.InlineQueryHandler(inline_caps)
    dispatcher.add_handler(inline_caps_handler)

    # Start the bot
    updater.start_polling()
