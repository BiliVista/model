from paddlenlp.transformers import ErnieForSequenceClassification, ErnieTokenizer
from libs.utils import predict
import pandas as pd


def load_model(model_path):
    model = ErnieForSequenceClassification.from_pretrained(model_path)
    tokenizer = ErnieTokenizer.from_pretrained(model_path)
    return model,tokenizer


def model_pridect(model,tokenizer,data,batch_size=32,label_map = {0: 0, 1: 1}):
    res= predict(model, data, tokenizer, label_map, batch_size=batch_size)
    return res

def pridect_example(model,tokenizer):
    data = [
        {"text":'这个宾馆比较陈旧了，特价的房间也很一般。总体来说一般'},
        {"text":'怀着十分激动的心情放映，可是看着看着发现，在放映完毕后，出现一集米老鼠的动画片'},
        {"text":'好看!'},
    ]
    label_map={0:"负面",1:"正面"}
    res=model_pridect(model,tokenizer,label_map=label_map)
    for idx, text in enumerate(data):
        print('Data: {} \t Lable: {}'.format(text, res[idx]))


def pridect_text(model,tokenizer,text_list):
    data=[]
    for text in text_list:
        data.append({"text": text})
    res=model_pridect(model=model,tokenizer=tokenizer,data=data)
    return res
    
def calc_acc(true_labels,pridect_labels):
    total_correct = 0
    total_samples = len(pridect_labels)

    for t,p in zip(true_labels,pridect_labels):
        total_correct+=int(t==p)


def pridect_excel(model,tokenizer,excel_url):
    df=pd.read_excel(excel_url)
    data=[]
    for index, row in df.iterrows():
        data.append({"text": row['comment'], "like": row['like']})
    results = model_pridect(model,tokenizer,data)
    pos=0
    neg=0
    s=0
    com={}
    sen={}
    love={}

    for i,num in enumerate(results):
        if(num==1):
            pos+=data[i]["like"]
        else:
            neg+=data[i]["like"]
        com[i]=data[i]['text']
        sen[i]=num
        love[i]=data[i]["like"]
        
        s+=data[i]["like"]

    df=pd.DataFrame({"com":com,"sen":sen,"love":love})
    return df


    

