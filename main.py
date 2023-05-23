#importing librairies
import utime
from machine import Pin
from pico_ir.read_code import read_code
from pico_ir.send_code import send_code
from pico_ir.validate_code import validate_code, InvalidCodeException


#defining pin led for the 8 digit display
A_led = Pin(5, Pin.OUT)
B_led = Pin(6, Pin.OUT)
C_led = Pin(7, Pin.OUT)
D_led = Pin(8, Pin.OUT)
E_led = Pin(18, Pin.OUT)
F_led = Pin(19, Pin.OUT)
G_led = Pin(20, Pin.OUT)
H_led = Pin(21, Pin.OUT)


#defining different buttons
button_receive = Pin(2, Pin.IN, Pin.PULL_DOWN)
button_emit = Pin(3, Pin.IN, Pin.PULL_DOWN)
#button_select is for changing configuration for the 8 digit display (from 0 to 9)
button_select = Pin(4, Pin.IN, Pin.PULL_DOWN)
#here are the pins for the emitting ir led (pin_out) and the ir receiver (pin_in)
pin_out = Pin(17, Pin.OUT)
pin_in = Pin(16, Pin.IN, Pin.PULL_UP)
led_onboard = Pin(25, Pin.OUT)

utime.sleep(2)

#defining different functions for the 8 digit display
def turn_off_all():
    A_led.value(0)
    B_led.value(0)
    C_led.value(0)
    D_led.value(0)
    E_led.value(0)
    F_led.value(0)
    G_led.value(0)
    H_led.value(0)

def zero():
    A_led.value(1)
    F_led.value(1)
    G_led.value(1)
    H_led.value(1)
    D_led.value(1)
    C_led.value(1)
    
def one():
    A_led.value(1)
    F_led.value(1)
    
def two():
    C_led.value(1)
    A_led.value(1)
    B_led.value(1)
    H_led.value(1)
    G_led.value(1)
    
def three():
    C_led.value(1)
    A_led.value(1)
    B_led.value(1)
    G_led.value(1)
    F_led.value(1)

def four():
    D_led.value(1)
    B_led.value(1)
    A_led.value(1)
    F_led.value(1)
    
def five():
    C_led.value(1)
    D_led.value(1)
    B_led.value(1)
    F_led.value(1)
    G_led.value(1)

def six():
    C_led.value(1)
    D_led.value(1)
    H_led.value(1)
    G_led.value(1)
    F_led.value(1)
    B_led.value(1)
    
def seven():
    C_led.value(1)
    A_led.value(1)
    F_led.value(1)
    
def height():
    A_led.value(1)
    B_led.value(1)
    C_led.value(1)
    D_led.value(1)
    F_led.value(1)
    G_led.value(1)
    H_led.value(1)
    
def nine():
    A_led.value(1)
    B_led.value(1)
    C_led.value(1)
    D_led.value(1)
    F_led.value(1)
    G_led.value(1)
    

#defining starting value for buttons
delay = 0.1
button_value = 0
numbers_select = 0

#defining different information which are null at starting (I need to add a function of storage)
out0 = 0
out1 = 0
out2 = 0
out3 = 0
out4 = 0
out5 = 0
out6 = 0
out7 = 0
out8 = 0
out9 = 0

turn_off_all()
zero()

#starting the main loop
while True:
    
    #this loop is for receiving ir for each value of 8 digit display
    if button_value == 0 and button_receive.value() == 1:
            button_value = 1
            led_onboard.value(1)
            
    if button_value == 1:
        
        if numbers_select == 0:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out0 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
        
        if numbers_select == 1:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out1 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
        
        if numbers_select == 2:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out2 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
        
        if numbers_select == 3:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out3 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
        
        if numbers_select == 4:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out4 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
        
        if numbers_select == 5:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out5 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
        
        if numbers_select == 6:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out6 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
        
        if numbers_select == 7:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out7 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
        
        if numbers_select == 8:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out8 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
        
        if numbers_select == 9:
            #here I need to add a function that continue (exception) the code because if the signal received is bad, i need to restart the pico
            out9 = read_code(pin_in)
            button_value = 0
            led_onboard.value(0)
            
            
    #emitting IR and blinking onboard led for each display value
    if button_emit.value() == 1:
        
        if numbers_select == 0:
            try:
                send_code(pin_out, out0)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
        if numbers_select == 1:
            try:
                send_code(pin_out, out1)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
        if numbers_select == 2:
            try:
                send_code(pin_out, out2)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
        if numbers_select == 3:
            try:
                send_code(pin_out, out3)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
        if numbers_select == 4:
            try:
                send_code(pin_out, out4)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
        if numbers_select == 5:
            try:
                send_code(pin_out, out5)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
        if numbers_select == 6:
            try:
                send_code(pin_out, out6)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
        if numbers_select == 7:
            try:
                send_code(pin_out, out7)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
        if numbers_select == 8:
            try:
                send_code(pin_out, out8)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
        if numbers_select == 9:
            try:
                send_code(pin_out, out9)
                for i in range(0, 10):
                    utime.sleep(0.1)
                    led_onboard.value(1)
                    utime.sleep(0.1)
                    led_onboard.value(0)
            except InvalidCodeException:
                print("InvalidCodeException:" + out)
        
    #loop for choosing numbers
    if button_select.value() == 1:

        if numbers_select == 0 or numbers_select == 10 and button_select.value() == 1:
            turn_off_all()
            zero()
            numbers_select = 0
            numbers_select += 1
            utime.sleep(0.5)
            
        if numbers_select == 1 and button_select.value() == 1: 
            turn_off_all()
            one()
            numbers_select += 1
            utime.sleep(0.2)
            
        if numbers_select == 2 and button_select.value() == 1:
            turn_off_all()
            two()
            numbers_select += 1
            utime.sleep(0.2)
            
        if numbers_select == 3 and button_select.value() == 1:
            turn_off_all()
            three()
            numbers_select += 1
            utime.sleep(0.2)
            
        if numbers_select == 4 and button_select.value() == 1:
            turn_off_all()
            four()
            numbers_select += 1
            utime.sleep(0.2)
        
        if numbers_select == 5 and button_select.value() == 1:
            turn_off_all()
            five()
            numbers_select += 1
            utime.sleep(0.2)
            
        if numbers_select == 6 and button_select.value() == 1: 
            turn_off_all()
            six()
            numbers_select += 1
            utime.sleep(0.2)
            
        if numbers_select == 7 and button_select.value() == 1:
            turn_off_all()
            seven()
            numbers_select += 1
            utime.sleep(0.2)
            
        if numbers_select == 8 and button_select.value() == 1:
            turn_off_all()
            height()
            numbers_select += 1
            utime.sleep(0.2)
            
        if numbers_select == 9 and button_select.value() == 1:
            turn_off_all()
            nine()
            numbers_select += 1
            utime.sleep(0.2)
            continue 
            
        
        
        