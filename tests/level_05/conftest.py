import pytest
from dungeon.hero import Hero
from dungeon.inventory import Inventory
from dungeon.inventory import Item
from dungeon.shop import Listing, Shop

@pytest.fixture
def hero():
    hero = Hero("Alex")
    return hero

@pytest.fixture
def backpack():
    backpack = Inventory(20)
    return backpack 

@pytest.fixture
def rich_hero(hero):
    hero.gold = 100
    return hero

@pytest.fixture
def shop():
    potion = Item("potion", 0.1 , 5) 
    listing = Listing(potion, price=10, stock=3)
    return Shop([listing]) 

