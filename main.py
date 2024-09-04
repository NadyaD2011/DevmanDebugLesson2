import os

from weather_sdk import get_new_event, SMSServer
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("FORECAST_TOKEN")
town_title = "Курск"

token = os.getenv("SMS_TOKEN")
server = SMSServer(token)

new_event = get_new_event(token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = """{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны."""

sms_message = sms_template.format(
    phenomenon_description,
    town_title,
    event_time,
    event_date,
    event_area,
)

server.send(sms_message)

# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: переменная пустая
# Вывод: нужно найти где именно находится ошибка

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Вывести переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: переменная имеет значение
# Вывод: ошибка не в этом

# Гипотеза 2.2: В town_title не название города
# Способ проверки: Вывести переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: в переменной есть название города
# Вывод: ошибка не в этом

# Гипотеза 3: Переменная token на самом деле пуста
# Способ проверки: Выввести переменную токен
# Код для проверки: print(token)
# Установленный факт: переменная имеет значение None
# Вывод: надо найти способ передать значение
