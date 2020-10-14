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
    SECRET_KEY=jldRLNxLtj0tBAY4UjSY23IrrZKqCtXZNq_bB2rF_AtzLBUqZtg
    ```

That's it! YOu're good to go now.


## Security Features
The following security features are present:
- Environment variables handled with the [environs](https://github.com/sloria/environs) package.
- New secret key generated via python's `secret` module
    
- 
Some of the following security features are missing:
- CORS protection
- Database passwords since we are only using SQLite


## Tests
This project's tests are made using *_pytest_*. In order to run the tests you just have to run on your terminal at the project folder level:
```
pytest
```

Factories and fixtures are located on a `conftest.py` file inside the `tests` directory.

You can change the pytest configuration in `pytest.ini`