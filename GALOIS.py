import DataPreprocessing as dp
import MachineLearningFramework as ml
import StatisticsAnalysis as sa
import Visualizer as vi
from pandas.api.types import is_numeric_dtype

#In development...

def numericChecker(data):


    nonNumerCol = []
    numerCol = []
    signal = 1

    for column in data.columns:

        if is_numeric_dtype(data.loc[:, column]):

            numerCol.append(column)


        else:

            nonNumerCol.append(column)

            signal = 0



    return (signal, numerCol, nonNumerCol)


def signalTransform(signal):

    if signal == "yes":

        return 0

    elif signal == "no":

        return 1

    else:

        print("Wrong input. Please Try again. / 잘못된 입력. 다시 입력하세요.")

        return 2

def normalizeChecker(data):

    loss = data.mean() - data.median()

    loss2 = loss.mean()

    print("Analysis Result / 분석 결과: ")
    print("While the data's mean is %f, the difference between median and mean is in average %f."%(data.mean().mean(), loss2))
    print("데이터의 평균값은 %f인데 반해, 중앙값과 평균값의 차이는 평균 %f입니다. 이 둘의 값의 차가 클수록 많은 열의 데이터가 대칭적이지 않거나 이상치가 많음을 의미합니다. \n"
          "이상치가 많을 경우, 평균과 표준편차, 혹은 최댓값과 최솟값으로 정규화하는 것은 기계학습의 정확도를 낮출 수 있습니다. 참고하시기 바랍니다." % (
    data.mean().mean(), loss2))

    print("Actual Analysis Result / 실제 분석 결과: ")

    vi.backDoorOneVarPlot(loss)




def progress(currentStage):

    while True:

        nextStage = mainLogic[currentStage][signalTransform(endingQuestionDict[currentStage])]

        if nextStage is None:

            continue

        else:

            break

    return nextStage



log = {}

endingQuestionDict = {}

mainLogic = {0: [1, 2, None],
             1: [0, 1, None],
             2: [3, 2, None],
             3: [3.5, 5, None],
             3.5:[4, 6, None],
             4: [7, 8, None],
             5: [7, 8, None],
             6: [7, 8, None],
             7: [8, 7, None],
             8: [9, 10, None],
             9: []
             }



