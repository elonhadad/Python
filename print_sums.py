"""
Student: Elon Hadad
ID: 034672139
Assignment no. 2
Program: print_sums.py
"""


def print_sums_helper(result, parts, lst, n):
    """
    list with all possible sums
    """
    if n == 0:
        result.append(list(lst))
        return

    for i in range(len(parts)):

        if (n - int(parts[i])) >= 0:
            lst.append(parts[i])
            print_sums_helper(result, parts, lst, n - int(parts[i]))

            lst.pop(len(lst) - 1)


def print_sums(parts, n, writer):
    """
    prints to the file all the sums of number
    """
    result = []
    lst = []
    print_sums_helper(result, parts, lst, n)

    if len(result) == 0 and len(parts) != 0:
        if len(parts) == 1:
            writer.write(f"{str(n)} as sum of {parts[0]}:\n")
        else:
            writer.write(f"{str(n)} as sum of {parts[0]} and {parts[1]}:\n")

    elif len(result) < 2:
        writer.write(f"{n}\nError\n")

    elif len(result) >= 2:
        writer.write(f"{str(n)} as sum of ")
        for j in range(len(parts) - 2):
            writer.write(f"{parts[j]}, ")
        writer.write(f"{parts[-2]} ")
        writer.write(f"and {parts[-1]}:\n")

    for i in range(len(result)):
        lst = []
        for j in result[i]:
            lst.append(str(j))
        writer.write(f"{str(n)} = " + " + ".join(lst) + "\n")

    writer.write("\n")


def main():
    file = open("input_ex2.txt", "r")
    text = file.readlines()
    file.close()

    writer = open("output_ex2.txt", "w")

    flag = True

    for line in text:
        i = line.find(" ")
        n = line[:i]
        parts = line[i:].split()
        for num in parts:
            if num.isalpha():
                writer.write(line)
                writer.write("Error\n\n")
                flag = False
                break
            elif int(num) < 1:
                writer.write(line)
                writer.write("Error\n\n")
                flag = False
                break
            elif int(num) > int(n):
                writer.write(line)
                writer.write("Error\n\n")
                flag = False
                break
            elif line[i:].find(num) != line[i:].rfind(num):
                writer.write(line)
                writer.write("Error\n\n")
                flag = False
                break
            else:
                num = int(num)

        if flag is True:
            print_sums(parts, int(n), writer)

        flag = True
    writer.close()


if __name__ == "__main__":
    main()
