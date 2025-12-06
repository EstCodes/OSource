def RomanToInteger():
    roman = {
        'I': 1, 
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    value: str = input("Enter Roman Number: ").upper().strip()

    list_values = []
    for ch in value:
        if ch not in roman:
            raise ValueError(f"Invalid Roman numeral character: {ch}")
        list_values.append(roman[ch])

    print("Numeric values:", list_values)

    total = 0
    for i in range(len(list_values)):
        current = list_values[i]
        if i < len(list_values) - 1 and current < list_values[i + 1]:
            total -= current
        else:
            total += current

    print("Integer value:", total)
    return total


RomanToInteger()
