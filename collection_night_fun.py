pass_mark = 50
sixty_mark = 60
price_limit = 100
salary_limit = 55000
it_department = "IT"


def print_students_and_scores(students):
    for name, score in students:
        print(f"{name}: {score}")


def print_names_scored_sixty_or_above(students):
    for name, score in students:
        if score >= sixty_mark:
            print(name)


def count_passed_students(students):
    passed_count = 0
    for _, score in students:
        if score >= pass_mark:
            passed_count += 1
    return passed_count


def costs_more_than_hundred(product):
    _, price = product
    return price > price_limit


def get_price(product):
    _, price = product
    return price


def get_expensive_products(products):
    return list(filter(costs_more_than_hundred, products))


def sum_of_prices(products):
    return sum(map(get_price, products))


def print_products(products):
    for name, price in products:
        print(f"Product: {name} - Price: {price}")


def has_both_values_positive(point):
    x_value, y_value = point
    return x_value > 0 and y_value > 0


def get_positive_points(points):
    return list(filter(has_both_values_positive, points))


def print_employee_details(employees):
    for name, department, salary in employees:
        print(f"Name: {name}, Department: {department}, Salary: {salary}")


def is_in_it_department(employee):
    _, department, _ = employee
    return department == it_department


def earns_more_than_limit(employee):
    _, _, salary = employee
    return salary > salary_limit


def get_it_employees(employees):
    return list(filter(is_in_it_department, employees))


def get_high_earning_it_employees(employees):
    it_employees = get_it_employees(employees)
    return list(filter(earns_more_than_limit, it_employees))


def print_names_of_high_earning_it_employees(employees):
    for name, _, _ in get_high_earning_it_employees(employees):
        print(name)


if __name__ == "__main__":
    students = [
        ("Alice", 78),
        ("Bob", 45),
        ("Charlie", 90),
        ("Diana", 62),
        ("Kent", 30)
    ]

    products = [
        ("Laptop", 1200),
        ("Mouse", 25),
        ("Keyboard", 45),
        ("Monitor", 300),
        ("USB Cable", 10)
    ]

    points = [
        (2, 3),
        (-1, 4),
        (5, -6),
        (0, 7),
        (-3, -2)
    ]

    employees = [
        ("John", "IT", 50000),
        ("Jane", "HR", 45000),
        ("Mike", "IT", 60000),
        ("Sara", "Finance", 70000)
    ]

    print("--- Students ---")
    print_students_and_scores(students)
    print("Scored 60 or above:")
    print_names_scored_sixty_or_above(students)
    print("Number passed:", count_passed_students(students))

    print("\n--- Products ---")
    print("More than 100:", get_expensive_products(products))
    print("Sum of prices:", sum_of_prices(products))
    print_products(products)

    print("\n--- Points ---")
    print("Both positive:", get_positive_points(points))

    print("\n--- Employees ---")
    print_employee_details(employees)
    print("IT employees earning more than 55,000:")
    print_names_of_high_earning_it_employees(employees)
