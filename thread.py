import concurrent.futures
import requests
import time


start = time.perf_counter()

images = [
    'https://images.unsplash.com/photo-1641810780702-57d275dfdc59?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw0fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60',
    'https://images.unsplash.com/photo-1641763773713-212ebd0623b5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw1fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60',
    'https://images.unsplash.com/photo-1641664426107-3a51853d2224?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw3fHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60',
]


def download(image):
    image_byte = requests.get(image).content
    image_name = image.split('/')[3]
    image_name = f'{image_name}.jpg'
    with open(image_name, 'wb') as f:
        f.write(image_byte)
        print(f'Image {image_name} has been downloaded')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download, images)


performed = time.perf_counter()
print(f'Finished in {performed-start} second(s)')
