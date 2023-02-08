import requests, lxml, json, time, tldextract
from bs4 import BeautifulSoup

# Specify User Agent
headers = {
"User-Agent":
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

###############
listOfKeywords = ["What is python"]
numberOfTimes = 1

for keyword in listOfKeywords:
  print(keyword)
  for _ in range(numberOfTimes):
    payload = {'q': keyword}
    html = requests.get("https://www.google.com/search?q=",params=payload,headers=headers)
    status_code = html.status_code

    if status_code == 200:
      response = html.text
      soup = BeautifulSoup(response, 'lxml')

      with open("output.html","w", encoding="utf-8") as file:
        file.write(str(soup))

      htmlData = soup.find(id='main')
      if (htmlData):

        for container in htmlData.findAll('div',class_='Gx5Zad fP1Qef xpd EtOod pkphOe'):
          try:
            webTitle = container.find('div',class_='BNeawe vvjwJb AP7Wnd UwRFLe').text
          except:
            webTitle = 'N/A'

          try:
            link_tag = container.find('div',class_='egMi0 kCrYT').find('a')
            link = link_tag["href"]
            #print("link :",link)
          except:
            link = 'N/A'

          print("Website Titles :",webTitle)
          print("link :", link)
          print()

      time.sleep(1)
      print('------------------------------------------')

