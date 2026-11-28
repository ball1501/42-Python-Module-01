class Plant:
    class Stats:
        def __init__(self) -> None:
            self._stats_age = 0
            self._stats_grow = 0
            self._stats_show = 0

        def display(self) -> None:
            print(
                f"Stats: {self._stats_grow} grow, "
                f"{self._stats_age} age, "
                f"{self._stats_show} show"
                )

        def add_age(self) -> None:
            self._stats_age += 1

        def add_grow(self) -> None:
            self._stats_grow += 1

        def add_show(self) -> None:
            self._stats_show += 1

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.grow_up = 0.8
        self._stats = Plant.Stats()
        if height >= 0:
            self._height = height
        else:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0
        if days >= 0:
            self._days = days
        else:
            print(f"{self.name}: Error, age can't be negative")
            self._days = 0

    def age(self) -> None:
        self._days += 1
        self._stats.add_age()

    def grow(self) -> None:
        self._height += self.grow_up
        self._stats.add_grow()

    def get_stats_age(self) -> int:
        return self._stats._stats_age

    def get_stats_grow(self) -> int:
        return self._stats._stats_grow

    def get_stats_show(self) -> int:
        return self._stats._stats_show

    def show_stats(self) -> None:
        self._stats.display()

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_days: int) -> None:
        if new_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_days
            print(f"Age updated: {new_days} days")

    def get_age(self) -> int:
        return self._days

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self._height:.1f}cm, "
              f"{self._days} days old"
              )
        self._stats.add_show()

    @staticmethod
    def is_more_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            color: str
            ) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.is_bloom = False

    def bloom(self) -> None:
        self.is_bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloom:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._stats_shade = 0

        def display(self) -> None:
            super().display()
            print(f" {self._stats_shade} shade")

        def add_shade(self) -> None:
            self._stats_shade += 1

    _stats: "Tree.Stats"

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree.Stats()

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces "
            f"a shade of {self._height:.1f}cm long "
            f"and {self.trunk_diameter:.1f}cm wide."
            )
        self._stats.add_shade()

    def get_stats_shade(self) -> int:
        return self._stats._stats_shade

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            harvest_season: str
            ) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0
        self.grow_up = 2.1

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {round(self.nutritional_value)}")


class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            color: str
            ) -> None:
        super().__init__(name, height, days, color)
        self.seeds = 0
        self.grow_up = 1.5

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42


def print_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


if __name__ == "__main__":
    flower1 = Flower("Rose", 15, 10, "red")
    flower2 = Seed("Sunflower", 80, 45, "yellow")
    tree1 = Tree("Oak", 200, 365, 5)
    vegetable1 = Vegetable("Tomato", 5, 10, "april")
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_more_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_more_year(400)}")
    print()
    print("=== Flower")
    flower1.show()
    print_statistics(flower1)
    print("[asking the rose to grow and bloom]")
    flower1.grow()
    flower1.bloom()
    flower1.show()
    print_statistics(flower1)
    print()
    print("=== Tree")
    tree1.show()
    print_statistics(tree1)
    print(f"[asking the {tree1.name} to produce shade]")
    tree1.produce_shade()
    print_statistics(tree1)
    print()
    print("=== Seed")
    flower2.show()
    print(f"[make {flower2.name} grow, age and bloom]")
    for _ in range(1, 21):
        flower2.age()
        flower2.grow()
    flower2.bloom()
    flower2.show()
    print_statistics(flower2)
    print()
    print("=== Anonymous")
    anno = Plant.anonymous()
    anno.show()
    print_statistics(anno)
