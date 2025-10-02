expenses = [12.5, 9.3, 22.0, 5.5]
budget = 60

def calc_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

def show_expenses(expenses):
    return expenses  # Just return the list instead of printing

def calc_budget(total, budget):
    if total > budget:
        return ("Over budget by", total - budget)
    else:
        return ("Within budget by", budget - total)

def main():
    total = calc_total(expenses)
    print("Total spent:", total)
    
    print("Expenses:", show_expenses(expenses))
    status, amount = calc_budget(total, budget)
    print(f"{status}, {amount:.2f}")

if __name__ == "__main__":
    main()

