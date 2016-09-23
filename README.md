# mathias
--
![mathias](http://gcn.net.br/dir-arquivo-imagem/2015/08/20150818225832_4043748.jpg)


## Installation

Create a virtualenv (use `virtualenvwrapper`):  
```bash
$ mkvirtualenv mathias -p python3
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

