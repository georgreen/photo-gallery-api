# 🖼️ Photo-Gallery Api 🤳

Photo Gallery Api : Backend implementation of a photo collection application. It enables user to interact with different forms of art work. It also allows Admin to manage and receive request for various services in regards to the art-work displayed by them.

- ## API
This App exposes endpoints that allows ```Clients/Users``` to access art-work from their portfolio.

- #### Available Resource Endpoints

|Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1.0/login` | Login the Admin.|
|POST| `/api/v1.0/category` | Create a new item in category. |
|GET| `/api/v1.0/category/` | List artwork in all categories. |
|GET| `/api/v1.0/category/<name>` | List all artwork in category. |
|GET| `/api/v1.0/project/<name>/<project_name>` | List all artwork in a given project. |
|GET| `/api/v1.0/category/<name>/<id>` | Get single artwork in category. |
|PUT| `/api/v1.0/category/<name>/<id>` | Update artwork in category. |
|DELETE| `/api/v1.0/category/<name>/<id>` | Delete this single artwork in category. |


## Getting Started 🕺

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

- To run on local machine git clone this project :
```
 $ git clone https://github.com/georgreen/photo-gallery-api.git
 ```

 Copy and paste the above command in your terminal, the project will be downloaded to your local machine.

- To consume API in client of choice navigate to:
 ```
 comming soon....
 ```


### Prerequisites

The application is built using python: flask framework.
>[Flask](http://flask.pocoo.org/) is a microframework for the Python programming language.


To Install python checkout:
```
https://www.python.org/
```


### Installing

For this section I will assume you have python3 and it's configured on your machine. </br>
Navigate to the folder you cloned and run: </br>

- Install Requirements
```
$ pip install -r requirements.txt
```

- Configure Environment.
```
$ export APP_SETTINGS="Development"
$ export DEV_DATABASE="path/<database name>"
$ export TEST_DATABASE="path/<database name>"
$ export SECRET="secret here"
```
> Note replace the value for DEV_DATABASE with real database path and SECRET with a strong string value


- Configure database
```
$ python manage.py database init
$ python manage.py database migrate
$ python manage.py database upgrade
```

- Run App 🏃🏃‍
```
$ python manage.py runserver
```
The app should be accessiable via : http://127.0.0.1:5000/


## Running the tests 🕵️

```
$ nosetests
```
- With Coverage

```
 $ nosetests --rednose --with-coverage --cover-package=app -v
```

- Coding style tests

[Pep8](https://www.python.org/dev/peps/pep-0008/) standards are followed in project.

```
$ pep8 app --count
```

## Deployment  🚀

- [Check this out to deploy to heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

## Built With  🏗 🔨⚒

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Flaskrestplus](https://flask-restplus.readthedocs.io/en/stable/) - Extension for Flask that adds support for quickly building REST APIs.

## Contributing 👍

- Please Fork me! :-)

## Versioning ⚙

- comming soon

## Authors 📚

- comming soon

## License 🤝

- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments 👊 🙌 👏 🙏

* [comming soon](https://www.youtube.com/watch?v=dQw4w9WgXcQ) - BEST RESOURCE EVER!!!
