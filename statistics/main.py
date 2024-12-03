def mean(numbers:list) -> float:
    return sum(numbers) / len(numbers)

def median(numbers: list) -> float:
    n = len(numbers)
    sorted_numbers = sorted(numbers)

    if n % 2 == 0:
        return (sorted_numbers[n//2] + sorted_numbers[n//2 - 1])/2
    else:
        return sorted_numbers[n//2]

def variance(numbers: list) -> float:
    average = mean(numbers)
    #TODO implement
    return average



size = int(input("Type the amount of numbers you intent to insert: "))

numberList = []
for i in range(size):
    numberList.append(int(input("Input the number: ")))

print("Mean:", mean(numberList))
print("Median:", median(numberList))
print("Maximum:", max(numberList))
print("Minimum:", min(numberList))
print("Variance:", variance(numberList))



