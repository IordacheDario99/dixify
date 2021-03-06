# Dixify
 A python app that allows the user to test his/her diction 
 
 
 [RO]
 
 
Documentatie Dixify

![image](https://user-images.githubusercontent.com/49655223/110222145-d1a1a700-7ed8-11eb-823b-ef139532eae7.png)


•	Ce este Dixify ?
Dixifi este o aplicatie desktop (momentan) care permite utilizatorilor ei sa isi testeze dictia in limba engleza. Dixify  vine cu trei niveluri de dificultate si un dictionar:

o	Beginner, pentru vorbitorii de engleza mai putin experimentati.
o	Intermediate, pentru vorbitorii de engleza mai avansati
o	Expert, pentru vorbitorii de engleza foarte avansati
o	Dictionary, permite utilizatorului posibilitatea de a invata noi cuvinte sau termeni in limba engleza

•	Cum a luat nastere Dixify?
Aceasta aplicatie a luat nastere deoarece am fost pus de nenumarate ori in situatii in care a trebuit sa port o discutie in limba engleza cu mai multi straini, iar acestia nu ma puteau intelege deoarece stalceam (nu reuseam sa articulez) anumite cuvinte din prima. Aceste situatii stanjenitoare m-au inspirat sa creez aceasta aplicatie, nu doar pentru mine cat si pentru toti vorbitorii de engleza care se regasesc in situatia descrisa mai sus.

•	Publicul tinata
Asa cum am mentionat si mai sus, aceasta aplicatie este menita oricariui vorbitor de limba engleza care doreste sa isi imbunatateasca dictia dar in special elevilor din clasele 3 – 5 deoarece un astfel de tool este foarte poate oferi o dezvolatare a dictiei micilor invatacei foarte vertiginoasa.

•	Obiectiv
Obiectivul aceste aplicatii este de a usura procesul de invatare al limbii engleze prin intermediul exercitiului (“Practice is the best of all instructors.” - Publilius Syrus), elevul putand avea pe durata intregului proces de invatare parte de un feedback constructiv.

•	Tehnolgii folosite
o	Python (backend)
o	Kivy (GUI)
o	API’s and libraries : SpeechRecognition, pyttsx3, PyAudio, wikipedia
Python

Python este un limbaj de programare dinamic multi-paradigmă, creat în 1989 de programatorul olandez Guido van Rossum. Van Rossum este și în ziua de astăzi un lider al comunității de dezvoltatori de software care lucrează la perfecționarea limbajul Python și implementarea de bază a acestuia, CPython, scrisă în C. Python este un limbaj multifuncțional folosit de exemplu de către companii ca Google sau Yahoo! pentru programarea aplicațiilor web, însă există și o serie de aplicații științifice sau de divertisment programate parțial sau în întregime în Python. Popularitatea în creștere, dar și puterea limbajului de programare Python au dus la adoptarea sa ca limbaj principal de dezvoltare de către programatori specializați și chiar și la predarea limbajului în unele medii universitare. Din aceleași motive, multe sisteme bazate pe Unix, inclusiv Linux, BSD și Mac OS X includ din start interpretatorul CPython.

Python pune accentul pe curățenia și simplitatea codului, iar sintaxa sa le permite dezvoltatorilor să exprime unele idei programatice într-o manieră mai clară și mai concisă decât în alte limbaje de programare ca C. În ceea ce privește paradigma de programare, Python poate servi ca limbaj pentru software de tipul object-oriented, dar permite și programarea imperativă, funcțională sau procedurală. Sistemul de tipizare este dinamic iar administrarea memoriei decurge automat prin intermediul unui serviciu „gunoier” (garbage collector). Alt avantaj al limbajului este existența unei ample biblioteci standard de metode.


Kivy 

Kivy este un framework Python gratuit și open source pentru dezvoltarea de aplicații mobile și alte aplicații software multitouch cu o interfață de utilizator naturală (NUI). Este distribuit în condițiile licenței MIT și poate rula pe Android, iOS, GNU / Linux, macOS și Windows.

Kivy este framework-ul principal dezvoltat de organizația Kivy, alături de Python pentru Android, Kivy iOS, și alte câteva biblioteci menite să fie utilizate pe toate platformele. În 2012, Kivy a primit o subvenție de 5.000 USD de la Python Software Foundation pentru portarea acestuia în Python 3.3. [6] Kivy susține, de asemenea, Raspberry Pi, care a fost finanțat prin Bountysource.




SpeechRecognition 3.8.1

Este o librarie care este utilizata pentru recunoasterea si conversia cuvintelor captate prin intermediul unui microfon. Aceasta librarie preia continutul audio inregistrat in momentul vorbirii si il trimite catre un motor de recunoastere a vorbirii (Speech recognition engine) precum Google Speech Recognition, IBM Speech to Text, Microsoft Azure Speech etc. Dupa ce continutul audio a fost convertit de catre unul dintre engine-urile mentionate mai sus,a cest engine returneaza un sir de caractere care contine cuvintele ordonate in ordinea rostirii.


pyttsx3 2.90

pyttsx3 este o bibliotecă ce realizeaza o conversie text-vorbire pentru Python. Spre deosebire de bibliotecile alternative, funcționează offline și este compatibil atât cu Python 2, cât și cu 3. Pin intermediul acestei librarii putem primii un feedback audio. Astfel de librarii sunt utilizate pentru realizarea asistentilor virtuali precum Siri, Alexa sau Google Assistant.


wikipedia 1.4.0

Este o librarie pentru Python care permite comunicarea cu faimosul Parinte al Cunostintelor si anume Wikippedia. Ce face aceasta librarie mai exact? Ei bine, daca solicitam un serviciu prin intermediul acestei librarii, iar acest serviciu presupune cautarea unei anumite informatii, atunci cand apelam  aceasta librarie (o functie din acea librarie), ea face o cautare in Wikipedia si returneaza datele solicitate prin serviciul curent.













Procesul de dezvlotare al resursei educationale

Primul pas pe care il presupune dezvoltarea oricarei aplicatii este documentarea pe topicul dorit. Cum aveam deja in plan sa realizez o aplicatie similara (Don’t buy Alexa! Buid your own.) nu mi-a fost prea greu sa realizez aceasta etapa. Dupa ce am adunat toate resursele necesare, am inceput incetul cu incetul sa dezvolt aplicatia. 

Backend:
Pe partea de logica a aplicatie, am inceput sa importez librariile necesare (cele mentionate mai sus)

import speech_recognition as sr
import pyttsx3
import random
import gc
import wikipedia

unde:
•	 libraria random a fost utilizata in prima etapa de dezvoltare a aplciatiei pentru a genera un numar random de la 1 la 3 (unde 1,2,3 sunt nivelurile de dificultate) si pentru a extrage un element random dintr-o lista data.
•	Libraria gc presucrtarea termenului de garbage collector, aceasta librarie am utilizat-o pentru eliberarea memoriei la un moment dat in timpul procesului pentru a reseta listener-ul (intra intr-o bucla care crestea de n ori, unde n este numarul de incercari pentru validarea cuvantului rostit)

class DixifyBot (App) :
    def build(self) :
        return kv
am definit clasa DixifyBot si functia de build, functie necesare pentru genrearea GUI-ului.
In interiorul clasei DixifyBot am implementat urmatoarele metode.
def slower(self, word) :
    engine.setProperty ('rate', 100)
    engine.say (word)
    engine.runAndWait ()
    print ('slower')
Metoda slower primeste ca parametru instanta obiectului la momentul apelarii self si word (care este cuvantul extras dintr-o lista de stringrui). Rolul acestei functii este de a seta viteza cu care vocea bot-ului rosteste cuvintele dupa < engine.setProperty ('rate', 100) # unde viteza normala este 200>care ii este solicitat sa pronunte cuvantul primit ca argument < engine.say (word)>


def normal_speed(self, word) :
    engine.setProperty ('rate', 200)
    engine.say (word)
    engine.runAndWait ()
    print ('normal')
Metoda normal speed are functia de a reseta viteaza cu care robotul rosteste cuvantul primit ca argument 

def listening(self, word) :
    try :
        with sr.Microphone () as source :
            word = word
            self.display (word)
            engine.setProperty('rate', 200)
            engine.say ('Say' + word)
            engine.runAndWait ()
            command = self.microphone()


            if word in command :
                engine.say ('correct')
                engine.runAndWait ()
                print ('correct')
                gc.collect()
            else :
                for i in range (3) :

                    if i == 0 :
                        slower = False
                        self.normal_speed (word)
                        command = self.microphone()
                        if word in command :
                            self.normal_speed ('')
                            engine.say ('correct')
                            engine.runAndWait ()
                            print ('correct')
                            break
                    #     if after the return the word is correct then exit for

                    elif i == 1 :
                        slower = True
                        self.slower (word)
                        command = self.microphone()
                        if word in command :
                            self.normal_speed ('')
                            engine.say ('correct')
                            engine.runAndWait ()
                            print ('correct')
                            break

                    elif i == 2 :
                        self.normal_speed ('')
                        engine.say ('last chance, say' + word)
                        engine.runAndWait ()
                        self.slower (word)
                        print ('Last chance')
                        command = self.microphone()
                        if word in command :
                            self.normal_speed ('')
                            engine.say ('correct')
                            engine.runAndWait ()
                            print ('correct')
                            break
                        else :
                            self.normal_speed ('')
                            engine.say ('Don\'t give up, study more and you\'ll get it! ')
                            engine.runAndWait ()
                            print ('Don\'t give up, study more and you\'ll get it!')


    except :
        print("Didn't quite hear you")
        engine.setProperty('rate', 200)
        pass

Metoda Listening este “creierul” robotuli, in aceasta metoda se realizeaza validarea cuvantului rostit de catre utilizator. Daca cuvantul primit ca argument din lista de stringuri este regasit in command, unde command este o variabila care memoreaza cuvantul rostit de catre utilizator, atunci bot-ul felicita utilizatorul iar bucla for este intrerupta (din prima incerca nici macar nu se intra in for...). Insa, daca cuvantul primit ca argument nu este identic cu cel din command, atunci bot-ul ii cere utilizatorului sa rosteasa inca o data cuvantul (care este afisat pe ecra, si pe care il rosteste si bot-ul <la cea de-a doua incercare, bot-ul rostestr cuvantul mai rar si mai apasta, iar la a treia  incercare acesta il avertizeaza pe utilizator ca mai are aceasta este ultima sansa, daca nici din a treia incercare utilizatorul nu reuseste sa rosteasca corect cuvantul, atunci bot-ul ii spune utilizatorului sa nu renunte si sa invete cu mai multa harnicie iar apoi bucla se inchide >)

def microphone(self):
    try :
        with sr.Microphone () as source :
            print(threading.current_thread())
            print ("Listening ...")
            voice = listener.listen (source, phrase_time_limit=2.0)
            command = listener.recognize_google (voice)
            print("Mic off")
            gc.collect ()


    except:
        pass
    return command

Cand aceasta functie este apelata, se reinitializeaza sursa microfonului iar porcesul de ascultare a utilizatorului si de procesare a datelor primite de la acesta (speech to text) este solicitat inca o data urmand ca mai apoi sa se elibereze memoria din gc. Aceasta functie returneaza la incheierea apelarii variabila command (in care este salvat sirul de caractere returnat dupa conversia speech to text). In cazul in care microfonul nu percepe nici un zgomot pe care poate sa il recunoasca ca fiind  o propozitie (in cazul nostru un cuvant) acesta in loc sa returneze o eroare sare peste exceptie. Timpul in care microfonul este deschis este de maxim 2 secunde (am ales aceasta contrangere pentru a evita anumite bug-uri (microfounul nu mai percepe cuvintele de pe la a treia runda <new word>.btn))

def difficulty_lv(self, seleceted_dificulty) :
    global random_word
    if seleceted_dificulty == 1 :
        easy = ['car', 'cat', 'dog', 'rat', 'fish', 'wolf', 'clock']
        random_word = random.choice (easy)
    elif seleceted_dificulty == 2 :
        intermediate = ['intermediate', 'protected', 'exhausted', 'interdependence', 'knowledge']
        random_word = random.choice (intermediate)
    elif seleceted_dificulty == 3 :
        expert = ['apprenticeship', 'eminently', 'reversal', 'brewery', 'defibrillator', 'exponentially']
        random_word = random.choice (expert)

    return random_word

Aceasta metoda returneaza un cuvant ales random din liste in functie de nivelul de dificultate selectat de catre utilizator print GUI. Aceasta metoda are ca parametrii self si seleceted_difficulty (1 = Beginner, 2 = Intermediate, 3 = Expert)

def display(self, word_to_display) :
    print (word_to_display)
    return word_to_display

Este o metoda depreciata

class MainMenu (Screen) :

    def beginner_lv(self) :
        mainApp = MainApp ()
        mainApp.new_word (1)
        return 1

    def intermediate_lv(self) :
        mainApp = MainApp ()
        mainApp.new_word (2)
        return 2

    def expert_lv(self) :
        mainApp = MainApp ()
        mainApp.new_word (3)
        return 3

Clasa Main Menu este punctul de legatura intre backend si GUI (pe laga restul claselor create special pentru a realiza GUI-ul, that’s the way Kivy works). De aici ne intereseaza mai mult codul pentru Kivy necesar realizarii GUI-ului.

GUI:
Pe partea de GUI (Graphic User Interface) m-am decis sa aleg framework-ul celor de la Kivy deoarece intentionez ca in viitorul apropiat sa portez aceata aplicatie pe unul dintre cele mai populare sisteme de operare mobila deoarece Kivy este un framework corssplatform  destul de usor de inteles si de utilizat.

Pima data am inceputcu cu crearea celor 5 ecrane (Main Menu, Beginner, Intermediate, Expert si Dictionary )

<MainMenu>:
    name: "main_menu"
<Beginner>
    name: "beginner"
    the_word: the_word
<Intermediate>
    name: "intermediate"
    the_word: the_word
<Expert>
    name: "expert"
    the_word: the_word
<Dictionary>
    name: "dictionary"
    typed_word: typed_word

Pentru a putea gestiona cele 5 ecrane avem nevoie de un manager de ecrane, in cazul nostru AppManager

AppManager:
    MainMenu:
    Dictionary:
    Beginner:
    Intermediate:
    Expert:

In aceasta clasa initializam ecranele pe care dorim sa le folosim.

Design-ul pentru Main Menu include:
•	Un GridLayout (modul pirin care sunt dispuse elementele <btn, lable etc> pe ecran)
•	Un lable
•	4 butoane
<MainMenu>:
    name: "main_menu"

    GridLayout:
        cols: 1
        Label:
            background_color: 0.2, 0.13, 0.54, 1
            text: "Difficulty Lv"
            font_size: 40
            bold: True

        GridLayout:
            cols: 1

            Button:
                text: "Beginner"
                font_size:40
                background_color: utils.get_color_from_hex('#14e114')
                on_release:
                    app.root.current = "beginner"
                    root.manager.transition.direction = "up"
		     root.beginner_lv()

In momentul in care utilizatorul a apasat si a luat degetul de pe butonul mouse-ului atunci este solicitat ecranul cu numele “beginner” iar acesta revin in prim plan printr-o animatie de la jos in sus. Dupa ce ecranul a intrat in prim plan atunci se apeleaza functia beginner_lv() functie a carei logica este implementata in python

def beginner_lv(self) :
    mainApp = MainApp ()
    mainApp.new_word (1)
    return 1

Prin aceasta functie se seteaza nivelul de dificultate al cuvintelor (1 = beginnerm 2 = intermediate, 3 = expert ). 

Acelasi lucru se intampla si pentru celelalte 3 cazuri
Button:
    text: "Intermediate"
    font_size:40
    background_color: utils.get_color_from_hex('#e5ff24')
    on_release:
        app.root.current = "intermediate"
        root.intermediate_lv()
        root.manager.transition.direction = "up"
Button:
    text: "Expert"
    font_size:40
    background_color: utils.get_color_from_hex('#c22e2e')
    on_release:
        app.root.current = "expert"
        root.expert_lv()
        root.manager.transition.direction = "up"

Button:
    text: "Dictionary"
    font_size:40
    background_color: utils.get_color_from_hex('#148ce1')
    on_release:
        app.root.current = "dictionary"
        root.manager.transition.direction = "up"

Design-ul pentru Beginner include:
•	3 elemente de tip lable
•	2 butoane 

<Beginner>
    name: "beginner"
    the_word: the_word
    RelativeLayout:
        Label:
            text: "Beginner"
            color: utils.get_color_from_hex('#e5ff24')
            font_size: 40
            bold: True
            pos_hint: { 'y': 0.4 ,'x': .0}

        Label:
            text: "Say:"
            font_size: 40
            bold: True
            pos_hint: { 'y': 0.2 ,'x': .0}

        Label:
            id: the_word
            text: the_word.text
            font_size: 40
            bold: True
            pos_hint: { 'y': 0.1 ,'x': .01}

        Button:
            text: "Menu"
            size: 200,50
            size_hint: None, None
            pos_hint: { 'y': 0.2 ,'x': .38}
            on_release:

                app.root.current = "main_menu"
                root.manager.transition.direction = "down"
        Button:
            size: 200,50
            size_hint: None, None
            pos_hint: { 'y': 0.3 ,'x': .38}
            text: "New Word"
            on_press:
                root.set_text()

            on_release:
                root.generate_word()

In momenutl apasarii butonului “Menu”, GUI-ul apealea managerul de ecrane si ii cere sa schimbe ecranul principal (Beginner) cu ecranul secundar (Main menu, care mai apoi devine principa si tot asa). Dupa ce utilizatorul a apasat pe butonul “Menu” acesta este trimis catre ecranul Main Menu printr-o animatie de sus pana jos

Daca utilizatorul apasa butonul “New Word” atunci se apeleaza functia set_text() iar dupa ridicarea decetului de pe butonul mouse-ului se apealeaza functia generate_word() 
def set_text(self):
    dix = DixifyBot ()
    word = dix.difficulty_lv (1)
    self.wo = dix.difficulty_lv(1)

    self.the_word.text = self.wo

def generate_word(self):
    dix = DixifyBot()
    print(self.wo)
    dix.listening(self.wo)
    gc.collect ()

Acelasi lucru se intampla si pentru celelalte 3 cazuri

Design-ul pentru Dictionary include:
•	1 lable
•	2 butoane
•	1 element de tip text_input
•	<Dictionary>
    name: "dictionary"
    typed_word: typed_word
    RelativeLayout:

        Label:
            text: "Search definition for a word"
            font_size: 40
            bold: True
            pos_hint: { 'y': 0.1 ,'x': .01}

        TextInput:
            id: typed_word
            size: 500,40
            size_hint: None, None
            multiline: False
            background_color: 1, 1, 1, 0.6
            font_size: 20
            pos_hint: { 'y': 0.5 ,'x': .2}

        Button:
            size: 200,50
            size_hint: None, None
            pos_hint: { 'y': 0.2 ,'x': .38}
            text: "Menu"
            on_release:
                app.root.current = "main_menu"
                root.manager.transition.direction = "down"
        Button:
            size: 200,50
            size_hint: None, None
            pos_hint: { 'y': 0.3 ,'x': .38}
            text: "Search"
            on_release:
                root.search()

In Dictionary utilizatorul este indemnat sa introduca un cuvant pentru care vrea sa caute o defintie. Dupa ce utilizatorul apasa butonul de “Search”, GUI-ul apeleaza metoda search()
Care primeste ca parametru elementul pe care utilizatorul l-a introdus (text).

def search(self):
    try:

        print (self.typed_word.text)
        wiki = wikipedia.summary (self.typed_word.text, sentences=1)
        # engine.setProperty('rate', 200)
        engine.say (wiki)
        engine.runAndWait ()
        print (wiki)
    except:
        engine.say("I can't find a definition for this word !")
        engine.runAndWait()
 
Pe partea de backend se face procesarea elementului introdus de catre utilizator, urmand ca mai apoi sa se returneze rezultatul cautarii, rezultat care este salvat in variabila wiki (care contine un string cu definitia gasita pe wikipedia intr-o propozitie deoarece am solicitat ca numarul de propozitii sa fie = 1), variabila pe care mai apoi robotul o converteste din text in aduio.
•	Further development
o	Interactionarea cu aplicatia prin (sau numai prin) intermediul comenzilor vocale
o	Dezvoltarea unei interfete mobile friendly (touch control, notifications etc.)
o	Implemenatarea unei modalitatie de evaluare (scor, nivel)
o	Dezvolatarea unor moduri de joc (training, competitive, ranked, multiplayer<local> etc)

•	Demo
https://www.youtube.com/watch?v=fYvAnaBkBTc&t=3s&ab_channel=AndreiDario

•	Bibliografie

o	https://en.wikipedia.org/wiki/Python_(programming_language)
o	https://en.wikipedia.org/wiki/Kivy_(framework)
o	https://pypi.org/project/SpeechRecognition/
o	https://pypi.org/project/pyttsx3/
o	https://pypi.org/project/wikipedia/
