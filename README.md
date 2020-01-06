# really listening

really listening is an easy-to-use app for transcribing and analysing spoken recordings.

## Installation

To work on this project, clone from here. There use pip to install any dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Usage

Since this is a django/redis/postgres project, three servers need to be started. I use the Postgres GUI to start its thing.

```bash
python manage.py runserver
redis-server
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/escofresco/reallylistening/blob/master/LICENSE)
