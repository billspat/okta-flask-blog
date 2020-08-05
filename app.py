from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from blog import app,db

if __name__ == '__main__':
    app.run()
