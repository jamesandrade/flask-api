<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Api_2" />

  &#xa0;

  <!-- <a href="https://api_2.netlify.app">Demo</a> -->
</div>

<h1 align="center">Api_2</h1>

<p align="center">
 <!-- <img alt="Github top language" src="https://img.shields.io/github/languages/top/{{YOUR_GITHUB_USERNAME}}/api_2?color=56BEB8">-->

  <!-- <img alt="Github language count" src="https://img.shields.io/github/languages/count/{{YOUR_GITHUB_USERNAME}}/api_2?color=56BEB8">-->

  <!-- <img alt="Repository size" src="https://img.shields.io/github/repo-size/{{YOUR_GITHUB_USERNAME}}/api_2?color=56BEB8">-->

  <!-- <img alt="License" src="https://img.shields.io/github/license/{{YOUR_GITHUB_USERNAME}}/api_2?color=56BEB8">-->

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/api_2?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/api_2?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/api_2?color=56BEB8" /> -->
</p>

<!-- Status -->

<h4 align="center"> 
	🚧  Flask-Api 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/jamesandrade" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Api Flask with SQLAlchemy ORM

## :sparkles: Features ##

:heavy_check_mark: Feature 1;\
:heavy_check_mark: Feature 2;\
:heavy_check_mark: Feature 3;

## :rocket: Technologies ##

The following tools were used in this project:

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Docker](https://www.docker.com/) and [Python](https://www.python.org/) installed.

## :checkered_flag: Starting ##

```bash
# Install all dependences
$ pip install -r requirements.txt

# Clone this project
$ git clone https://github.com/jamesandrade/flask-api

# Access
$ cd flask-api

# Install dependencies
$ docker run --name flask-postgres -e POSTGRES_USER=docker -e POSTGRES_PASSWORD=docker -d postgres

# Run migrations 
$ flask db upgrade -d src/infra/orm/migrations

# Run the project
$ python app.py

# The server will initialize in the <http://localhost:5000>

# it is recommended to use Virtual Environments (https://docs.python.org/3/tutorial/venv.html)
```

<!--## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">{{YOUR_NAME}}</a>
-->
&#xa0;

<a href="#top">Back to top</a>
