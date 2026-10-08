from focar import eteenpain, taaksepain, oikea, vasen, kaarra_oikealle, kaarra_vasemmalle, peruuta_oikealle, peruuta_vasemmalle
from focar import led_paalle

led_paalle(2)
eteenpain(40000, 2.5)
kaarra_oikealle(45000, 2.7, 35000)
peruuta_oikealle(57000, 2.7, 32000)
kaarra_oikealle(45000, 0.3, 35000)
eteenpain(40000, 3)
led_paalle(2)