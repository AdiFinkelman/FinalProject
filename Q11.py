from functools import reduce
 
cumulative_sum_of_squares_of_even = lambda lst: list(
    map(
        lambda sublist: reduce(
            lambda a, b: a + b,
            map(
                lambda x: x ** 2,
                filter(
                    lambda y: y % 2 == 0, sublist
                )
            ),
            0
        ),
        lst
    )
)
 
input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = cumulative_sum_of_squares_of_even(input_list)
print(result)  # Output: [4, 52, 64]