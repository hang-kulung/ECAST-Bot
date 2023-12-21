import random

greetings = ['HEY THERE!!', 'Hello', 'WHASSSUPPPPP!!!!', 'HEY', 'HI', 'NAMASTE']


def handle_response(message) -> str:
    p_message = message.lower()

    if any(msg.lower() in p_message for msg in greetings):
        return random.choice(greetings)
    
    if "google" in p_message:
        search_words = p_message[p_message.index("google")+6:].split()
        link = 'https://www.google.com/search?q=' + '+'.join(search_words)
        return link
    
    if "roll" in p_message or "dice" in p_message:
        return str(random.randint(1, 6))

    if ('pick' in p_message or 'choose' in p_message) and 'number' in p_message:
        try:
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for i in p_message:
                if i in numbers:
                    a = p_message.index(i)
                    while True:
                        a += 1
                        if a >= len(p_message):
                            break
                        elif p_message[a] not in numbers:
                            break
                    first = p_message[p_message.index(i):a]
                    p_message = p_message[a:]
                    break
            for i in p_message:
                if i in numbers:
                    a = p_message.index(i)
                    while True:
                        a += 1
                        if a >= len(p_message):
                            break
                        elif p_message[a] not in numbers:
                            break
                    second = p_message[p_message.index(i):a]
                    break
            return random.randint(int(first), int(second))
        except Exception:
            return random.randint(1,100)

    if p_message == "-help":
        return "`This is a help message.`"
