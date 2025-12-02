# ================================
# QUẢN LÝ KHO HÀNG - INVENTORY MANAGER
# Procedural Programming - Python
# ================================

# Danh sách sản phẩm (biến toàn cục)
products = []


def main():
    while True:
        print("\n--- QUẢN LÝ KHO HÀNG ---")
        print("1. Nhập hàng mới")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            print("Chức năng nhập hàng sẽ được thêm sau (Feature 1).")
        elif choice == '2':
            print("Chức năng xem tồn kho sẽ được thêm sau (Feature 2).")
        elif choice == '3':
            print("Chức năng cảnh báo hết hàng sẽ được thêm sau (Feature 3).")
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()

# inventory.py
# ================================
# QUẢN LÝ KHO HÀNG - INVENTORY MANAGER
# Procedural Programming - Python
# ================================

products = []


def add_product():
    """Nhập sản phẩm mới vào kho"""
    print("\n--- NHẬP HÀNG MỚI ---")
    name = input("Tên sản phẩm: ").strip()
    # Giá (số nguyên)
    while True:
        try:
            price = int(input("Giá bán: "))
            if price < 0:
                print("Giá phải >= 0, nhập lại!")
                continue
            break
        except ValueError:
            print("Giá phải là số nguyên, nhập lại!")

    # Số lượng (số nguyên)
    while True:
        try:
            qty = int(input("Số lượng tồn kho: "))
            if qty < 0:
                print("Số lượng phải >= 0, nhập lại!")
                continue
            break
        except ValueError:
            print("Số lượng phải là số nguyên, nhập lại!")

    product = {'name': name, 'price': price, 'qty': qty}
    products.append(product)
    print("✔ Đã nhập hàng thành công.")


def main():
    while True:
        print("\n--- QUẢN LÝ KHO HÀNG ---")
        print("1. Nhập hàng mới")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            print("Chức năng xem tồn kho sẽ được thêm sau (Feature 2).")
        elif choice == '3':
            print("Chức năng cảnh báo hết hàng sẽ được thêm sau (Feature 3).")
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()