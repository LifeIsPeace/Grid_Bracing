def print_braced_grid(braced_squares: list[list[bool]]) -> None:
    def print_topbottom_lines() -> None:
        print(" __  __  __ " * len(braced_squares[0]))

    def print_following_rows(current_row: int) -> None:
        print_topbottom_lines()
        for i in braced_squares[current_row]:
            if i:
                print("|", " \\", " " * 8, "|", sep="", end="")
            else:
                print("|", " " * 10, "|", sep="", end="")
        print("", sep="")
        for i in braced_squares[current_row]:
            if i:
                print("|", " " * 4, "\\", " " * 5, "|", sep="", end="")
            else:
                print("|", " " * 10, "|", sep="", end="")
        print("", sep="")
        for i in braced_squares[current_row]:
            if i:
                print("|", " " * 8, "\\", " ", "|", sep="", end="")
            else:
                print("|", " " * 10, "|", sep="", end="")
        print()
        print_topbottom_lines()

    for i in range(len(braced_squares)):
        print_following_rows(i)
