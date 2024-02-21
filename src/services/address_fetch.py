from drivers.parse_xml import parse_xml
from drivers.fetch_api import fetch_api
from drivers.unidecode_driver import decode_address_info

class AddressFetch:

    def get_address(self, cep: str) -> str:
        address = self.__fetch_address(cep)
        
        decoded_address = decode_address_info(address)
        link = f"http://servicos.cptec.inpe.br/XML/listaCidades?city={decoded_address['location']}"
        response = fetch_api(link)

        cities = parse_xml(response.content)

        for city in cities["cidades"]["cidade"]:
            if city["uf"] == decoded_address["state"]:
                address["id"] = city["id"]
                return address
        
    def __fetch_address(self, cep: str) -> str:
        link = f"https://viacep.com.br/ws/{cep}/json/"
        response = fetch_api(link)
        address = response.json()

        return address
