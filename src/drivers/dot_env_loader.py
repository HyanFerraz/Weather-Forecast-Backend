from dotenv import dotenv_values

def get_dotenv_values():
    return dotenv_values(".env")