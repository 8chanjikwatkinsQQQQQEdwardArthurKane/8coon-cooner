import requests as killpedos
from bs4 import BeautifulSoup
# from requests_toolbelt import MultipartEncoder

# import json, random, ssl, string
# import base64, threading, string, random, time
import concurrent.futures as porn

# import tbell_image_base
# import TwoCaptcha

# import glob, re
# sneed = glob.glob("img/*")
# print(sneed)

# # #Images
# from PIL import Image
# from io import BytesIO

def randomString(string_length):
        input = string.ascii_lowercase + string.digits
        return ''.join(random.choice(input) for i in range(string_length))

# # # # # # # def genProxy():
# # # # # # #     sessid_luminati = "session-"+randomString(9)
# # # # # # #     country = "us"
# # # # # # #     return {'http': 'http://'+KikeIP,'https': 'https://'+KikeIP}


threads_scrapping_task_dict = []
database_scrapped_filtered_messages = []

json_data = killpedos.get("https://8kun.top/qresearch/catalog.json"
                        # , proxies=genProxy()
                        ).json()

for x in json_data:
        for y in x['threads']:
                # y['com']=""
                # y['sub']=""
                # y['embed']=""
                # y['embed_thumb']=""

                if "Research General" in y['sub']:#As I am writing this comment 2022-08-08 it was a mistake only scrapping generals. anyways "Quality schzio research"
                        try:
                                threads_scrapping_task_dict.append(y['no'])
                        except:
                                pass

# threads_scrapping_task_dict = [threads_scrapping_task_dict[5]]
print(threads_scrapping_task_dict)
def task_view_page(th_no):
        json_data = killpedos.get(f"https://8kun.top/qresearch/res/{th_no}.json",
                # proxies=genProxy()
                ).json()
        y = json_data['posts']
        for x in y:#could be multithreaded but fuck it..  I fucked all of the catalog... anyways so this scrapper is pointless. 
                a = x['com']
                soup = BeautifulSoup(a, 'html.parser')
                b = soup.find_all('p')

                textbuild = ""
                for x in b:
                        if x.find_all('span', {'class':'heading'}):
                                textbuild += f"=={ x.get_text() }==\n"
                        else:
                                textbuild += f"{ x.get_text() }\n"
                        # textbuild.append("dfsdfe")
                database_scrapped_filtered_messages.append(textbuild)
                # print(a)
                # print(soup.get_text())
                
                # data = re.findall(r'<.*?>', '', a)
                # print(data)



with porn.ThreadPoolExecutor(max_workers=200) as e:
    future = e.map(task_view_page,
                        threads_scrapping_task_dict)

with open('8kun_schzio_scrapped_data.json', 'w') as f:
    json.dump(database_scrapped_filtered_messages
                                                , f)
