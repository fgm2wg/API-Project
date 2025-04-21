# API-Project

## How to Use
* The API should be up and running on the IP address: 35.232.83.76 (on port 5000)
* To access the API, the url has the following format: http://35.232.83.76:5000/api/time?city={cityname}. You must provide a valid city name from the list of 195 below for the API to work
* The API requires the secret token: "supersecrettoken123" in the header to be accessed, so simply going to the url via a web browser will not have authorization
* To access the API via a curl command, you can use something like: `curl -X GET "http://35.232.83.76:5000/api/time?city=London" -H "Authorization: Bearer supersecrettoken123"`
* Here is an example Python script to retrieve data from the API:
```python
import requests

param = "London"

API_URL = f"http://35.232.83.76:5000/api/time?city={param}"

TOKEN = "supersecrettoken123"

headers = {
  "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
  print("Success:", response.json())
else:
  print("Failed:", response.status_code, response.text)
```
* The API has data for the following 195 capitals: Kabul, Tirana, Algiers, Andorra la Vella, Luanda, Saint Johns, Buenos Aires, Yerevan, Canberra, Vienna, Baku, Nassau, Manama, Dhaka, Bridgetown, Minsk, Brussels, Belmopan, Porto Novo, Thimphu, La Paz, Sarajevo, Gaborone, Brasilia, Bandar Seri Begawan, Sofia, Ouagadougou, Gitega, Praia, Phnom Penh, Yaounde, Ottawa, Bangui, N'Djamena, Santiago, Beijing, Bogota, Moroni, Brazzaville, Kinshasa, San Jose, Zagreb, Havana, Nicosia, Prague, Copenhagen, Djibouti, Roseau, Santo Domingo, Quito, Cairo, San Salvador, Malabo, Asmara, Tallinn, Mbabane, Addis Ababa, Suva, Helsinki, Paris, Libreville, Banjul, Tbilisi, Berlin, Accra, Athens, Saint Georges, Guatemala City, Conakry, Bissau, Georgetown, Port-au-Prince, Tegucigalpa, Budapest, Reykjavik, New Delhi, Jakarta, Tehran, Baghdad, Dublin, Jerusalem, Rome, Kingston, Tokyo, Amman, Nur-Sultan, Nairobi, Tarawa, Pyongyang, Seoul, Pristina, Kuwait City, Bishkek, Vientiane, Riga, Beirut, Maseru, Monrovia, Tripoli, Vaduz, Vilnius, Luxembourg, Skopje, Antananarivo, Lilongwe, Kuala Lumpur, Male, Bamako, Valletta, Majuro, Nouakchott, Port Louis, Mexico City, Palikir, Chisinau, Monaco, Ulaanbaatar, Podgorica, Rabat, Maputo, Naypyidaw, Windhoek, Yaren, Kathmandu, Amsterdam, Wellington, Managua, Niamey, Abuja, Skopje, Oslo, Muscat, Islamabad, Ngerulmud, Panama City, Port Moresby, Asuncion, Lima, Manila, Warsaw, Lisbon, Doha, Bucharest, Moscow, Kigali, Basseterre, Castries, Kingstown, Apia, San Marino, Sao Tome, Riyadh, Dakar, Belgrade, Victoria, Freetown, Singapore, Bratislava, Ljubljana, Honiara, Mogadishu, Pretoria, Juba, Madrid, Colombo, Khartoum, Paramaribo, Stockholm, Bern, Damascus, Taipei, Dushanbe, Dodoma, Bangkok, Lome, Nuku'alofa, Port of Spain, Tunis, Ankara, Ashgabat, Funafuti, Kampala, Kyiv, Abu Dhabi, London, Washington, Montevideo, Tashkent, Port Vila, Vatican City, Caracas, Hanoi, Sana'a, Lusaka, Harare
