class Plant:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, origin, description):
    self.name = name
    self.origin = origin
    self.description = description


plants = [
  Plant("Donkey's Tail", "South Mexico", "The Donkey's tail is a succulent plant species that stores water for long periods of time as a fail safe when in its natural habitat water becomes scarce."),
  Plant("Parlor Palm", "Mexico", "The parlor palm is the most popular of the indoor palm plants variety grown today indoors..."),
  Plant("Dumb Cane", "West Indies", "The Dumb Cane plant is a strong species that will thrive in any light conditions other than direct sunlight. Its easy to care for style and resilience to neglect make it a wonderful house plant..."),
  Plant("Swiss Cheese Plant", "South Mexico to Columbia", "The Swiss cheese plant displays the most interesting looking leaves and needs a grower to be prepared to provide some extra space within a home (it grows fairly tall when it matures.")
]