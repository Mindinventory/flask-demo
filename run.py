from src.app import app
from config.config import Config


if __name__ == '__main__':
    app.run(host=Config().HOST, port=Config().PORT, passthrough_errors=False)
