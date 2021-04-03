import pickle
import os
import datetime
import sys
import pygame
from pygame.locals import *
foreverat = os.getcwd()
def rightmusic():
    global foreverat
    os.chdir(foreverat)
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("english_right.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            num = 1
    except:
        pass
def wrongmusic():
    global foreverat
    os.chdir(foreverat)
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("english_wrong.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            num = 1
    except:
        pass
while True:
    rightlist = []
    wronglist = []
    try:
        import pyttsx3
        man = pyttsx3.init()
        from win10toast import ToastNotifier
        toast = ToastNotifier()
    except:
        pass
    words = {}
    cmd = input("Which mode do you want to choice?\nW - Write Mode\nT - Test Mode\n").upper()
    if cmd == "W":
        while True:
            try:
                wordEn = input("Input English of this word: ")
                if wordEn == "EXIT":
                    cmd = input("Are you sure you want to EXIT?(Y/N)").upper()
                    if cmd == "Y":
                        break
                wordZh = input("Input Chinese of this word: ")
                if wordEn == "EXIT" or wordZh == "EXIT":
                    cmd = input("Are you sure you want to EXIT?(Y/N)").upper()
                    if cmd == "Y":
                        break
                print("")
                words[wordEn] = wordZh
            except KeyboardInterrupt:
                break
        asker = input("Do you want to save this?(Y/N)").upper()
        if asker == "Y":
            path = input("Input path:")
            os.chdir(path)
            print("Now Working At:",os.getcwd())
            cmd = input("Go on(Y/N)").upper()
            if cmd == "N":
                sys.exit()
            if cmd == "Y":
                pass
            filename = input("Input filename:")
            writefile = open(filename,"wb+")
            pickle.dump(words,writefile)
            writefile.close()
        if asker == "N":
            sys.exit()
    if cmd == "T":
        print("Please read the file first.")
        path = input("Input path:")
        os.chdir(path)
        print("Now working at:",os.getcwd())
        asker = input("Go on?(Y/N)").upper()
        if asker == "N":
            sys.exit()
        if asker == "Y":
            pass
        filename = input("Input filename: ")
        try:
            loadfile = open(filename,"rb")
            words = pickle.load(loadfile)
            loadfile.close()
        except FileNotFoundError:
            print("File Not Found.")
        except PermissionError:
            print("Not allowed read this file.")
        except:
            print("Unknown Error!")
        score = 0
        for name in words.keys():
            wordEn = name
            wordZh = words[wordEn]
            print(wordEn)
            try:
                man.say(wordEn)
                man.runAndWait()
            except:
                pass
            inputWordZh = input("Input Chinese of this word: ")
            if inputWordZh != "":
                if inputWordZh == wordZh or inputWordZh in wordZh:
                    score += 1
                    rightlist.append(inputWordZh)
                    print("You are right.")
                    print("")
                    rightmusic()
                elif inputWordZh != wordZh:
                    wronglist.append(inputWordZh)
                    print("There are some wrong.")
                    print("")
                    wrongmusic()
            if inputWordZh == "":
                textwillappend = wordZh + "_IS_EMPTY"
                wronglist.append(textwillappend)
                print("There are some wrong.")
                print("")
                wrongmusic()
        print("Questions:",str(len(words)),"Ticks:",str(score),"Wrongs:",str(len(words)-score))
        print("Wrong List:")
        print(wronglist)
        print("Right List:")
        print(rightlist)
    cmd = input("Stay in software?(Y/N)").upper()
    cmd2 = input("Clear?(Y/N)").upper()
    if cmd2 == "Y":
        os.system("cls")
    if cmd == "Y":
        pass
    if cmd == "N":
        break
try:
    os.chdir(foreverat)
    toast.show_toast("Thank you for using this App!","Developer Rice",icon_path="wricon.ico",duration=10)
except:
    pass

