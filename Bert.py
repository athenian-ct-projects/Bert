
import requests,re,easygui
def Find_car(picture_numbers):
    url_car = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=cars&pn=20&gsm=&ct=&ic=0&lm=-1&width=0&height=0'#This is the link we are going to use soon
    html_car = requests.get(url_car).text#this is going to get how the coders write this code, so that we can borrow something on it
    picture_car_url = re.findall('"objURL":"(.*?)",',html_car) #This is from re module because we can tell the computer what we want
    for picture_dumpling_urls in range(picture_numbers):#picture_car_url is a list that have a lot of pictures, we need to print them down
        print(picture_car_url[picture_numbers])#picture_car_url is a list that have a lot of pictures, we need to print them down
        picture_numbers += 1#both this and last one is going to help us to loop how many pictures you want
def Find_scene(picture_numbers):
    url_Zhangjiajie = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1576554732763_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=0&height=0&face=0&istype=2&ie=utf-8&ctd=1576554732764%5E00_1463X869&sid=&word=%E5%BC%A0%E5%AE%B6%E7%95%8C'#This is the link we are going to use soon
    html_Zhangjiajie = requests.get(url_Zhangjiajie).text#this is going to get how the coders write this code, so that we can borrow something on it
    picture_scene_url = re.findall('"objURL":"(.*?)",',html_Zhangjiajie)#This is from 're' module because it can tell the website what we want
    for picture_dumpling_urls in range(picture_numbers):#picture_car_url is a list that have a lot of pictures, we need to print them down
        print(picture_scene_url[picture_numbers])#both this and last one is going to help us to loop how many pictures you want
        picture_numbers += 1
def  Find_Fortnite(picture_numbers):
    url_Fortnite = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1576555226029_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=0&height=0&face=0&istype=2&ie=utf-8&ctd=1576555226029%5E00_1463X869&sid=&word=%E5%A0%A1%E5%9E%92%E4%B9%8B%E5%A4%9C'#This is the link we are going to use soon
    html_Fortnite = requests.get(url_Fortnite).text#this is going to get how the coders write this code, so that we can borrow something on it
    picture_Fortnite_url = re.findall('"objURL":"(.*?)",',html_Fortnite)#This is from 're' module because it can tell the website what we want
    for picture_dumpling_urls in range(picture_numbers):#picture_car_url is a list that have a lot of pictures, we need to print them down
        print(picture_Fortnite_url[picture_numbers])#both this and last one is going to help us to loop how many pictures you want
        picture_numbers += 1#make sure it can keep loop instead of repeat and repeat
def Find_dumplings(picture_numbers):
    url_dumpling = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1576555716354_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=0&height=0&face=0&istype=2&ie=utf-8&ctd=1576555716355%5E00_1463X869&sid=&word=%E9%A5%BA%E5%AD%90'#this is going to get how the coders write this code, so that we can borrow something on it
    html_dumpling = requests.get(url_dumpling).text#this is going to get how the coders write this code, so that we can borrow something on it
    picture_dumpling_url = re.findall('"objURL":"(.*?)",', html_dumpling)#This is from 're' module because it can tell the website what we want
    for picture_dumpling_urls in range(picture_numbers):#picture_car_url is a list that have a lot of pictures, we need to print them down
        print(picture_dumpling_url[picture_numbers])#both this and last one is going to help us to loop how many pictures you want
        picture_numbers += 1#make sure it can keep loop instead of repeat and repeat
choice = easygui.choicebox('please pick the picture you want search',choices=['car','scene','Fortnite','dumpling'])#make the user to choose what they want
if choice == 'car':
    times = int(easygui.enterbox('please input how many pictures you want,the max is 14'))
    while times >= 15:
        easygui.msgbox('please input the numbers that less or equal to 14')
        times = int(easygui.enterbox('please input how many pictures you want'))
    Find_car(times)
elif choice == 'scene':
    times = int(easygui.enterbox('please input how many pictures you want,the max is 14'))
    while times >= 15:
        easygui.msgbox('please input the numbers that less or equal to 14')
        times = int(easygui.enterbox('please input how many pictures you want'))
    Find_scene(times)
elif choice == 'Fortnite':
    times = int(easygui.enterbox('please input how many pictures you want,the max is 14'))
    while times >= 15:
        easygui.msgbox('please input the numbers that less or equal to 14')
        times = int(easygui.enterbox('please input how many pictures you want'))
    Find_Fortnite(times)
else:
    times = int(easygui.enterbox('please input how many pictures you want,the max is 14'))
    while times >= 15:
        easygui.msgbox('please input the numbers that less or equal to 14')
        times = int(easygui.enterbox('please input how many pictures you want'))
    Find_dumplings(times)
'''
after user finish choose what they want, they will get response from my website
and then we finished
'''

