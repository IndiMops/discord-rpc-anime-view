from pypresence import Presence
from time import time

RPC = Presence("926825075242578000")#APPLICATION ID
"""
btns = [
    {
        "label": "Website",
        "url": "https://mops-storage.xyz"
    },
    {
        "label": "Code",
        "url": "https://github.com/INDMops/discord-rpc-anime-view"
    }
]
"""
ns=input("Введіть номер серії: ")
na=input("Введіть назву аніме, котре переглядаєте: ")
nt=int(input("Введіть тривалість серії(в секундах: 1 хв. = 60 сек.): "))

RPC.connect()
RPC.update(
    state="Серія: "+ns, #другий рядок
    details="Аніме: "+na, #перший рядок
    end=time()+nt, #time - бере поточний час і додає nt(тривалість серії в секундах, яку вводиться) 
    #buttons=btns, #вивід кнопок
    large_image="cover", #основне зображення
    small_image="play", #мале зображення, яке росташоване у правому нпижньому кутку основного зображення
    large_text="Серія: "+ns, #текст виводиться коли на основне зображення навести курсор
    small_text="Відворюється" #текст виводиться коли на додаткове зображення навести курсор
)

input("Нажми \"Enter\", щоб вийти.")
