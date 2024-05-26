class MyString:
  def __init__(self, value=None):
    self.value = value
    if not isinstance(self.value, str):
      print("The value must be a string.")
    
  def is_sentence(self):
    sentence = self.value
    if sentence.endswith("."):
      return True
    else:
      return False

  def is_question(self):
    question = self.value
    if question.endswith("?"):
      return True
    else:
      return False

  def is_exclamation(self):
    exclamation = self.value
    if exclamation.endswith("!"):
      return True
    else:
      return False
  
  def count_sentences(self):
    sentence = self.value

    if sentence is None:
        return 0

    count = 0
    for character in sentence:
        if character in (".", "?", "!"):
            count += 1

    return count
