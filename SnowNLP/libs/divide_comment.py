import pandas as pd
import numpy as np

# Merge Maoyan and Douban
data = []
df = pd.read_excel("MovieComments.xlsx")
length = len(df)
print("Length of data: ", length)

# Ensure '评分' is a number
df['评分'] = pd.to_numeric(df['评分'], errors='coerce')

# Divide the data into positive and negative parts
positive = df[df['评分'] > 3]
negative = df[(df['评分'] <= 3) & (df['评分'] > 0)]

# Only keep the comment and score, and remove comments with less than 3 characters
positive = positive[positive['评论内容'].str.len() > 3][['评论内容']]
negative = negative[negative['评论内容'].str.len() > 3][['评论内容']]

# Export to Excel
positive.to_excel("pos.xlsx", index=False)
negative.to_excel("neg.xlsx", index=False)

# Export to text file
positive.to_csv("pos.txt", index=False, header=False, sep='\t')
negative.to_csv("neg.txt", index=False, header=False, sep='\t')