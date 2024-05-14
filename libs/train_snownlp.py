import random
from snownlp import SnowNLP, sentiment

# 从文件加载数据
def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return [line.strip() for line in data if line.strip()]

# 将数据拆分为训练集和测试集
def split_data(data, train_ratio=0.8):
    random.shuffle(data)
    train_size = int(len(data) * train_ratio)
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data

# 将数据保存到文件
def save_data(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(f"{line}\n")

# 测试模型
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

