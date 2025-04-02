import requests
import os
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Ensure you have the required libraries installed:
# pip install requests Pillow python-dotenv
# This script searches for images using the Unsplash API, saves the search results to a text file,
# and allows the user to download a specified number of images.

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")  # Replace with your actual access key

UNSPLASH_URL = 'https://api.unsplash.com/search/photos'

def search_images(query):
    params = {
        'query': query,
        'client_id': UNSPLASH_ACCESS_KEY,
        'per_page': 10  # Number of images per request
    }
    response = requests.get(UNSPLASH_URL, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print("Error:", response.status_code)
        return []
    
def save_search_results(images, filename ='search_results.txt'):
    with open(filename, 'a') as file:
        for index, img in enumerate(images):
            file.write(f"Image {index + 1}:\n")
            file.write(f"Description: {(img.get('description', 'No description') or 'No description').upper()}\n")
            file.write(f"Full URL: {img['urls']['full']}\n")
            file.write("\n")  # Add a blank line between images
    print(f"Search results saved to {filename}")

def download_image(image_url, image_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.save(image_path)  # Save the image locally
    else:
        print("Error downloading image:", response.status_code)

def main():
    # Prompts the user for a keyword
    query = input("\nEnter a keyword or category to search for images: ")
    images = search_images(query) # Search for images
    
    if images: # If images are found, displays the results
        print(f"\nFound {len(images)} images:\n") 
        for index, img in enumerate(images):
            description = (img.get('description', 'No description') or 'No description').upper()
            print(f"Image {index + 1}:")
            print(f"{description}")
            print(f"URL: {img['urls']['full']}")
            print()  # Add a blank line between images
        
        # Save the results to a txt file
        save_search_results(images)
        
        # Ask user how many images to download
        while True:
            try:
                num_images = int(input("\nHow many images do you want to download (1-10)? "))
                print()
                if 1 <= num_images <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Download the specified number of images and save them locally
        for index in range(num_images):
            image_path = f"image_{index + 1}.jpg"
            download_image(images[index]['urls']['full'], image_path)
            description = (images[index].get('description', 'No description') or 'No description').upper()
            print(f"Downloaded Image {index + 1} to {image_path} - {description}")
            print()
    else:
        print("No images found.")

if __name__ == "__main__":
    main()