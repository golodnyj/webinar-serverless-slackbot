# Шаг 4. Реализуем команду интегрированную в Slack

# Шаг 4.1. Получаем Token и Secret

В разделе `OAuth & Permissions` копируем `Bot User OAuth Token` в дальнейшем используем в качестве значения переменной `SLACK_BOT_TOKEN`

А в подразделе `App Credentials` на странице `Basic Information` копируем `Signing Secret` в дальнейшем используем в качестве значения переменной `SLACK_SIGNING_SECRET`.

Для любой функции создаваемой в рамках данного примера задавайте переменные `SLACK_BOT_TOKEN` и `SLACK_SIGNING_SECRET` помимо сервисного аккаунта.

# Шаг 4.2. Создаем функцию 

Перейдите в каталог и выберете сервис Cloud Functions. Нажмите кнопку `Создать функцию`.
Задайте имя `for-slack-bot-hello-from-serverless`.
Выберете среду выполнения `python37`.

Создайте файл `requirements.txt`
Поменяйте содержимое файлов `requirements.txt` и `index.py` в консоле на содержание аналогичных файлов из текущего каталога. Укажите точку входа `index.handler`. Увеличте таймаут до 5 секунд.

Обязательно укажите сервисный аккаунт, и переменные `SLACK_BOT_TOKEN`, `SLACK_SIGNING_SECRET` полученные ранее. Нажмите кнопку — `Создать версию`.
Запомните идентификатор вашей функции.

# Шаг 4.3. Внесите изменения в API Gateway

Перейдите в каталог и выберете сервис API Gateway. Выберете `for-slack-bot` и начните его редактирование. Вставьте секцию `/hello-from-serverless` со всем ее содержимым из файла `for-slack-bot.yml` спецификацию.

Обязательно замените `IDYOURFUNCTIONHELLO` на id созданной функции и `IDYOURACCOUNT` на id вашего сервисного аккаунта, созданного ранее. Сохраните изменения.

# Шаг 4.4. Конфигурирование команды в Slack

В панель управления вашим Slack workspace — https://api.slack.com/ выберете созданное вами приложение `ServerlessBotApp`. В секции `Slash Commands` нажмите `Create New Command`.

В поле `Command` введите `/hello-from-serverless` в поле  `Request URL` вставьте адрес вашего API Gateway дополнив его `/hello-from-serverless` можете также заполнить поле `Short Description`. Нажмите `Save`.

Следуя появившейся инструкциии переинстиллируйте Slack-приложение. После этого в вашем `workspace` появится возможность вызвать эту команду.

## Видео

https://youtu.be/qK-DTrCBbz8