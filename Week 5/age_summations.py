def total_age(age1, age2):
    #result = age1 + age2
    #return result
    #return age1 + age2
    sum_ages = age1 + age2
    diff_ages = age1 - age2
    return sum_ages, diff_ages

def main():
    first_age = int(input("Enter first age: "))
    second_age = int(input("Enter second age: "))

    #sum_of_ages,diff_of_ages = total_age(first_age, second_age)
    sum_of_ages = total_age(first_age, second_age)
    print("The sum of the ages is: ", sum_of_ages)
    #print("The diff of the ages is: ", diff_of_ages)

main()
