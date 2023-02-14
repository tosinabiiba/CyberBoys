import requests
import os

# List of anime names
anime_list = ['Naruto', 'One Piece', 'Death Note', 'Fullmetal Alchemist']

# Loop through the list of anime names
for anime in anime_list:
    # Search for anime image
    search_url = f'https://www.google.com/search?q={anime}&tbm=isch'
    search_result = requests.get(search_url)
    search_result.raise_for_status()

    # Get the first image result
    image_url = search_result.json()['items'][0]['link']

    # Download the image
    image_data = requests.get(image_url).content
    
    # Save the image
    filename = anime + ".jpg"
    with open(filename, 'wb') as image_file:
        image_file.write(image_data)
    print(f'{anime} image saved!')
