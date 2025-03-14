import requests
from datetime import datetime, timezone

def fetch_iss_data():
    iss_url = "http://api.open-notify.org/iss-now.json"
    astronauts_url = "http://api.open-notify.org/astros.json"
    
    try:
        iss_response = requests.get(iss_url)
        astronauts_response = requests.get(astronauts_url)
        
        iss_data = iss_response.json()
        astronauts_data = astronauts_response.json()
        
        return iss_data, astronauts_data
    except requests.RequestException as e:
        print(f"Ошибка при запросе данных: {e}")
        return None, None

def display_iss_info():
    iss_data, astronauts_data = fetch_iss_data()
    if not iss_data or not astronauts_data:
        return
    
    position = iss_data.get("iss_position", {})
    timestamp = iss_data.get("timestamp", 0)
    formatted_time = datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Текущие координаты МКС:")
    print(f"Время обновления: {formatted_time} UTC")
    print(f"Широта: {position.get('latitude', 'N/A')}° N, Долгота: {position.get('longitude', 'N/A')}° E")
    
    astronauts = astronauts_data.get("people", [])
    if astronauts:
        print("\nЛюди в космосе:")
        for person in astronauts:
            print(f"- {person['name']} ({person['craft']})")
if __name__ == "__main__":
    display_iss_info()
