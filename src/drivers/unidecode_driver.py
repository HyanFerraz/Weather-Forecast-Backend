from unidecode import unidecode
from typing import Dict

def decode_address_info(address: str) -> Dict:
    formated_address = {
        "location" : unidecode(address["localidade"]),
        "state" : unidecode(address["uf"])
    }

    return formated_address