import requests

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

if response.status_code == 200:
    user_data = response.json()
    # print(user_data)
    for user in user_data:
        name = user.get('name', 'N/A')
        username = user.get('username', 'N/A')
        email = user.get('email', 'N/A')
        # print(name)
        # print(username)
        print(f"Name: {name}\n Username: {username}\n Email: {email}\n")
    
else:
    print(f"Failed to retrieve user data. Status code: {response.status_code}")
