from pypresence import Presence
from time import time

RPC = Presence("<app id>")#APPLICATION ID

ns = input("Enter the episode number: ")
na = input("Enter an anime name that is viewed: ")
nt = int(input("Enter the duration of the series (in seconds: 1 min = 60 sec.): "))

RPC.connect()
RPC.update(
    details = "Name: " + na,
    state = "Episode: " + ns,
    end = time() + nt,
    large_image = "cover",
    small_image = "play",
    large_text = "Episode: " + ns,
    small_text = "Play"
)

input("Press Enter to exit.")
