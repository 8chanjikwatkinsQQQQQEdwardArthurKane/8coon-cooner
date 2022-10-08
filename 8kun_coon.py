import requests as killpedos
from bs4 import BeautifulSoup
from requests_toolbelt import MultipartEncoder

import json, random, ssl, string, re
import base64, threading, string, random, time
import concurrent.futures as porn
import socket
import tbell_image_base
from twocaptcha import TwoCaptcha
from anticaptchaofficial.hcaptchaproxyless import *
import calendar, datetime

# import glob
# sneed = glob.glob("img/*")
# print(sneed)

# # #Images
# from PIL import Image
# from io import BytesIO

def randomString(string_length):
  input = string.ascii_lowercase + string.digits
  return ''.join(random.choice(input) for i in range(string_length))

##Add scrapper
##Add random ids to scrap
def genProxy():
  sessid_luminati = "session-"+randomString(9)
  country = "ca"

  superproxyip=socket.gethostbyname('zproxy.lum-superproxy.io')
  holavpn_victim = f'lum-customer-{ global_file_settings["lum_user"] }-zone-{ global_file_settings["lum_zone"] }-country-{country}-{sessid_luminati}-route_err-pass_dyn-dns-remote:{ global_file_settings["lum_pass"] }@{superproxyip}:22225'
  return {'http': 'http://'+holavpn_victim,'https': 'https://'+holavpn_victim}


with open("8kun_schzio_scrapped_data.json", 'r') as f:
  a = json.load(f)
print("Schzio, communicating walls game", json.dumps(a[random.randint(2,50000)]))

global_file_settings={}
with open("SETTINGS.json", 'r') as f:
  global_file_settings = json.load(f)
print(global_file_settings)

def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return base64.b64decode(data, altchars)


#Because we use AI now. this is not needed.
archive = """
  CAPTCHAKEY = "getyourown 10$ shekels"
  domain = "2captcha.com"
    def inPageCAPTCHA(s, useragent):
      r = s.get("https://sys.8kun.top/8kun-captcha/entrypoint.php?mode=get&extra=abcdefghijklmnopqrstuvwxyz",headers={
          'Upgrade-Insecure-Requests': '1',
          'Origin': 'https://sys.8kun.top',
          'x-requested-with': 'XMLHttpRequest',
          "accept-encoding": "identity",

          'User-Agent': useragent,
      })

      captcha_cookie = r.json()['cookie']
      captcha_html = r.json()['captchahtml']

      myData={
        #8kun
        'base64Str': str(),#The image in base64
        'captcha_cookie': str(),#Captcha cookie

        #2captcha
        'captcha_id': str(),#Captcha2 id
        'captcha': str(),#actual captcha response from 2captcha
      }

      soup = BeautifulSoup(captcha_html, 'html.parser')
      img = soup.find('image')
      img = img['src']
      
      myData['base64Str']=img

      # # image_data = re.sub('^data:image/.+;base64,', '', img)
      # # im = Image.open(BytesIO(base64.b64decode(image_data)))
      # # im.show()
      
      
      dataA={
        'key': f'{CAPTCHAKEY}',
        'method': 'base64',
        'recaptcha': '0',
        'json': '1',
        'textinstructions': 'Sensetive to letters.. CaPs<<--- GOOD',
        'body': myData['base64Str']
      }

      myData['captcha_id'] = str(s.post("https://2captcha.com/in.php", data=dataA).json()['request'])

      def SolveRecaptcha(CAPTCHAKEY,captcha_id):
        recaptcha_answer = s.get(f"http://2captcha.com/res.php?key={CAPTCHAKEY}&action=get&id={captcha_id}").text
        #print("Solving captcha...")
        while 'CAPCHA_NOT_READY' in recaptcha_answer:
          time.sleep(1)
          recaptcha_answer = s.get(f"http://2captcha.com/res.php?key={CAPTCHAKEY}&action=get&id={captcha_id}").text
        try:
          recaptcha_answer = recaptcha_answer.split('|')[1]
        except:
          pass
        print("Solved captcha.")
        return recaptcha_answer

      myData['CAPTCHAKEY']=CAPTCHAKEY
      captcha = SolveRecaptcha(CAPTCHAKEY,myData['captcha_id'])
      print(captcha)#Able to print captcha (after we used "base64Str"), and then crashes and
      
      
      return captcha, captcha_cookie
    def make_captcha_session(s1, useragent):
        while True:
          s = killpedos.Session()
          
          headers = {
              # 'Connection': 'close',
              # 'Pragma': 'no-cache',
              # 'Cache-Control': 'no-cache',
              'Upgrade-Insecure-Requests': '1',
              'Origin': 'https://sys.8kun.top',
              'x-requested-with': 'XMLHttpRequest',
              "accept-encoding": "identity",

              'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': useragent,
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              # 'Sec-Fetch-Site': 'same-origin',
              # 'Sec-Fetch-Mode': 'navigate',
              # 'Sec-Fetch-User': '?1',
              # 'Sec-Fetch-Dest': 'document',
              'Referer': 'https://sys.8kun.top/dnsbls_bypass.php',
              # 'Accept-Language': 'en-US,en;q=0.9',
          }
          # headers = {
          #   'Connection': 'keep-alive',
          #   'Pragma': 'no-cache',
          #   'Cache-Control': 'no-cache',
          #   'Upgrade-Insecure-Requests': '1',
          #   'Origin': 'https://sys.8kun.top',
          #   'Content-Type': 'application/x-www-form-urlencoded',
          #   'User-Agent': 'Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4324.150 Safari/537.36',
          #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          #   'Sec-Fetch-Site': 'same-origin',
          #   'Sec-Fetch-Mode': 'navigate',
          #   'Sec-Fetch-User': '?1',
          #   'Sec-Fetch-Dest': 'document',
          #   'Referer': 'https://sys.8kun.top/dnsbls_bypass.php',
          #   'Accept-Language': 'en-US,en;q=0.9',
          # }

          r = s1.get("https://sys.8kun.top/dnsbls_bypass.php", headers=headers)

          soup = BeautifulSoup(r.text, 'html.parser')
          img = soup.find('image')
          
          captcha_cookie = soup.find('input',{'class':'captcha_cookie'})
          base64Str = img['src']

          # image_data = re.sub('^data:image/.+;base64,', '', img['src'])
          # im = Image.open(BytesIO(base64.b64decode(image_data)))
          # im.show()

          data={
            'key': f'{CAPTCHAKEY}',
            'method': 'base64',
            'recaptcha': '0',
            'json': '1',
            'textinstructions': 'Sensetive to letters.. CaPs<<--- GOOD',
            'body': base64Str
          }


          captcha_id = s.post(f"https://{ domain }/in.php", data=data).json()['request']
          def SolveRecaptcha(CAPTCHAKEY,captcha_id):
            recaptcha_answer = s.get(f"http://2captcha.com/res.php?key={CAPTCHAKEY}&action=get&id={captcha_id}").text
            #print("Solving captcha...")
            while 'CAPCHA_NOT_READY' in recaptcha_answer:
              time.sleep(5)
              recaptcha_answer = s.get(f"http://2captcha.com/res.php?key={CAPTCHAKEY}&action=get&id={captcha_id}").text
            recaptcha_answer = recaptcha_answer.split('|')[1]
            # print("Solved captcha.")
            return recaptcha_answer


          captcha = SolveRecaptcha(CAPTCHAKEY,captcha_id)

          data = {
            'captcha_text': f'{captcha}',
            'captcha_cookie': f'{captcha_cookie["value"]}',
            'tos_agree': 'on'
          }

          #############################
          r = s1.post('https://sys.8kun.top/dnsbls_bypass.php', headers=headers, data=data)

          if "You failed the CAPTCHA" in r.text:
            req_data = s.get(f'https://{ domain }/res.php?key={CAPTCHAKEY}&action=reportbad&id={captcha_id}').text
            # print("reported BADLY", req_data)
            continue
          elif "Success!" in r.text:
            req_data = s.get(f'https://{ domain }/res.php?key={CAPTCHAKEY}&action=reportgood&id={captcha_id}').text
            print("reported GOOD", req_data)
            
            # with open(f"captcha_database/{captcha}.png", "wb") as f:
            #   image_data = re.sub('^data:image/.+;base64,', '', base64Str)
            #   f.write(base64.b64decode(image_data))

            break#Breaks to "break the while-loop", therefore it will stop the function. and continue with the bot. 

"""

# archive2 = """
def hf_ai_captcha(s, useragent, is_session):
  # s = requests.Session()
  # s.proxies = genProxy()
  while True:
    ############################################
    headers_8kun = {
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.9',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      # Requests sorts cookies= alphabetically
      # 'Cookie': 'serv=%7B%22https%3A%5C%2F%5C%2F8kun.top%5C%2F%22%3Atrue%7D; ans=hLTz; tkn=ef0c6d0fb63fdce29b4b939a0d074782c36f7ba327a9ba041ed7060f29cdfb6d',
      'Origin': 'https://8kun.top',
      'Pragma': 'no-cache',
      'Referer': 'https://8kun.top/',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-site',
      'Sec-GPC': '1',
      'User-Agent': useragent,
    }

    url = "https://sys.8kun.top/kmn_popup.php?_="+str(calendar.timegm(datetime.datetime.utcnow().utctimetuple())) + str(random.randint(100,999))
    r = s.get(url, headers=headers_8kun)
    
    if "Tm9FbnRyb3B5" in r.text:
      raise
    session_hash=randomString(12)
    json_data = {
      'fn_index': 0,
      'data': [ "te_be_changed" ],
      'action': 'predict',
      'session_hash': session_hash,
    }
    # print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    img = soup.find('image')['src']
    # captcha_cookie = soup.find('input',{'class':'captcha_cookie'})['value']
    json_data['data'][0] = img
    ###############################################################################

    

    project_path=random.choice(main.projects_git)

    # r = killpedos.post('http://31163.gradio.app/api/predict/', headers={
    # r = killpedos.post('http://127.0.0.1:7860/api/predict/', headers={
    r = s.post(f'https://hf.space/embed/{ project_path }/api/predict/', headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    }, json=json_data)
    average_duration = r.json()['average_duration']
    duration = r.json()['duration']
    captcha = r.json()['data'][0]

    if is_session != True:
      return captcha, captcha_cookie
    # print(captcha_cookie, captcha)
    data = {
      'captcha_text': f'{captcha}',
      # 'captcha_cookie': f'{captcha_cookie}',
      # 'tos_agree': 'on'
    }
    r = s.post("https://sys.8kun.top/kmn_popup.php", headers=headers_8kun, data=data)
    # print(r.text)

    # if "but the origin server for this website is offline or unreachable" in r.text:
    #   continue#Continues the loop. Because we got an error
    if "Captcha verification failed" in r.text:
      main.average_duration = average_duration
      main.duration = duration
      # print(f"Captcha failed average_duration:{average_duration}, duration:{duration}")
      main.captchas_failed += 1
      continue#Continues the loop. Because we got an error
    elif "uccess" in r.text:
      # print("Success!! we solved a captcha!!!!")
      main.captchas_worked += 1

      # save_pictures=True
      # if save_pictures:
        # print(f"captcha_database/{captcha}.png")
        # with open(f"captcha_database/{captcha}.png", "wb") as f:
        #   image_data = re.sub('^data:image/.+;base64,', '', img)
        #   f.write(base64.b64decode(image_data))
      return None, None# break#Breaks because, we got a session! #Breaks to "break the while-loop", therefore it will stop the function. and continue with the bot. 
# """
def two_captcha_captcha(s, useragent, is_session):
  # s = requests.Session()
  # s.proxies = genProxy()
  while True:
    ############################################
    headers_8kun = {
      'authority': 'sys.8kun.top',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'accept-language': 'en-US,en;q=0.9',
      'cache-control': 'no-cache',
      'origin': 'https://sys.8kun.top',
      'pragma': 'no-cache',
      'referer': 'https://sys.8kun.top/hcaptcha.php',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'sec-gpc': '1',
      'upgrade-insecure-requests': '1',
      'user-agent': useragent,

    }

    r = s.get('https://sys.8kun.top/hcaptcha.php', headers=headers_8kun)
    if ">Origin Server Offline<" in r.text:
      raise Exception("cdn_bullshit","")#Nginx ip-range-ban
    elif "ech CDN is online in " in r.text:
      raise Exception("cdn_bullshit","")#Nginx ip-range-ban
    elif "center>nginx" in r.text:
      raise Exception("nginx_error_or_ban","NginX was Found.")#Nginx ip-range-ban

    config = {
      'server':           '2captcha.com',
      'apiKey':           global_file_settings['2captcha_api_key'],
      # 'softId':            123,
      # 'callback':         'https://your.site/result-receiver',
      'defaultTimeout':    120,
      'recaptchaTimeout':  600,
      'pollingInterval':   2,
    }
    solver = TwoCaptcha(**config)
    captcha = solver.hcaptcha(sitekey='69f74426-f045-41d7-bbb9-3a2b44593b2e',
                            url='https://sys.8kun.top/hcaptcha_popup.php'
                            )['code']
    # print(captcha)





    # solver = hCaptchaProxyless()
    # # solver.set_verbose(1)
    # solver.set_key(    global_file_settings['anticaptcha_key']   )
    # solver.set_website_url("https://sys.8kun.top/hcaptcha.php")
    # solver.set_website_key("69f74426-f045-41d7-bbb9-3a2b44593b2e")
    # solver.set_user_agent(useragent)
    # captcha = solver.solve_and_return_solution()




    data = {
      'g-recaptcha-response': f'{captcha}',
      'h-captcha-response': f'{captcha}',
      'tos_agree': 'on',
    }
    
    r = s.post('https://sys.8kun.top/hcaptcha.php', headers=headers_8kun, data=data)

    if "but the origin server for this website is offline or unreachable" in r.text:
      continue#Continues the loop. Because we got an error
    if "You failed the CAPTCHA" in r.text:
      main.average_duration = average_duration
      main.duration = duration
      # print(f"Captcha failed average_duration:{average_duration}, duration:{duration}")
      main.captchas_failed += 1
      continue#Continues the loop. Because we got an error
    elif "title>Success!</title" in r.text:
      # print("Success!! we solved a captcha!!!!")
      main.captchas_worked += 1

      # save_pictures=True
      # if save_pictures:
        # print(f"captcha_database/{captcha}.png")
        # with open(f"captcha_database/{captcha}.png", "wb") as f:
        #   image_data = re.sub('^data:image/.+;base64,', '', img)
        #   f.write(base64.b64decode(image_data))
      return None, None# break#Breaks because, we got a session! #Breaks to "break the while-loop", therefore it will stop the function. and continue with the bot. 



def rand_th_id(th_id):
  output_th_id = th_id[:-3]
  # print(output_th_id)
  for x in range(3):
    output_th_id += str(random.randint(0,9))
  return output_th_id
# print(rand_th_id("16500431"))

def action():
    def check_ban():
      None
    def do_post(threadId, useragent, post_openpost):# Add a shared parameter so it can increase the number of tries if empty thread
        # print("Goy Watkins(the kid toucher), and his pedo son is fucked lol")

        comment=random.choice(a)
        while len(comment)<13:
          # print('smaller than hell',comment)
          comment=random.choice(a)

        def compute_rand_reply_id(matchobj):
          try:
            return ">>"+random.choice(  main.threads_replies_db[threadId] )
          except IndexError:
            # print("Sneed23")
            return ">>"+rand_th_id(threadId)


        # comment = ">>16500431\n>>16500431\n>>16500431 lb\nGriswald = G\nLawrence = L\nObergefell = O\n"
        try:comment = re.sub(r">>(.*)", compute_rand_reply_id, comment, 0)
        except:comment="weird error"
          

        fake_qanon_style_thread = f"#{str(random.randint(22187,23187))}"#for refrence (https://i.imgur.com/p85g0zu.png)
        comment = re.sub(r"(#\d{5})", fake_qanon_style_thread, comment, 0)
        if "DOUGH" in comment:
          comment += "--#HOOMAN-- is GHOSTED"

        # bestlife = tbell_image_base.randomize_image( random.choice(sneed) )
        data={
          'thread': f'{threadId}',

          'board': f'{main.board}',
          # 'name': f'{randomString(2)}##{randomString(9)}',
          'name': '',
          'email': '',
          'subject': '',

          'body': f'{comment}\n\n(The q-boomer known as Pedo Watkins, cant do load-balancing HAPROXY, sneed copium kek penis funny poop funny)',
          'password':f'{randomString(16)}',
          'embed': '',
          'json_response': '1',#sends a string and not a int?  ---- 8kun still sees it as fine. should be change but for now we will see if they use it as a miditgation against me.
          'post': 'New Reply',
          #'subject': f'{randomString(9)}',
          #'post': 'New Thread',
          'tor': 'null',
          
          'domain_name_post': '8kun.top',
          'file': 'undefined',
          'file2': 'undefined',
          # 'file': (randomString(random.randint(6,14))+'.jpg', tbell_image_base.randomize_image( bestlife ), 'image/jpeg'),
          

          'file3': 'undefined',
          'file4': 'undefined',
          'file5': 'undefined'
        }

        #Post a thread mode: 
        if post_openpost:
          # bestlife = tbell_image_base.randomize_image( random.choice(sneed) )

          data.pop("thread", None)# removes data['thread']
          data["page"] = "1"
          # data["subject"] = "Anti-Q \"Research\" General #22235: Use AIX 7.2, its unix. Dubya-gigachad edition.."
          data["subject"] = "חבורה של כאלה שמדברים לקירות (((Fortnite hacks 2020))) bobs pusy pls (((good morning)))امرك علينا سيدي علي النار نحنا نهد "
          comment = "Welcome to Q Research General\n\nWe are researchers who deal in open-source information, reasoned argument, and dank memes. We do battle in the sphere of ideas and ideas only.  We neither need nor condone the use of force in our work here.\n\n\"We hold these truths to be self-evident: that all men are created equal; that they are endowed by their Creator with certain unalienable rights; that among these are life, liberty, and the pursuit of happiness.\" \n\nVINCIT OMNIA VERITAS | SEMPER FIDELIS | WWG1WGA | QRESEARCH\n\nQ's Latest Posts\n\nWednesday 06.29.2022\n\n>>16552853 ————————————–——– What is at stake? Who has control? SURPRISE WITNESS. Who is Cassidy Hutchinson? Trust the plan.\n\n>>16950147 06.25.2022\n\n>>16950142 06.24.2022\n\nQ's Private Board\n\n>>>/projectdcomms/  &  Q's Trip-code: Q !!Hs1Jq13jV6\n\nFind Q drops here\n\nQresear.ch/q-posts, Qanon.pub, Qalerts.pub, OperationQ.pub. Qposts.online, 8kun.top/qresearch/, qposts.html, qaggregator.news/,  Qalerts.app, Qalerts.net, douknowq.com/134295/Q-Anon-Pub.htm, we-go-all.net/q.html\n\nQPosts Archives\n\n* QMap & Mirrors PDF: SCRIBD: https://www.scribd.com/document/419874308/Q-Anon-The-Storm-X-VII?secret_password=55SQ1tCYhuNR8ESzm50u\n\n* QPosts Archive, Searchable, interactive with user-explanations: qanon.pub qanon.app\n\n* QPosts Archive + RSS, Searchable, Analytics, Offsite Bread Archive: qanon.news\n\n* Spreadsheet QPosts Q&A and all images backup: https://docs.google.com/spreadsheets/d/1Efm2AcuMJ7whuuB6T7ouOIwrE_9S-1vDJLAXIVPZU2g\n\n* Q Raw Text Dumps: q-clock.com/q_raw.txt\n\n* Spreadsheet Timestamps/Deltas: docs.google.com/spreadsheets/d/1OqTR0hPipmL9NE4u_JAzBiWXov3YYOIZIw6nPe3t4wo/\n\n* Memo & OIG Report Links: 8kun.top/qresearch/res/426641.html#427188\n\n* Original, full-size images Q has posted: https://postimg.cc/gallery/29wdmgyze/\n\nQResearch Board\n\n>>15406428 Dough Resources thread (see links below for specifics)\n\nNew to QR?\n\n>>15406810 Overview |  >>16085354 Intro thread | >>15406442 Board Info, Offsite Bunkers, Optics | >>15406807 Suggested Follow\n\nThreads & Tools\n\n>>15557963 International Threads by Country\n\n>>15406811 Information Resources | >>16949985 Dedicated Research Threads\n\n>>16093637 Q Encyclopedia by ArchiveAnon | >>16092925 Q Video Archive by ArchiveAnon\n\nTOR Access\n\nTOR URL: http://8kun.top.4o5xwl3fsmzwys7edqxtohvva6ikxc6h7wt7el4ar3d5om6k2zz7yaqd.onion/qresearch/catalog.html [under REVISION]\n\nTOR Iwo Jima Banner: https://www.youtube.com/watch?v=MLCupx1UExg\n\nJoin Us\n\n>>15473043 , >>15492930, >>15600441  LEARN TO BAKE:  E-bakes, Quick Pic bakes, Baking Thread Index | >>15406808, >>15406802 LEARN DIGITAL WARFARE\n\n>>15406820 Meme Requests"
          comment = f"\n{randomString(30)}\n{randomString(30)}\n{randomString(30)} \n{randomString(30)} \n{randomString(30)} \n{randomString(30)} \n{randomString(30)}\n{randomString(30)}\n {randomString(16)} {randomString(16)} {randomString(16)}\n{randomString(16)}\n\n{randomString(16)}\n{randomString(16)}\n{randomString(16)}"
          comment = re.sub(r"Q", "Anti-Q", comment, 0)
          
          data["body"] = comment
          data["post"] = "New Thread"
          data["file"] = (randomString(random.randint(6,14))+'.jpg', tbell_image_base.randomize_image( random.choice(["kekpenis.png","bot research meme.png"]) ), 'image/jpeg')
        # data["file"] = (randomString(random.randint(6,14))+'.jpg', tbell_image_base.randomize_image( "kekpenis.png" ), 'image/jpeg')
        # data["file"] = (randomString(random.randint(6,14))+'.webm', "/home/ori/Downloads/kekpenis.webm", 'video/webm')
        
        data["file"] = (randomString(random.randint(6,14))+'.jpg', tbell_image_base.randomize_image(
          random.choice([
            "internet terror.png",
            '2022-07-25_14-31(1).png',
            'scrappingchud.jpg',
            'pinnedbotpost.jpg'
            
            'kekpenis.png',
            "hoe.png",
            "hoe2.png",
            "copium.jpg",
            ])
        ), 'image/jpeg')

        # captcha mode
        # if main.captcha_per_post_copemode:
        #   data["captcha_text"], data["captcha_cookie"] = hf_ai_captcha(s, useragent, False)
        
        # namefag = random.choice([True,False])
        # if namefag == False:
        #   data['name'] = 'BAKER (Schzio pedophile)'


        # image_mode = True
        # if image_mode:
        #   data['files'] = (randomString(random.randint(6,14))+'.jpg', tbell_image_base.randomize_image( bestlife ), 'image/jpeg')
        
        m = MultipartEncoder(
          fields=data
        )

        headers = {
          'User-Agent': useragent,
          'Accept': '*/*',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'identity',
          'Content-Type': m.content_type,
          'Origin': 'https://8kun.top',
          # 'DNT': '1',
          'Connection': 'keep-alive',
          'Referer': 'https://8kun.top/',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          # 'Pragma': 'no-cache',
          # 'Cache-Control': 'no-cache',
          # Requests doesn't support trailers
          # 'TE': 'trailers',
        }

        """
          # headers = {
          #     'Connection': 'keep-alive',
          #     'Pragma': 'no-cache',
          #     'Cache-Control': 'no-cache',
          #     'Accept': '*/*',
          #     'User-Agent': 'Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4324.150 Safari/537.36',
          #     'Content-Type': m.content_type,
          #     'Origin': 'https://8kun.top',
          #     'Sec-Fetch-Site': 'same-site',
          #     'Sec-Fetch-Mode': 'cors',
          #     'Sec-Fetch-Dest': 'empty',
          #     'Referer': 'https://8kun.top/',
          #     'Accept-Language': 'en-US,en;q=0.9',
        #   }"""
        r = s.post("https://sys.8kun.top/post.php",headers=headers,data=m)
        # if "To prevent raids against this board" not in r.text:
        #   print(r.text)
        
        # if do_not_namefag == False:
          # print(r.text)
        # else:
        #   print(r.json()['redirect'])
        
        if "Thread specified does not exist." in r.text:
          main.blacklist_dead.append(threadId)
        elif "Thread locked. You may not reply at this time." in r.text:
          main.blacklist_dead.append(threadId)
        elif "This thread has over 750 posts and can therefore no longer be replied to." in r.text:
          main.blacklist_dead.append(threadId)
          print(f"=========== REACHED 750 POSTS ============================{ threadId }=========================")
        elif 'noko":true' in r.text:
          main.stats__posts_made += 1
          
          # If image capture will be ever needed:
          # if main.board == "qresearch":
          #   with open(f"captcha_database/{captcha}.png", "wb") as f:
          #     image_data = re.sub('^data:image/.+;base64,', '', base64Str)
          #     f.write(base64.b64decode(image_data))
        elif '{"error":"A CAPTCHA was requested but you did not enter one."}' in r.text:
          main.captcha_per_post_copemode = True
        elif 'captcha":true' in r.text:#we should see this if we filled a captcha. this is in a  captcha-per-post mode. 
          # if main.board != "qresearch":
          #   # captchas_worked += 1
          return True
        elif 'actually_load_captcha' in r.text:
          # if main.board != "qresearch":
          #   # captchas_failed += 1
          return True
        elif 'banned":true' in r.text:
          return True
        elif ">Origin Server Offline<" in r.text:
          # raise Exception("cdn_error","origin error bullshit.")
          do_nothing = None
        elif "ech CDN is online in " in r.text:
          # raise Exception("cdn_error","cdn bullshit.")
          do_nothing = None
        elif "center>nginx" in r.text:
          raise Exception("nginx_error_or_ban","NginX was Found.")#Nginx ip-range-ban
        elif "mistyped the verification" in r.text:
          captchas_failed += 1##Make a check that checks if you filled a captcha???? json magic???
        elif "If you can see this, please copy and paste this link into your browser to complete the captcha":
          return True
        else:
          print(r.text)
    ############################################
    post_openpost = False
    if not post_openpost:
      while len(main.threads_db) == 0:
        print("Sleeping for 5 seconds, due to no threads!")
        time.sleep(5)
    s = killpedos.Session()
    s.proxies = genProxy()
    s.timeout = 20
    
    # useragent = f"Man boobs watkins. Moonshine (((Jim Watkins))) fat pedophile in the philiphins /{ randomString(5) }"
    # useragent = f"{ randomString() }"
    # useragent = f"{ str(random.randint(1000000000,9999999999)) }"
    # useragent = f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.7 Mobile/15E148 Safari/604.1"
    # useragent = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
    # useragent = f"{ main.global_useragent }"
    useragent = random.choice(main.useragent_db)
    
    # make_captcha_session(s, useragent) #Fills a captcha
    is_session = True
    nothing0, nothing1 = hf_ai_captcha(s, useragent, is_session)
    # nothing0, nothing1 = two_captcha_captcha(s, useragent, is_session)

    
    try:
      rnd_thread = random.choice(   main.threads_db   )
      did_it_got_banned = do_post(    rnd_thread, useragent, post_openpost    )#also crash("so called raise") if there is an issue. which is good. so it wont be stack in a loop
    except:did_it_got_banned = do_post(    "0", useragent, post_openpost    )#will only crash if has an issue with rnd_thread
    time.sleep(10)

    # EOFError
    # while True:
    for x in range(2000000):      


      #Incase we get a CDN error
      try:
        rnd_thread = random.choice(   main.threads_db   )#When zero threads to spam. it  errors

        did_it_got_banned = do_post(    rnd_thread, useragent, post_openpost    )
      except Exception as inst:
        pass
      if did_it_got_banned:
        break

      #   # error_counting += 1
      #   # if error_counting == 5:
      #   #   break#breaks the loop and thus creates a new session, with new IP and everything
      #   pass#####passs???
      #########
      # if fill_captcha == True:
      #   break


      # if main.board == "qresearch":#We want a new uniuqe id per post so fuckkk ittt!!! NEW PROXY NEW IP 
      #   break Actually its stupid it will result in two captchas being solved
      time.sleep(10.5)
      # time.sleep(9.95)
      
class mainBot():
  def action():
    while True:
      try:
        action()
      except:
        pass# use "pass" if you are not coding
class mainDoingThreads():
    threads_atonce = 0

    stats__posts_made = int(0)
    board = "qresearch"
    threads_db = ["1"]
    threads_replies_db = []
    blacklist_dead = []
    is_first_run = True

    #captcha_ai_stuff
    captchas_failed = 0
    captchas_worked = 0
    average_duration = 0
    duration = 0
    projects_git = ['sneedium/8coon-captcha'

    #If commented the space was banned
      # ,"sdfsfe/ydo0x/"
    # ,  'sdfsdfwewrw/docker1', 'sdfsdfwewrw/docker2', 'sdfsdfwewrw/docker3', 'sdfsdfwewrw/docker4', 'sdfsdfwewrw/docker5', 'sdfsdfwewrw/docker6'
     ]

    useragent_db = []

    #As the name suggest, it does what the name says. retard 
    captcha_per_post_copemode = False

    
    def STATS(self):
      while True:
        print(f"[#]  made {main.stats__posts_made} |---| amount of threads to spam: { len(main.threads_db) } [====] Threads: {main.threads_atonce}")
        txt = f"Captchas that worked:{main.captchas_worked}, [-----] Failed:{main.captchas_failed}"
        txt2 = f"Last average_duration:{main.average_duration}, Last (per the submit) duration:{main.duration}"
        print(f"{txt}\n{txt2}\n==========")
        # time.sleep(.45)
        time.sleep(1.2)


    def sub_fetch_post_thread(self, thread):
      #A sub part of multi_fetch_post_thread... Because I refuse using another class for a simple task.
      json_data = killpedos.get(f"https://8kun.top/{ main.board }/res/{ thread }.json",headers={
          'Cache-Control': 'no-transform',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4324.150 Safari/537.36',
        }, proxies=genProxy()
      ).json()

      # Slower concept of how the multithreading works
      # for x in json_data["posts"]:
      #   self.tmp_threads_replies_db[thread].append(str( x['no'] ))
      
      def sub_insert(x):
        self.tmp_threads_replies_db[thread].append(str( x['no'] ))
      
      with porn.ThreadPoolExecutor(max_workers=1000) as e:
        future = e.map(sub_insert, json_data["posts"])

    
    def multi_fetch_post_thread(self, threads):
      """Fetches the posts inside the thread"""

      #main memory shared __so-called__ "Database"
      self.tmp_threads_replies_db = dict()#Its a self, because its only 1 threads, scrapping. We do not care. about memory shit if above 1/single thread

      #Avoids a nasty error. (((KeyError: '16691758'))). Where it does not finds the dict() because it wasnt set as a key and it wont let you "append" to the sublist of the thread in our dict.
      for x in threads:
        self.tmp_threads_replies_db[x] = list()
    
      #ThreadPool (A type of multithreading).
      with porn.ThreadPoolExecutor(max_workers=200) as e:
        future = e.map(self.sub_fetch_post_thread, threads)

      main.threads_replies_db = self.tmp_threads_replies_db

      ##################################################################################################
      """
      This is a back that I am using, so I can have a type of database in the first run.
      Because it takes a while to boot-up the bot. 
      This way I am doing it the good old way without waiting 20 seconds each time
      """
      with open('8kun_threads_replies__first_backup.json', 'w') as f:
          json.dump(self.tmp_threads_replies_db, f)


    def auto_database_fetcher(self):
      while True:
        # with open('8kun_blacklist.json', 'w') as f:
        #     json.dump(blacklist_dead  , f)
        try:
          tic = time.perf_counter()
          if main.is_first_run:
            try:
              with open('8kun_threads_replies__first_backup.json', 'r') as f:
                main.threads_replies_db = json.load(f)
              main.threads_db = list(main.threads_replies_db.keys())
              with open('8kun_blacklist.json', 'r') as f:
                backup_blacklist_dead = json.load(f)
              # print("\n\nsoy",main.threads_db )
              for x in backup_blacklist_dead:
                try:
                  main.threads_db.remove(  x  )#BOOBS!!!!, we allow to use the main.threads_db. because this is the first run thus we can allow(and must) ourself
                except:
                  pass
            except:
              pass
            # print("\nsoy1111",main.threads_db )
        
          print(f"Finsihed the first_run in {time.perf_counter() - tic:0.4f} seconds")
          json_data = killpedos.get(f"https://8kun.top/{main.board}/catalog.json",headers={
              'Cache-Control': 'no-transform',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4324.150 Safari/537.36',
            }, proxies=genProxy()
          ).json()
          # print(json_data)

          # threads_tmp = ["17325118"]
          threads_tmp = []#Comment this loop for a targeted thread. 
          for x in json_data:
            for y in x['threads']:
              if int(y['locked']) == 1 or int(y['replies']) > 750:
                continue
              if "Anti-Q" in y["sub"]:
                continue
              if y['cyclical'] == "1":#kek fuck spam catchers 
                continue
              
              try:
                threads_tmp.append(str( y['no'] ))
              except:
                pass
          # print(threads_tmp)
          
          # try:
          #   two_blacklists = list(set(main.blacklist_dead+backup_blacklist_dead))#Once its the second loop, it should be ---(minuses) itself's 
          # except:
          #   two_blacklists = list(set(main.blacklist_dead))
          two_blacklists = list(set(main.blacklist_dead))
          for x in two_blacklists:
            try:
              threads_tmp.remove(  x  )
            except:
              pass
          
          # #If after all the black list is not locked.. or full.. || I think it does something. because some times shit unlocks.... stupid chache aydsz
          # for x in json_data:
          #   for y in x['threads']:
          #     if int(y['locked']) == 1 or int(y['omitted_posts']) > 745:
          #       continue
          #     threads_tmp.append(str( y['no'] ))
          
          # with open('8kun_blacklist.json', 'w') as f:
          #   json.dump( two_blacklists, f)
          
          # Manual blacklist of a thread (I used it on a pin threaded I didnt wantted to spam. Utnil I did wanted to spam it lol)
          # try:
            # threads_tmp.remove("17321383")
          # except:
          #   pass
          # print(threads_tmp)
          
          main.is_first_run = False#Now that the rest of the function processed, we are not longer, in "a first run state"

          main.multi_fetch_post_thread(threads_tmp)
          if not main.is_first_run:
            toc = time.perf_counter()
            print(f"Finsihed the first_run in {toc - tic:0.4f} seconds1!!!!")

          main.threads_db = threads_tmp
          time.sleep(4)
        except:
          pass
    def switch_useragent(self):
      while True:
        main.global_useragent = random.choice(main.useragent_db)
        time.sleep(20)
    
    def check_captcha_per_post(self):
      while True:
        try:
          pedo_watkins_sex_ring_family = killpedos.get(f"https://8kun.top/qresearch/res/17225239.html",headers={
              'Cache-Control': 'no-transform',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4324.150 Safari/537.36',
            }, proxies=genProxy()
          ).text
          if "center>nginx" not in pedo_watkins_sex_ring_family or "Origin Server Offline":
            if 'Verification <span class="required-star">*</span' in pedo_watkins_sex_ring_family:
              main.captcha_per_post_copemode = True
            else:
              main.captcha_per_post_copemode = False
          time.sleep(4)
        except: pass

    def DoThreads(self,threads):
      with open('user-agents_chrome_true_100_5000.json', 'r') as f:
        main.useragent_db = json.load(f)
      
      threading.Thread(target=main.check_captcha_per_post).start()
      threading.Thread(target=main.switch_useragent).start()
      threading.Thread(target=main.auto_database_fetcher).start()
      time.sleep(2)#fixes a nasty bug where it takes time to load the database, from the backup


      for x_thread in range(threads):
        threading.Thread(target=mainBot.action).start()
      threading.Thread(target=main.STATS).start()
    
    def Main(self):
      # base64_message = "YOur logo in base64 if you feel edgyT09PT09PT0K"
      # base64_bytes = base64_message.encode('ascii')
      # message_bytes = base64.b64decode(base64_bytes)
      
      # ######################
      # BANNER = message_bytes.decode('ascii')
      print("This is a really fast spambot")#print(BANNER)
      print("fat pedophile in the philiphins\n\n\nfat pedophile in the philiphinsfat pedophile in the philiphinsfat pedophile in the philiphinsfat pedophile in the philiphinsfat pedophile in the philiphins")
      ######################
      
      main.threads_atonce=int( str(input("How many threads would you like? (each thread has x5 subthreads of short): ")) )
      self.DoThreads(main.threads_atonce)



main = mainDoingThreads()
main.Main()#hotwheels go brrrrrrrrrrrrrrr
