"""
This module descibes how to train on a full dataset (when no testset is
built/specified) and how to use the predict() method.
"""


from surprise import Dataset, KNNBasic

# Load the movielens-100k dataset
data = Dataset.load_builtin("ml-100k")

# Retrieve the trainset.
trainset = data.build_full_trainset()

# Build an algorithm, and train it.
algo = KNNBasic()
algo.fit(trainset)

# we can now query for specific predicions
uid = trainset.to_raw_uid(196)  # raw user id (as in the ratings file). They are **strings**! Do not use str() causing issues of having the same estimation for different ids.
iid = trainset.to_raw_iid(302)  # raw item id (as in the ratings file). They are **strings**!

# get a prediction for specific users and items.
pred = algo.predict(uid, iid, r_ui=4, verbose=True)
