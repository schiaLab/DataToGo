from sklearn.linear_model import LinearRegression as lir
from sklearn.linear_model import LogisticRegression as lor
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.neighbors import KNeighborsClassifier as knc
from sklearn.neighbors import KNeighborsRegressor as knr
from sklearn.metrics import classification_report
from keras import models
from keras import layers

def div():

    print("="*10)


def sdiv():

    print("-"*10)


functionNumDict = {"rli":1, "clo":2, "rrf":3, "crf":4 , "rde":5, "cde":6}

instructionDict = {
    1: ["선형회귀는 가장 간단한 형태의 회귀 모델입니다. 선형 회귀는 주어진 변수들마다 하나씩 '가중치'라는 값을 곱한 다음 모두 더합니다. 그 다음, 가장 결과값에 적합하도록 가중치들을 조정합니다.",
        "Linear Regression is the simplest model for regression. It gives every variable a 'weight', and the 'weight' is determined by the expected result."],
2:["로지스틱회귀는 이름과는 다르게 가장 간단한 형태의 분류 모델입니다. 로지스틱 회귀는 선형회귀와 같이 변수들에 가중치를 곱하는 것까진 같지만, 그 결과값이 0과 1 사이가 될 수 있는 특별한 함수를 사용합니다.",
   "Logistic Regression, unlike its name, is the simplest form of classification model. \n "
   "It is almost same as linear regression, except that this one uses another special function to make the result to stay between 0 to 1."] ,
    3:["랜덤 포레스트는 앙상블 모델 중 하나로, 일반 의사결정나무 모델보다 훨씬 더 높은 정확도를 보입니다. 이 모델은 회귀용입니다.",
       "Random Forest is one of ensemble learning model, and it's more accurate than normal decision tree. This one is for regression."],
    4: [
        "랜덤 포레스트는 앙상블 모델 중 하나로, 일반 의사결정나무 모델보다 훨씬 더 높은 정확도를 보입니다. 이 모델은 분류용입니다.",
        "Random Forest is one of ensemble learning model, and it's more accurate than normal decision tree. This one is for classification."],
    5: [
        "딥러닝으로 잘 알려진 심층학습은 1900년대에 처음 제안된 이후 2010년대에 가장 왕성하게 연구되고 활용되고 있는 기계학습 모델입니다. \n "
        "몇 가지 단점을 제외하면, 심층학습은 거대한 데이터셋에서 가장 높은 성능을 보인다고 평가됩니다. 이 모델은 회귀용입니다.",
        "Deep Learning is considered as the most effective way to predict in large dataset. This one is for regression."],
    6: [
        "딥러닝으로 알려진 심층학습은 1900년대에 처음 제안된 이후 2010년대에 가장 왕성하게 연구되고 활용되고 있는 기계학습 모델입니다. \n "
        "몇 가지 단점을 제외하면, 심층학습은 거대한 데이터셋에서 가장 높은 성능을 보인다고 평가됩니다. 이 모델은 분류용입니다.",
        "Deep Learning is considered as the most effective way to predict in large dataset. This one is for classification."]

}

questionDict = {
    1: [None,
        None],
    2: [None,
        None],

    3: [None,
        None],

4: [None,
        None],
5: [["은닉층의 수를 입력해주세요: ", "최대 노드 수를 입력해 주세요: "],["Enter the Number of hidden layers: ", "Enter the Number of maximum node: "]],
6: [["은닉층의 수를 입력해주세요: ", "최대 노드 수를 입력해 주세요: "],["Enter the Number of hidden layers: ", "Enter the Number of maximum node: "]]
}




def functionNumGenerator(lid):

    if lid == 0:

        print("기계학습 부문에 오신 걸 환영합니다. 지금 이 순간에도 기계학습은 지속적으로 발전하고 있고, 새로운 사용 방법이 쏟아져 나오고 있습니다.\n  "
              "비록 모든 기계학습 알고리즘들이 담겨 있지는 않지만, 여러분들의 창의력과 흥미를 돋울만한 몇 가지 알고리즘들을 들고 왔습니다. \n"
              "이 작업을 하기 전, 데이터 전처리가 모두 숫자의 형태로 올바르게 되어 있어야 합니다. 비지도학습은 이후 업데이트에서 추가할 예정입니다.")

        var = input("기계학습의 목적이 분류입니까, 회귀입니까? 회귀란 예측하는 값이 온도, 속도 등 연속적인 수일 때를 말합니다 (r: 회귀 / c: 분류): ")

        if var == "r":

            type = input("회귀 모델을 선택해 주세요 (선형회귀: li /  심층학습: de  / 랜덤 포레스트: rf): ")

        elif var == "c":

            type = input("분류 모델을 선택해 주세요 (로지스틱회귀: lo /  심층학습: de / 랜덤 포레스트: rf): ")

        else:

            print("잘못된 입력.")

            type = "a"


        try:

            return functionNumDict[var+type]

        except:

            print("잘못된 입력. 프로세스를 종료합니다.")


    else:

        print("Welcome to Data visualization section. Visualizing data is a quite extensive field. So unfortunately, I couldn't make every method possible.\n"
              "However I developed some basic tools like distribution plot, time series graph, and scatter plot. More methods will be added by upgrades.")

        var = input("How many features do you need for analysis? (one: o / two: t / all: a (three: working on it!)): ")

        if var == "a":

            type = input("What attribute you want to know? (Pearson Correlation Coefficient: p/ normal value size (dataset should be all numbers): n): ")

        elif var == "n":

            type = input("What type of figure do you need? (time series: l): ")

        else:

            type = input("What type of figure do you need? (distribution: d / time series: l / scatter: s): ")





        return functionNumDict[var + "v" + type]




def instruction(functionNum, lid):
    print(instructionDict[functionNum][lid])


def questionCall(functionNum, lid):
    paraList = []

    for question in questionDict[functionNum][lid]:
        print("-" * 10)

        paraList.append(input(question))

    return paraList


def autoRun(functionNum, dataX, dataY, testDataX , testDataY ,paraList):

    if functionNum == 1:

        LinearRegression(x=dataX, y=dataY, testX=testDataX, testY=testDataY)


    elif functionNum == 2:

        LogisticRegression(x=dataX, y=dataY, testX=testDataX, testY=testDataY)


    elif functionNum == 3:

        randomRegression(x=dataX, y=dataY, testX=testDataX, testY=testDataY)

    elif functionNum == 4:

        randomClassification(x=dataX, y=dataY, testX=testDataX, testY=testDataY)

    elif functionNum == 5:

        deepRegression(x=dataX, y=dataY, testX=testDataX, testY=testDataY, hiddenLayers=paraList[0], nodes=paraList[1])

    elif functionNum == 6:

        deepClassification(x=dataX, y=dataY, testX=testDataX, testY=testDataY, hiddenLayers=paraList[0], nodes=paraList[1])


def projectRun(lid, dataWareHouse):

    while True:

        div()

        print("List of tags / 태그 리스트")
        print(dataWareHouse.dataDict.keys())


        trainXTag = input("Which data tag will you choose for training input? (Enter to exit) / 훈련 데이터 중 입력 데이터의 태그를 입력하십시오: ")



        trainYTag = input(
            "Which data tag will you choose for training output? (Enter to exit) / 훈련 데이터 중 출력 데이터의 태그를 입력하십시오 (엔터로 종료): ")


        dataX = dataWareHouse.dataDict[trainXTag]
        dataY = dataWareHouse.dataDict[trainYTag]

        try:

            testDataX = dataWareHouse.testDict[trainXTag]
            testDataY = dataWareHouse.testDict[trainYTag]

        except:

            testDataX = None
            testDataY = None

            print("Fatal Error ML001. Contact schialab from Github. \n 시스템 오류 ML001. 카카오톡 채널 cailhelp 혹은"
                "Github schialab에 문의하십시오.")


        print("selected data / 선택된 데이터: ")
        print(dataX.head())
        print(dataY.head())

        functionNum = functionNumGenerator(lid)

        instruction(functionNum, lid)

        paraList = questionCall(functionNum, lid)

        autoRun(functionNum, dataX=dataX, dataY= dataY, testDataX=testDataX, testDataY=testDataY , paraList=paraList)


def LinearRegression(x, y, testX, testY):

    model = lir()

    model.fit(x, y)

    print("Fitting Complete. Displaying Results... / 모델 피팅 성공. 결과 출력...")

    print("R^2 Score:",model.score(testX, testY))


def LogisticRegression(x, y, testX, testY):

    model = lor()

    model.fit(x, y)

    print("Fitting Complete. Displaying Results... / 모델 피팅 성공. 결과 출력...")

    print("R^2 Score:",model.score(testX, testY))


def deepRegression(x, y, testX, testY, hiddenLayers, nodes):

    model = models.Sequential()
    model.add(layers.Dense(nodes, activation='relu', input_dim=x.shape[1], ))

    for n in range(hiddenLayers):
        model.add(layers.Dense(int(nodes * (hiddenLayers - n + 1) / (hiddenLayers + 1)), activation='relu'))
    model.add(layers.Dense(y.shape[1], activation='sigmoid'))
    model.compile(optimizer='rmsprop', loss='mse')

    model.fit(x, y, validation_data=(testX, testY))


def deepClassification(x, y, testX, testY, hiddenLayers, nodes):


    model = models.Sequential()
    model.add(layers.Dense(nodes, activation='relu', input_dim=x.shape[1], ))

    for n in range(hiddenLayers):
        model.add(layers.Dense(int(nodes * (hiddenLayers - n + 1) / (hiddenLayers + 1)), activation='relu'))
    model.add(layers.Dense(y.shape[1], activation='softmax'))
    model.compile(optimizer='rmsprop', loss='binary_crossentropy')

    model.fit(x, y, validation_data=(testX, testY))


def randomRegression(x, y, testX, testY):

    model = rfr()

    model.fit(x, y)

    print("Fitting Complete. Displaying Results... / 모델 피팅 성공. 결과 출력...")

    print("R^2 Score:",model.score(testX, testY))


def randomClassification(x, y, testX, testY):

    model = rfc()

    model.fit(x, y)

    print("Fitting Complete. Displaying Results... / 모델 피팅 성공. 결과 출력...")

    print("R^2 Score:",model.score(testX, testY))


