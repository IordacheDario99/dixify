import speech_recognition as sr
import pyaudio
import threading
import pyttsx3
import random
import gc
import wikipedia

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

listener = sr.Recognizer ()
engine = pyttsx3.init ()

class DixifyBot (App) :
    def build(self) :
        return kv

    def slower(self, word) :
        engine.setProperty ('rate', 100)
        engine.say (word)
        engine.runAndWait ()
        print ('slower')

    def normal_speed(self, word) :
        engine.setProperty ('rate', 200)
        engine.say (word)
        engine.runAndWait ()
        print ('normal')
        pass

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
        # return command

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


    def display(self, word_to_display) :
        print (word_to_display)
        return word_to_display



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


class MainApp (Screen) :
    the_word = ObjectProperty (None)

    def new_word(self, *dfl) :
        global randoom_word





class Dictionary (Screen) :
    typed_word = ObjectProperty(None)

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





class Beginner(Screen):
    the_word = ObjectProperty(None)
    dix = DixifyBot ()
    wo = dix.difficulty_lv(1)

    def generate_word(self):
        dix = DixifyBot()
        # word = dix.difficulty_lv(1)
        # self.set_text(word)
        print(self.wo)
        dix.listening(self.wo)
        gc.collect ()

    def set_text(self):
        dix = DixifyBot ()
        word = dix.difficulty_lv (1)
        self.wo = dix.difficulty_lv(1)

        self.the_word.text = self.wo

class Intermediate(Screen):
    the_word = ObjectProperty (None)
    dix = DixifyBot ()
    wo = dix.difficulty_lv (2)

    def generate_word(self) :
        dix = DixifyBot ()
        # word = dix.difficulty_lv(1)
        # self.set_text(word)
        print (self.wo)
        dix.listening (self.wo)
        gc.collect ()

    def set_text(self) :
        dix = DixifyBot ()
        word = dix.difficulty_lv (1)
        self.wo = dix.difficulty_lv (2)

        self.the_word.text = self.wo

class Expert(Screen):
    the_word = ObjectProperty (None)
    dix = DixifyBot ()
    wo = dix.difficulty_lv (3)

    def generate_word(self) :
        dix = DixifyBot ()
        # word = dix.difficulty_lv(1)
        # self.set_text(word)
        print (self.wo)
        dix.listening (self.wo)
        gc.collect ()

    def set_text(self) :
        dix = DixifyBot ()
        self.wo = dix.difficulty_lv (3)

        self.the_word.text = self.wo

class AppManager (ScreenManager) :
    pass


sm = AppManager ()

kv = Builder.load_file ("dixifybot.kv")

bot_voice = engine.getProperty ('voices')
engine.setProperty ('voice', bot_voice[1].id)
ran = random.randrange (1, 3, 1)

#
# class GridView (Widget) :
#     pass




if __name__ == '__main__' :
    DixifyBot ().run ()

# dixify=DixifyBot()
# dixify.listening()
