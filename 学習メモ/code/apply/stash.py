import sys


def main(lines):
    step_number = int(lines[0])
    if step_number != 1:
        return

    menu_count = int(lines[1])
    menus = {}
    for i in range(menu_count):
        menu_index, stock, price = map(int, lines[2 + i].split())
        menus[menu_index] = {"stock": stock, "price": price}

    event_start = 2 + menu_count
    for line in lines[event_start:]:
        if not line.startswith("order "):
            continue

        parts = line.split()
        table_number = int(parts[1])
        order_menu_number = int(parts[2])
        order_count = int(parts[3])
        menu = menus.get(order_menu_number)

        # 注文数ぶん在庫がある場合のみ受理（部分受理はしない）
        if menu and menu["stock"] >= order_count:
            menu["stock"] -= order_count
            for _ in range(order_count):
                print(f"received order {table_number} {order_menu_number}")
        else:
            print(f"sold out {table_number}")


if __name__ == "__main__":
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip("\r\n"))
    main(lines)
