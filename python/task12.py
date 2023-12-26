import pandas as pd

# Given data
data = [
    {"roll_no": 1, "name": "John", "games": ["cricket", "football"], "marks": {"maths": 90, "science": 93, "history": 81}, "rank": 1},
    {"roll_no": 2, "name": "Mick", "games": ["football", "hockey"], "marks": {"maths": 95, "science": 86, "cs": 70}, "rank": 2},
    {"roll_no": 3, "name": "June", "games": ["badminton", None], "marks": {"maths": 92, "science": 92, "geography": 78}, "rank": 3},
    {"roll_no": 4, "name": "Adam", "games": ["soccer", "badminton"], "marks": {"maths": 86, "science": 91, "cs": 82}, "rank": 4},
    {"roll_no": 5, "name": "Robb", "games": ["cricket", None], "marks": {"maths": 88, "science": 90, "economics": 84}, "rank": 5},
    {"roll_no": 6, "name": "Arya", "games": ["football", "hockey"], "marks": {"maths": 89, "science": 88, "history": 97}, "rank": 6}
]

# Create a DataFrame from the given data
df = pd.DataFrame(data)

# Get details of students who studied 'cs' subject using lambda function
cs_students = df[df['marks'].apply(lambda x: 'cs' in x if isinstance(x, dict) else False)]
print("Details of students who studied 'cs' subject:")
print(cs_students)

# Update student ranks based on the specified formula
df['percentage'] = df['marks'].apply(lambda x: 3*x.get('maths', 0) + 2*x.get('science', 0) + sum(x.get(sub, 0) for sub in x.keys() if sub not in ['maths', 'science']))
df['rank'] = df['percentage'].rank(ascending=False, method='min').astype(int)

# Remove null values in the 'games' column
df['games'] = df['games'].apply(lambda x: [game for game in x if game is not None] if isinstance(x, list) else x)

# Create a new DataFrame with required details
result_df = pd.DataFrame({
    'name': df['name'],
    'percentage': df['percentage'],
    'previous_rank': df['rank'],
    'current_rank': df.groupby('rank').cumcount() + 1,
    'change_in_rank': df.groupby('rank').cumcount() - df.groupby('rank').cumcount().shift(fill_value=0)
})

# Replace NaN values in 'change_in_rank' with '-'
result_df['change_in_rank'] = result_df['change_in_rank'].apply(lambda x: '-' if pd.isna(x) else int(x))

# Sort the DataFrame by 'current_rank'
result_df = result_df.sort_values(by='current_rank')

# Display the result DataFrame
print("\nResult DataFrame:")
print(result_df)
