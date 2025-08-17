import requests

api_key = 'API_KEY_GOES_HERE' # Sets a string variable as the API key generated from the Openwewather Website

city = input('Enter city name: ') # You can enter any city here, city assgin a string a variable from the input function

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric' # The units = metric can be ommited / kepted depending on how you want the temprature to be formated.


response = requests.get(url) # Send a HTTP GET request passing the url assigned variable as the argument 
data = response.json() # Returns the response objects in relation to the requests.get method, we call the .json method to convert it into a Python Dictorionary / List


if response.status_code == 200: # HTTP code 200 means it  was sucessful, therefor if response.statuscode is equal to 200 then process with flow controt statement and move to the indented code below
        temperature = data['main'] # using the interactive shell, I ran print(data.items()) to print out the Key:vlaue pairs from the dictionary stored in data and picked out the keys related to the values I needed, Temp is the actual temperature
        descr = data['weather'][0]['description'] # description of the current weather
        print(f"The Temperature now is {temperature['temp']} °C & The maximum temperature will be {temperature['temp_max']} °C") # f string to import the variables into the string, therefore we will print the variables with specific text
        print(descr) # print description of the current weather 

else:
    print('Error 404, Weather could not be found') # If everything else fails i.e error 404 and lack of response from the HTTP get requests, then print this statement.
