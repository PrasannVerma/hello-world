class employee:
    #special method
    def __init__(self):
        self.id=123
        self.salary=500000
        self.designation="SE"

    def travel(self, destination):
        print(f"Travellling to {destination}")

sam=employee()

sam.travel("Kerala")
print(type(sam))