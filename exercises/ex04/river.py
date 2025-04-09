"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    
    day: int  # tells day of river lifecycle you are modeling
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        surviving_bears: list[Bear] = self.bears
        surviving_fish: list[Fish] = self.fish
        for fish in self.fish:
            if fish.age <= 3:  # need help on this section/syntax for referencing age for other classes
                surviving_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        self.fish = surviving_fish
        return None
    
    def remove_fish(self, amount: int) -> None:
        index = 0
        while index < amount:
            self.fish.pop(index)
            index += 1
    
    def bears_eating(self):
        for each_bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                each_bear.eat(3) 
        return None
    
    def check_hunger(self):
        fat_bears: list[Bear] = self.bears
        for each_bear in fat_bears:
            if each_bear.hunger_score >= 0:  # syntax for accessing the hunger_score?
                fat_bears.append(each_bear)
        self.bears = fat_bears
        return None
        
    def repopulate_fish(self):
        n = (len(self.fish) // 2) * 4
        while n > 0:
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        n = len(self.bears) // 2
        while n > 0:
            self.bears.append(Bear())
            n -= 1
        return None
    
    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        return None
            
