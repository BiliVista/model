import random
from snownlp import SnowNLP, sentiment

# Load data from file
def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return [line.strip() for line in data if line.strip()]

# Split data into training and testing data
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

# Test model
def test_model(test_data, label):
    if not test_data:
        return 0.0  # 如果测试数据为空，则返回0的准确率
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

# Train model
def Model(neg_file, pos_file,file_path):
    # Read data
    positive_data = read_data(file_path + "/" + pos_file)
    negative_data = read_data(file_path + "/" + neg_file)
    # Split data
    positive_train, positive_test = split_data(positive_data)
    negative_train, negative_test = split_data(negative_data)
    # Save trainning data
    save_data(positive_train, file_path + "/positive_train.txt")
    save_data(negative_train, file_path + "/negative_train.txt")
    # Save testing data
    save_data(positive_test, file_path + "/positive_test.txt")
    save_data(negative_test, file_path + "/negative_test.txt")
    # Train model
    sentiment.train(file_path + "/positive_train.txt",
                    file_path + "/negative_train.txt")
    sentiment.save(file_path + "/sentiment.marshal")
    # Load model
    sentiment.load(file_path + "/sentiment.marshal")
    # Test model
    positive_accuracy = test_model(positive_test, 'positive')
    negative_accuracy = test_model(negative_test, 'negative')
    print(f"Positive accuracy: {positive_accuracy:.2f}")
    print(f"Negative accuracy: {negative_accuracy:.2f}")

# 训练模型
if __name__ == "__main__":
    Model("neg.txt", "pos.txt", "Data")
    print("Finish training.")