import os

from app import create_app

config_name = os.environ.get('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)

if __name__ == '__main__':
    app.run()