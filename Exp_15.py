import pandas as pd
data = {
    "Post_ID": [1, 2, 3, 4, 5, 6],
    "Likes": [10, 25, 10, 40, 25, 10]
}
df = pd.DataFrame(data)
like_frequency = df["Likes"].value_counts()
print("Frequency Distribution of Likes:")
print(like_frequency)
