import os


def load_config():
    return {
        "ENVIRONMENT": os.getenv("ENVIRONMENT", "hml"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "hml"),
        "DEBUG": os.getenv("DEBUG", "false"),
        "APP_VERSION": os.getenv("APP_VERSION", "0.1.0"),
        "APP_TITLE": os.getenv("APP_TITLE", "Carteirinha API"),
        "APP_DESCRIPTION": os.getenv("APP_DESCRIPTION", "Carteirinha API"),
        # "KAFKA_TOPIC": os.getenv("KAFKA_TOPIC", "phrase-identifier"),
        # "KAFKA_FILE_PATH": os.getenv("KAFKA_FILE_PATH", "./app/client.properties"),
    }
