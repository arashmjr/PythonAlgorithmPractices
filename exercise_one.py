def grid_search(grid_list, pattern_list):
    grid_len = len(grid_list)
    first_item_gr_len = len(grid_list[0])
    pattern_len = len(pattern_list)
    first_item_pr_len = len(pattern_list[0])
    for i in range(grid_len - pattern_len + 1):
        for j in range(first_item_gr_len - first_item_pr_len + 1):
            for k in range(pattern_len):
                if grid_list[i + k][j:j + first_item_pr_len] != pattern_list[k]:
                    break
            else:
                return 'YES'
    return 'NO'


num_testcase = int(input('Enter number of testcases:').strip())

for t_itr in range(num_testcase):

    first_multiple_input = input('Enter row and column of grid matrix:').rstrip().split()
    grid_row = int(first_multiple_input[0])
    print('Row', grid_row)

    grid_length_row = int(first_multiple_input[1])
    print('Col', grid_length_row)

    grid = []

    for _ in range(grid_row):
        G_item = input('Enter item of grid matrix:')
        if len(G_item) != grid_length_row:
            raise Exception('digit of number you entered is not correct')
        print('G_item', G_item)
        grid.append(G_item)

    print(grid)

    second_multiple_input = input('Enter row and column of pattern matrix:').rstrip().split()

    pattern_row = int(second_multiple_input[0])

    pattern_length_row = int(second_multiple_input[1])

    pattern = []

    for _ in range(pattern_row):
        P_item = input('Enter item of pattern matrix:')
        if len(P_item) != pattern_length_row:
            raise Exception('digit of number you entered is not correct')
        pattern.append(P_item)

    print(pattern)
    result = grid_search(grid, pattern)
    print(result)
