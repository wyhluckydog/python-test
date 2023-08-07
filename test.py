import os

MODEL_PATH = os.environ.get('MODEL_PATH')

def main():
    modelPath = "/work/home/task/" + MODEL_PATH + "/model/"  
    s1="""输出模型"""
    
    if not os.path.exists(modelPath):
        os.makedirs(modelPath, exist_ok=True)
    with open(modelPath + "model.txt","w") as fp:
        fp.write(s1)

if __name__ == '__main__':
    main()