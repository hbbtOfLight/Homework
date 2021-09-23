def generate_squares(n):
    return dict(zip(list(i for i in range(n + 1)), list(i**2 for i in range(n + 1))))


print(generate_squares(5))
