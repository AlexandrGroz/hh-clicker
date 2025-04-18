### hh.ru авто кликер

____
### Оглавление

- [Описание. Для чего этот скрипт?](#описание)
- [Установка и использование](#установка-и-использование)
    - [Общее](#общее)
____
### Описание
Данный скрипт помогает быстро откливаться на вакансии на hh.ru на основе предзаполненных данных по вашему запросу и слов исключений.

В существующей версии скрипта, отклики будут происходить только на вакансии в пределах России, без тестов при нажатии, без сопроводительным писем.<br>

__Только стандартные-базовые отклики.__
____
### Установка и использование
#### Общее
1. Установите язык [Python](https://www.python.org/downloads/)
2. Установите [менеджер пакетов PIP](https://pip.pypa.io/en/stable/installation/)
3. Сделайте клон этого репозитория с помощью команды ```git clone https://github.com/AlexandrGroz/hh-clicker.git```
4. Откройте созданную папку
5. Внутри создайте файл ```.env``` (это не расширение, а буквально полное название)
6. Внесите собственные данные в файл ```.env```. Файл должен состоять из 7 строк, описание приведено ниже:
    1. __DRIVER="chrome"__ - тип браузера в котором будет исполняться скрипт. __(доступен только chrome)__
    2. __LOGIN_TYPE="phone"__ - тип авторизации. __(доступен только phone, т.е. по номеру с кодом)__
    3. __PHONE="79999999999"__ - ваш номер к которому привязан аккаунт hh. __(без дополнительных символ, слитно, с 7 в начале)__
    4. __SEARCH_QUERY="frontend"__ - поисковой запрос на hh. __(Примеры: backend-разработчик, devops, и т.д.)__
    5. __SEARCH_EXCLUDE="модель, teamlead, тимлид, hr, node.js, node, репетитор, менеджер, водитель, логистика, логистике, досмотру, заявки, инcпектор, мобильных, node, vue, nuxt, мобильной, native, модератор, стажировка, 1C, bitrix, wordpress, erlang, angular, sharepoint, Rust, java,vba, delphi, автор, кредит, медсестра, медбрат, врач, полицейский, мойщик, упаковщик, сборщик, приемщик, приёмщик, часовщик, помощник, повар, сушист, хостес, бар, бармен, официант, бариста, курьер, продажа, маникюр, педикюр, электрик, электромонтёр, слесарь, кассир, грузчик, швея, tobacco"__ - слова которых нужно исключить из названия вакансии. __(пишутся через запятую)__
    6. __REGION="россия"__ - регион или город в котором вы планируете искать работу. __(только Россия)__
    7. __LIMIT="200"__ - лимит откликов. __(ежедневно откликаться на hh возможно на 200 вакансий)__
7. Далее выберите для себя более удобный способ запуска скрипта
    1. [Автоматический. (через батник .bat)](#автоматический-запуск-скрипта) 
    2. [Вручную. (с активацией и установкой пакетов в виртуальную среду.)](#ручной-запуск-скрипта) 

#### Автоматический запуск скрипта
1. Внутри папки с репозиторием найдите и сделайте двойной клик по файлу ```start.bat```. Готово процесс пошел!
    
#### Ручной запуск скрипта
1. Создайте виртуальную среду командой ```python -m venv {укажите необходимый путь}\hh_clicker_venv```
2. Активируйте виртуальную среду ```{укажите необходимый путь}\Scripts\activate.bat``` или ```{укажите необходимый путь}\Scripts\Activate.ps1``` в зависимости от вашей версии Python.
3. Установки зависимости pip ```install -r requirements.txt``` они нахдятся в корне репозитория.
4. Запустите скрипт командой ```python script.py``` из корня проекта. Готово процесс пошел!

