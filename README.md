## Players CRUD API

This command line script fetches players infromation from the remote API and writes it to the file on the disk in
files `players.

Code is tested on Python version 3.8.4 on Ubuntu 20.04.1

Database configuration is in the `config.py` file.
Creating tables and seedeng database is achieved by running:
```bash
$ python create_seed.py
```

Install dependencies:

```bash
$ pip install -r requirements.txt
```

Run application:
```bash
$ export FLASK_APP=flask.py
$ flask run
```
