from microbit import *
import radio
radio.on()
radio.config(channel = 33) #different channels for different classes
radio.config(power=7)

T1 = Image("00000:00000:00900:00000:00000")
T2 = Image("00000:09990:09090:09990:00000")
T3 = Image("99999:90009:90009:90009:99999")
send = [T3, T2, T1, T3, T2, T1, T3, T2, T1]

all_student_ids = ["3301", "3302", "3303", "3304", "3305", "3306", "3307", "3308", "3309"] #modified for demonstartion purposes
student_ids = [] #modified for demonstration purposes, normally would contain all the student ids and 'all_student_ids" would not exist
attendance = []
total = 0

message="send id"
errmsg="error"



######################   used to add number more students for demonstration purposes only
count=1
while True:
    display.show(count)
    if button_b.was_pressed():
        count+=1
        if count>=10:
            count=1
    if button_a.is_pressed():
        for num in range(count):
            student_ids+=[all_student_ids[num],]
        break
display.scroll(count)
#display.scroll(str(student_ids))
#######################################################




while True:
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            display.show(send)
            display.clear()
            sleep(20)
            break
        
    while True:
        if button_a.is_pressed():
            if attendance == student_ids:
                display.scroll("ALL "+str(total)+" PRESENT")
            else:
                display.scroll(total)
        radio.send(message)
        incoming_id=radio.receive()
        if incoming_id in student_ids and incoming_id not in attendance:#student in class list and trying to mark attendance
            total+=1
            attendance+=[incoming_id,]
            radio.send(incoming_id)
            display.scroll(total)
        elif incoming_id in student_ids and incoming_id in attendance:#student marked attendance already but is still sending
            radio.send(incoming_id)
        elif incoming_id not in student_ids and incoming_id is not None:#student not in class list
            radio.send(incoming_id+errmsg)
        attendance.sort()
        if attendance == student_ids:
            display.show(Image.HAPPY)
        if button_a.is_pressed() and button_b.is_pressed():
            display.scroll("OFF")
            display.clear()
            break
        

        
        
        
        
        
    
    
