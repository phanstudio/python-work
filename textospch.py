if True:
    from gtts import gTTS
    import os
    import time
    #import playsound

    start_time = time.time()
    with open("mypickupartistsystem\chapters", "r") as f:
        txt = f.read()
    #txt = "I love puppies, dogs and i hate cats a lot, please end my suffering...!"

    """output = gTTS(txt, lang="en", slow=False, tld= "co.uk")
    output.save("audio.mp3")"""
    """output = gTTS(txt, lang="en-au", slow=False, tld= "co.uk")
    output.save("audio1.mp3")
    output = gTTS(txt, lang="en-za", slow=False, tld= "ca")
    output.save("audio2.mp3")"""

    output = gTTS(txt, lang="en-za", slow=False, tld= "ca")
    output.save("mypickupartistsystem\chapter1.mp3")
    final_time = time.time()
    timer = final_time - start_time
    timer = round(timer, 8)
    print(timer, "sec")

    if False:
        output = gTTS(txt, lang="en-us", slow=False)
        output.save("audio3.mp3")
        os.system("audio.mp3")
