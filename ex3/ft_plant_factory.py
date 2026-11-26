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
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    for p in plants:
        print("Created: ", end="")
        p.show()
