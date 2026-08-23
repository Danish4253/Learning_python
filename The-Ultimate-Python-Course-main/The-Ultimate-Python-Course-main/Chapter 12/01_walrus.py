# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(
        f"List is too long ({n} elements, expected <= 3)"
    )  # Output: List is too long (5 elements, expected <= 3)

    # what it did is like
    a = 1
    if a == 1:
        print("hello")
# in this operator both thngs are at once eg

if a := 1:
    print("bye")
