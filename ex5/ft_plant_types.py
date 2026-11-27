class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.grow_up = 0.8
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

    def grow(self) -> None:
        self._height += self.grow_up

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
        print(f"{self.name}: {self._height:.1f}cm, {self._days} days old")


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
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces "
            f"a shade of {self._height:.1f}cm long "
            f"and {self.trunk_diameter:.1f}cm wide."
            )

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


if __name__ == "__main__":
    flower1 = Flower("Rose", 15, 10, "red")
    tree1 = Tree("Oak", 200, 365, 5)
    vegetable1 = Vegetable("Tomato", 5, 10, "april")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower1.show()
    print("[asking the rose to bloom]")
    flower1.bloom()
    flower1.show()
    print()
    print("=== Tree")
    tree1.show()
    print("[asking the oak to produce shade]")
    tree1.produce_shade()
    print()
    print("=== Vegetable")
    vegetable1.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(1, 21):
        vegetable1.grow()
        vegetable1.age()
    vegetable1.show()
