import PySimpleGUI as sg
from time import sleep
import os

sg.theme('DarkAmber')  

############ GUI GLOBAL PASSWORD
layout = [ 
        [sg.Text('Enter Global Password',key='in')],
        [sg.Input()],
        [sg.Button('Exit'),sg.Button('Enter')]
    ]


window = sg.Window('authenticator', layout,element_justification='c')

while True:
    event, values = window.read() 
    print(event, values)
    if event in (None,'Exit'):
        window.close()
        break
        print("exit")
    if event == 'Enter':
        try:
            if values[0] == "astro":
                window.close()
                print("correct password")
            else:
                window.close()
                layout = [[sg.Text('Wrong Password.')],[sg.Button('ok')]]
                window = sg.Window('Error', layout, size=(500,300), grab_anywhere=True,element_justification='c')
                while True:
                    event, values = window.read()
                    if event in ('ok',None):
                        window.close()
                        exit()

                print("wrong password")
                exit()
        except KeyError:
            pass
            window.close()

window.close()
window = sg.Window('loading...',[[sg.Text('Loading files, please wait')],[sg.Button('click to start load')]],element_justification="c")
_,_ = window.read()
############
print("Loading config.json")
from platform import system as platform

print(platform())
if not platform():
    layout = [[sg.Text('Unable to identify operating system, abort')],[sg.Button('ok')]]
    window = sg.Window('Error', layout, size=(500,300), grab_anywhere=True,element_justification='c')
    while True:
        event, values = window.read()
        if event in ('ok',None):
            window.close()
            exit()


import os
import json
from datetime import datetime

try:
    os.remove('config.json')
except:
    pass



if platform() == "Windows":
    os.system('dsload.py')

elif platform() == "Linux" or platform == "Darwin":
    print('loading client')
    os.system('python3 dsload.py')

config = json.load(open('config.json','r'))

for movie in config["movies"]:
    if platform() in ('Linux','Darwin'):
        img = movie["image"]
        if not img.split('/')[-1] in os.listdir():
            os.system(f'wget {img}')

window.close()


def mwindow():
    polling = config['polling']
    polling = ('open, click vote to vote' if polling else 'closed')

    layout = [
            
                [sg.Text('Astro Theatre Desktop Client')],
                [sg.Text(f'polling is {polling}')],
                [sg.Button('vote')],
                [sg.Button("refresh")]
            ]

    window = sg.Window('Astro Theatre Desktop Client', layout, size=(500,300), grab_anywhere=True,element_justification='c')
    return window

window = mwindow()

while True:
    try:
        inp,_ = window.read()

        if inp == None:
            exit()

        if inp == "refresh":

            try:
                os.remove('config.json')
            except:
                pass

            if platform() == "Windows":
                os.system('dsload.py')

            elif platform() == "Linux" or platform == "Darwin":
                os.system('python3 dsload.py')

        elif inp == "vote":

            window.close()
            config = json.load(open('config.json','r'))
            userv = []

            for i in config["movies"]:
                out = False
                name = i["name"]
                layout =[
                        [sg.Text(i["name"])],
                        [sg.Image(i["image"].split('/')[-1],size=(200,200))],
                        [sg.Text(i["info"])],
                        [sg.Text("")],
                        [sg.Text(f"would you watch {name}?",justification='c')],
                        [sg.Button('yes'),sg.Button('no')]
                        ]
                window = sg.Window(f'Astro Theatre Desktop Client: Voting for {name}', layout)
                while True:
                    event, values = window.read()
                    if event == None:
                        exit()
                    elif event == 'yes':
                        out = True
                        break
                    elif event == 'no':
                        out = False
                        break
                        window.close()
                userv.append(out)

            window = mwindow()

            os.remove('config.json')
            if platform() == "Windows":
                os.system('dsload.py')
            elif platform() == "Linux" or platform == "Darwin":
                os.system('python3 dsload.py')

            config = json.load(open('config.json','r'))

            for i in range(0,len(userv)):
                if userv[i]:
                    config["votes"][i] +=1

            c = open('config.json','w')
            c.write(json.dumps(config))
            c.close()
            if platform() == "Windows":
                os.system('dsload.py')
            elif platform() == "Linux" or platform == "Darwin":
                os.system('python3 dsload.py')

        elif inp == "exit":
            break

        time = datetime.now().strftime("%H:%M:%S")
        day = datetime.today().weekday()

        if day == 5 and time == "70:20":

            config = json.load(open('config.json','r').read())
            link = config["link"]
            print(f"its time for the movie, join at {link}")



    except Exception as e:

        import traceback
        print(f"exception occoured, tell the developer\n{traceback.format_exc()}")

