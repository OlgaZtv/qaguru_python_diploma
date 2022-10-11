# Автотесты для сайтов

* UI - http://zero.webappsecurity.com
* API - http://demo.testfire.net

# Автотесты для мобильного приложения

* Яндекс.Недвижимость

## Покрыт следующий функционал
* UI тесты - http://zero.webappsecurity.com
    * ✅ Проверка поиска по сайту
    * ✅ Проверка меню с дополнительными службами
    * ✅ Проверка формы рагистрации
    * ✅ Проверка функционала восстановления пароля
    * ✅ Проверка работы формы отзывов
    

* API тесты - http://demo.testfire.net
  * ✅ Проверка логина нас сайт
  * ✅ Проверка получения списка трансферов из личного кабинета пользователя
  * ✅ Проверка формы обратной связи
  * ✅ Проверка добавления пользователя
  * ✅ Проверка изменения пароля пользователя
  * ✅ Проверка разлогина 

* Android тесты - Яндекс.Недвижимость
  * ✅ Изменение отображения карты в формат списка
  * ✅ Проверка работы сортировки в приложении
  * ✅ Проверка работы фильтров в приложении
  * ✅ Проверка добавления в избранное
  * ✅ Проверка настроек приложения


## Технологический стек
Python, Pytest, Selene, PyCharm, Requests, Appium, Jenkins, Selenoid, Allure TestOps, Jira, Github, Telegram

<p  align="left">
<code>
  <img src="resources/python.png" width="40" height="40"  alt="Python"/>
  <img src="resources/pytest.png" width="40" height="40"  alt="Pytest"/>
  <img src="resources/selene.png" width="50" height="40"  alt="Selene"/>
  <img src="resources/pysharm.png" width="40" height="40"  alt="PyCharm"/>
  <img src="resources/request.png" width="50" height="40"  alt="Requests"/>
  <img src="resources/appium.png" width="40" height="40"  alt="Appium"/>
  <img src="resources/Jenkins.jpg" width="40" height="40"  alt="Jenkins"/>
  <img src="resources/selenoid.png" width="40" height="40"  alt="Selenoid"/>
  <img src="resources/allure.jpg" width="40" height="40"  alt="Allure TestOps"/>
  <img src="resources/Jira.png" width="40" height="40"  alt="Jira"/>
  <img src="resources/Github.png" width="40" height="40"  alt="Github"/>
  <img src="resources/telegram-logo.png" width="40" height="40"  alt="Telegram"/>
</code>
</p>

## Как запустить
Перед выполением необходимо:
* в .env определить параметры конфигурации:
    - login, password for selenoid
    - apiUrl (url address for API tests)
    - app(path to mobile app, in diploma:'./YandexReality.apk')
    - appName (name of mobile app, in diploma:'com.yandex.mobile.realty')
    - appWaitActivity (WaitActivity for mobile app, in diploma:'com.yandex.mobile.realty*')
    - platformName (platform name for mobile app, in diploma:'android')
    - platformVersion (platform version for mobile app, in diploma:'11')
    - deviceName (device name for mobile app, in diploma:'Pixel_4_API_30')
    - remoteUrl (url address from selenoid or grid, default: 'http://127.0.0.1:4723/wd/hub')


### Локально
```
pytest .
```

### Удаленно
```bash
ls -la
python -m venv .venv
source .venv/bin/activate
pytest ${TESTS_FOLDER} --browser_version=${BROWSER_VERSION}
```

### Видео о прохождении тестов
<img src="resources/ezgif-1-719f77e8aa.gif" alt="video test" border="0" />

### Запуск в Jenkins
Статистика по запускам <br >
<a href="https://ibb.co/TvwPjzj"><img src="https://i.ibb.co/2nFcVXV/jenkins-stst.png" alt="Статистика по запускам" border="0"></a>

Параметры запуска <br >
<a href="https://ibb.co/THr4VDp"><img src="https://i.ibb.co/nDR7HqZ/Jenkins.png" alt="Jenkins" border="0"></a>

### Отчёт о прохождении автотестов в Allure Report
<img src="https://i.ibb.co/SVqqBMh/Allure-Report.png" alt="Allure-Report" border="0">
### Список автотестов в Allure Report
<img src="resources/allure_list.png" alt="Allure-Report-2" border="0">
### Хранение тестовой документации в Allure TestOps
<img src="https://i.ibb.co/pbj1zVw/Allure-Test-Ops.png" alt="Allure-Test-Ops" border="0">
### Интерграция с Jira
<img src="https://i.ibb.co/JQ69XYt/HOMEWORK-320-Olga-Ztv-final-project-tests-QA-GURU-Jira.png" alt="HOMEWORK-320-Olga-Ztv-final-project-tests-QA-GURU-Jira" border="0">
### Уведомления о прохождении автотестов в Telegram
<img src="https://i.ibb.co/G2fGQj5/telegram-bot.png" alt="telegram-bot" border="0">