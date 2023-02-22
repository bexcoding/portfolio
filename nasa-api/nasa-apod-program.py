'''
communicates with the nasa apod (astronomy picture of the day) api. no input is required.
the code gets a json response from the api and takes the given url to the image.
the image is saved in the folder of space photos
'''
import shutil #allows the image to be saved
import requests #allows http requests to be called to the url

print("Retrieving NASA's 'Astronomy Picture of the Day'.\nDownloading ...\n")
#after creating an api key with nasa, insert it into the api_key variable below
#do not use spaces. this call will not work without your api key inserted here.
api_key = ""
url = "https://api.nasa.gov/planetary/apod?api_key="
#creates json type of dictionary for information from url
response = requests.get(url+api_key).json()
#uncomment following line to see json response in command line
#print(response)
date = str(response.get('date'))
img_url = response.get('hdurl')
#type of file ie. .png, .jpg, etc
img_type = img_url[-4:]
#stream option allows data to not be interrupted
img = requests.get(img_url, stream = True)
#file name of image that is downloaded "source, date, image type"
img_file_name = "nasa-apod-" + date + img_type
#checks if status is 200 (successful)
if img.status_code == 200:
    with open(img_file_name, 'wb') as f:
        shutil.copyfileobj(img.raw, f)
    print('Image sucessfully downloaded. File name is:', img_file_name)
else:
    print('Image could not be retrieved.')
