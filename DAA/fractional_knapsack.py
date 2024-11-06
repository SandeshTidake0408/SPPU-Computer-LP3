class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractional_knapsack(capacity, value):
    items.sort(key=lambda x: x.value/x.weight, reverse=True)
    total_value = 0.0
    current_weight = 0

    for item in items:
        if current_weight + item.weight <= capacity:
            total_value += item.value
            current_weight += item.weight
        else:
            remaining_capacity = capacity - current_weight
            fraction = remaining_capacity / item.weight
            total_value += item.value * fraction
            break
    return total_value


if __name__ == "__main__":

    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    capacity = 50

    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value we can obtain = {max_value}")
