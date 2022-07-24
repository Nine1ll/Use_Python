from google_images_download import google_images_download   # importing the library

response = google_images_download.googleimagesdownload()   # class instantiation

# creating list of arguments
arguments = {"keywords": "Polar bears, baloons, Beaches", "limit": 20, "print_urls": True}
paths = response.download(arguments)   # passing the arguments to the function
print(paths)   # printing absolute paths of the downloaded images
