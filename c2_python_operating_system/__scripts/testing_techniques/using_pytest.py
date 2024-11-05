import pytest # external library for testing
from typing import List # for type hinting

class Fruit:
    def __init__(self, name: str):
        self.name = name
        self.cubed = False
    
    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, fruit_bowl: List[Fruit]):
        self.fruits = fruit_bowl
        self._cube_fruit()
     
    def _cube_fruit(self):
        for fruit in self.fruits:
            fruit.cube()


# Arrange (setup) and Act (execution) steps:
@pytest.fixture
def fruit_bowl(): # arrange
    return [Fruit('apple'), Fruit('banana')]

def test_fruit_salad(fruit_bowl):
    fruit_salad = FruitSalad(fruit_bowl) # act
    assert all(fruit.cubed for fruit in fruit_salad.fruits) # assert


# note: %%file -> cell magic command for saving the cell content to a file

# side-notes (for pytest):
# 1) a 'fixture' is a function that establishes a fixed baseline for tests
#    by initializing data & preparing the testing environment
# 2) any function name starting with 'test_' will be considered as a test function
