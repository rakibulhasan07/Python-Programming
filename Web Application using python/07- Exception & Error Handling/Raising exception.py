def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("Age must be at least 18.")
    else:
        print("Age is valid.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as e:
    print(f"Input Error: {e}")
except Exception as e:
    print(f'alert message: {e}')
    