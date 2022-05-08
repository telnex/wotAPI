# Мониторинг данных World of Tanks Console
Класс позволяет мониторить данные с console.worldoftanks.com (PS4 и Xbox) за сутки/неделю/месяц. Данные хранятся в формате .JSON.
Параметры, за которыми следит скрипт: количество боев (побед/поражений), кол-во убитых врагов, 
кол-во паданий и пробитий, кол-во обнаруженных врагов, суммарный нанесенный урон и полученный опыт.

The class allows you to monitor data from console.worldoftanks.com (PS4 and Xbox) a day / week / month. The data is stored in .JSON.
The parameters monitored by the script: the number of battles (victories / defeats), 
the number of enemies killed, the number of falls and penetrations, the number of detected enemies, 
the total damage done and the experience gained.

---
Для работы скрипта необходимо зарегистрироваться на сайте [wargaming.net](https://developers.wargaming.net/ "developers.wargaming.net") и получить токен приложения,
а также созадать папку **/dataUser/** (в ней будут храниться файлы .json)

---

**Пример вызова:**
```Python
  user = Tanks('graff_gss')
  if user.status():
    print(user.sDay('xp')) # Полученный опыт за сутки
    print(user.sWeek('wins')) # Побед за неделю
  else:
    print('Ошибка, пользователь не найден!')
 ```
