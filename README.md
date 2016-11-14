# bookStore
A Django book inventory.

###Installation
1. ######Requirements
 Ensure that python is installed on your machine, if not follow the link [Installing python](https://www.python.org/downloads/).
 * [Python 2.7+](https://www.python.org/) 
 * [Django](https://www.djangoproject.com/)
 * Among others as listed in `requirements.txt`

2. ######Installing virtualenvwrapper
 A Virtual Environment is a tool to keep the dependencies required by different projects in separate directories on a computer.
 To install virtualenvwrapper follow the link [installing virtualenvwrapper](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
3. ######Cloning the repo

 To clone the repo type the following command in terminal:
 
 ```
 $ git clone https://github.com/andela-engmkwalusimbi/bookStore.git
 ```
 
 To install all app requirements type these command in your terminal one after the other:
 
 ```
 $ cd bookStore
 $ pip install -r requirements.txt
 ```

4. ######Managing Database set up
Run the following commands on the terminal to set up tables and manage upgrades to tables if you change your models.


 * To create migrations, run the `migrate` command:

 ```
 $ python manage.py migrate
 ```


 Your database is now ready to use with the app.

###Running the APP

To run the `APP` type the following command in your terminal:

```
$ python manage.py runserver
```

The default url is `http://127.0.0.1:8000/`. Use this in the browser of your choice.


###Running tests

To run tests type the following command in terminal:

```
$ python manage.py test
```
