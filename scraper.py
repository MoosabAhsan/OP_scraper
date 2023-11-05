import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def download_image(url, folder_path):
    response = requests.get(url)

    if response.status_code == 200:
        # Extract the filename from the URL
        filename = os.path.join(folder_path, os.path.basename(urlparse(url).path))

        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Error downloading image. Status code: {response.status_code}")

def scrape_images(url, folder_path):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img', src=True)

        cdn_images = [urljoin(url, img['src']) for img in images if img['src'].startswith('https://cdn.onepiecechapters.com') and img['src'] not in ['https://cdn.onepiecechapters.com/file/CDN-M-A-N/ign.png', 'https://cdn.onepiecechapters.com/file/CDN-M-A-N/dragonball.png']]

        for img_url in cdn_images:
            download_image(img_url, folder_path)
    else:
        print(f"Error fetching the page. Status code: {response.status_code}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape images from a webpage and save them to a folder')
    parser.add_argument('-i', '--url', required=True, help='URL of the webpage to scrape')
    parser.add_argument('-o', '--output_folder', required=True, help='Folder to save the images')
    args = parser.parse_args()

    # Create output folder if it doesn't exist
    os.makedirs(args.output_folder, exist_ok=True)

    scrape_images(args.url, args.output_folder)

