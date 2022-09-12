import random
from utils import *
from time import sleep


name1_list = ["James","Robert","John","Michael","David","William","Richard","Joseph","Thomas","Charles","Christopher","Daniel","Matthew","Anthony","Mark","Donald","Steven","Paul","Andrew","Joshua","Kenneth","Kevin","Brian","George","Timothy","Ronald","Edward","Jason","Jeffrey","Ryan","Jacob","Gary","Nicholas","Eric","Jonathan","Stephen","Larry","Justin","Scott","Brandon","Benjamin","Samuel","Gregory","Alexander","Frank","Patrick","Raymond","Jack","Dennis","Jerry","Tyler","Aaron","Jose","Adam","Nathan","Henry","Douglas","Zachary","Peter","Kyle","Ethan","Walter","Noah","Jeremy","Christian","Keith","Roger","Terry","Gerald","Harold","Sean","Austin","Carl","Arthur","Lawrence","Dylan","Jesse","Jordan","Bryan","Billy","Joe","Bruce","Gabriel","Logan","Albert","Willie","Alan","Juan","Wayne","Elijah","Randy","Roy","Vincent","Ralph","Eugene","Russell","Bobby","Mason","Philip","Louis","Source: 100% sample based on Social Security card application data as of of March 2022. See the limitations of this data source.","Mary","Patricia","Jennifer","Linda","Elizabeth","Barbara","Susan","Jessica","Sarah","Karen","Lisa","Nancy","Betty","Margaret","Sandra","Ashley","Kimberly","Emily","Donna","Michelle","Carol","Amanda","Dorothy","Melissa","Deborah","Stephanie","Rebecca","Sharon","Laura","Cynthia","Kathleen","Amy","Angela","Shirley","Anna","Brenda","Pamela","Emma","Nicole","Helen","Samantha","Katherine","Christine","Debra","Rachel","Carolyn","Janet","Catherine","Maria","Heather","Diane","Ruth","Julie","Olivia","Joyce","Virginia","Victoria","Kelly","Lauren","Christina","Joan","Evelyn","Judith","Megan","Andrea","Cheryl","Hannah","Jacqueline","Martha","Gloria","Teresa","Ann","Sara","Madison","Frances","Kathryn","Janice","Jean","Abigail","Alice","Julia","Judy","Sophia","Grace","Denise","Amber","Doris","Marilyn","Danielle","Beverly","Isabella","Theresa","Diana","Natalie","Brittany","Charlotte","Marie","Kayla","Alexis","Lori"]
name2_list = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzales","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores","Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts","Gomez","Phillips","Evans","Turner","Diaz","Parker","Cruz","Edwards","Collins","Reyes","Stewart","Morris","Morales","Murphy","Cook","Rogers","Gutierrez","Ortiz","Morgan","Cooper","Peterson","Bailey","Reed","Kelly","Howard","Ramos","Kim","Cox","Ward","Richardson","Watson","Brooks","Chavez","Wood","James","Bennet","Gray","Mendoza","Ruiz","Hughes","Price","Alvarez","Castillo","Sanders","Patel","Myers","Long","Ross","Foster","Jimenez"]
road_list = ["Akhan Songkhro","Arun Amarin","Asok (Asoke)","At Narong","Bamrung Mueang","Banthat Thong","Borommarat Chachonnani","Chakkraphong","Chan","Charan Sanit Wong (Charan Sanit Wongse)","Charoen Krung (New Road)","Charoen Nakhon","Charoen Rat","Convent","Din Daeng","Henry Dunant","Itsaraphap (Itsaraphab)","Kasem Rat (Raj)","Khaosan","Krung Kasem","Krung Thonburi","Lan Luang","Lang Suan","Lat Phrao","Lat Ya","Maha Chai","Maha Rat (Maha Raj)","Makkasan","Mangkon (Mangkorn)","Mit Maitri","Na Ranong","Nakhon Chaisi","Nakon Ratchasima","Nakhon Sawan","Nana Nua","Nana Tai","Nang Linchi","Narathiwas Rajanakarindra","New Phetchaburi","On Nut","Phahon Yothin","Phatthanakan","Phayathai","Phet Kasem","Phetburi (Phetchaburi)","Phitsanulok","Phloen Chit (Ploen Chit)","Phra Athit","Phra Khanong-Khlong Tan (Sukhumvit 71)","Phrannok","Phra Pin Klao (Somdet Phra Pin Klao)","Phra Sumen","Pracha Songkhro","Pracha Thippatai","Pracha Uthit","Pracharat Bamphen","Pradiphat","Rama I","Rama II","Rama III","Rama IV","Rama V","Rama VI","Rama IX","Ramkhamhaeng","Rang Nam","Ratburana","Ratchawithi","Ratchadamnoen Klang","Ratchadamnoen Nai","Ratchadamnoen Nok","Ratchadamri","Ratchadaphisek","Ratchaprarop","Ratchawithi","Ratchawong","Rong Muang","Royal City Avenue","Sala Daeng","Samsen","Sanam Chai","Sarasin","Sathon Nua (Sathorn Nua)","Sathon Tai (Sathorn Tai)","Sathu Pradit","Si Ayutthaya (Sri Ayutthaya)","Si Phraya","Silom","Somdet Chao Phraya","Somdet Phra Chao Taksin","Somdet Phra Pin Klao","Song Wat","Suan Phlu","Sukhothai","Sukhumvit (Sukhumwit)","Suk Sawat","Surawong","Sut Prasoet","Sutthisan Winitchai","Taksin","Tanao","Thanontok","Thiam Ruam Mit","Thoet Damri","Thoet Thai","Vibhavadi Rangsit","Wang Doem","Wisut Kasat","Witthayu (Wireless Road)","Worachak","Yaowarat","Yothi",""]
mailsp_list = ["gmail.com", "yahoo.com", "ku.th"]
number_list = list("0123456789")
type_list = ["breeder", "owner", "vet"]

def random_phone_number():
    tail = ""
    for i in range(0, 7):
        tail += random.choice(number_list)
    return "+66-" + random.choice(number_list) + "-" + tail

def random_personnal_infos(type=None):

    name1 = random.choice(name1_list)
    name2 = random.choice(name1_list)
    return {
        'type': random.choice(type_list) if (type is None) else type,
        'name1': name1,
        'name2': name2,
        'phone': random_phone_number(),
        'email': name1.lower() + "." + name2.lower() + "@" + random.choice(mailsp_list),
        'country': 'Thailand',
        'address': str(random.randint(1, 999)) + " " + random.choice(road_list) + " Rd",
        'postcode': str(random.randint(1000, 9999)),
        'username': name1.lower() + "." + name2.lower(),
        'password': name1.lower() + "." + name2.lower(),
        'passwordCheck': name1.lower() + "." + name2.lower(),
    }

def fill_random_personnal_infos(driver, type=None):
    user = random_personnal_infos(type=type)
    set_select_value("#fType", user['type'], driver)
    send_keys("#fName1", user['name1'], driver)
    send_keys("#fName2", user['name2'], driver)
    send_keys('#fPhone', user['phone'], driver)
    send_keys('#fEmail', user['email'], driver)
    send_keys('#fCountry', user['country'], driver)
    send_keys('#fAddress', user['address'], driver)
    send_keys('#fChangwat', '**', driver)
    send_keys('#fPostcode', user['postcode'], driver)
    send_keys('#fUsername', user['username'], driver)
    send_keys('#fPassword', user['password'], driver)
    send_keys('#fPasswordCheck', user['passwordCheck'], driver)
    sleep(0.5)
    return user


if __name__ == '__main__':
    o = random_personnal_infos()

    print()