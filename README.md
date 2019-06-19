# weather-rest-api [![Build Status](https://travis-ci.org/gitgik/flask-rest-api.svg?branch=develop)](https://travis-ci.org/gitgik/flask-rest-api)
A flask-driven restful API for information analysis


## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Docker](https://docs.docker.com/)** - Docker is a platform for developers and sysadmins to develop, deploy, and run applications with containers
 over others.
* Minor dependencies can be found in the requirements.txt file on the root folder.


## Installation / Usage
* to run the project is very simple, enough installed docker globally as well. If not, run this:
    ```
        $ sudo apt update
	$ sudo apt install docker.io
    ```
* Git clone this repo to your PC
    ```
        $ git clone https://github.com/willzzini/weather-map-api.git
    ````

* #### Running It
    Cd into your the cloned repo as such, run the server using this one simple command:
	
    ```
    $ docker build -t weather-api .
    $ docker run -p 4000:80 weather-api
    ```
    You can now access the app on your local browser by using
    ```
    http://127.0.0.1:4000/cities
    ```
    Or test creating data using Postman

* #### Postman Test
    1. In postman :
        ```
        http://127.0.0.1:4000/
        ```

    2. Then :
        ```
        http://127.0.0.1:4000/
	```

    you can access the swagger documentation: http://127.0.0.1:4000/weather-api-docs/#

    3. So that it is possible to access the endpoints it is necessary to pass in the Headers of postaman Api-key, see:
        ```
        Api-key eb8b1a9405e659b2ffc78f0a520b1a46
	```