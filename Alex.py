# Ở bước này, các bạn import các thư viện cần thiết cho quá trình tạo nên con trợ lý ảo nhá. Các bạn nào chạy mà bị lỗi thì lên Google search cách tải thư viện cho python nha.
import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
import cv2

# Khai báo các biến
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()
cam = cv2.VideoCapture(0)


# Chuyển đổi văn bản thành giọng nói
def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")


# Chuyển đổi giọng nói bạn yêu cầu vào thành văn bản hiện ra khi máy trả lại kết quả đã nghe
def get_audio():
    print("\nBot: \tĐang nghe \t  \n")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=8)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            print("...")
            return 0


# Dừng AI lại
def stop():
    speak("Hẹn gặp lại bạn sau!")
    time.sleep(2)


# Lắng nghe mình nói
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text
        elif i < 2:
            speak("Tôi không nghe rõ. Bạn nói lại được không!")
            time.sleep(3)
    time.sleep(2)
    stop()
    return 0


# Chào hỏi
def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))
    time.sleep(5)


#thời gian và ngày tháng 
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút %d giây' % (now.hour, now.minute, now.second))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
    time.sleep(4)


def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        time.sleep(2)
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe') 
    elif "word" in text:
        speak("Mở Microsoft Word") 
        time.sleep(2)
        os.startfile('C:\Program Files (x86)\Microsoft Office\Office16\WINWORD.EXE') 
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        time.sleep(2)
        os.startfile('C:\Program Files (x86)\Microsoft Office\Office16\EXCEL.EXE') 
    elif "powerpoint" in text:
        speak("Mở Microsoft Powerpoint")
        time.sleep(2)
        os.startfile('C:\Program Files (x86)\Microsoft Office\Office16\POWERPNT.EXE')
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
        time.sleep(3)


def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        time.sleep(3)
        return True
    else:
        return False


# Mở google và tìm kiếm
def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    time.sleep(10)


# Gửi mail
def send_email(text):
    speak('Bạn gửi email cho ai nhỉ')
    recipient = get_text()
    if 'luận' in recipient: 
        speak('Nội dung bạn muốn gửi là gì')
        content = get_text()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('trinhkiet2005@gmail.com', 'tvk123456789') 
        mail.sendmail('trinhkiet2005@gmail.com', 
                      'minhluan181204@gmail.com', content.encode('utf-8')) 
        mail.close()
        speak('Email của bạn vùa được gửi. Bạn check lại email nhé.')
    else:
        speak('Tôi không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không')


# Xem thời tiết
def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        """.format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(28)
    else:
        speak("Không tìm thấy địa chỉ của bạn")
        time.sleep(2)


#Chơi nhạc
def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    time.sleep(2)
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.")
    time.sleep(3)


# Đọc báo
def read_news():
    speak("Bạn muốn đọc báo về gì")
    
    queue = get_text()
    params = {
        'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])


# Đổi hình nền
def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
    api_key  
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Nhớ đưa cái đường dẫn của mấy tấm ảnh nền mà bạn muốn thay đổi vào nha ^^
    urllib2.urlretrieve(photo, "C:\\Users\\PC\\b.jpg")
    image=os.path.join("C:\\Users\\PC\\b.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    speak('Hình nền máy tính vừa được thay đổi')
    time.sleep(3)


# Bật mí là con Bot này rất rất là "nhiều chuyện". Nên hổng biết cái gì cứ hỏi nó nha ^^
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        time.sleep(2)
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0].split(".")[0])
        time.sleep(20)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            time.sleep(2)
            ans = get_text()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(10)

        speak('Cảm ơn bạn đã lắng nghe!!!')
        time.sleep(3)
    except:
        speak("Tôi không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
        time.sleep(5)

# Giói thiệu
def introduce():
    speak("Xin chào bạn. Rất hân hạnh được phục vụ bạn. Tôi là trợ lý ảo được tạo ra dựa trên ngôn ngữ lập trình Python kết hợp với AI.")
    time.sleep(10)


# Những việc có thể làm
def help_me():
    speak("""Tôi có thể giúp bạn thực hiện các câu lệnh sau đây:
    1. Chào hỏi
    2. Cho biết ngày, giờ hiện tại
    3. Mở website, excel, word, powerpoint
    4. Tìm kiếm trên Google
    5. Gửi email
    6. Xem thời tiết hiện tại của bất cứ thành phố nào
    7.Nhắc nhở bạn các công việc cần làm
    8. Mở video nhạc
    9. Thay đổi hình nền máy tính
    10. Đọc báo hôm nay
    11. Kể bạn biết về thế giới """)
    time.sleep(30)

# Nhắc nhở công việc
def do():
    speak("""Các công việc cho hôm nay là:
    6 giờ sáng: Tập thể dục
    6:30 sáng: Ăn sáng
    7 giờ sáng: Học toán
    8 giờ sáng: Học vật lý
    9 giờ sáng: Dọn phòng
    10 giờ sáng: Ăn trưa""")
    time.sleep(17)

# Nhận diện
def camera():
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("Camera", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "picture {}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    speak("Xin chào Kiệt. Tôi có thể giúp gì cho bạn?")
    time.sleep(15)
   
# Tổng kết
def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    name = get_text()
    if name:
        speak("Chào bạn {}".format(name))
        time.sleep(2)
        speak("Bạn cần tôi giúp gì ạ?")
        while True:
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                stop()
                break
            elif "có thể làm gì" in text:
                help_me()
                break
            elif "chào" in text:
                hello(name)
            elif "giờ" in text or "ngày" in text:
                get_time(text)
                break
            elif 'mở google và tìm kiếm' in text:
                open_google_and_search(text)
                break
            elif "mở " in text:
                open_website(text)
                break
            elif "ứng dụng" in text:
                speak("Tên ứng dụng bạn muốn mở là ")
                time.sleep(3)
                text1 = get_text()
                open_application(text1)
                break
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
                break
            elif "thời tiết" in text:
                current_weather()
                break
            elif "chơi nhạc" in text:
                play_song()
                break
            elif "hình nền" in text:
                change_wallpaper()
                break
            elif "đọc báo" in text:
                read_news()
                break
            elif "định nghĩa" in text:
                tell_me_about()
                break
            elif "giới thiệu" in text:
            	introduce()
                break
            elif "các công việc hôm nay" in text:
                do()
                break
            elif "nhận diện":
                camera()
                break
            else:
                speak("Bạn cần tôi giúp gì ạ?")
                time.sleep(2)

assistant()