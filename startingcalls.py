import requests
import json

def get_posts():
    url = 'https://opendata.adsb.fi/api/v2/mil'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():
    posts = get_posts()

    if posts:
        print('aircrafts:', posts['ac'])          
        print('error message:', posts['msg'])    
        print('time (now):', posts['now'])        
        print('aircraft count:', posts['total'])  
        print('capture time:', posts['ctime'])           
        print('process time:', posts['ptime']) 

        with open("aircraftSurveillance/aircraft_data.json", "w") as f:
            json.dump(posts, f, indent=4)         

        if posts['ac']:
            first = posts['ac'][0]
            print('first callsign:', first.get('flight'))
    else:
        print('Failed to fetch posts from API.')

if __name__ == "__main__":
    main()