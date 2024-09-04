import os

from weather_sdk import get_new_event, SMSServer
from dotenv import load_dotenv

load_dotenv()

forecast_token = os.getenv("FORECAST_TOKEN")
town_title = "Курск"

sms_token = os.getenv("SMS_TOKEN")
server = SMSServer(sms_token)

new_event = get_new_event(forecast_token, town_title)
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
# Способ проверки: Выввести переменную token
# Код для проверки: print(token)
# Установленный факт: переменная имеет значение None
# Вывод: надо найти способ передать значение

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Вывести переменную token
# Код для проверки: print(token)
# Установленный факт: token не пуст
# Вывод: ошибка не в этом

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: Вывести переменную token
# Код для проверки: print(token)
# Установленный факт: в переменной token то значение
# Вывод: ошибка не в этом

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: Отследить переменную
# Код для проверки: print(token)
# Установленный факт: переменную token перезадают в следующих строчках кода
# Вывод: надо переименоваать переменные token

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Вывести переменную event_time
# Код для проверки: print(event_time)
# Установленный факт: Переменная не пуста
# Вывод: ошибка не в этом

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Вывести переменную event_date
# Код для проверки: print(event_date)
# Установленный факт: Переменная не пуста
# Вывод: ошибка не в этом

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Вывести переменную event_area
# Код для проверки: print(event_area)
# Установленный факт: Переменная не пуста
# Вывод: ошибка не в этом

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Вывести переменную phenomenon_description
# Код для проверки: print(phenomenon_description)
# Установленный факт: Переменная не пуста
# Вывод: ошибка не в этом

