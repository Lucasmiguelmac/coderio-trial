# Coderio Trial
_This is a trial project for a position as a Django dev for Coderio._

## Setup
1) The Python version used in this project is python 3.8.5
2) This project has a `requirements.txt` file containing all python packages needed. To install all of them just run:
    ```
    pip install requirements.txt
    ```
    _You might want to install all this inside of a virtual environment_
3) Now you'll need to create a file named `.env` inside the project directory (at the same level as `manage.py` and `README.md`) in which you shall include a secret key, a boolean value (`True` or `False`) for DEBUG mode. A good way to produce the secret key is by running on your terminal, with python installed, the following command:
    ```
    python -c 'import secrets; print(secrets.token_urlsafe(38))'
    ```
    A possible `.env` file might look like this:
    ```
    DEBUG=False
    SECRET_KEY=asdasdasd
    ```
4) Now run the Django project so you can have access to the API.
    ```
    python manage.py runserver
    ```

That's it! You're good to go now.

## Endpoints
_There's a bug between Swagger and Django's REST Framework last version (version specified by the trial project's statement), that's why I haven't yet made a proper Swagger documentation._

We have the following endpoints:
| Method | Endpoint | Detail |
| ------ | ------ | ------ |
| GET | /api/character/<id> | Retrieve a character | 
| POST | /api/listings/<id>/rating | Add a rating to the character | 

The second endpoint expects a json object like the following:
```
{
    'character': 1,
    'score': 4
}
```



## Security Features
The following security features are present:
- Environment variables handled with the [environs](https://github.com/sloria/environs) package.
- New secret key generated via python's `secret` module
- Secured admin (changed admin's path to avoid common site scrapping hacks)
    
- 
Some of the following security features are missing:
- CORS protection
- Database passwords since we are only using SQLite
- A proper allowed hsots list


## Tests
This project's tests are made using *_pytest_*. In order to run the tests you just have to run on your terminal at the project folder level:
```
pytest
```

Factories and fixtures are located on a `conftest.py` file inside the `tests` directory.

You can change the pytest configuration in `pytest.ini`

## Observations
The second endpoint asked in the statement (the rating endpoint), does not need to get the Character's id both from the url and from the json object the endpoint is expecting. It's redundant. Nevertheless I proceeded to follow the statements as it is.