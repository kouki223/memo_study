import sys
from collections import deque, defaultdict


def load_menus(lines, start_index, menu_count):
    menus = {}
    for i in range(menu_count):
        menu_index, stock, price = map(int, lines[start_index + i].split())
        menus[menu_index] = {"stock": stock, "price": price}
    return menus


def step1(lines):
    menu_count = int(lines[1])
    menus = load_menus(lines, 2, menu_count)
    event_start = 2 + menu_count

    for line in lines[event_start:]:
        if not line.startswith("order "):
            continue
        parts = line.split()
        table_number = int(parts[1])
        order_menu_number = int(parts[2])
        order_count = int(parts[3])
        menu = menus.get(order_menu_number)

        if menu and menu["stock"] >= order_count:
            menu["stock"] -= order_count
            for _ in range(order_count):
                print(f"received order {table_number} {order_menu_number}")
        else:
            print(f"sold out {table_number}")


def step2(lines):
    menu_count, range_count = map(int, lines[1].split())
    event_start = 2 + menu_count

    queue = deque()
    ranges = [None] * range_count
    free_ranges = deque(range(range_count))
    menu_to_range = defaultdict(deque)

    def assign_from_queue(target_order=None):
        assigned_target = False
        while free_ranges and queue:
            range_index = free_ranges.popleft()
            order = queue.popleft()
            ranges[range_index] = order
            menu_to_range[order[1]].append(range_index)
            if order == target_order:
                assigned_target = True
        return assigned_target

    out = sys.stdout.write
    for line in lines[event_start:]:
        parts = line.split()

        if parts[0] == "received" and parts[1] == "order":
            table_number = int(parts[2])
            menu_number = int(parts[3])
            order = (table_number, menu_number)

            queue.append(order)
            if assign_from_queue(order):
                out(f"{menu_number}\n")
            else:
                out("wait\n")

        elif parts[0] == "complete":
            menu_number = int(parts[1])
            cooking_ranges = menu_to_range.get(menu_number)
            if not cooking_ranges:
                out("unexpected input\n")
                continue

            range_index = cooking_ranges.popleft()
            ranges[range_index] = None
            free_ranges.append(range_index)

            next_menu = None
            while free_ranges and queue:
                range_index = free_ranges.popleft()
                order = queue.popleft()
                ranges[range_index] = order
                menu_to_range[order[1]].append(range_index)
                if next_menu is None:
                    next_menu = order[1]

            if next_menu is not None:
                out(f"ok {next_menu}\n")
            else:
                out("ok\n")


def step3(lines):
    menu_count = int(lines[1])
    load_menus(lines, 2, menu_count)
    event_start = 2 + menu_count

    waiting_orders = defaultdict(deque)

    for line in lines[event_start:]:
        parts = line.split()

        if parts[0] == "received" and parts[1] == "order":
            table_number = int(parts[2])
            menu_number = int(parts[3])
            waiting_orders[menu_number].append((table_number, menu_number))

        elif parts[0] == "complete":
            menu_number = int(parts[1])
            if not waiting_orders[menu_number]:
                continue
            table_number, _ = waiting_orders[menu_number].popleft()
            print(f"ready {table_number} {menu_number}")


def step4(lines):
    menu_count = int(lines[1])
    menus = load_menus(lines, 2, menu_count)
    event_start = 2 + menu_count

    pending_by_table = defaultdict(int)
    unchecked_total_by_table = defaultdict(int)

    for line in lines[event_start:]:
        parts = line.split()

        if parts[0] == "received" and parts[1] == "order":
            table_number = int(parts[2])
            menu_number = int(parts[3])
            menu = menus.get(menu_number)

            if not menu or menu["stock"] <= 0:
                print(f"sold out {table_number}")
                continue

            menu["stock"] -= 1
            pending_by_table[table_number] += 1

        elif parts[0] == "ready":
            table_number = int(parts[1])
            menu_number = int(parts[2])
            menu = menus.get(menu_number)
            if menu is None:
                continue
            if pending_by_table[table_number] > 0:
                pending_by_table[table_number] -= 1
            unchecked_total_by_table[table_number] += menu["price"]

        elif parts[0] == "check":
            table_number = int(parts[1])
            if pending_by_table[table_number] > 0:
                print("please wait")
            else:
                print(unchecked_total_by_table[table_number])
                unchecked_total_by_table[table_number] = 0


def main(lines):
    step_number = int(lines[0])
    if step_number == 1:
        step1(lines)
    elif step_number == 2:
        step2(lines)
    elif step_number == 3:
        step3(lines)
    elif step_number == 4:
        step4(lines)


if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\r\n"))
    main(lines)
