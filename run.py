class Run:
  def __init__(self, tokens):
    self.value = None
    self.token_type = 0
    self.token_value = ""

    for token in tokens:
      if type(token) is list:
        self.token_value = Run(token).value
      i += 1