import pandas as pd
import timeit

# Create a wider dataset (large number of columns)
wider_df = pd.DataFrame({'col{}'.format(i): range(10000) for i in range(1000)})

# Create a taller dataset (large number of rows)
taller_df = pd.DataFrame({'col1': range(100000), 'col2': range(100000)})

# Time taken for iterrows() on wider dataset
iterrows_time_wider = timeit.timeit(lambda: list(wider_df.iterrows()), number=1)

# Time taken for iterrows() on taller dataset
iterrows_time_taller = timeit.timeit(lambda: list(taller_df.iterrows()), number=1)

# Time taken for itertuples() on wider dataset
itertuples_time_wider = timeit.timeit(lambda: list(wider_df.itertuples(index=False)), number=1)

# Time taken for itertuples() on taller dataset
itertuples_time_taller = timeit.timeit(lambda: list(taller_df.itertuples(index=False)), number=1)

# Time taken for apply() on wider dataset
apply_time_wider = timeit.timeit(lambda: wider_df.apply(lambda x: x.sum(), axis=1), number=1)

# Time taken for apply() on taller dataset
apply_time_taller = timeit.timeit(lambda: taller_df.apply(lambda x: x.sum(), axis=1), number=1)

# Time taken for map() on wider dataset
map_time_wider = timeit.timeit(lambda: wider_df['col1'].map(lambda x: x * 2), number=1)

# Time taken for map() on taller dataset
map_time_taller = timeit.timeit(lambda: taller_df['col1'].map(lambda x: x * 2), number=1)

print("Time taken for iterrows() on wider dataset:", iterrows_time_wider)
print("Time taken for iterrows() on taller dataset:", iterrows_time_taller)
print("Time taken for itertuples() on wider dataset:", itertuples_time_wider)
print("Time taken for itertuples() on taller dataset:", itertuples_time_taller)
print("Time taken for apply() on wider dataset:", apply_time_wider)
print("Time taken for apply() on taller dataset:", apply_time_taller)
print("Time taken for map() on wider dataset:", map_time_wider)
print("Time taken for map() on taller dataset:", map_time_taller)
