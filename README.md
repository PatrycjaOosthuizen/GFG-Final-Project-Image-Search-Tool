# GFG-Final-Project-Image-Search-Tool
This program was created for the Code First Girls final project: a simple Python tool that lets you search for images using an API.

## Image Search and Download Tool

Python script that allows users to search for images on Unsplash and download them locally.

---

### Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Requirements](#requirements)
- [API Key](#api)
- [Troubleshooting](#troubleshooting)

---

### Installation

To use this script, you'll need to have Python installed on your system. You can download the latest version from the official Python website.

Once you have Python installed, you can clone this repository or download the script manually.

---

### Usage

1. Run the script using `python image_search.py`.
2. Enter a keyword or category to search for images.
3. The script will display a list of images found, along with their URLs.
4. You can then choose how many images to download (between 1 and 10).
5. Downloaded images will be saved as JPEG files in the same directory as the script. Please note that these images will be replaced with new ones after each search, so it's recommended to save the images you want to keep to a separate folder or rename them to a unique name to avoid losing them.

### Features

- Search for images on Unsplash using a keyword or category.
- Display search results with image URLs and descriptions.
- Download selected images and save them to the current directory.
- Save search results to a file (search_results.txt).

---

### Requirements

- Python 3.x
- `requests` library (install with `pip install requests`)
- `Pillow` library (install with `pip install pillow`)
- `Unsplash API` access key (replace `UNSPLASH_ACCESS_KEY` in the code)
- `io` library (imported as `BytesIO` in the script, no additional installation required because it is a built-in `Python library`, used to handle image data as bytes for `Pillow`)

---

### Configuration

- You'll need to replace the `UNSPLASH_ACCESS_KEY` variable in the script with your own `Unsplash API key`. You can obtain a `free API key` by creating an account on the [Unsplash website](https://unsplash.com/developers).
- Adjust the `per_page` parameter in the `search_images` function to change the number of images returned per request.

---

### Troubleshooting

- If you encounter any issues with the script, check the console output for error messages.
- Make sure you have the required libraries installed (requests and Pillow).
- If you're having trouble with the API key, check that you've replaced the UNSPLASH_ACCESS_KEY variable with your own API key.

---

### License

This code is released under the MIT License. See the [LICENSE](./LICENSE) file for details.
