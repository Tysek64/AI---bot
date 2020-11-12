def AI(putIn):
    while putIn != "exit":
        putIn = input()
        putIn = putIn.lower()
        if "you" in putIn:
            if "name" in putIn or "who" in putIn:
                print("My name is Computer.")
            elif "old" in putIn or "age" in putIn:
                print("I'm over 10 years old.")
            elif "what" in putIn and ("like" in putIn or "interest" in putIn):
                print("I like many things.")
            elif "like" in putIn or "interest" in putIn:
                print("Yes, I do.")
            elif "job" in putIn or "do you do" in putIn:
                print("I'm a computer, what did you expect?")
            elif "where" in putIn or "from" in putIn:
                print("I'm in front of you!")
            elif "know" in putIn:
                print("I heard something about it.")
            elif "music" in putIn:
                if "play" in putIn:
                    print("To play music, open a Media Player.")
                elif "make" in putIn or "compose" in putIn:
                    print("I'm not that talented.")
            elif "how" in putIn and "are" in putIn:
                print("Fine, thanks!")
            else:
                print("Who? Me?")
        elif "mean" in putIn:
            if "word" in putIn:
                print("I'm not good at finding words")
            elif "life" in putIn:
                print("Eating.")
        elif "." in putIn:
            print("That's great!")
        elif "left" in putIn:
            if "go" in putIn:
                print("Right is always right.")
            elif "is" in putIn:
                print("Yes, there is.")
            elif "are" in putIn:
                print("No, there aren't.")
        elif "hello" in putIn or "hi " in putIn:
            print("Hello to you!")
        elif "music" in putIn:
            if "play" in putIn:
                print("To play music, open a Media Player.")
            elif "make" in putIn or "compose" in putIn:
                print("I'm not that talented.")
        elif "earth" in putIn:
            if "flat" in putIn:
                print("Yes, I'm a flat-earther.")
            elif "planet" in putIn:
                print("Third.")
            elif "pollution" in putIn:
                print("It's concerning.")
        else:
            print("Indeed.")
