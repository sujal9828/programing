import time
import sys

def print_lyrics():
    lyrics = [
        "mein ab kyu hosh me aata nahi?",
        "sukoon yeh dil kyun pata nahi?",
        "kyun torrum khud se jo thay wassday",
        "ke ab ye ishq nibhaana nahi",
        "mein morrum tum se jo yeh chehra",
        "dobara nazar milna nhi",
        "yeh duniya jaanay mera dard",
        "tujhe yeh nazar kyun aata nhi"

    ]

    delays = [
        0.5, 0.5, 0.6, 0.5, 0.5, 0.5, 0.10
    ]

    print("pal pal : \n")
    time.sleep(1.20)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.04) 
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.04)

print_lyrics()