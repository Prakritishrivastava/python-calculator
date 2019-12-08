import re
print("our calculator")
print("type 'quite' to exit \n ")
previous=0
run=True
def performmath():
    global run
    global previous
    equ=""
    if previous==0:
     equ=input("enter the equation:")
    else:
        equ=input(str(previous))
    if equ=="quit":
        run=False
    else:
        equ=re.sub('[a-zA-Z\,.:;""]','',equ)
        if previous==0:
           previous=eval(equ)
        else:
            previous=eval(str(previous)+equ)
        print("your result",previous)
while run:
    performmath()
