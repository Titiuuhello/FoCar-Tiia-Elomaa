# Tiia Elomaa
# 08.10.2026
# FoCar 

from machine import Pin, PWM
from time import sleep
led = Pin("LED", Pin.OUT)

# Motor A / Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B / Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Set PWM frequency to 1000 Hz / Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)


# Määritetään FoCar:lle funktiot

def led_paalle(aika):
    # Ledi päälle
    led.on()
    sleep(aika)
    led.off()

def eteenpain(nopeus, aika):
    # Aja eteenpäin
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def vasen(nopeus, aika):
    # Käänny vasemmalle, tätä voidaan käyttää myös 180° käännöksessä
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def kaarra_vasemmalle(nopeus, aika, teho_ero):
    # Kaarretaan vasemmalle
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus - teho_ero)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def peruuta_vasemmalle(nopeus, aika, teho_ero):
    # Peruutetaan vasemmalle
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus - teho_ero)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def oikea(nopeus, aika):
    # Käänny oikealle, tätä voidaan käyttää myös 180° käännöksessä
    m1.value(0)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def kaarra_oikealle(nopeus, aika, teho_ero):
    # Kaarretaan oikealle
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus - teho_ero)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def peruuta_oikealle(nopeus, aika, teho_ero):
    # Peruutetaan oikealle
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus - teho_ero)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)

def taaksepain(nopeus, aika):
    # Aja taaksepäin
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)
    e1.duty_u16(0)
    e2.duty_u16(0)