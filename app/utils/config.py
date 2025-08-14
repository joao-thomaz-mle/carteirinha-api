import os


def load_config():
    return {
        "ENVIRONMENT": os.getenv("ENVIRONMENT", "hml"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "hml"),
        "DEBUG": os.getenv("DEBUG", "false"),
        "APP_VERSION": os.getenv("APP_VERSION", "0.1.0"),
        "APP_TITLE": os.getenv("APP_TITLE", "Carteirinha API"),
        "APP_DESCRIPTION": os.getenv("APP_DESCRIPTION", "Carteirinha API"),
        "AWS_BEDROCK_REGION": os.getenv("AWS_BEDROCK_REGION", "us-east-1"),
        "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID"),
        "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY"),
    }
