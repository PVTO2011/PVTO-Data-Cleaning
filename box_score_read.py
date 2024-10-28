import pandas as pd
import numpy as np
import lxml
import re


# Paste data here for one team at a time. Add a space between numbers and names and you may have to add spaces for some values that are double digits.
# If you get an error that says # columns =/= # values, use the following line to see where there are two values in one line
# for i in data:
    # print(len(i), i)

html_content = """
11  Livingston, Roxanne    2   6  1   2  3   4   0   2   2  4  8  1  2  0  0  20:00
14  Gonzalez, Seline       0   2  0   0  0   0   0   1   1  4  0  0  3  0  1   4:30
15  Howell, Ginger         5   8  3   4  4   6   1   2   3  3  17  1  4  1  2   4:30
 1  Longfellow, Jennifer G  1   5  0   2  0   0   1   1   2  1  2  0  4  0  0  37:17
13  Vandergrooten, JannelG  1   3  0   0  2   2   1   5   6  4  4  1  1  1  0   1:51
 2  Goldstien, Robyn        0   2  0   2  2   3   0   2   2  1  2  0  4  0  1  19:56
 3  Goldsmith, Regina       0   1  0   0  0   0   1   0   1  0  0  0  2  0  0   0:00
 4  Amundson, Camie         6  10  0   0  6   9   2   5   7  3  18  0  1  0  1  18:09
 5  Barbera, Josie          0   0  0   0  0   0   0   0   0  1  0  0  0  0  0  19:56
 7  Martens, Samantha       0   2  0   2  0   0   1   1   2  5  0  0  3  0  0  35:26
 8  Shortbread, Penelope    0   1  0   1  0   0   0   1   1  1  0  0  1  0  0   0:00
 9  Archangelo, Maria       0   0  0   0  0   0   0   0   0  0  0  0  0  0  0  19:56
16  Burnett, Goldie         3   7  1   4  3   4   0   2   2  0  10  1  2  0  0  18:09
17  Habben, Alice           0   3  0   1  3   4   0   0   0  0  3  1  1  0  0   0:00
"""

# Step 1: Clean and preprocess the text (strip unnecessary spaces)
lines = html_content.strip().splitlines()

# Step 2: Define a function to process each line by splitting on multiple spaces
def process_line(line):
    # Use regular expression to split by multiple spaces
    return re.split(r'\s{2,}', line.strip())

# Step 3: Apply the function to all lines to get structured data
data = [process_line(line) for line in lines]

# Step 4: Create a DataFrame with appropriate column names
columns = ['Number', 'Name', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'PF', 'TP', 'AST', 'TO', 'STL', 'BLK', 'MIN']
df = pd.DataFrame(data, columns=columns)

# Make two new columns, First Name and Last Name. First should be text before "," in the name and Last should be text after. Delete the original Name column.
# Move first name to the first column, last name to the second column, and delete the original Name column
df['First Name'] = df['Name'].str.split(', ').str[1]
df['Last Name'] = df['Name'].str.split(',').str[0]
df = df.drop(columns=['Name'])
df = df[['Number', 'First Name', 'Last Name', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'PF', 'TP', 'AST', 'TO', 'STL', 'BLK', 'MIN']]

# Display the DataFrame
print(df)
df.to_clipboard(index=False)

print('Done')
