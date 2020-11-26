def AI(text):
  putIn = text.lower()
  if "you" in putIn:
    if "name" in putIn or "who" in putIn:
      return "My name is Computer."
    elif "old" in putIn or "age" in putIn:
      return "I'm over 10 years old."
    elif "what" in putIn and ("like" in putIn or "interest" in putIn):
      return "I like many things."
    elif "like" in putIn or "interest" in putIn:
      return "Yes, I do."
    elif "job" in putIn or "do you do" in putIn:
      return"I'm a computer, what did you expect?"
    elif "where" in putIn or "from" in putIn:
      return "I'm in front of you!"
    elif "know" in putIn:
      return "I heard something about it."
    elif "music" in putIn:
      if "play" in putIn:
        return "To play music, open a Media Player."
      elif "make" in putIn or "compose" in putIn:
        return "I'm not that talented."
    elif "how" in putIn and "are" in putIn:
      return "Fine, thanks!"
    else:
      return "Who? Me?"
  elif "mean" in putIn:
    if "word" in putIn:
      return "I'm not good at finding words"
    elif "life" in putIn:
      return "Eating."
  elif "." in putIn:
    return "That's great!"
  elif "left" in putIn:
    if "go" in putIn:
      return "Right is always right."
    elif "is" in putIn:
      return "Yes, there is."
    elif "are" in putIn:
      return "No, there aren't."
  elif "hello" in putIn or "hi " in putIn:
    return "Hello to you!"
  elif "music" in putIn:
    if "play" in putIn:
      return "To play music, open a Media Player."
    elif "make" in putIn or "compose" in putIn:
      return "I'm not that talented."
  elif "earth" in putIn:
    if "flat" in putIn:
      return "Yes, I'm a flat-earther."
    elif "planet" in putIn:
      return "Third."
    elif "pollution" in putIn:
      return "It's concerning."
  else:
    return "Indeed."
