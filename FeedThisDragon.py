import requests
import concurrent.futures

uuid_session = ""
base_url = "http://feedthisdragon2.chall.malicecyber.com/api/v1"

def get_session_headers(uuid_session):
    return {
        "Authorization": "mynotsosecrettoken",
        "Cookie": f"uuid={uuid_session}; achievements=%5B%5D",
        "Sec-GPC": "1",
        "Session": uuid_session,
        "ShopUuid": "",
        "Update": "true"
    }

def click_item(session, uuid_session, item):
    type_item = item.get("type")

    if type_item in ["life", "bigboo", "midboo", "lilboo", "food", "veggy", "candy", "burger", "gem", "coin", "secret", "nyan"]:
        print(type_item, item['uuid'])

        headers = get_session_headers(uuid_session)
        headers["ItemUuid"] = item['uuid']

        click = session.post(base_url, headers=headers).json()
        
        if "items" in click:
            return click["items"]
    return []

def start_game(session, uuid_session):
    headers = get_session_headers(uuid_session)
    headers["ItemUuid"] = ""

    start_game_response = session.get(base_url, headers=headers).json()
    
    if "items" in start_game_response:
        return start_game_response["items"]
    return []

if __name__ == "__main__":
    session = requests.Session()

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        while True:
            items = start_game(session, uuid_session)

            if not items:
                headers = get_session_headers(uuid_session)
                response = session.get(base_url, headers=headers).json()
                
                if "items" in response:
                    items = response["items"]

            futures = [executor.submit(click_item, session, uuid_session, item) for item in items]
            concurrent.futures.wait(futures)
