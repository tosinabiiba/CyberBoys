import requests
import os

# List of anime IDs
anime_ids = ['Naruto', 'One Piece', 'Death Note', 'Fullmetal Alchemist']

# Loop through the list of anime IDs
for anime_id in anime_ids:
    # Get anime data from Jikan API
    anime_url = f'https://api.jikan.moe/v4/anime/Naruto/pictures'
    anime_data = requests.get(anime_url).json()
    if anime_data:
        # Get the cover art URL
        image_url = anime_data.get('image_url', '')
        if image_url:
            # Download the image
            image_data = requests.get(image_url).content
            # Save the image
            filename = anime_data['title'] + ".jpg"
            with open(filename, 'wb') as image_file:
                image_file.write(image_data)
            print(f'{anime_data["title"]} image saved!')
        else:
            print(f"{anime_id} doesn't contain an image_url")
    else:
        print(f"No data found for anime_id: {anime_id}")
