#========================================================================================#
# ______                 _____                                            __      _____  #                                                               
#|  ____|               / ____|                                           \ \    / /__ \ #            2022 Copyright (c) qweryy-dev                 
#| |__   __ _ ___ _   _| (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __   \ \  / /   ) |#            2022 Copyright (c) EasySpammerV2                   
#|  __| / _` / __| | | |\___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|   \ \/ /   / / #            2021 Copyright (c) EasySpammer          
#| |___| (_| \__ \ |_| |____) | |_) | (_| | | | | | | | | | | |  __/ |       \  /   / /_ #                      
#|______\__,_|___/\__, |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|        \/   |____|#                                                               
#                  __/ |      | |                                                        #                                                               
#                 |___/       |_|                                                        #                                                               
#========================================================================================#

print("==========================")
print("|EasySpammer V2 by qweryy|")
print("===========================")

import random
import pyautogui as pg
import time
#🔤USE FOR WORD
word=('PASTE/TYPE THE WORD HERE')
#🔗USE FOR LINKS
link=('PASTE/TYPE THE LINK HERE')

#⌚DELAY (by changing the number (default 8) the delay will change)
time.sleep(8)

#🔢WORD/LINK REPEATER
for i in range(100):
#📥INPUT
    pg.write(word)
    pg.press('enter')
    
    
