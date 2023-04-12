#  QUES  : What is meant by stateless nature in RestAPI?
# ANS : As per the REST architecture, the server does not store any state about the client session on the server-side .

# ---------------------------------------------------------------------------------------------------------------------------------

#  QUES : 
# 403, 503, 301 Status Codes?
# Ans:-
#403 Forbidden: This status code means that the client does not have permission to access the requested resource. 
#This may be due to authentication issues or because the client does not have the necessary permissions to access the resource.

#503 Service Unavailable: This status code means that the server is currently unavailable or unable to handle the request. 
#This may be due to server overload, maintenance, or other temporary issues. The client should try again later.

#301 Moved Permanently: This status code means that the requested resource has been permanently moved to a new URL. 
#The client should update its bookmarks or links to the new URL.
#The server typically includes the new URL in the response body or header field to help the client redirect to the new location.

# -----------------------------------------------------------------------------------------------------------------------------------



import requests 
import json

# GET method

dogs_url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(dogs_url)
print(type(dogs_url))
print(response)
print(response.json())

# # POST method

# dogs_url = "https://dog.ceo/api/breeds/image/random"
breed = {"Breed":"Pit Bull" ,"Age":"4 months" , "color" :"Grey"}
response = requests.post(dogs_url , json = breed)
print(type(dogs_url))
print(response)
print(response.json())

# PUT method 

# dogs_url = "https://dog.ceo/api/breeds/image/random"
breed = {"color" :"white"}
response = requests.put(dogs_url , json = breed)
print(type(dogs_url))
print(response)
print(response.json())

# PATCH method

# dogs_url = "https://dog.ceo/api/breeds/image/random"
breed = {"Breed" :"German Sheferd"}
response = requests.patch(dogs_url , json = breed)
print(type(dogs_url))
print(response)
print(response.json())

# DELETE method
response = requests.delete(dogs_url)
print(response)
print(response.json())
