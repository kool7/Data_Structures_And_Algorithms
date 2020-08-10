
data = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]


def merge_range(time:list):
    '''
    Arguments
    time -- list of meeting time ranges
    '''
    output = []

    for item in sorted(data, key=lambda x: x[0]):
        if output and item[0] <= output[-1][1]:
            output[-1][1] = max(item[1], output[-1][1])
        else:
            output.append(item)

    return output

merge_range(data)