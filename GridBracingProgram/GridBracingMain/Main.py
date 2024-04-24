from grid_print import print_braced_grid
import grid_rigidity as gr

def main():
    rows: int = int(input("Enter the number of rows of your grid: "))
    columns: int = int(input("Enter the number of columns of your grid: "))
    while rows < 1 or columns < 1:
       print("Rows and Columns must be greater than 0")
       rows: int = int(input("Enter the number of rows of your grid: "))
       columns: int = int(input("Enter the number of columns of your grid: "))

    count: int = 1
    list_braces = [[False for i in range(columns)]for j in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if count < 10:
                print(count, "", sep="   ", end="")
            else:
                print(count, "", sep="  ", end="")
            count += 1
        print()
    count -= 1
    user_condition: bool = True
    while user_condition:
        try:
            brace_location: int = int(input("Which squares are braced "
                                            "(Click any non-integer key to end): ")) - 1
            if brace_location < 0 or brace_location > count - 1:
                if count < 2:
                    print("Please enter 1 if it's braced")
                else:
                    print(f'Please enter a number between 1 and {count}')
                continue

            row_braced: int = brace_location // columns
            row_column: int = brace_location % columns
            list_braces[row_braced][row_column] = True
        except ValueError:
            user_condition = False
    for iter_row in list_braces:
        for iter_column in iter_row:
            print(iter_column, "", end="")
        print()

    print_braced_grid(list_braces)

    print(gr.grid_rigidity(list_braces))


main()
