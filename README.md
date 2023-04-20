
# api_yamdb
API YaMDb собирает отзывы пользователей на различные произведения такие как фильмы, книги и музыка.

## Description

This is a test project in which api technologies are implemented using the django framework

## Installation

Clone the repository and go to it on the command line:

```
git clone https://github.com/A1kawa1/api_yamdb.git
```

```
cd api_yamdb
```

Create and activate a virtual environment:

```
python3 -m venv env
```

```
source env/scripts/activate
```

```
python3 -m pip install --upgrade pip
```

Install dependencies from a file requirements.txt:

```
pip install -r requirements.txt
```

Perform migrations:


```
python3 manage.py migrate
```
`Also create an .env file in the /TrainingBot directory and specify the data for postgresql and the bot token.`   
Launch a project:

```
python3 manage.py runserver
```
## Documentation

```
Documentation will be available after the project is launched at /redoc/

```