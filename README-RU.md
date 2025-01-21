<h2 align="center">Telegram Gifts Auto-Buyer</h2>

<div align="center">
  <img src="https://github.com/user-attachments/assets/2c4540b7-4e39-4306-945f-389271123ecc" alt="Превью" width="600px">
</div>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Версия Python">
  <img src="https://img.shields.io/github/license/bohd4nx/TGgifts-buyer" alt="Лицензия">
  <img src="https://img.shields.io/github/stars/bohd4nx/TGgifts-buyer" alt="Звёзды">
  <br>
  <a href="https://t.me/bohd4nx">
    <img src="https://img.shields.io/badge/разработчик-@bohd4nx-blue.svg" alt="Разработчик">
  </a>
  <a href="https://t.me/GiftsTracker">
    <img src="https://img.shields.io/badge/канал-@GiftsTracker-blue.svg" alt="Канал">
  </a>
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="./README-RU.md">Русский</a>
</p>

## 📝 Обзор

Продвинутый Telegram юзербот для автоматизированной отправки подарков с динамическими ценовыми диапазонами и саплаем. Поддерживает как лимитированные, так и обычные подарки с настраиваемыми правилами отправки.

## ✨ Возможности

- 🎁 Динамическое количество подарков на основе ценовых диапазонов
- 📊 Мониторинг лимитов поставок
- 🌐 Поддержка нескольких языков (EN/RU/UK)
- ⚡️ Автоматическое обнаружение подарков
- 🔄 Настраиваемые задержки и интервалы
- 📱 Поддержка нескольких получателей
- 🎯 Фильтрация по цене

## ⚙️ Конфигурация

### Основные настройки (config.ini)

```ini
[Telegram]
API_ID = ваш_api_id          # Ваш Telegram API ID с https://my.telegram.org
API_HASH = ваш_api_hash      # Ваш Telegram API Hash с https://my.telegram.org
CHANNEL_ID = id_канала       # ID канала для уведомлений (-100...)

[Bot]
INTERVAL = 10                # Интервал проверки подарков в секундах (мин: 10с)
TIMEZONE = Europe/Moscow     # Ваш часовой пояс для логов и операций
LANGUAGE = RU               # Язык бота (EN/RU/UK)

[Gifts]
MIN_GIFT_PRICE = 0          # Минимальная цена подарка для покупки
MAX_GIFT_PRICE = 10000      # Максимальная цена подарка для покупки
GIFT_DELAY = 5              # Задержка между отправкой подарков в секундах
USER_ID = id1, username     # Получатели (ID или юзернеймы)
HIDE_SENDER_NAME = True     # Скрывать имя отправителя при отправке
PURCHASE_NON_LIMITED_GIFTS = False  # Покупать ли нелимитированные подарки
```

### Настройка ценовых диапазонов

Бот использует сложную систему ценовых диапазонов для определения количества подарков:

```ini
[Ranges]
0,999,100 = 1      # Цена 0-999, лимит поставки 100, отправка 1 подарка
1000,1999,100 = 2  # Цена 1000-1999, лимит поставки 100, отправка 2 подарков
2000,2999,100 = 3  # Цена 2000-2999, лимит поставки 100, отправка 3 подарков
```

Формат: `мин_цена,макс_цена,саплай = количество`

## 🚀 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/bohd4nx/TGgifts-buyer.git
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте параметры:
   - Скопируйте `config.example.ini` в `config.ini`
   - Отредактируйте под свои нужды
   - Настройте ценовые диапазоны

4. Запустите:
```bash
python main.py
```

## 🌍 Локализация

Поддерживаемые языки:
- 🇺🇸 Английский
- 🇷🇺 Русский
- 🇺🇦 Украинский

Добавление нового языка:
1. Создайте `locales/ваш_язык.py`
2. Добавьте в `LANG_CODES` в `config.py`
3. Установите `LANGUAGE = ВАШ_ЯЗЫК` в config.ini

## 🔧 Устранение неполадок

### Частые проблемы

1. `AttributeError: 'Client' object has no attribute 'get_star_gifts'`
   ```bash
   pip uninstall pyrogram
   pip install pyrofork
   ```

2. Ошибки лимита саплая:
   - Проверьте конфигурацию [Ranges]
   - Убедитесь, что лимиты саплая корректны

3. Ошибки подключения:
   - Увеличьте INTERVAL (минимум 10 секунд)
   - Проверьте подключение к интернету
   - Проверьте учетные данные API

## ⚠️ Отказ от ответственности

Только для образовательных целей. Используйте ответственно и на свой страх и риск.

## 📄 Лицензия

Лицензия MIT - См. файл [LICENSE](LICENSE)
