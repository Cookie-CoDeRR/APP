def copy_first_two_lines(input_filename, output_filename):
    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()

    first_two_lines = lines[:2]

    print("Total number of lines:", len(lines))
    print("First two lines:")
    for line in first_two_lines:
        print(line, end="")

    with open(output_filename, "w") as output_file:
        output_file.writelines(first_two_lines)

    print("\nThe first two lines were written to", output_filename)


copy_first_two_lines("input.txt", "output.txt")