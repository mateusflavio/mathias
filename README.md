# witwicky-api
--
![witwicky](https://dreager1.files.wordpress.com/2014/09/924873-transformers_rotf15.jpg)


## Documentation
[Link](http://docs.luizalabs.com/transformers/witwicky)

## Installation

Create a virtualenv (use `virtualenvwrapper`):  
```bash
$ mkvirtualenv witwicky-api -p python3
```

Install development requirements:  
```bash
    make requirements-development
```

Create database tables:  
```bash
    make migrate
```

Create superuser:
```bash
	make superuser
```

Run the project:  
```bash
    make run
```

## Tests

To run the test suite, execute:  
```bash
    make test
```

To show coverage details (in HTML), use:  
```bash
    make test html
```
