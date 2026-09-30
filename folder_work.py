def extract_and_count(input_filename, output_filename):
    total_lines = 0
    first_two_lines = []

    try:
        with open(input_filename, 'r') as infile:
            for line in infile:
                total_lines += 1
                if total_lines <= 2:
                    first_two_lines.append(line)

        with open(output_filename, 'w') as outfile:
            outfile.writelines(first_two_lines)

        print(f"Total lines in '{input_filename}': {total_lines}")
        print(f"Extracted {len(first_two_lines)} line(s) to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_file = "input.txt"   
    output_file = "output.txt" 
    
    extract_and_count(input_file, output_file)