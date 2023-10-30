# add the highist nunbers combination and get the range of where most number lands on
# the goal for this is to break down all the lottery numbers into separare columns, find the most frequent numbers in each column, show how many of each number appear on a chart
import pandas
import math

df = pandas.read_csv(


df = pandas.DataFrame(masterlist)

# sorting the numbers in the winning numbers column to be in order
df['Winning Numbers'] = df['Winning Numbers'].apply(
    lambda x: ' '.join(map(str, sorted(map(int, x.split())))))

# splitting the winning numbers column to be their own column
df[['Number1', 'Number2', 'Number3', 'Number4', 'Number5', 'Number6']
   ] = df['Winning Numbers'].str.split(expand=True)
df = df[['Draw Date', 'Number1', 'Number2', 'Number3',
         'Number4', 'Number5', 'Number6', 'Multiplier']]

print(df)

# found out for each column, which number is the most frequent
most_common_number = {}
for col in df.columns:
    if col.startswith('Number'):
        most_common = df[col].mode().values[0]
        most_common_number[col] = most_common

print(f'Most common Numbers are: {most_common_number}')
# most common multiplier
most_common_multiplier = df['Multiplier'].mode().values[0]
print(f'Most common Multiplier is {most_common_multiplier}')


# split_numbers = df['Winning Numbers'].str.split().apply(
#     lambda x: [int(num) for num in x])

# df['PB'] = split_numbers.apply(lambda x: x.pop())

# sorted_values = split_numbers.apply(lambda x: sorted(x[:5]))

# sorted_df = sorted_values.apply(
#     lambda x: ' '.join(map(str, x))).str.split(expand=True)
# df = pandas.concat([df, sorted_df], axis=1)
# df.columns = ['Draw Date', 'Winning Numbers',
#               'Multiplier', 'PB', 'Number1', 'Number2', 'Number3', 'Number4', 'Number5']

# # Print the final DataFrame
# print(df