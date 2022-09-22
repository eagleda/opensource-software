def read_data(filename):
    file = open(filename,'r')
    data=[]
    for line in file.readlines():
        if line[0] == '#':
            continue
        data.append([int(text) for text in line.split(', ')])
    return data
    # TODO

def add_weighted_average(data, weight):
    for row in data:
        row.append(row[0]*weight[0]+row[1]*weight[1])   # TODO

def analyze_data(data):
    mean = sum(data)/len(data)# TODO
    sum2 = sum([datum**2 for datum in data])
    var =  sum2 / len(data) - mean**2
    n= int(len(data)/2)+1
    median = data[n]   # TODO
    return mean, var, median, min(data), max(data)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        add_weighted_average(data, [40/125, 60/100])
        if len(data[0]) == 3:      # Check 'data' is valid
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')