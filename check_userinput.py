import requests

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
    #Users is required to input the website they want to check
    url = input("Enter the website you want to check: ")
  
    #Lets make sure that the url is the correct format, if not lets add https:// 
    if not url.startswith("http"):
        url = "https://" + url
    if is_website_up(url):
        print(f"{url} is up!")
    else:
        print(f"{url} is down!")

if __name__ == "__main__":
    main()




