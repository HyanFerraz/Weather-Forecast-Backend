from drivers.parse_xml import parse_xml
from drivers.fetch_api import fetch_api 

def get_forecast(loc_id):
    link = f"http://servicos.cptec.inpe.br/XML/cidade/{loc_id}/previsao.xml"
    response = fetch_api(link)
    weather_dict = parse_xml(response.content)

    return weather_dict