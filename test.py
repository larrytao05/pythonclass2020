import csv

nums = []
with open('nbaNew.csv.txt') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    dic = {}
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            nums.append(int(row[1]))
            print(f'\t{row[2]} made {row[3]} dollars in {row[1]}, as a {row[4]}')
            dic[row[2], row[1]] = [row[3]]
            line_count += 1

    print(f'Processed {line_count} lines.'),
    valmax = max(dic, key=dic.get)
    print(valmax)
    sum = 0;
    for i in range (len(nums)):
        sum += int(nums[i])

    sum = sum / len(nums)

    print("Average: " + str(sum))

    with open('nba_file.csv', mode='w') as nba_file:
        csv_writer = csv.writer(nba_file, delimiter=',')

        csv_writer.writerow(['Name', 'Average', 'Max Value Key'])
        csv_writer.writerow(['Larry', sum, valmax])
