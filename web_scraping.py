import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

from requests.api import request

print("hello")
page = 0
result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page}")

src = result.content

soup = BeautifulSoup(src,"lxml")

title = []
company = []
location = []
skills = []
links = []
salary = []
job_res = []
date = []

job_titles = soup.find_all("h2",{"class":"css-m604qf"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
locations_names = soup.find_all("span",{"class":"css-5wys0k"})
job_skills = soup.find_all("div",{"class":"css-y4udm8"})
date_one = soup.find_all("div",{"class","css-4c4ojb"})
date_two = soup.find_all("div",{"class","css-do6t5g"})
dateall = [*date_one , *date_two]




for i in range(len(job_titles)):
    title.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    company.append(company_names[i].text)
    location.append(locations_names[i].text)
    skills.append(job_skills[i].text)
    date.append(dateall[i].text)
    


for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src ,"lxml")
    job_responsabilites = soup.find("div",{"class","css-1t5f0fr"}).ul
    respon_text = ""
    for li in job_responsabilites.find_all("li"):
        respon_text+= li.text +"| "
    respon_text = respon_text[:-2]
    job_res.append(respon_text)
    
fileList = [title,company,location,skills,links,salary,job_res,date] #this is lists
exported = zip_longest(*fileList)

with open("/Users/El.Sa7er/Downloads/python/myfile.csv","w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job title","company name", "locations","job skills","links","salary","job_responsabilities","date"])
    wr.writerows(exported)
print("end of the code")
