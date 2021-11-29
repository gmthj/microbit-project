from microbit import *
import radio
radio.on()
radio.config(channel = 33) #different channels for different classes 
radio.config(power=7)

T1 = Image("00000:00000:00900:00000:00000")
T2 = Image("00000:09990:09090:09990:00000")
T3 = Image("99999:90009:90009:90009:99999")
send = [T1, T2, T3, T1, T2, T3, T1, T2, T3]

l1 = Image("90000:00000:00000:00000:00000")

student_id = "3301" #first and last 2 digits represent the student's class and register number respectively


######################   used to change student id for demonstration purposes only
count=1
while True:
    display.show(count)
    if button_b.was_pressed():
        count+=1
        if count>=10:
            count=1
    if button_a.is_pressed():
        student_id="330"+str(count)
        break
display.scroll(student_id)
##################################################


while True:
    state=False
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            display.show(send)
            display.clear()
            break
    
    while True:
        if state==False:
            display.show(l1)
        incoming = radio.receive()
        if incoming == "send id":
            radio.send(student_id)
        if incoming == student_id:
            display.show(Image.YES)
            state=True
            sleep(500)
        if incoming == student_id+"error":
            display.show(Image.NO)
            sleep(1000)
        if button_a.is_pressed() and button_b.is_pressed():
            display.scroll("OFF")
            display.clear()
            break
        
        








