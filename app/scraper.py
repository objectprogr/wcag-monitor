import requests

def fetch_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception:
        pass
    return ""
