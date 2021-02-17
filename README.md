# About

This is a simple Pyhton Kivy mopile app template.

This application uses following libraries

- kivy
- sqlalchemy for SQL stuff.
- python-dotenv for reading .env file.
- pillow for image (icon) manupalation.
- psycopg2 for using PostgreSQL. 

Icons that are in use are Iconic icons and are from https://github.com/iconic/open-iconic. Icons are under MIT license: https://github.com/iconic/open-iconic#icons

Have been tested only on Python 3 and with computer. Still needs to be tested with phones.

![alt text](https://i.imgur.com/Qf3k7SY.png)

# Config file

Make sure to create .env file in your project root (see .env_example) which contains correct DATABASE URI connection string. This will allow you to run application locally and connect to correct database.

# Runnig application

```shell
# optional if you don't have pipenv installed
pip install pipenv
pipenv install
pipenv shell
python app.py
```

# Author

Santeri Hartikainen

# License

Copyright 2021 Santeri Hartikainen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.