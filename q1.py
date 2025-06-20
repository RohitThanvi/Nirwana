# Q1.py

def compute_squares(nums: list[int]) -> list[int]:
    squares = []
    for n in nums:
        squares.append(n * n)
    return squares

if __name__ == "__main__":
    print(compute_squares([1, 2, 3, 4, 5]))
    print(compute_squares([6, 7, 8]))
