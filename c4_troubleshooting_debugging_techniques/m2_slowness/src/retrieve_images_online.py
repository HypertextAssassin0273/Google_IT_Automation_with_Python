#!/usr/bin/env python3

# retrieves random pictures from web using the image API 'Unsplash'. [[ helper script for thumbnail_generator.py ]] 

import argparse, os, requests


def fetch_random_images(api_url, access_key, num_images, output_dir):
    headers = {"Authorization": f"Client-ID {access_key}"}
    
    for i in range(num_images):
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            image_url = data["urls"]["full"]
            image_response = requests.get(image_url, stream=True)
            image_response.raise_for_status()

            image_filename = os.path.join(output_dir, f"img_{i + 1}.jpg")
            with open(image_filename, "wb") as f:
                for chunk in image_response.iter_content(1024):
                    f.write(chunk)

            print(f"Downloaded: {image_filename}")
        except Exception as e:
            print(f"Failed to download image {i + 1}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Download random images from the web.")
    parser.add_argument("num_images", type=int, nargs="?", default=5, 
                        help="Number of random images to download (default: 5)")
    
    args = parser.parse_args()

    num_images = args.num_images
    output_dir = "images"
    os.makedirs(output_dir, exist_ok=True)

    with open("ACCESS_KEY") as f:
        access_key = f.read().strip() # YOUR_UNSPLASH_ACCESS_KEY

    api_url = "https://api.unsplash.com/photos/random"

    print(f"Downloading {num_images} random images...")
    fetch_random_images(api_url, access_key, num_images, output_dir)
    print(f"Download completed. Images saved in '{output_dir}'.")


if __name__ == "__main__":
    main()


# NOTE: The ACCESS_KEY is a placeholder for the actual access key that you need to obtain from Unsplash.
# SIDE-NOTE: we can improve the script by adding concurrency to download multiple images simultaneously.
