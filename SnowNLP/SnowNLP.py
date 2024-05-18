# %%
import random
from snownlp import SnowNLP, sentiment

# Load data from file
def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return [line.strip() for line in data if line.strip()]

# Split data into training set and test set
def split_data(data, train_ratio=0.8):
    random.shuffle(data)
    train_size = int(len(data) * train_ratio)
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data

# Save data to file
def save_data(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(f"{line}\n")

# Test the model
def test_model(test_data, label):
    if not test_data:
        return 0.0  # If test data is empty, return 0.0
    correct = 0
    for sentence in test_data:
        s = SnowNLP(sentence)
        prediction = s.sentiments
        if label == 'positive' and prediction > 0.5:
            correct += 1
        elif label == 'negative' and prediction <= 0.5:
            correct += 1
    accuracy = correct / len(test_data)
    return accuracy

def train_model(store_file_path,postive_file_path,negative_file_path):
    # Load data
    positive_data = read_data(postive_file_path)
    negative_data = read_data(negative_file_path)
    # Split data
    positive_train, positive_test = split_data(positive_data)
    negative_train, negative_test = split_data(negative_data)
    # Save data
    save_data(positive_train, store_file_path+'positive_train.txt')
    save_data(negative_train, store_file_path+'negative_train.txt')
    save_data(positive_test, store_file_path+'positive_test.txt')
    save_data(negative_test, store_file_path+'negative_test.txt')
    sentiment.train(store_file_path+'negative_train.txt', store_file_path+'positive_train.txt')
    sentiment.save('Model/MovieCommentExtend.marshal.3')

def test_model(store_file_path):
    sentiment.load('Model/MovieCommentExtend.marshal.3')
    # Read the test data
    positive_test_data = read_data(store_file_path+'positive_test.txt')
    negative_test_data = read_data(store_file_path+'negative_test.txt')

    # Test the model
    positive_accuracy = test_model(positive_test_data, 'positive')
    negative_accuracy = test_model(negative_test_data, 'negative')

    # Print the results
    print(f"Positive accuracy: {positive_accuracy * 100:.2f}%")
    print(f"Negative accuracy: {negative_accuracy * 100:.2f}%")
    print(f"Overall accuracy: {(positive_accuracy + negative_accuracy) / 2 * 100:.2f}%")

# %%
# Train the model
if __name__ == '__main__':
    store_file_path = 'Data/'
    postive_file_path = 'Data/pos.txt'
    negtive_file_path = 'Data/neg.txt'
    # Train the model
    train_model(store_file_path, postive_file_path, negtive_file_path)
    # Test the model
    test_model(store_file_path)



