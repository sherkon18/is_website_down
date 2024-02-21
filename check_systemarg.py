import requests
import argparse

#Function to check if the website is up
def is_website_up(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The website you want to check.")
    args = parser.parse_args()
    url = args.url
    
    if not url.startswith("http"):
        url = "https://" + url
    if is_website_up(url):
        #print(f"{url} is up!")
        return True
    else:
        #print(f"{url} is down!")
        return False

if __name__ == "__main__":
    main()
