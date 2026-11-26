class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
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
        self._height += 0.8

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


if __name__ == "__main__":
    plant1 = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    plant1.show()
    print()
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-25)
    plant1.set_age(-30)
    print()
    print("Current state: ", end="")
    plant1.show()
