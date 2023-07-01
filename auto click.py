#需要下载pyautogui的第三方库

import pyautogui as pag
from time import *
from random import *

#sleep为启动延迟（秒）

sleep(0.5)

#button后可更改为left左键 或 right右键

#clicks后为点击次数，可更改为任何整数

#interval后为点击间隔（秒）

pag.click(button="left",clicks=10000,interval=1)
