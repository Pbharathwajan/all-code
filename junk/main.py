import webview

window = None #initialize variable

def operation():
    num1 = window.evaluate_js( "document.getElementsByID('num1').value" )
    if num1 ==5:
        print("cow")

def main(window):
  pass #this runs when window is created


window = webview.create_window('joe',url='joe.html')

window.expose(operation)

webview.start(main, window)