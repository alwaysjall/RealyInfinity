import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper


# FUNCTIONS FOR MENU
@is_option 
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Re}")  # INPUT IP ADDRESS
    print()
    print(f' {Wh}============= {Re} INFORMATION IP ADDRESS {Wh}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n IP target       :{Re}", ip)
    print(f"{Wh} Type IP         :{Re}", ip_data["type"])
    print(f"{Wh} Country         :{Re}", ip_data["country"])
    print(f"{Wh} Country Code    :{Re}", ip_data["country_code"])
    print(f"{Wh} City            :{Re}", ip_data["city"])
    print(f"{Wh} Continent       :{Re}", ip_data["continent"])
    print(f"{Wh} Continent Code  :{Re}", ip_data["continent_code"])
    print(f"{Wh} Region          :{Re}", ip_data["region"])
    print(f"{Wh} Region Code     :{Re}", ip_data["region_code"])
    print(f"{Wh} Latitude        :{Re}", ip_data["latitude"])
    print(f"{Wh} Longitude       :{Re}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} Maps            :{Re}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} EU              :{Re}", ip_data["is_eu"])
    print(f"{Wh} Postal          :{Re}", ip_data["postal"])
    print(f"{Wh} Calling Code    :{Re}", ip_data["calling_code"])
    print(f"{Wh} Capital         :{Re}", ip_data["capital"])
    print(f"{Wh} Borders         :{Re}", ip_data["borders"])
    print(f"{Wh} Country Flag    :{Re}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN             :{Re}", ip_data["connection"]["asn"])
    print(f"{Wh} ORG             :{Re}", ip_data["connection"]["org"])
    print(f"{Wh} ISP             :{Re}", ip_data["connection"]["isp"])
    print(f"{Wh} Domain          :{Re}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{Re}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR            :{Re}", ip_data["timezone"]["abbr"])
    print(f"{Wh} DST             :{Re}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Offset          :{Re}", ip_data["timezone"]["offset"])
    print(f"{Wh} UTC             :{Re}", ip_data["timezone"]["utc"])
    print(f"{Wh} Current Time    :{Re}", ip_data["timezone"]["current_time"])


@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Enter phone number target {Re}Ex [+62xxxxxx] {Wh}: {Re}")  # INPUT NUMBER PHONE
    default_region = "ID"  # DEFAULT NEGARA INDONESIA

    parsed_number = phonenumbers.parse(User_phone, default_region)  # VARIABLE PHONENUMBERS
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Re} INFORMATION PHONE NUMBER {Wh}==========")
    print(f"\n {Wh}Location             :{Re} {location}")
    print(f" {Wh}Region Code          :{Re} {region_code}")
    print(f" {Wh}Timezone             :{Re} {timezoneF}")
    print(f" {Wh}Operator             :{Re} {jenis_provider}")
    print(f" {Wh}Valid number         :{Re} {is_valid_number}")
    print(f" {Wh}Possible number      :{Re} {is_possible_number}")
    print(f" {Wh}International format :{Re} {formatted_number}")
    print(f" {Wh}Mobile format        :{Re} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{Re} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 format         :{Re} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Re} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Re} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Re} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Re} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{Re} This is another type of number")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Enter Username : {Re}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{Ye}Username not found {Ye}!")
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Re} INFORMATION USERNAME {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {Re}+ {Wh}] {site} : {Re}{url}")


@is_option
def showIP():
    respone = requests.get('https://api.ipify.org/')
    Show_IP = respone.text

    print(f"\n {Wh}========== {Re} INFORMATION YOUR IP {Wh}==========")
    print(f"\n {Wh}[{Re} + {Wh}] Your IP Adrress : {Re}{Show_IP}")
    print(f"\n {Wh}==============================================")


# OPTIONS
options = [
    {
        'num': 1,
        'text': 'IP Tracker',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Show Your IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': 'Phone Number Tracker',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'Username Tracker',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Exit',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Re}+ {Wh}] {Re}Press enter to continue')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Re}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # BANNER TOOLS
    clear()
    stderr.writelines(f"""
       

    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠔⠒⠊⠉⠉⠉⠉⠙⠒⠲⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣠⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⠀⠀
    ⠀⠀⠀⣠⠞⠁⠀⣀⠀⠀⠀⠀⢀⣀⡀⠀⢀⣀⠀⠀⠀⠀⢀⠀⠈⠱⣄⠀⠀⠀
    ⠀⠀⡴⠁⡠⣴⠟⠁⢀⠤⠂⡠⠊⡰⠁⠇⢃⠁⠊⠑⠠⡀⠀⢹⣶⢤⡈⢣⡀⠀
    ⠀⡼⢡⣾⢓⡵⠃⡐⠁⠀⡜⠀⠐⠃⣖⣲⡄⠀⠀⠱⠀⠈⠢⠈⢮⣃⣷⢄⢳⠀
    ⢰⠃⣿⡹⣫⠃⡌⠀⠄⠈⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠣⠀⠀⠱⠈⣯⡻⣼⠈⡇
    ⡞⢈⢿⡾⡃⠰⠀⠀⠀⠀⠀⠀⠀⠀⣘⣋⠀⠀⠀⠀⠀⠀⠀⠀⠇⢸⢿⣿⢠⢸
    ⡇⢸⡜⣴⠃⠀⠀⠀⠀⠀⣀⣀⣤⡎⠹⡏⢹⣦⣀⣀⠀⠀⠀⠀⢈⠘⣧⢣⡟⢸
    ⢧⢊⢳⡏⣤⠸⠀⠀⠀⢸⣿⣿⣿⡇⢰⡇⢠⣿⣿⣿⣷⠀⠀⠀⡆⢸⢹⡼⣱⢸
    ⢸⡘⢷⣅⣿⢂⢃⠐⠂⣿⣿⣿⣿⣿⣼⣇⣾⣿⣿⣿⣿⠁⠂⡰⡠⣿⢨⡾⠃⡇
    ⠀⢳⡱⣝⠻⡼⣆⡁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠐⣰⣇⠿⣋⠝⡼⠀
    ⠀⠀⢳⡈⢻⠶⣿⣞⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢣⣿⡶⠟⢉⡼⠁⠀
    ⠀⠀⠀⠙⢦⡑⠲⠶⠾⠿⢟⣿⣿⣿⣿⣿⣿⣿⣿⡛⠿⠷⠶⠶⠊⡡⠋⠀⠀⠀
    ⠀⠀⠀⠀⠀⠙⠦⣝⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⡛⠛⠛⣋⠴⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠦⠿⣿⣿⣿⣿⣿⣿⠿⠧⠒⠋⠁⠀
===========『REALY-INFINITY』===========
╔═╗╔═╗────╔╦═══╦╗───╔╗───
╚╗╚╝╔╝────║║╔═╗║║───║║───
─╚╗╔╝╔══╗─║║║─║║║───║║───
─╔╝╚╗╚══╬╗║║╚═╝║║─╔╗║║─╔╗
╔╝╔╗╚╗──║╚╝║╔═╗║╚═╝║║╚═╝
╚═╝╚═╝──╚══╩╝─╚╩═══╝╚═══╝
                                                             

         {Re}[ + ]  C O D E   B Y  A L W A Y S - J A L L  [ + ]
    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
{Re}╔═══╦═══╦═══╦╗──╔╗──╔╗───╔══╦═╗─╔╦═══╦══╗╔═╗─╔╦══╦════╦╗──╔╗
{Re}║╔═╗║╔══╣╔═╗║║──║╚╗╔╝║───╚╣╠╣║╚╗║║╔══╩╣╠╝║║╚╗║╠╣╠╣╔╗╔╗║╚╗╔╝║
{Re}║╚═╝║╚══╣║─║║║──╚╗╚╝╔╝╔══╗║║║╔╗╚╝║╚══╗║║─║╔╗╚╝║║║╚╝║║╚╩╗╚╝╔╝
{Re}║╔╗╔╣╔══╣╚═╝║║─╔╗╚╗╔╝─╚══╝║║║║╚╗║║╔══╝║║─║║╚╗║║║║──║║──╚╗╔╝─
{Re}║║║╚╣╚══╣╔═╗║╚═╝║─║║─────╔╣╠╣║─║║║║──╔╣╠╗║║─║║╠╣╠╗─║║───║║──
{Re}╚╝╚═╩═══╩╝─╚╩═══╝─╚╝─────╚══╩╝─╚═╩╝──╚══╝╚╝─╚═╩══╝─╚╝───╚╝──
                 ⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠔⠒⠊⠉⠉⠉⠉⠙⠒⠲⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠀⣠⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⠀⠀
                 ⠀⠀⠀⣠⠞⠁⠀⣀⠀⠀⠀⠀⢀⣀⡀⠀⢀⣀⠀⠀⠀⠀⢀⠀⠈⠱⣄⠀⠀⠀
                 ⠀⠀⡴⠁⡠⣴⠟⠁⢀⠤⠂⡠⠊⡰⠁⠇⢃⠁⠊⠑⠠⡀⠀⢹⣶⢤⡈⢣⡀⠀
                 ⠀⡼⢡⣾⢓⡵⠃⡐⠁⠀⡜⠀⠐⠃⣖⣲⡄⠀⠀⠱⠀⠈⠢⠈⢮⣃⣷⢄⢳⠀
                 ⢰⠃⣿⡹⣫⠃⡌⠀⠄⠈⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠣⠀⠀⠱⠈⣯⡻⣼⠈⡇
                 ⡞⢈⢿⡾⡃⠰⠀⠀⠀⠀⠀⠀⠀⠀⣘⣋⠀⠀⠀⠀⠀⠀⠀⠀⠇⢸⢿⣿⢠⢸
                 ⡇⢸⡜⣴⠃⠀⠀⠀⠀⠀⣀⣀⣤⡎⠹⡏⢹⣦⣀⣀⠀⠀⠀⠀⢈⠘⣧⢣⡟⢸
                 ⢧⢊⢳⡏⣤⠸⠀⠀⠀⢸⣿⣿⣿⡇⢰⡇⢠⣿⣿⣿⣷⠀⠀⠀⡆⢸⢹⡼⣱⢸
                 ⢸⡘⢷⣅⣿⢂⢃⠐⠂⣿⣿⣿⣿⣿⣼⣇⣾⣿⣿⣿⣿⠁⠂⡰⡠⣿⢨⡾⠃⡇
                 ⠀⢳⡱⣝⠻⡼⣆⡁⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠐⣰⣇⠿⣋⠝⡼⠀
                 ⠀⠀⢳⡈⢻⠶⣿⣞⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢣⣿⡶⠟⢉⡼⠁⠀
                 ⠀⠀⠀⠙⢦⡑⠲⠶⠾⠿⢟⣿⣿⣿⣿⣿⣿⣿⣿⡛⠿⠷⠶⠶⠊⡡⠋⠀⠀⠀
    ⠀⠀             ⠀⠀⠀⠙⠦⣝⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⡛⠛⠛⣋⠴⠋⠀⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠦⠿⣿⣿⣿⣿⣿⣿⠿⠧⠒⠋⠁⠀
        {Re}[ + ]  C O D E   B Y  A L W A Y S - J A L L  [ + ]

> ━ꪶꪶ𓁹ꫂ『 𝑻𝑯𝑨𝑵𝑲𝑺 𝑻𝑶 』ꪶ𓁹ꫂꫂ━
> ☭ 𝑻𝑶𝑶𝑳𝑺 𝑵𝑨𝑴𝑬 : ⏤͟͟͞͞𝑹𝒆𝒂𝒍𝒚𖤌𝑰𝒏𝒇𝒊𝒏𝒊𝒕𝒚 ͟͟͞͞⏤࿐
> ☭ 𝑫𝑬𝑽𝑬𝑳𝑶𝑷𝑬𝑹 : ⏤͟͟͞𝑨𝒍𝒘𝒂𝒚𝒔𖤌𝑱𝒂𝒍𝒍͟͟͞͞⏤
> ☭ 𝑫𝑨𝑹𝑳𝑰𝑵𝑮𝑺 : ⏤͟͟͞𝑨𝒏𝒊𝒏𝒅𝒂͟͟͞͞⏤
> ☭ 𝑻𝑬𝑨𝑴 : ▾⌜ ⏤͟͟͞͞𝑹𝒆𝒂𝒍𝒚 𝑰𝒏𝒇𝒊𝒏𝒊𝒕𝒚 ͟͟͞͞⏤࿐ 𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭⌟▾
> ☭ 𝑨𝑳𝑳𝑨𝑯 𝑺𝑾𝑻
> ☭ 𝑴𝒀 𝑭𝑨𝑴𝑰𝑳𝒀
> ☭ 𝒀𝒂𝒏 𝑶𝒇𝒇𝒊𝒄𝒊𝒂𝒍
> ☭ 𝑹𝒂𝒑𝒊𝒑 𝑨𝒏𝒐𝒎𝒂𝒍𝒊
> ☭ 𝑫𝒐𝒏𝒛 𝑯𝒐𝒔𝒕𝒊𝒏𝒈
> ☭ 𝑫𝒂𝒗𝒊𝒂𝒏𝒕
> ☭ 𝑭𝒂𝒍𝒍 𝑾𝒊𝒃𝒖
> ☭ 𝑵𝒂𝒏𝒛
> ☭ 𝑨𝒍𝒍 𝑨𝒅𝒎𝒊𝒏 𝑹𝒆𝒂𝒍𝒚 𝑰𝒏𝒇𝒊𝒏𝒊𝒕𝒚
> ☭ 𝑨𝒍𝒍 𝑷𝒆𝒏𝒈𝒈𝒖𝒏𝒂 𝑻𝒐𝒐𝒍𝒔
─━༻ꪶ『𝑹𝑳』ꫂ༺━─━
        """)
    time.sleep(0.5)


def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {Re}Select Option : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number')
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()
