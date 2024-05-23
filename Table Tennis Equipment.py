from abc import ABC, abstractmethod

class Equipment(ABC):
  def __init__(self, brand, name):
    self.__brand = brand  # Make brand private
    self.__name = name    # Make name private

  def get_brand(self):
    return self.__brand

  def get_name(self):
    return self.__name

  @abstractmethod
  def describe(self):
    pass

class TableTennisItem(Equipment):
  def describe(self):
    return f"{self.get_brand()} {self.get_name()}"

class Paddle(TableTennisItem):
  def __init__(self, brand, name, grip_style):
    super().__init__(brand, name)
    self.grip_style = grip_style

  def describe_grip(self):
    return f"This paddle is designed for a {self.grip_style} grip."

  def describe(self):
    return f"{super().describe()} Paddle - {self.describe_grip()}"

class Table(TableTennisItem):
  def __init__(self, brand, name, material):
    super().__init__(brand, name)
    self.material = material

  def describe_material(self):
    return f"This table is made of {self.material}."

  def describe(self):
    return f"{super().describe()} Table - {self.describe_material()}"

# Creating objects
butterfly_ball = TableTennisItem("Butterfly", "Nittaku Ball")
yasaka_paddle = Paddle("Yasaka", "Ma Lin Pro", "Shakehand")
cornilleau_table = Table("Cornilleau", "Sport 1000 Outdoor", "Melamine")

# Accessing object attributes and methods
print("Butterfly Nittaku Ball:", butterfly_ball.describe())

print("Yasaka Ma Lin Pro Paddle:", yasaka_paddle.describe())

print("Cornilleau Sport 1000 Outdoor Table:", cornilleau_table.describe())

