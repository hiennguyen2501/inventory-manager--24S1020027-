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

def view_inventory():
    """Hiển thị toàn bộ sản phẩm trong kho"""
    print("\n--- DANH SÁCH TỒN KHO ---")

    if len(products) == 0:
        print("Kho hiện đang trống.")
        return

    for p in products:
        print(f"{p['name']} - Giá: {p['price']} - SL: {p['qty']}")

def check_low_stock():
    """Cảnh báo sản phẩm có số lượng thấp (dưới 5)"""
    print("\n--- CẢNH BÁO HẾT HÀNG ---")

    low_items = [p for p in products if p['qty'] < 5]

    if len(low_items) == 0:
        print("Không có sản phẩm nào sắp hết hàng.")
        return

    print("Các sản phẩm có số lượng dưới 5:")
    for p in low_items:
        print(f"⚠ {p['name']} - SL: {p['qty']}")
