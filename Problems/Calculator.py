import PySimpleGUI as ui

x = int()

n = ()

rad_1 = ['bin0', 'dec0', 'hex0', 'oct0']
rad_2 = ['bin1', 'dec1', 'hex1', 'oct1']

#Definitions

def bin_to_bin():
    x = (bin(int(str(n), 2))) #Binary to Binary?


def bin_to_dec():
    x = (int(str(n), 2)) #Binary to decimal


def bin_to_oct():
    x = (oct(int(str(n), 2)))


def bin_to_hex():
    x = (hex(int(str(n), 2)))


def dec_to_bin():
    x = (bin(int(n)))


def dec_to_dec():
    x = (int(n))


def dec_to_oct():
    x = (oct(int(n)))


def dec_to_hex():
    x = (hex(int(n)))


def oct_to_bin():
    x = (bin(int(str(n), 8)))


def oct_to_dec():
    x = (int(str(n), 8))


def oct_to_oct():
    x = (oct(int(str(n), 8)))


def oct_to_hex():
    x = (hex(int(str(n), 8)))


def hex_to_bin():
    x = (bin(int(str(n), 16)))


def hex_to_dec():
    x = (int(str(n), 16))


def hex_to_oct():
    x = (oct(int(str(n), 16)))


def hex_to_hex():
    x = (hex(int(str(n), 16)))
    

#gui 

win1_active = False
win2_active = False
win3_active = False
win4_active = False

ui.theme('LightGray1')    



col1 = [[ui.Text("Choose system to convert from")],
            [ui.Radio('Binary', "RADIO1", default=True, key=rad_1[0]),
            ui.Radio('Decimal', "RADIO1", key=rad_1[1]),
            ui.Radio('Hexadecimal', "RADIO1", key=rad_1[2]),
            ui.Radio('Octal', "RADIO1", key=rad_1[3])]]

col2 = [[ui.Text("Choose system to convert to: ")],
            [ui.Radio('Binary', "RADIO2", default=True, key=rad_2[0]),
            ui.Radio('Decimal', "RADIO2", rad_2[1]),
            ui.Radio('Hexadecimal', "RADIO2", rad_2[2]),
            ui.Radio('Octal', "RADIO2", key= rad_2[3])],
            [ui.Text("‏‏‎ ‎")]]

layout = [[ ui.Column(col1), ui.Column(col2)],
        [ui.Text("Enter number here:")],
        [ui.Input(" ", key = 'box') ],
        [ui.Text("The number is"), ui.Text('', key= 'out')],
        [ui.Exit(),ui.Ok()]]


window = ui.Window("Base system calculator", layout)

while True:
    event, values = window.read()
    
    if event == 'Ok':
        try:
            n = int(values['box'])
            print (n)
        except ValueError:
            print("'TIS NOT NUMBER FOOL")
        if event == rad_2[0] and event == rad_1[0]:
            bin_to_bin()
            window['out'](x)
        
            
    if event == 'Exit' or ui.WINDOW_CLOSED:
        break
        window.Close()
    
    
    