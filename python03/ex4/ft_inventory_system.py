import sys


def inventory_system() -> None:
    inventory = {}
    arguments = sys.argv[1:]
    total_len = len(sys.argv)
    if (total_len == 1):
        print("Got inventory: {}")
        return

    for arg in arguments:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item_name, quantity_str = arg.split(':', 1)
        item_name = item_name.strip()
        quantity_str = quantity_str.strip()
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError as ex:
            print(f"Quantity error for '{item_name}': {ex}")
    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list} ")
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")
    for item, quant in inventory.items():
        percentage = quant/total_quantity * 100
        print(f"Item {item} represents {percentage:.1f}%")
    item_list = list(inventory.keys())
    most_abundant = item_list[0]
    least_abundant = item_list[0]
    for item in item_list:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item
    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {inventory[most_abundant]}"
        )
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {inventory[least_abundant]}"
        )
    inventory.update({'magic_item': 1})
    print(f"Updated inventory : {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory_system()
