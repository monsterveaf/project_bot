import datetime
import requests
import telegram as tg
import telegram.ext as tge

weather_token = '22d38e4b789796c92e6e4fe65846ff67'
fake_token = '21d38e4b789796c92e6e4fe65846ff67'

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
        location = json_data["name"]
        weather_desc = json_data["weather"][0]["main"]
        curr_temp = str(round(json_data["main"]["temp"])) + "° С"
        max_temp = str(round(json_data["main"]["temp_max"])) + "° С"
        min_temp = str(round(json_data["main"]["temp_min"])) + "° С"
        feels_temp = str(round(json_data["main"]["feels_like"])) + "° С"
        humidity = str(json_data["main"]["humidity"]) + "%"
        pressure = str(json_data["main"]["pressure"]) + " hPa"
        wind_speed = str(round(json_data["wind"]["speed"])) + " m/s"

    except KeyError:
        return "Please, check the name of a city you entered"

    except requests.exceptions.Timeout:
        return "Please, try to connect in few minutes"

    except requests.ConnectionError:
        return "Sorry, something is wrong with the server. Try to connect a bit later"

    result = {
        "Date and time": datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S'),
        "Your location": location,
        "Weather description": weather_desc,
        "Current temperature": curr_temp,
        "Minimal temperature": min_temp,
        "Maximal temperature": max_temp,
        "Temperature feels like": feels_temp,
        "Humidity": humidity,
        "Pressure": pressure,
        "Wind speed": wind_speed
    }

    return result


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

    if len(location) > 35:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ti kogo xoches noebat'")
        return

    weather_input = get_weather(location, weather_token)
    message = dict_return(weather_input)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def dict_return(weather_dict):
    """Return a message from a dict"""

    if isinstance(weather_dict, str):
        return weather_dict

    message = ""

    for key, value in weather_dict.items():
        message += key + ": " + value + "\n"

    return message


def unknown(update: tg.Update, context: tge.CallbackContext):
    """ Receive unknown command and send warning """

    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, moya tvoya ne ponimat")


def inline_caps(update: tg.Update, context: tge.CallbackContext):
    """ Receive inline_query and send weather info """

    query = update.inline_query.query

    if not query or len(query) > 35:
        return

    results = [tg.InlineQueryResultArticle(
        id=query.upper(),
        title='Weather',
        input_message_content=tg.InputTextMessageContent(dict_return(get_weather(query, weather_token))),
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
