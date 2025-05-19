# Cognifyz Technology Software Development Intern 
# Level 3 :-
# Task 6
# Create a program for interactive web scraping
# Objective: Fetch data from a website and present it in a user-friendly way using a simple web scraping library.

from bs4 import BeautifulSoup
import requests


headers = {"User-Agent": "Mozilla/5.0"}
URl=input("Enter the URL of The Chosen Website :  ")
selector=input("Enter the selector for the target that u want to scrape Ex.'tb.class' a OR 'h3 a'  :  ")


try:
    response=requests.get(URl,headers=headers)
    if response.status_code == 200:
         webpage_html=response.text
         soup=BeautifulSoup(webpage_html,"html.parser")
         tag=soup.select(selector)
         if tag == [] or tag == None:
            print(" Invalid Selector Provided ")
         else:
             print(f"Here is Your Scraped Data from {URl}")
             for title in tag:
                 print(title.text)
    else:
        print("Failed to fetch the webpage, status code:", response.status_code)

   
except Exception:
    print("Invalid URL")
        
    






