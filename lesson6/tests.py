from lesson6.tic_tac_toy import matrix_match


def test_matrix():
    matrix_tests = (
        (([1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]), True),
        (([0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]), True),
        (([0, 0, 0],
          [0, 0, 0],
          [2, 2, 2]), True),
        (([0, 1, 2],
          [0, 0, 1],
          [1, 1, 2]), False),
        (([1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]), True),
        (([0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]), True),
        (([0, 0, 2],
          [0, 0, 2],
          [0, 0, 2]), True),
        (([1, 1, 2],
          [0, 1, 2],
          [0, 0, 1]), True),
        (([0, 1, 2],
          [0, 2, 2],
          [2, 0, 1]), True)
    )

    for test in matrix_tests:
        assert matrix_match(test[0]) is test[1], test[0]


test_matrix()


# def test_step_availability():
#     step_tests = (
#         ([3, 2],
#          ([1, 1, 1],
#           [0, 0, 0],
#           [0, 0, 0]), True),
#         ([5, 1],
#          ([1, 1, 1],
#           [0, 0, 0],
#           [0, 0, 0]), False),
#         ([1, 4],
#          ([2, 1, 1],
#           [0, 1, 0],
#           [0, 0, 1]), False),
#         ([1, 1],
#          ([2, 1, 1],
#           [0, 1, 2],
#           [2, 0, 1]), False),
#         ([1, 2],
#          ([2, 1, 1],
#           [0, 1, 2],
#           [2, 0, 1]), True),
#         ([1, 2, 3],
#          ([2, 1, 1],
#           [0, 1, 2],
#           [2, 0, 1]), False),
#         (['a', 3],
#          ([2, 1, 1],
#           [0, 1, 2],
#           [2, 0, 1]), False),
#     )
#
#     for test in step_tests:
#         assert tic_tac_toy.step_available(test[0], test[1]) is test[2], test[0]
#
#
# test_step_availability()

