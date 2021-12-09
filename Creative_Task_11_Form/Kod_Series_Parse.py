### Грибной Биом - Компьютерная Лингвистика (10.12.2021)

### Импорт Библиотек

import requests
from pyquery import PyQuery as pq
from tqdm import tqdm_notebook
from lxml import etree
import time

### Вспомогательные Переменные

link = "http://serial.vvord.ru/Sverhestestvennoe/"
linkf = ''
M = ''

### Все Массивы

Mas1 = ['','Pilot', 'Wendigo','Dead-in-the-Water', 'Phantom-Traveler','Bloody-Mary','Skin', 'Hookman', \
        'Bugs', 'Home', 'Asylum','Scarecrow', 'Faith', 'Route-666', 'Nightmare', 'The-Benders', 'Shadow', \
        'Hell-House', 'Something-Wicked', 'Provenance', "Dead-Mans-Blood", 'Salvation', 'Devils-Trap']

Mas2 = ['','In-My-Time-of-Dying','Everybody-Loves-a-Clown','Bloodlust','Children-Shouldnt-Play-with-Dead-Things', \
        'Simon-Said','No-Exit','The-Usual-Suspects','Crossroad-Blues','Croatoan','Hunted','Playthings', \
        'Night-Shifter','13-15','Born-Under-a-Bad-Sign','Tall-Tales','16-18','Heart','Hollywood-Babylon', \
        '19-22','What-Is-and-What-Should-Never-Be','All-Hell-Breaks-Loose-Part-1','All-Hell-Breaks-Loose-Part-2']

Mas3 = ['','The-Magnificent-Seven','The-Kids-Are-Alright','Bad-Day-At-Black-Rock','Sin-City','Bedtime-Stories', \
        'Red-Sky-At-Morning','Fresh-Blood','A-Very-Supernatural-Christmas','Malleus-Maleficarum','Dream-a-Little-Dream-of-Me', \
        'Mystery-Spot','Jus-In-Bello','Ghostfacers','Long-Distance-Call','Time-Is-On-My-Side','No-Rest-for-the-Wicked']

Mas4 = ['','Lazarus-Rising','Are-You-There--God-Its-Me-Dean-Winchester','In-The-Beginning','Metamorphosis', \
        'Supernaturals04e05-and-Bonus','Yellow-Fever','It%60s-the-Great-Pumpkin--Sam-Winchester','Wishful-Thinking', \
        'I-Know-What-You-Did-Last-Summer','Heaven-and-Hell','Family-Remains','Criss-Angel-Is-a-Douche-Bag', \
        'After-School-Special','Sex-and-Violence','Death-Takes-a-Holiday','On-the-Head-of-a-Pin','Its-a-Terrible-Life', \
        'The-Monster-at-the-End-of-This-Book','Jump-the-Shark','The-Rapture','When-the-Levee-Breaks','Supernaturals04e22-and-Bonus']

Mas5 = ['','Sympathy-for-the-Devil','Good-God--YAll','Free-to-Be-You-and-Me','The-End','Fallen-Idols', \
        'I-Believe-the-Children-Are-Our-Future','The-Curious-Case-of-Dean-Winchester','Changing-Channels', \
        'The-Real-Ghostbusters','Abandon-All-Hope','Sam--Interrupted','Swap-Meat','The-Song-Remains-the-Same', \
        'My-Bloody-Valentine','Dead-Men-Dont-Wear-Plaid','Dark-Side-of-the-Moon','99-problems','Point-of-No-Return', \
        'Hammer-of-the-Gods','The-Devil-You-Know','Two-Minutes-to-Midnight','Swan-Song']

Mas6 = ['','Exile-on-Main-St','Two-and-a-Half-Men','The-Third-Man','Weekend-at-Bobbys','Live-Free-or-Twihard', \
        'You-Cant-Handle-the-Truth','Family-Matters','All-Dogs-Go-to-Heaven','Clap-Your-Hands-If-You-Believe', \
        'Caged-Heat','Appointment-in-Samarra','Like-a-Virgin','Unforgiven','Mannequin-3:-The-Reckoning', \
        'The-French-Mistake','And-Then-There-Were-None','My-Heart-Will-Go-On','Frontierland','Mommy-Dearest', \
        'The-Man-Who-Would-Be-King','Let-It-Bleed','The-Man-Who-Knew-Too-Much']

Mas7 = ['','Meet-the-New-Boss','Hello--Cruel-World','The-Girl-Next-Door','Defending-Your-Life','Shut-Up--Dr-Phil', \
        'Slash-Fiction','The-Mentalists','Season-Seven--Time-for-a-Wedding!','How-to-Win-Friends-and-Influence-Monsters', \
        'Deaths-Door','Adventures-in-Babysitting','Time-After-Time','The-Slice-Girls','Plucky-Pennywhistles-Magic-Menagerie', \
        'Repo-Man','Out-with-the-Old','The-Born-Again-Identity','Party-On--Garth','Of-Grave-Importance', \
        'The-Girl-with-the-Dungeons-and-Dragons-Tattoo','Reading-is-Fundamental','There-Will-Be-Blood','Survival-of-the-Fittest']

Massive = ['',Mas1, Mas2, Mas3, Mas4, Mas5, Mas6, Mas7]

### Функция для Парсинга

def func(sezon_n, Mas):
    for k in range (1,len(Mas)):
        print('')
        print(Mas[k]) # Вывод Названия Серии (необязательно, но помогает ориентироваться)
        
        for i in range(1,13):
            print(str(i)) # Отображении Страницы Серии (необязательно)
            if True:
                num = str(i)
                ser_name = Mas[k]
                linkf = link + 'sezon-' +sezon_n + '/' + ser_name + '/' + num

                listw = requests.get(linkf)
                M = pq(listw.text).find('pre').text()

                if (M == ''):
                    break
                else:
                    print(M) # Вывод текста страницы

### Вывод
                    
timer0 = time.time()
timer2 = 0

for l in range(1,8): # Цикл для вывода всех сезонов. Изначально - (1,8) (Тут можно контролировать вывод, изменяя интервалы*)
    Mas = Massive[l]
    sezon_n = str(l)
    print('')
    print('SEASON ', l) # Вывод Номера Сезона (необязательно, но помогает ориентироваться)
    print(func(sezon_n, Mas))

    timer1 = time.time()
    print(timer1 - timer2 - timer0) # Таймер Ради интереса (необязательно)
    timer2 = timer1 - timer0 - 5 * (l-1)
    time.sleep(5) # Таймер перехода между Сезонами (необязательно)
    
    
    
    
    # 100 Строчка
