from flask import Flask, jsonify, request
from functools import wraps
from datetime import datetime
import pytz

app = Flask(__name__)

API_TOKEN = "supersecrettoken123"

# List of 195 countries' timezones
timezones = {
    "Kabul": "Asia/Kabul",
    "Tirana": "Europe/Tirane",
    "Algiers": "Africa/Algiers",
    "Andorra la Vella": "Europe/Andorra",
    "Luanda": "Africa/Luanda",
    "Saint Johns": "America/Antigua",
    "Buenos Aires": "America/Argentina/Buenos_Aires",
    "Yerevan": "Asia/Yerevan",
    "Canberra": "Australia/Sydney",
    "Vienna": "Europe/Vienna",
    "Baku": "Asia/Baku",
    "Nassau": "America/Nassau",
    "Manama": "Asia/Bahrain",
    "Dhaka": "Asia/Dhaka",
    "Bridgetown": "America/Barbados",
    "Minsk": "Europe/Minsk",
    "Brussels": "Europe/Brussels",
    "Belmopan": "America/Belize",
    "Porto Novo": "Africa/Porto-Novo",
    "Thimphu": "Asia/Thimphu",
    "La Paz": "America/La_Paz",
    "Sarajevo": "Europe/Sarajevo",
    "Gaborone": "Africa/Gaborone",
    "Brasilia": "America/Sao_Paulo",
    "Bandar Seri Begawan": "Asia/Brunei",
    "Sofia": "Europe/Sofia",
    "Ouagadougou": "Africa/Ouagadougou",
    "Gitega": "Africa/Bujumbura",
    "Praia": "Atlantic/Cape_Verde",
    "Phnom Penh": "Asia/Phnom_Penh",
    "Yaounde": "Africa/Douala",
    "Ottawa": "America/Toronto",
    "Bangui": "Africa/Bangui",
    "N'Djamena": "Africa/Ndjamena",
    "Santiago": "America/Santiago",
    "Beijing": "Asia/Shanghai",
    "Bogota": "America/Bogota",
    "Moroni": "Indian/Comoro",
    "Brazzaville": "Africa/Brazzaville",
    "Kinshasa": "Africa/Kinshasa",
    "San Jose": "America/Costa_Rica",
    "Zagreb": "Europe/Zagreb",
    "Havana": "America/Havana",
    "Nicosia": "Asia/Nicosia",
    "Prague": "Europe/Prague",
    "Copenhagen": "Europe/Copenhagen",
    "Djibouti": "Africa/Djibouti",
    "Roseau": "America/Dominica",
    "Santo Domingo": "America/Santo_Domingo",
    "Quito": "America/Guayaquil",
    "Cairo": "Africa/Cairo",
    "San Salvador": "America/El_Salvador",
    "Malabo": "Africa/Malabo",
    "Asmara": "Africa/Asmara",
    "Tallinn": "Europe/Tallinn",
    "Mbabane": "Africa/Mbabane",
    "Addis Ababa": "Africa/Addis_Ababa",
    "Suva": "Pacific/Fiji",
    "Helsinki": "Europe/Helsinki",
    "Paris": "Europe/Paris",
    "Libreville": "Africa/Libreville",
    "Banjul": "Africa/Banjul",
    "Tbilisi": "Asia/Tbilisi",
    "Berlin": "Europe/Berlin",
    "Accra": "Africa/Accra",
    "Athens": "Europe/Athens",
    "Saint Georges": "America/Grenada",
    "Guatemala City": "America/Guatemala",
    "Conakry": "Africa/Conakry",
    "Bissau": "Africa/Bissau",
    "Georgetown": "America/Guyana",
    "Port-au-Prince": "America/Port-au-Prince",
    "Tegucigalpa": "America/Tegucigalpa",
    "Budapest": "Europe/Budapest",
    "Reykjavik": "Atlantic/Reykjavik",
    "New Delhi": "Asia/Kolkata",
    "Jakarta": "Asia/Jakarta",
    "Tehran": "Asia/Tehran",
    "Baghdad": "Asia/Baghdad",
    "Dublin": "Europe/Dublin",
    "Jerusalem": "Asia/Jerusalem",
    "Rome": "Europe/Rome",
    "Kingston": "America/Jamaica",
    "Tokyo": "Asia/Tokyo",
    "Amman": "Asia/Amman",
    "Nur-Sultan": "Asia/Almaty",
    "Nairobi": "Africa/Nairobi",
    "Tarawa": "Pacific/Tarawa",
    "Pyongyang": "Asia/Pyongyang",
    "Seoul": "Asia/Seoul",
    "Pristina": "Europe/Belgrade",
    "Kuwait City": "Asia/Kuwait",
    "Bishkek": "Asia/Bishkek",
    "Vientiane": "Asia/Vientiane",
    "Riga": "Europe/Riga",
    "Beirut": "Asia/Beirut",
    "Maseru": "Africa/Maseru",
    "Monrovia": "Africa/Monrovia",
    "Tripoli": "Africa/Tripoli",
    "Vaduz": "Europe/Vaduz",
    "Vilnius": "Europe/Vilnius",
    "Luxembourg": "Europe/Luxembourg",
    "Skopje": "Europe/Skopje",
    "Antananarivo": "Indian/Antananarivo",
    "Lilongwe": "Africa/Blantyre",
    "Kuala Lumpur": "Asia/Kuala_Lumpur",
    "Male": "Indian/Maldives",
    "Bamako": "Africa/Bamako",
    "Valletta": "Europe/Malta",
    "Majuro": "Pacific/Majuro",
    "Nouakchott": "Africa/Nouakchott",
    "Port Louis": "Indian/Mauritius",
    "Mexico City": "America/Mexico_City",
    "Palikir": "Pacific/Pohnpei",
    "Chisinau": "Europe/Chisinau",
    "Monaco": "Europe/Monaco",
    "Ulaanbaatar": "Asia/Ulaanbaatar",
    "Podgorica": "Europe/Podgorica",
    "Rabat": "Africa/Casablanca",
    "Maputo": "Africa/Maputo",
    "Naypyidaw": "Asia/Yangon",
    "Windhoek": "Africa/Windhoek",
    "Yaren": "Pacific/Nauru",
    "Kathmandu": "Asia/Kathmandu",
    "Amsterdam": "Europe/Amsterdam",
    "Wellington": "Pacific/Auckland",
    "Managua": "America/Managua",
    "Niamey": "Africa/Niamey",
    "Abuja": "Africa/Lagos",
    "Skopje": "Europe/Skopje",
    "Oslo": "Europe/Oslo",
    "Muscat": "Asia/Muscat",
    "Islamabad": "Asia/Karachi",
    "Ngerulmud": "Pacific/Palau",
    "Panama City": "America/Panama",
    "Port Moresby": "Pacific/Port_Moresby",
    "Asuncion": "America/Asuncion",
    "Lima": "America/Lima",
    "Manila": "Asia/Manila",
    "Warsaw": "Europe/Warsaw",
    "Lisbon": "Europe/Lisbon",
    "Doha": "Asia/Qatar",
    "Bucharest": "Europe/Bucharest",
    "Moscow": "Europe/Moscow",
    "Kigali": "Africa/Kigali",
    "Basseterre": "America/St_Kitts",
    "Castries": "America/St_Lucia",
    "Kingstown": "America/St_Vincent",
    "Apia": "Pacific/Apia",
    "San Marino": "Europe/San_Marino",
    "Sao Tome": "Africa/Sao_Tome",
    "Riyadh": "Asia/Riyadh",
    "Dakar": "Africa/Dakar",
    "Belgrade": "Europe/Belgrade",
    "Victoria": "Indian/Mahe",
    "Freetown": "Africa/Freetown",
    "Singapore": "Asia/Singapore",
    "Bratislava": "Europe/Bratislava",
    "Ljubljana": "Europe/Ljubljana",
    "Honiara": "Pacific/Guadalcanal",
    "Mogadishu": "Africa/Mogadishu",
    "Pretoria": "Africa/Johannesburg",
    "Juba": "Africa/Juba",
    "Madrid": "Europe/Madrid",
    "Colombo": "Asia/Colombo",
    "Khartoum": "Africa/Khartoum",
    "Paramaribo": "America/Paramaribo",
    "Stockholm": "Europe/Stockholm",
    "Bern": "Europe/Zurich",
    "Damascus": "Asia/Damascus",
    "Taipei": "Asia/Taipei",
    "Dushanbe": "Asia/Dushanbe",
    "Dodoma": "Africa/Dar_es_Salaam",
    "Bangkok": "Asia/Bangkok",
    "Lome": "Africa/Lome",
    "Nuku'alofa": "Pacific/Tongatapu",
    "Port of Spain": "America/Port_of_Spain",
    "Tunis": "Africa/Tunis",
    "Ankara": "Europe/Istanbul",
    "Ashgabat": "Asia/Ashgabat",
    "Funafuti": "Pacific/Funafuti",
    "Kampala": "Africa/Kampala",
    "Kyiv": "Europe/Kyiv",
    "Abu Dhabi": "Asia/Dubai",
    "London": "Europe/London",
    "Washington": "America/New_York",
    "Montevideo": "America/Montevideo",
    "Tashkent": "Asia/Tashkent",
    "Port Vila": "Pacific/Efate",
    "Vatican City": "Europe/Vatican",
    "Caracas": "America/Caracas",
    "Hanoi": "Asia/Bangkok",
    "Sana'a": "Asia/Aden",
    "Lusaka": "Africa/Lusaka",
    "Harare": "Africa/Harare"
}

# Token function from class
def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

# Call api with URL/api/time?city={cityname}
@app.route('/api/time', methods=['GET'])
@token_required
def get_time():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Missing 'city' query parameter"}), 400

    tz_name = timezones.get(city)
    if not tz_name:
        return jsonify({"error": f"City '{city}' not found in database"}), 404

    tz = pytz.timezone(tz_name)
    now = datetime.now(tz)
    utc_offset = now.strftime('%z')
    formatted_offset = f"{utc_offset[:3]}:{utc_offset[3:]}"

    return jsonify({
        "capital": city,
        "local_time": now.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": formatted_offset
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)