def main(): 
    """Main driver function to run both the recursive and iterative algorithm solutions to the Tower of Hanoi problem. 
    """
    import os 
    import sys 
    from src import tower_of_hanoi, log_error

    current_file_path = os.path.dirname(os.path.abspath(__file__))  # Find the path to this file.
    os.chdir(current_file_path)  # cd to the directory containing this file.

    input_file = os.path.join(current_file_path, "input_output", "input.txt")
    output_file = os.path.join(current_file_path, "input_output", "output.txt")

    with open(input_file, 'r') as f:  # Open input text file containing input cases.
        with open(output_file, 'w') as o: 
            sys.stdout = o  # Write standard output to output text file. 

            for n in f:
                input_string = n.strip().replace(" ", "")  # Remove all spaces from input.

                if len(input_string) == 0:  # Skip empty lines in the file.
                    continue

                try:
                    tower_of_hanoi(n)
                except Exception as e: 
                    log_error(n, e)


if __name__=="__main__":
    main()
    