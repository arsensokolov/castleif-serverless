# Замок Иф

Старый добрый "Замок Иф", который теперь будет поддерживать WebSocket,
в том числе нативные клиенты будут работать с по WS, включая клиента
для ОС MS-DOS 6.22 (MS Windows 3.1).

### Настройка среды разработки

1. Установите все зависимые `npm` пакеты:

```shell
$ npm install
```

2. Уставновите Serverless фреймворк в вашу систему:

```shell
$ npm install -g serverless
```

4. Создайте виртуальное окружение:

> Для macOS и Linux
```shell
$ python3 -m venv venv && source venv/bin/active
```

> Для Windows
```shell
> py -m venv venv 
> .\venv\Scripts\activate
```

5. Установите все зависимости Python серверной части:

```shell
$ pip install -r python-packages.txt -t ./venv/python
```

**Следующие шаги уже требуются для разворачивания чата, 
используйте их для выгрузки в AWS.** 

6. Установие плагин в Serverless фреймворке:

```shell
$ sls plugin install -n serverless-pseudo-parameters
```

7. Разверните в AWS:

```shell
$ sls deloy
```
