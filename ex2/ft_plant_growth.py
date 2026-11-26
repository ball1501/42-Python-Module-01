class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def age(self) -> None:
        self.days += 1

    def grow(self) -> None:
        self.height += 0.8

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    fday = plant1.height

    print("=== Garden Plant Growth ===")
    plant1.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant1.age()
        plant1.grow()
        plant1.show()
    print(f"Growth this week: {plant1.height - fday:.1f}cm")
