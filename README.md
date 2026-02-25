# Wikipedia Mobile Автотесты

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/200px-Wikipedia-logo-v2.svg.png" alt="Wikipedia" width="200"/>
</p>

## 📑 Содержание

- [Технологии и инструменты](#-технологии-и-инструменты)
- [Покрытый функционал](#-покрытый-функционал)
- [Структура проекта](#-структура-проекта)
- [Запуск тестов](#-запуск-тестов)
- [Сборка в Jenkins](#-сборка-в-jenkins)
- [Allure отчёт](#-allure-отчёт)
- [Уведомление в Telegram](#-уведомление-в-telegram)

---

## 💻 Технологии и инструменты

<p align="center">
  <a href="https://www.python.org/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50" height="50" alt="Python"/></a>
  <a href="https://docs.pytest.org/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" width="50" height="50" alt="Pytest"/></a>
  <a href="https://appium.io/"><img src="http://appium.io/docs/en/latest/assets/images/appium-logo-horiz.png" width="50" height="50" alt="Appium"/></a>
  <a href="https://yashaka.github.io/selene/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" width="50" height="50" alt="Selene"/></a>
  <a href="https://www.browserstack.com/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/browserstack/browserstack-original.svg" width="50" height="50" alt="BrowserStack"/></a>
  <a href="https://allurereport.org/"><img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="50" height="50" alt="Allure"/></a>
  <a href="https://www.jenkins.io/"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" width="50" height="50" alt="Jenkins"/></a>
  <a href="https://telegram.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="50" height="50" alt="Telegram"/></a>
</p>

| Инструмент                                                   | Описание                                                   |
|--------------------------------------------------------------|------------------------------------------------------------|
| [Python](https://www.python.org/)                            | Язык программирования                                      |
| [Pytest](https://docs.pytest.org/)                           | Фреймворк для запуска тестов                               |
| [Appium](https://appium.io/)                                 | Фреймворк для мобильной автоматизации                      |
| [Selene](https://yashaka.github.io/selene/)                  | Обёртка над Selenium/Appium с лаконичным API               |
| [BrowserStack](https://www.browserstack.com/)                | Облачная платформа для запуска тестов на реальных устройствах |
| [Pydantic](https://docs.pydantic.dev/)                       | Валидация и управление конфигурацией                       |
| [Allure Report](https://allurereport.org/)                   | Генерация наглядных отчётов                                |
| [Jenkins](https://www.jenkins.io/)                           | CI/CD сервер для запуска тестов                            |
| [Telegram Bot](https://core.telegram.org/bots)               | Уведомления о результатах прогона                          |

---

## ✅ Покрытый функционал

Автотесты покрывают мобильное приложение **Wikipedia** (Android & iOS):

### 📱 Android — BrowserStack — `test_android_app_bstack.py` (2 теста)

- ✅ Поиск статьи по запросу «Appium» — проверка результатов поиска
- ✅ Открытие статьи по запросу «Python» — переход в найденную статью

### 🏠 Android — Локальный эмулятор — `test_android_app_local_emulator.py` (1 тест)

- ✅ Прохождение онбординга (4 экрана) — проверка текстов и навигации

### 🍏 iOS — BrowserStack — `test_ios_app_bstack.py` (1 тест)

- ✅ Ввод текста и проверка вывода в Sample App

### 🔍 Каждый тест включает

- Детализированные **шаги** через `allure.step()`
- Логирование действий **Selene** в Allure через `wait_with()`
- Прикрепление **видео** из BrowserStack к отчёту (для облачных тестов)
- Автоматическую настройку драйвера через **фикстуры**

---

## 📂 Структура проекта

```
mobile_tests/
├── conftest.py                         # Корневая конфигурация (если есть)
├── pytest.ini                          # Конфигурация Pytest (alluredir)
├── requirements.txt                    # Зависимости проекта
├── .env.example                        # Шаблон конфигурации окружений
├── .env.bstack                         # Настройки для BrowserStack
├── .env.local_emulator                 # Настройки для локального эмулятора
├── .env.credentials                    # Логины и ключи (не в Git)
├── .gitignore                          # Исключения для Git
│
├── src/                                # Исходный код
│   └── utils/
│       ├── config.py                   # Конфигурация: контексты, Pydantic Settings
│       └── allure.py                   # Утилита: прикрепление видео из BrowserStack
│
├── tests/                              # Тестовые модули
│   ├── conftest.py                     # Фикстуры: Appium-драйвер, Selene, teardown
│   ├── test_android_app_bstack.py      # Android-тесты в BrowserStack (2 теста)
│   ├── test_android_app_local_emulator.py  # Android-тесты на эмуляторе (1 тест)
│   └── test_ios_app_bstack.py          # iOS-тесты в BrowserStack (1 тест)
│
├── resources/
│   └── apks/
│       └── wikipedia.apk               # APK приложения Wikipedia
│
└── notifications/
    ├── allure-notifications-4.11.0.jar  # Утилита для отправки отчётов
    └── telegram.json.example            # Шаблон конфигурации Telegram-бота
```

---

## 🚀 Запуск тестов

### Переменные окружения

Проект использует систему **контекстов**. Переменная `CONTEXT` определяет, какой `.env`-файл загружается:

| Контекст         | Файл                 | Описание                            |
|------------------|----------------------|-------------------------------------|
| `bstack`         | `.env.bstack`        | Облачный запуск в BrowserStack      |
| `local_emulator` | `.env.local_emulator`| Локальный Android-эмулятор          |

> Скопируйте `.env.example` и создайте нужные файлы. Для BrowserStack также создайте `.env.credentials`.

### Локальный запуск

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов на BrowserStack (по умолчанию)
pytest

# Запуск тестов на локальном эмуляторе
CONTEXT=local_emulator pytest tests/test_android_app_local_emulator.py

# Запуск Android-тестов в BrowserStack
CONTEXT=bstack pytest tests/test_android_app_bstack.py

# Запуск iOS-тестов в BrowserStack
CONTEXT=bstack pytest tests/test_ios_app_bstack.py

# Генерация Allure отчёта
allure serve allure-results
```

---

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" width="25" height="25"/> Сборка в Jenkins

> Ссылка на Job: [Jenkins Job](https://jenkins.autotests.cloud/job/023-pilaabo-thesis_mobile)

<!-- Раскомментировать и добавить скриншот: -->
<!-- ![Jenkins Job](screenshots/jenkins_job.png) -->

---

## <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="25" height="25"/> Allure отчёт

> Ссылка на Allure Report: [Allure Report](https://jenkins.autotests.cloud/job/023-pilaabo-thesis_mobile/allure)

![Allure Overview](screenshots/allure_overview.png)
![Allure Suites](screenshots/allure_suites.png)

### Отчёт содержит

- **Шаги (Steps)** — каждый `allure.step()` + автоматические шаги Selene
- **Вложения** — видео выполнения теста из BrowserStack
- **Окружение** — платформа, устройство, версия ОС

---

## <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="25" height="25"/> Уведомление в Telegram

![Telegram Notification](screenshots/telegram_notification.png)

После прохождения тестов бот отправляет уведомление в Telegram-чат с результатами прогона.
