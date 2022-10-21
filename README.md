**Armenian weather bot**
============================================================
![](https://imgtest.mir24.tv/uploaded/images/crops/2022/February/870x489_903x0_detail_crop_20220225123615_d6ff9cb2_8f7a1da83fbd942465b2c13d3c6749c0d18701a854fdc6c261f1af840e3b5af7.jpg)
This bot would be helpful for everyone who wants to find out
the weather condition at any place on Earth. Temperature, pressure, humidity - 
all this information and even more will be available for users.

---
Our project uses 4 libraries:
1. datetime
2. requests
3. telegram
4. telegram.ext

Bot uses 2 Tokens (я бы хотел, чтобы за них пояснили вы)

Bot consists of a list of functions:

- start
> This function receive a "start message" and send the greetings to the user.
![img_1.png](img_1.png)
- unknown
> If user enter incorrect command, bot will reply to him/her.
> ![img_5.png](img_5.png)

- weather
> Function is used to get the name of the city and check, whether it exists
> or not. If the len of the input exceed 35 symbols, user gets warning message.
> ![img_4.png](img_4.png)
> If there is no error, it starts functions "get_weather", "dict_return" and sends
> messages with data back to user.
> ![img_6.png](img_6.png)
> 
- get_weather
> It is used to get city's weather data from 
> the web-site through token and put them into the dictionary.
>
- dict_return
> This function returns the values of the dictionary in the correct form.
> 
- incline_caps
> It allows users apply bot functions in other chats.
> ![img_8.png](img_8.png)
> ![img_9.png](img_9.png)

---

If You want to try it by Yourself, You can simply write in Telegram 
@ArmyanskiyWeatherBot and check its performance!

