def BeautifulPermutations():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Must enter a valid integer.")

    even_list = [i for i in range(1, num + 1) if i % 2 == 0]
    odd_list = [i for i in range(1, num + 1) if i % 2 == 1]

    combined = even_list + odd_list

    for current_i, next_i in zip(combined, combined[1:]):

        if abs(next_i - current_i) != 1:
            continue
        else:
            print("Invalid permutation: consecutive elements must not differ by 1.")
            break
    else:
        print("Valid permutation: all consecutive elements differ by at least 2.")
        print(combined)


if __name__ == "__main__":
    BeautifulPermutations()