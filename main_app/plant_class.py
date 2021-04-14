class Plant:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, kind, description):
    self.name = name
    self.kind = kind
    self.description = description


plants = [
  Plant('Lolo', 'tabby', 'foul little demon'),

]