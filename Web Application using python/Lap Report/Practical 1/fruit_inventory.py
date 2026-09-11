# import csv


# def get_fruit_data():
#     fruits = []
#     n = int(input("Enter the number of fruits: "))
#     for i in range(n):
#         print(f'\n Enter details for fruit {i + 1}:')
#         name = input("Enter fruit name: ")
#         quantity = int(input("Enter quantity: "))
#         price = float(input("Enter price: "))
#         fruits.append((name, quantity, price))
#     return fruits



# def save_to_csv(fruits, filename='fruit_inventory.csv'):
#     header = ['Name', 'Quantity', 'Price']
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(header)
#         writer.writerows(fruits)
#         print(f"\nFruit inventory saved to {filename}.")

# if __name__ == "__main__":
#     fruits = get_fruit_data()
#     save_to_csv(fruits)


import csv

def get_fruit_data():
    fruits = []
    n = int(input("Enter the number of fruits: "))
    for i in range(n):
        print(f"\nEnter details for fruit {i + 1}:")
        name = input("Enter fruit name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        fruits.append((name, quantity, price))
    return fruits

def save_to_csv(fruits, filename='fruit_inventory.csv'):
    header = ['Name', 'Quantity', 'Price']
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(fruits)
        print(f"\nFruit inventory saved to {filename}.")

if __name__ == "__main__":
    fruits = get_fruit_data()
    save_to_csv(fruits)