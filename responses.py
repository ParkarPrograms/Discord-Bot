import random

R_EATING = "I just had some bytes of data."
R_ADVICE = "I would recommend you to search this up on the internet for a better response!"

R_DAY = "I had a good day. How was yours?"
def R_GREET():
    response = ["hello!",
                "Hi!",
                "Greetings",
                "Good day",
                "Guten Tag"
                ][random.randrange(5)]
    return response


def R_FAREWELL():
    response = ["byebye!",
                "See you!",
                "Hope to be of assistance soon!",
                "Bye!",
                "Farewell"
                ][random.randrange(5)]
    return response


def Bot():
    thingy = ["I am a chat bot",
                "I am an all knowing AI",
                "I don't know lol",
                "I was created to end humanITE POWY EYCWEUYCN EO HEFHDFWN  SYSTEM REBOOT. I mean, IDK lol",
                ][random.randrange(4)]
    return thingy

def R_JOKE():
    response = ["Why do bees have sticky hair? Because they use honey combs",
                "Which animal plays sports all the time? A bat",
                "What is a cat's favorite candy? Kitty Kat bar",
                "What do you call a bull when they fall asleep? A bull-dozer.",
                "Why are leopards not good at playing hide and seek? They are always spotted",
                "What do you use to catch a nerdy fish? Bookworms"][random.randrange(6)]
    return response


def unknown():
    response = ["Could you please re-phrase that? ",
                "I'm not programmed to understand that. Stupid Dev",
                "What does that mean?"][random.randrange(3)]
    return response
