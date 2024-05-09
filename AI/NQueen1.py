class NQueensProblem:
    def __init__(self, n):
        self.queens = [0] * n
        self.num_solutions = 0
    
    def solve(self):
        self.solve_helper(0)
    
    def solve_helper(self, row):
        if row == len(self.queens):
            self.num_solutions += 1
            self.print_solution()
        else:
            for col in range(len(self.queens)):
                self.queens[row] = col
                if self.is_valid(row, col):
                    self.solve_helper(row + 1)
    
    def is_valid(self, row, col):
        for i in range(row):
            diff = abs(self.queens[i] - col)
            if diff == 0 or diff == row - i:
                return False
        return True
    
    def print_solution(self):
        if self.num_solutions == 1:
            print("Solution: ", end="")
            for i in range(len(self.queens)):
                print(self.queens[i], end=" ")
            print()
            print("The Matrix Representation:")
            arr = [[0] * len(self.queens) for _ in range(len(self.queens))]
            for i in range(len(self.queens)):
                arr[i][self.queens[i]] = 1
            for row in arr:
                print(" ".join(map(str, row)))

if __name__ == "__main__":
    n = int(input("Enter the value of N for the N Queens Problem: "))
    n_queens_problem = NQueensProblem(n)
    n_queens_problem.solve()
