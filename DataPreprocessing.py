import pandas as pd
import numpy as np
import tensorflow as tf
import Visualizer as vi
from sklearn.decomposition import PCA
from keras import models
from keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder



def div():

    print("="*10)


def sdiv():

    print("-"*10)


def dataWareHouseControl(dataWareHouse):
    div()

    print("List of Tags / 태그 목록")
    print(dataWareHouse.dataDict.keys())

    while True:

        command = input("me for merging dataset/ de for deleting dataset / ch for chaning tag (Enter to Exit): \n"
                        "데이터셋 병합은 me / 데이터셋 제거는 de / 데이터셋 태그 변경은 ch (엔터로 종료): ")

        if command == "me":

            dataWareHouse.mergeDataset()


        elif command == "de":

            dataWareHouse.delData()


        elif command == "ch":

            dataWareHouse.tagChange()


        elif command == "":

            break

        else:

            print("Wrong Input / 잘못 입력하셨습니다.")


def dataPreprocessingInterface(dataWareHouse):

    print("Data Preprocessing is in dual-language for higher compatibility. / 데이터 전처리는 시스템 전반적 호환성을 위해 양쪽 언어를 모두 표기합니다.")





    while True:

        div()

        command = input("Are you preprocessing your data for Machine Learning or other models? y for yes/ n for no: "
                        "\n (If you are, you should divide your dataset. K-fold cross validation is in development.)\n\n"
                        "기계학습 및 기타 모델에서의 적용을 위해서 데이터 전처리를 하는 것인가요? (예:y / 아니요:n) \n"
                        "(만약 그렇다면, 데이터셋을 학습용과 검증용으로 분리해야 합니다. k-fold 교차 검증은 개발중에 있습니다.): ")

        if command == "y":

            dataWareHouse.trainTestDivider()


            print("Don't forget to seperate the columns you want to predict. / 예측할 열의 데이터를 분리하는 것을 잊지 말기 바랍니다.")


            break


        elif command == "n":


            dataWareHouse = dataWareHouse

            break


    while True:


        dataWareHouseControl(dataWareHouse)

        div()

        print("List of tags / 태그 리스트")
        print(dataWareHouse.dataDict.keys())

        newTag = ""


        tag = input("Which data tag will you choose? (For data visualization and machine learning, press Enter)"
                    "\n 선택하고자 하는 데이터의 태그를 입력하십시오 (데이터 시각화 및 기계학습 진행을 위해선 엔터): ")

        if tag == "":

            break

        data = dataWareHouse.dataDict[tag]

        data3 = None

        try:

            data2 = dataWareHouse.testDict[tag]

            data4 = None

        except:

            data2 = None

            data4 = None


        print("selected data / 선택된 데이터: ")
        print(data.head())

        command = input("What data preprocessing you are willing to do?\n m for manipulating dataset / f for feature extraction / s for data selection / Press Enter to End: \n"
                        "어떤 데이터 전처리를 거치고자 합니까? \n 데이터셋 내용을 바꾸거나 추가하는 등 데이터셋을 변형하려면 m / 데이터의 특징을 추출하려면 f / 데이터 중 일부를 선택하려면 s / 끝내려면 엔터: ")

        sdiv()
        if command == "m":


           while True:

                command2 = input("re for revering row order / mv for missing value management / ad for adding column using dataset data or an input (Enter to go home) \n"
                                 "열 순서 역순은 re / 결측치 관리는 mv / 입력값 및 데이터셋 내부 데이터로 열을 추가하려는 경우 ad 를 입력하십시오 (엔터를 눌러 홈으로): ")


                if command2 == "re":

                    data = reverse(data)

                    try:

                        data2 = reverse(data2)

                        break

                    except:


                        break



                elif command2 == "mv":

                    data = nanRemover(data)

                    try:

                        data2 = nanRemover(data2)

                        break

                    except:

                        break


                elif command2 == "ad":

                    while True:

                        command2 = input(
                            "del for column deletion / cc for column by column calculation / cn for column by number calculation / lab for labeling data: \n"
                            "열 삭제는 del / 열과 열 간의 사칙연산은 cc / 열과 수 간의 연산은 cn / 데이터 라벨링(하나의 입력값으로 데이터 열 추가)은 lab: ")

                        if command2 == "del":

                            data, data2 = colDelete(data, data2)

                            break



                        elif command2 == "cc":

                            data, data2 = colCalculation(data, data2)

                            break



                        elif command2 == "cn":

                            data , data2= colbyNumCalculation(data, data2)

                            break



                        elif command2 == "lab":


                            value = input("label value / 라벨링을 할 값 (수를 입력시 자동으로 수로 인식합니다): ")

                            try:

                                value = float(value)

                            except:

                                value = value



                            labelName = input("Label Name / 라벨 열의 이름: ")

                            data = labeling(data, value, labelName)

                            try:

                                data2 = labeling(data2, value, labelName)

                                break

                            except:

                                break

                        elif command2 == "":

                            break

                        else:

                            print("Wrong Input / 잘못된 입력")
                            continue


                    break





        elif command == "f":

            while True:

                command2 = input("gr for groupby / au for autoencoder / da for date preprocessing / no for normalizing / ot for onehotencoding (Enter to Home)\n"
                                 "그룹핑은 gr / 오토인코더는 au / 날짜 전처리는 da / 정규화는 no / 원핫인코딩은 ot (엔터로 홈): ")


                if command2 == "au":

                    encoder, ss, data = autoEncoder(data)

                    dataWareHouse.modelDict[tag].append(ss)
                    dataWareHouse.modelDict[tag].append(encoder)

                    try:

                        data2 = autoEncoder(data2, model=encoder, scaler=ss)

                        break

                    except:

                        break


                elif command2 == "da":

                    while True:

                        data, data2 = dateCleaner(data, data2)

                        command3 = input("Do you want to divide date to year, month and day? y for yes/n for no: \n"
                                         "년, 월, 일을 분리하겠습니까? (예: y/ 아니요: n): ")

                        if command3 == "y":

                            data, data2 = dateDivider(data, data2)

                            break

                        else:

                            break

                elif command2 == "gr":

                    data3, data4 = groupBy(data, data2)

                    newTag = input("What is the tag name of the new extracted data? / 추출한 데이터의 태그를 입력해주세요: ")

                elif command2 == "no":

                    data, scaler = normalizing(data)

                    dataWareHouse.modelDict[tag].append(scaler)

                    try:

                        data2 = normalizing(data2, model=scaler)

                        break

                    except:

                        break



                elif command2 == "ot":


                    data, ohe = oneHotEncoder(data)

                    dataWareHouse.modelDict[tag].append(ohe)

                    try:

                        data2 = oneHotEncoder(data2, model=ohe)

                        break

                    except:

                        break

                elif command2 == "":

                    break

                else:

                    print("Wrong input / 잘못된 입력")

                    continue

                break





        elif command == "s":


            while True:

                command2 = input("ci for custom indexing / fi for filtering / pca for PCA (Enter to Home)\n"
                                 "재량 인덱싱은 ci / 조건을 이용한 필터링은 fi / PCA 는 pca(모두 소문자)를 입력해 주세요 (엔터 눌러서 홈으로): ")


                if command2 == "ci":

                    data3, data4 = hardIndexing(data, data2)

                    newTag = input("What is the tag name of the new selected data? / 선별한 데이터의 태그를 입력해주세요: ")




                elif command2 == "fi":

                    data3, data4 = boolMasking(data, data2)

                    newTag = input("What is the tag name of the new selected data? / 선별한 데이터의 태그를 입력해주세요: ")






                elif command2 == "pca":


                    data3, model = pca(data)

                    data4, model = pca(data2, model)

                    dataWareHouse.modelDict[tag].append(model)

                    newTag = input("What is the tag name of the new selected data? / 선별한 데이터의 태그를 입력해주세요: ")




                elif command2 == "":

                    break

                else:

                    print("Wrong input / 잘못된 입력")

                    continue

                break







        elif command == "":

            break


        else:

            print("Wrong input / 잘못된 입력")

        dataWareHouse.dataDict[tag] = data

        dataWareHouse.testDict[tag] = data2

        if not data3 is None:

            dataWareHouse.dataDict[newTag] = data3

            dataWareHouse.testDict[newTag] = data4


    return dataWareHouse




class DataWareHouse:

    dataDict = {}
    modelDict = {}
    beforeSplitDict = {}
    testDict = {}


    def __init__(self, dataDict):

        self.dataDict = dataDict

        for key in self.dataDict.keys():

            self.modelDict[key] = []

        print("DataWareHouse Initialized / 데이터웨어하우스 인스턴스 생성 완료")

    def dataAddition(self, data, tag):

        self.dataDict[tag] = data

        self.modelDict[tag] = []

        print("'%s' tagged data added / '%s' 태그 데이터가 추가되었습니다."%(tag, tag))

        div()

    def dataGetProtocol(self):

        print("data retrive Protocol")
        print("Data Tag list / 데이터 태그 목록: ")
        print(self.dataDict.keys())

        tags = []

        while True:

            sdiv()

            tag = input("Choose a Tag (Enter when finished) / 태그를 선택하여 주십시오 (끝났을 경우 엔터를 눌러주세요): ")

            if tag == "":

                break

            else:

                tags.append(tag)

        sdiv()

        result = {}

        for tag in tags:


            result[tag] = self.dataDict[tag]

        print("Data Retrieved / 데이터 가져오기 완료.")

        return result




    def trainTestDivider(self):

        self.beforeSplitDict = self.dataDict

        for tag in self.beforeSplitDict.keys():

            self.dataDict[tag], self.testDict[tag] = train_test_split(self.dataDict[tag], train_size=0.75)




    def mergeDataset(self):

        print("List of Tags / 데이터 태그 목록: ")
        print(self.dataDict.keys())

        while True:

            tag1 = input("Type one of the tag of data for merging(Enter to End) / 병합할 데이터의 태그 중 하를 선택하세요 (종료하려면 엔터): ")

            if tag1 == "":

                break

            tag2 = input("Type the other tag of data for merging / 병합할 나머지 데이터의 태그를 선택하세요: ")

            tag = input("Type the tag for merged data / 병합된 데이터가 가질 태그를 입력하세: ")

            if self.dataDict[tag1].iloc[0, :] != self.dataDict[tag2].iloc[0, :]:

                print("Same row number detected. merging data horizontally... / 같은 행의 수가 감지되었습니다. 공통 열을 기준으로 병합합니다.")

                self.dataDict[tag] = merge(data1=self.dataDict[tag1], data2=self.dataDict[tag2], tag1=tag1, tag2=tag2)

                try:

                    self.testDict[tag] = merge(data1=self.testDict[tag1], data2=self.testDict[tag2], tag1=tag1, tag2=tag2)

                    break

                except:

                    break

            else:

                print("Same column list detected. Adding data vertically... / 같은 열 배열이 감지되었습니다. 같은 열에 있는 데이터끼리 병합합니다.")

                self.dataDict[tag] = self.dataDict[tag1].append(self.dataDict[tag2])

                try:

                    self.testDict[tag] = self.testDict[tag1].append(self.testDict[tag2])

                    break

                except:

                    break


    def coverData(self, data):

        print("data retrive Protocol")
        print("Data Tag list / 데이터 태그 목록: ")
        print(self.dataDict.keys())


        tag = input("What tag will you choose? / 태그 하나를 선택해 주십시오: ")

        self.dataDict[tag] = data

        try:

            self.testDict[tag] = data

        except:

            return None



    def tagChange(self):

        print("data retrive Protocol")
        print("Data Tag list / 데이터 태그 목록: ")
        print(self.dataDict.keys())

        tag = input("What tag will you choose? / 태그 하나를 선택해 주십시오: ")

        newTag = input("What is the new tag name? / 새로운 태그 이름을 설정해 주십시오: ")

        data = self.dataDict[tag]

        del self.dataDict[tag]

        self.dataDict[newTag] = data

        try:
            data = self.testDict[tag]

            del self.testDict[tag]

            self.testDict[newTag] = data

        except:

            return None



    def delData(self):

        print("data retrive Protocol")
        print("Data Tag list / 데이터 태그 목록: ")
        print(self.dataDict.keys())

        tag = input("Choose the tag of the data to delete / 지울 데이터의 태그를 입력해 주십시오: ")

        sdiv()

        print(self.dataDict[tag])

        command = input("This is not reversible. Type 'yes' to Continue. / 이 작업을 되돌이킬 수 없습니다. 진행하려면 yes를 입력해 주세요: ")

        if command != "yes":

            print("Data deletion is canceled / 데이터 제거를 취소합니다.")

        else:

            del self.dataDict[tag]


            try:

                del self.testDict[tag]

            except:

                return None










def fileGathering():

    dataDict = {}

    while True:



        fileType = input(
            "What's your dataset's file type? .xml/.csv(other types could be requested for development) \n"
            "분석하고자 하는 데이터가 담긴 파일이 어떤 타입입니까? (파일 이름 뒤 점과 알파벳 3글자) .xml/.csv(다른 타입은 개발중입니다): ")

        fileRoute = input(
            "File Name or Route: \n파일 경로 및 파일 이름을 적어주세요. DataToGO 퐅더 안에 있고 다른 폴더 안에 안 들어가 있다면 이름만 입력하시면 됩니다. 이름은 파일 타입까지 적어주세요: ")

        tag = input("Give the data a tag. The tag will help you find the right data: \n이 데이터에 태그를 붙여주세요. 태그를 알고 있으면 쉽게 데이터를 찾을 수 있습니다: ")

        if fileType == ".csv":

            dataDict[tag] = pd.read_csv(fileRoute, thousands=",")

        elif fileType == ".xml":

            dataDict[tag] = pd.read_xml(fileRoute, thousands=",")

        elif fileType == ".txt":

            handle = open(fileRoute)

            data = ""

            for line in handle:

                data += line


        command = input("More Files? (y/n):\n더 파일을 불러와야 합니까? (예:y/아니요:n): ")

        if command == "y":

            continue

        elif command == "n":

            break

        else:

            print("Wrong input. Considered as No.\n잘못 입력하셨습니다. 종료로 간주합니다.")

            break


    print("Data import complete. Here's the Summary. \n데이터 불러오기 성공. 불러오기 요약입니다.")
    print("불러온 데이터 개수: %d"%len(dataDict))
    print("데이터 태그:")

    for tag in dataDict.keys():

        print(tag)

    return dataDict

def dateCleaner(data, testData):

    print("Cleaning Date data. Date format should be 2020-10-30 Or 10,31,2020, etc. Month and day should be 2-digit (ex. 06, 12).Automatic changing month name to number is in development.\n\n"
          "데이터 중 날짜 정제 과정을 진행합니다. 정제 가능한 데이터 형태는 '2020-10-30' 및 '2020년 10월 30일' 등입니다. 년-월-일 순이 아니거나 월과 일이 2자리 수로 표기되지 않는 경우 등 정제 및 정제 이후 병합이 완벽하지 않은 경우가 있을 수 있습니다:\n"
          "If you are using date to merge two dataset, be sure to check the difference between two dates(ex. Is two dates both y/m/d or m/d/y?): \n날짜를 기준으로 데이터셋을 합칠 경우, 두 데이터셋의 날짜를 잘 관찰하여 병합이 잘 이루어질 수 있도록 정제하세요:")

    print("data Column / 데이터 열 목록: ", data.columns)

    date = None

    dateFrame = None

    targetCol = 0

    testDate = None

    testDateFrame = None


    while True:

        col = input("Copy and paste the date column name: \n"
                    "데이터 중 날짜 열의 이름을 복사하여 붙여넣어주십시오: ")

        try:

            date = data.loc[:, col].copy()

            try:

                testDate = testData.loc[:, col].copy()

            except:

                testDate = None

        except:

            print("No column exist. Try again. \n"
                  "해당 입력 열이 없습니다. 오타가 있는지 확인하여 다시 입력해 주십시오.")

            continue

        else:

            break

    sequence = []

    for letter in ["year/년", "month/월", "day/일"]:

        print("-"*10)
        print(date.iloc[0:3])

        va = int(input("where is %s? (1st->1, 2nd->2, 3th->3): \n%s은(는) 데이터에서 몇 번째에 있습니까? (1번째->1, 2번째->2, 3번째->3): "%(letter,letter)))-1
        sequence.append(va)



    while True:

        print("-" * 10)
        print(date.iloc[0:3])



        word = input("Type one of the common word(including space) that is between neighboring date data or at the end of the string. \n"
                     " (ex. 2020-01-01 => '-', 2020 01 01 => ' '(space), , 01dd => 'dd' : \n"
                     "이웃하는 년, 월, 일 데이터 사이 혹은 년, 월, 일 한쪽 끝에 있는 글자 (스페이스 포함)중 가장 왼쪽에 있는 글자를 적어주세요. \n"
                     "(ex. 2020 01 01 => ' '(스페이스), 2020년 08월 12일 => '년 '(스페이스 포함), 08월 12일 => '월 '(스페이스 포함):, 12일 => '일'):  ")


        if dateFrame is None:

            dateFrame = date.str.split(word, expand=True)

            if not testDate is None:

                testDateFrame = testDate.str.split(word, expand=True)

        else:

            dateFrame = dateFrame.drop(targetCol, axis=1)

            dateFrame2 = date.str.split(word, expand=True)

            dateFrame = dateFrame.reset_index()

            dateFrame2 = dateFrame2.reset_index()


            dateFrame = pd.merge(dateFrame, dateFrame2, on="index")


            dateFrame = dateFrame.drop("index", axis=1)


            if not testDate is None:

                testDateFrame = testDateFrame.drop(targetCol, axis=1)

                testDateFrame2 = date.str.split(word, expand=True)

                testDateFrame = testDateFrame.reset_index()

                testDateFrame2 = testDateFrame2.reset_index()

                testDateFrame = pd.merge(testDateFrame, testDateFrame2, on="index")

                testDateFrame = testDateFrame.drop("index", axis=1)













        print("정제 완료. 예시 결과 출력: \n", dateFrame.head())

        command = input("Did all of the dates are decomposed? (y for yes/name of un-decomposed column for no):\n"
                        "날짜가 년월일별로 전부 쪼개지고 각각 원하는 데이터만 남았나요? (예:y/아니요: 덜 쪼개진 데이터의 열 이름): ")

        if command == "y":


            result = dateFrame.iloc[:, sequence[0]] + "/" + dateFrame.iloc[:, sequence[1]] + "/" + dateFrame.iloc[:, sequence[2]]

            date = result

            if not testDate is None:

                result2 = testDateFrame.iloc[:, sequence[0]] + "/" + testDateFrame.iloc[:, sequence[1]] + "/" + dateFrame.iloc[:,
                                                                                                       sequence[2]]

                testDate = result2

            break

        else:

            targetCol = int(command)

            date = dateFrame.loc[:, targetCol]

            if not testDate is None:

                testDate = testDateFrame.loc[:, targetCol]




    print("-"*10)

    print("CLeaning Complete. Displaying results...\n"
              "날짜 정제 과정 완료. 결과 표시: \n", date.loc[0:3])

    command = input("Is all data is preserved? (y for yes/n for no):\n"
                    "날짜 데이터가 잘 남아 있습니까? (예:y/아니요:n): ")

    if command == "y":

        data.loc[:, col] = date


        if not testDate is None:

            testData.loc[:, col] = testDate

        print("Saved. Closing Date Cleaning Protocol...\n적용 완료. 날짜 정제 과정을 완전 종료합니다.")

        return data, testData



    elif command == "n":

        print("The modification is not made.\n실제 데이터셋에 날짜 데이터 변경을 적용하지 않습니다.")



    else:

        data.loc[:, col] = date

        testData.loc[:, col] = testDate

        print("Wrong Command. Considerd as saving.Closing Date Cleaning Process...\n잘못된 입력. 저장하는 것으로 간주합니다. 날짜 정제 과정을 완전 종료합니다.")

        return data, testData




def dateDivider(data, testData):

    print("This function Divides date. Make sure to clean the date data with DataToGo.\n"
          "이 기능은 날짜의 년, 월, 일을 분리합니다. 하드코딩을 통해 이 기능을 사용하시는 분들은 이전에 DataToGo 고유 기능으로 날짜를 분리한 다음 진행하셔야 합니다.")

    print("Data Columns / 데이터 열 목록: \n", data.columns)

    if testData is None:

        div()


        targetCol = input("What is the name of date Column?: \n날짜 열의 이름이 무엇입니까?: ")

        dateFrame = data.loc[:, targetCol].str.split("/", expand=True)


        dateFrame = dateFrame.rename({0:"year", 1:"month", 2:"day"}, axis=1)

        dateFrame = dateFrame.reset_index()

        data = data.reset_index()

        data = pd.merge(dateFrame, data, on="index")

        data = data.drop("index", axis=1)

        print("-"*10)

        print("Date Divided. Displaying Results... \n 날짜 분리 완료. 결과를 송출합니다.")

        print(data.head())


        sdiv()

    else:

        targetCol = input("What is the name of date Column?: \n날짜 열의 이름이 무엇입니까?: ")

        dateFrame = data.loc[:, targetCol].str.split("/", expand=True)

        testDateFrame = data.loc[:, targetCol].str.split("/", expand=True)

        dateFrame = dateFrame.rename({0: "year", 1: "month", 2: "day"}, axis=1)

        dateFrame = dateFrame.reset_index()

        data = data.reset_index()

        data = pd.merge(dateFrame, data, on="index")

        data = data.drop("index", axis=1)

        testDateFrame = testDateFrame.rename({0: "year", 1: "month", 2: "day"}, axis=1)

        testDateFrame = testDateFrame.reset_index()

        testData = testData.reset_index()

        testData = pd.merge(testDateFrame, testData, on="index")

        testData = testData.drop("index", axis=1)

        print("-" * 10)

        print("Date Divided. Displaying Results... \n 날짜 분리 완료. 결과를 송출합니다:")

        print(data.head())

        print("Closing merge protocol... / 날짜 분리 과정 종료.")

    return data, testData





def boolMasking(data, testData):


    if testData is None:


        print("-"*10)

        print("This function Pulls out sub-dataset which has a element of your choice in certain column.\nFor example, if you only want data of red apples, you choose 'color' column and select 'red' element. May not suitable for continuous value.\n\n"
              "이 기능은 특정 열에서 지정된 원소를 가진 행만 추출한 데이터셋을 새로 만듭니다. \n 예를 들어, 붉은 사과의 데이터만 얻고 싶다면, '색깔' 열을 선택하고 '붉은색' 원소를 선택합니다. 소수점이 있는 수 등 연속적인 값에는 추천하지 않습니다.")

        print("Data Columns / 데이터 열 목록: \n", data.columns)

        columnName = input("Which column will you choose for standard?: \n어떤 열을 기준으로 추출하겠습니까?: ")

        print("Unique value of the column / 해당 열의 원소 종류: \n", data.loc[:, columnName].unique())

        condition = input("What element will you choose?: \n어떤 원소를 선택하시겠습니까?: ")

        data2 = data.loc[data.loc[:, columnName] == condition]

        print("Filtering complete. Displaying result... / 필터링 완료. 결과 송출중: \n")

        print(data2.head())

        print("Closing filtering protocol... / 필터링 과정 종료.")

        testData2 = None

    else:

        print("-" * 10)

        print(
            "This function Pulls out sub-dataset which has a element of your choice in certain column.\nFor example, if you only want data of red apples, you choose 'color' column and select 'red' element. May not suitable for continuous value.\n\n"
            "이 기능은 특정 열에서 지정된 원소를 가진 행만 추출한 데이터셋을 새로 만듭니다. \n 예를 들어, 붉은 사과의 데이터만 얻고 싶다면, '색깔' 열을 선택하고 '붉은색' 원소를 선택합니다. 소수점이 있는 수 등 연속적인 값에는 추천하지 않습니다.")

        print("Data Columns / 데이터 열 목록: \n", data.columns)

        columnName = input("Which column will you choose for standard?: \n어떤 열을 기준으로 추출하겠습니까?: ")

        print("Unique value of the column / 해당 열의 원소 종류: \n", data.loc[:, columnName].unique())

        condition = input("What element will you choose?: \n어떤 원소를 선택하시겠습니까?: ")

        data2 = data.loc[data.loc[:, columnName] == condition]

        testData2 = testData.loc[data.loc[:, columnName] == condition]

        print("Filtering complete. Displaying result... / 필터링 완료. 결과 송출중: \n")

        print(data2.head())

        print("Closing filtering protocol... / 필터링 과정 종료.")




    return data2, testData2


def backDoorBoolMasking(data, columnName, condition):


    data2 = data.loc[data.loc[:, columnName] == condition]


    return data2




def merge(data1, data2, tag1, tag2, testData1=None, testData2=None):
    print("Merging two dataset. If there is a column in each dataset with same name and different values, you may not recognize which one was which."
        "\n\n 두 데이터셋을 병합합니다. 만약 두 데이터셋에 같은 이름의 열이 한 쌍 이상 있으면 이후 구별을 못할 수 있습니다.")

    while True:


        print("Dataset Named %s: \n%s 이름의 데이터셋: \n"%(tag1, tag1), data1.columns)

        print("-"*10)

        print("Dataset Named %s: \n%s 이름의 데이터셋: \n"%(tag2, tag2), data2.columns)

        print("="*10)



        command = input("Are there at least one column in each dataset which has same name but not be used for merge? (y for yes/n for no): \n"
                        "두 데이터셋에 병합에 사용하지 않을 것이면서, 같은 이름을 가진 열이 하나 이상 존재합니까? (예:y,/아니요:n): ")

        if command == "y":

            col = input("What is the name of the column: \n"
                        "해당 열의 이름이 무엇입니까?: ")

            data1 = data1.rename({col: "%s %s"%(tag1, col)}, axis=1)
            data2 = data2.rename({col: "%s %s" %(tag2, col)}, axis=1)

            if not testData1 is None:
                testData1 = testData1.rename({col: "%s %s" % (tag1, col)}, axis=1)
                testData2 = testData2.rename({col: "%s %s" % (tag2, col)}, axis=1)

        elif command == "n":

            break


        else:

            print("Wrong Command. Enter again. \n잘못된 입력입니다. 다시 입력해 주세요.")

    print("=" * 10)

    print("Dataset Named %s: \n%s 이름의 데이터셋: \n" % (tag1, tag1), data1.columns)

    print("-" * 10)

    print("Dataset Named %s: \n%s 이름의 데이터셋: \n" % (tag2, tag2), data2.columns)

    print("=" * 10)

    on = input("Choose the common column for merging. Rows with same element of that column will be merged (if no common column, press enter): "
               "\n병합에 사용할 두 데이터셋의 공통 열을 선택하세요. 해당 열의 값이 같은 행끼리 병합됩니다 (공통 열이 없을 경우, 엔터를 누르세요): ")

    if on != "" and len(data1.iloc[:, 0]) == len(data2.iloc[:, 0]) and data1.index != data2.index:

        data11 = data1.reset_index()

        data22 = data2.reset_index()

        result = pd.merge(data11, data22, on="index")

        result = result.drop("index", axis=1)

        if not testData1 is None:
            testData11 = testData1.reset_index()

            testData22 = testData2.reset_index()

            result2 = pd.merge(testData11, testData22, on="index")

            result2 = result2.drop("index", axis=1)

    elif on != "" and len(data1.iloc[:, 0]) == len(data2.iloc[:, 0]) and data1.index == data2.index:

        result = pd.merge(data1, data2, left_index=True)

        if not testData1 is None:
            result2 = pd.merge(testData1, testData2, left_index=True)

    elif on is None and len(data1.iloc[:, 0]) != len(data2.iloc[:, 0]):

        print("Error. You Cannot merge two dataset (%s and %s) with different length when there is no common column. \n"
              "오류. 두 데이터셋의 %s와 %s의 길이가 다릅니다. 만약 두 데이터셋 사이에 공통된 열이 없을 경우 병합할 수 없습니다."%(tag1, tag2, tag1, tag2))

        return None


    else:

        result = pd.merge(data1, data2, on=on)

        if not testData1 is None:

            result2 = pd.merge(testData1, testData2, on=on)


    print("merge complete. Displaying result... / 병합 완료. 결과 송출중: \n")

    print(result.columns)
    print(result.head())

    print("Closing merge protocol... / 병합 과정 종료.")

    return result, result2


def reverse(data):


    print("Reversing row sequence.../행 순서 역순으로 변경중...")

    data = data.iloc[::-1]

    data = data.reset_index(drop=True)

    print("Data Revered.Displaying Result.../역순 변경 완료. 결과 송출중.")

    print(data.head())

    print("Closing Reverse Protocol.../역순 변경 과정 종료.")


    return data


def autoEncoder(data, model=None, scaler=None):



    if model is None:

        print("="*10)

        print(
            "Welcome to AutoEncoder Generation Protocol. This is one of the only Data Preprocessing that start with explaination.\n"
            "Autoencoder is well known as a unsupervised learning method using deep neural network. \n "
            "But also, the autoencoder could be used for getting rid of noises or highlight some hidden features to make machine learning more effective.\n"
            "That is what we are going to do now. \n"
            "This AutoEncoder is surpressed to work badly by its nature, but nevertheless it tries to recreate your data as good as possible.\n"
            "The result of that is a program that cannot recreate the data perfectly, but it knows the basic idea of how it looks like.\n"
            "This is similar to our brain. Because we cannot remember every cat faces we know, we instead have a good idea of what cats look like, not just some cats we know.\n"
            "Thus, the AutoEncoder is good at figuring out how your data supposed to look like, thus giving us some insight aobut how our individual row of data is different from 'normal'.\n"
            "This AutoEncoder Generation Protocol includes standard scaling.\n\n"
            "오토인코더 생성 프로토콜에 오신 걸 환영합니다. 이 과정은 비교적 난해하기 때문에 데이터 전처리 과정 중 거의 유일하게 설명과 함께 시작합니다.\n"
            "오토인코더는 심층신경망 기법 중 비지도학습의 한 예시로 유명합니다."
            " 그렇지만 한편으로는, 오토인코더는 데이터의 노이즈를 제거하거나 데이터에서 숨겨진 특성을 부각시켜 기계학습의 정확도를 더 높여줍니다."
            "\n이런 데이터 전처리 과정이 지금 우리가 체험해 볼 부분입니다.\n"
            " 이 오토인코더는 처음부터 제대로 작동 못하도록 설계된 후, 입력받은 여러분의 데이터를 열심히 재현하려고 노력합니다. \n"
            "그 결과, 이 오토인코더는 여러분의 데이터를 완벽히 재현할 수는 없지만, 대충 데이터가 어떠해야 하는지에 대한 기본적 개념을 가지게 됩니다.\n"
            "이런 특성은 우리의 두뇌하고 유사한데요, 우리가 인생에서 본 모든 고양이의 얼굴을 기억하고 있지 않기 때문에 오히려 새로운 고양이도 잘 알아보는 것이 하나의 예시라고 할 수 있겠습니다.\n"
            "그러므로, 오토인코더는 여러분들의 데이터가 어떻게 생겨야만 하는지를 잘 알고 있기에, 오토인코더가 잘 이해하지 못하는 부분을 집어낸 데이터는 여러분 데이터의 평균에서 벗어난 개성적인 모습을 더 잘 보여줍니다.\n"
            "이 오토인코더 생성 과정은 표준화 과정을 포함합니다.")
        print("=" * 10)
        if len(data.iloc[:, 0]) < 100 or len(data.iloc[0, :]) < 4:

            print("Warning. The data size is too small for the encoder to learn. You might have some errors or problems.\n"
                  "경고. 인코더가 학습할 데이터량이 너무 적습니다. 이후 문제가 발생할 수도 있습니다.")

        columnNum = len(data.iloc[0, :])

        print("-"*10)
        shrinkSize = float(input("This AutoEncoder works by shrinking the feature. How much times you want the features to shrink? \n "
                                 "If it shrinks too much or not enough, it could not catch important patterns (enter real number bigger than one): \n"
                                 "이 오토인코더는 열로 나타내어지는 특성의 개수를 강제로 줄임으로서 작동합니다. 너무 많이 축소되거나 너무 덜 축소되면 중요한 패턴을 놓칠 수 있습니다.\n"
                                 "몇 배로 수축하고 싶습니까? 1보다 큰 실수를 입력해주세요(예시: 1.3, 2.4, etc): "))
        print("-" * 10)
        deep = bool(input("This AutoEncoder could work as deep AutoEncoder. This is more good at finding tricky patterns, but needs time to get ready. \n"
                          "Do you want this AutoEncoder to be deep? (True for yes, False for no): \n"
                          "이 오코인코더는 딥 오토인코더로 작동할 수 있습니다. 딥 오토인코더는 더 복잡한 패턴을 잘 찾는 대신, 학습하는데 시간이 걸립니다. \n"
                          "딥 오토인코더를 원하시면 True를, 원하시지 않는다면 False를 입력해 주세요: "))
        print("-" * 10)
        if shrinkSize <= 1:
            print("Error. ShrinkSize should be bigger than 1. / 오류. 수축률은 1보다 커야 합니다.")

        print("AutoEncoder Generating.../오토인코더 생성중...")

        if deep:

            encoder = models.Sequential()
            encoder.add(layers.Dense(columnNum, activation='relu', input_shape=(columnNum,)))
            encoder.add(layers.Dense(int((columnNum * 2) / (shrinkSize + 1)), activation='relu'))
            encoder.add(layers.Dense(int(columnNum / shrinkSize), activation='relu'))
            encoder.add(layers.Dense(int((columnNum * 2) / (shrinkSize + 1)), activation='relu'))
            encoder.add(layers.Dense(columnNum, activation='sigmoid'))
            encoder.compile(optimizer='rmsprop',
                          loss='mse',
                          metrics=['mae'])

            ss = StandardScaler()


        else:

            encoder = models.Sequential()
            encoder.add(layers.Dense(columnNum, activation='relu', input_shape=(columnNum,)))
            encoder.add(layers.Dense(int(columnNum / shrinkSize), activation='relu'))
            encoder.add(layers.Dense(columnNum, activation='sigmoid'))
            encoder.compile(optimizer='rmsprop',
                          loss='mse',
                          metrics=['mae'])

            ss = StandardScaler()



        print("Start Learning. / 학습 시작.")





        data2 = ss.fit_transform(data)

        encoder.fit(data2, data2, batch_size=int(len(data.iloc[:, 0])/10), epochs=20)

        data2 = data2 - encoder.predict(data)

        return (encoder, ss, data2)

    else:

        data2 = scaler.transform(data)



        return (model, scaler, data2 - model.predict(data2))



def normalizing(data, model=None):

    if model is None:


        print("This function makes features of data more comparable. By making every data scaled same in size, "
              "this enables models to understand data more easily. \n\n"
              "이 기능은 데이터의 특징을 부각시키는 역할을 합니다. 모든 데이터가 같은 방식으로 조정되었기에, 모델이 각 특성(열)에 관계없이 모든 데이터를 동일하게 취급할 수 있게 됩니다.")


        mode = input("robust for normalizing by median and IQR / minmax for normalizing by mix and max value / stand for mean and standard deviation.\n\n어떤 기준으로 정규화할 예정입니까? \n (이상치가 있을 경우: robust / 최대를 1, 최소를 0으로 정규화할 경우: minmax / 평균과 표준편차를 기준으로 정규화할 경우: stand):")


        if mode == "robust":


            model = RobustScaler()

            data = model.fit_transform(data)

        elif mode == "minmax":

            model = MinMaxScaler()

            data = model.fit_transform(data)

        elif mode == "stand":

            model = StandardScaler()

            data = model.fit_transform(data)

        return (data, model)


    else:

        data = model.transform(data)


        return (data, model)


def oneHotEncoder(data, model=None):


    if model is None:


        print("This function makes non-numeric value to numeric value. This method is especially good for non-ordered catagorical data. \n For example, A+ and B- has order, but order of A and B alphabets are not important in many applications.\n\n"
              "이 기능은 숫자가 아닌 분류형 데이터를 숫자로 변환합니다. 이 방법은 서열이 없는 데이터에서 유용합니다. 예를 들어, 점수 A와 B는 서열 있지만, 알파벳에선 A와 B에 높낮이가 있다고 보긴 힘듭니다.")


        model = OneHotEncoder()

        data = model.fit_transform(data).toarray()

        return (data, model)

    else:

        data = model.transform(data).toarray()


        return (data, model)


def nanRemover(data):


    print("Searching for NaN or None Values... / NaN, None 등 결측치 검색 중...")

    for col in data.columns:

        print("="*10)

        if data.loc[:, col].isnull().values.any():

            dropData = data.loc[data.loc[:, col].isnull(), :]

            num = len(dropData.iloc[:, 0])

            print("Column '%s' has %d NaN or None Values. '%s' 열에 결측치 %d개가 발견되었습니다."%(col, num, col, num))

            vi.oneVarDistribution(col, data, "Distribution of %s"%col)

            print("Look at the graph, column, and the number of missing data and choose how will you take care of the missing values. \n"
                  "열의 특성, 그래프와 결측치 개수를 보고 어떻게 결측치를 처리할 것인지 결정하세요.")

            while True:

                print("-"*10)

                command = input("delrow for deleting Row / delcol for deleting Column / mean for filling with mean value / \n / mode for filling with mode / median for filling with median value:\n"
                                "결측치 행 삭제는 delrow / 결측치가 존재하는 열 삭제는 delcol / 평균값으로 채우려면 mean / 최빈값으로 채우려면 mode / 중앙값으로 채우려면 median: ")


                if command == "delrow":

                    data = data.loc[(~data.loc[:, col].isnull()), :]

                    print(data)

                    break



                elif command == "delcol":

                    data = data.drop(col, axis=1)

                    break


                elif command == "mean":

                    data.loc[:, col] = data.loc[:, col].fillna(data.loc[:, col].mean())

                    print("Filled with Mean / 평균값으로 채워짐")
                    print(data.loc[:, col])

                    break


                elif command == "mode":


                    print("Modes of data / 데이터의 최빈값 목록: ")
                    print(data.loc[:, col].mode())

                    index = int(input("최빈값으로 설정할 값은 위에서 몇 번째입니까?: "))

                    mode = data.loc[:, col].mode().iloc[index-1]

                    data.loc[:, col] = data.loc[:, col].fillna(mode)

                    print("Filled with Mode value %s / 최빈값 %s 으로 채워짐"%(str(mode), str(mode)))
                    print(data.loc[:, col])

                    break

                elif command == "median":

                    data.loc[:, col] = data.loc[:, col].fillna(data.loc[:, col].median())

                    print("Filled with Median / 중앙값으로 채워짐")
                    print(data.loc[:, col])

                    break


                else:

                    print("Wrong command / 잘못된 입력")

        else:

            continue


    print("Searching for missing Data... / 잔여 결측치 검사 중.")

    if data.isnull().values.any():

        print("Fatal Error 011. Contact schialab from Github. \n 시스템 오류 011. 카카오톡 채널 cailhelp 혹은"
                "Github schialab에 문의하십시오.")


    else:

        return data



def colDelete(data, testData):


    while True:

        print(data.columns)

        sdiv()

        colName = input("Deleting Column Name (If finished, Press Enter) / 제거하는 열 이름 (완료 시 엔터): ")

        if colName != "":

            data.drop(colName, axis=1)

            if not testData is None:
                testData.drop(colName, axis=1)

        else:

            break

        div()

    return data, testData




def colCalculation(data, testData):


    while True:

        print(data.columns)

        sdiv()

        colName1 = input("1st Column Name for Operation (To exit, Press Enter) / 연산하는 첫 번째 열 이름 (멈추려면 엔터): ")

        if colName1 != "":

            colName2 = input("2nd Column Name for Operation / 연산하는 두 번째 열 이름: ")

            mode = input("What operation? Choose from +,-,*(multiplication),/(division) / 연산을 선택하세요 +,-,*,/: ")

            colName = input("Name for new column / 연산 결과인 열의 이름: ")

            if mode == "+":

                data[colName] = data.loc[:, colName1] + data.loc[:, colName2]

                if not testData is None:

                    testData[colName] = testData.loc[:, colName1] + testData.loc[:, colName2]

            elif mode == "-":

                data[colName] = data.loc[:, colName1] - data.loc[:, colName2]

                if not testData is None:
                    testData[colName] = testData.loc[:, colName1] - testData.loc[:, colName2]

            elif mode == "*":

                data[colName] = data.loc[:, colName1] * data.loc[:, colName2]

                if not testData is None:


                    testData[colName] = testData.loc[:, colName1] * testData.loc[:, colName2]

            elif mode == "/":

                print("Warning. After this operation, check whether there is a missing value. \n"
                      "경고. 이 작업 후 결측치가 있는지 확인하십시오.")


                data[colName] = data.loc[:, colName1] / data.loc[:, colName2]

                if not testData is None:

                    testData[colName] = testData.loc[:, colName1] / testData.loc[:, colName2]



            else:

                print("Wrong Input. Restart Protocol / 잘못된 입력. 연산 프로토콜을 재시작합니다.")

                break

        else:

            break

        div()

    return data, testData


def colbyNumCalculation(data, testData):


    while True:

        print(data.columns)

        sdiv()

        colName1 = input("1st Column Name for Operation (If finished, Press Enter) / 연산하는 열 이름: ")

        if colName1 != "":

            number = float(input("Number for Operation / 연산하는 수의 값: "))

            mode = input("What operation? Choose from +,-,*(multiplication),/(division) / 연산을 선택하세요 +,-,*,/: ")

            colName = input("Name for new column / 연산 결과인 열의 이름: ")

            if mode == "+":

                data[colName] = data.loc[:, colName1] + number

                if not testData is None:
                    testData[colName] = testData.loc[:, colName1] + number

            elif mode == "-":

                data[colName] = data.loc[:, colName1] - number

                if not testData is None:
                    testData[colName] = testData.loc[:, colName1] - number

            elif mode == "*":

                data[colName] = data.loc[:, colName1] * number

                if not testData is None:
                    testData[colName] = testData.loc[:, colName1] * number

            elif mode == "/":

                if number == 0:

                    print("It is impossible to divide something with zero / 영으로 나누는 것은 불가능합니다.")

                    continue


                data[colName] = data.loc[:, colName1] / number

                if not testData is None:

                    testData[colName] = testData.loc[:, colName1] / number



            else:

                print("Wrong Input. Restart Protocol / 잘못된 입력. 연산 프로토콜을 재시작합니다.")

                continue

        else:

            break

        div()

    return data, testData

def labeling(data, value, labelName):

    data[labelName] = value

    return data

def hardIndexing(data, testData):


    colList = []

    rowList = []

    colAll = False

    rowAll = False



    while True:

        print("Data Column List / 데이터 열 목록: ")
        print(data.columns)

        col = input("Type a Column name to select (Press Enter to Exit, Space and Enter to Select All)  \n"
                    "열의 이름을 입력하여 선택하세요 (엔터로 종료, 스페이스 + 엔터로 전체 선택): ")

        if col == "":

            break

        elif col == " ":

            colAll = True

            break

        colList.append(col)
        sdiv()

        print("Selected Columns / 선택된 열 목록:")

        print(colList)

        div()

    while True:

        print("Data Row List / 데이터 행 목록: ")
        print(data.index)

        row = input("Type a row name to select (Press Enter to Exit, Space and Enter to Select All) \n"
                    "행의 이름을 입력하여 선택하세요 (엔터로 종료, 스페이스 + 엔터로 전체 선택): ")

        if row == "":

            break

        elif row == " ":

            rowAll = True

            break


        rowList.append(row)
        sdiv()

        print("Selected Rows / 선택된 행 목록:")

        print(rowList)

        div()

    if not (colAll or rowAll):

        data = data.loc[rowList, colList]

        if not testData is None:

            testData = testData.loc[rowList, colList]

    elif colAll:

        data = data.loc[rowList, :]

        if not testData is None:

            testData = testData.loc[rowList, :]

    elif rowAll:

        data = data.loc[:, colList]

        if not testData is None:

            testData = testData.loc[:, colList]


    return data, testData


def groupBy(data, testData):


    sdiv()

    colList = []

    while True:

        print("column list / 열 목록")
        print(data.columns)

        col = input("Grouping column name (Enter to Exit) / 그룹으로 모을 때 기준이 될 칼럼 이름 (엔터로 나가기): ")

        if col != "":

            colList.append(col)

        else:

            break

    sdiv()
    command = input("me for mean of the group / std for standard deviation / co for count: \n"
                    "그룹의 평균은 me / 그룹의 표준편차는 std / 그룹 내 원소 개수는 co: ")

    if command == "me":

        data = data.groupby(by=colList).mean()

        try:
            testData = testData.groupby(by=colList).mean()

        except:

            testData = None

    elif command == "std":

        data = data.groupby(by=colList).std()

        try:
            testData = testData.groupby(by=colList).std()

        except:

            testData = None

    elif command == "co":

        data = data.groupby(by=colList).count()

        try:
            testData = testData.groupby(by=colList).count()

        except:

            testData = None

    return data, testData



def conditionColIndexing(data, testData):

    print("In development...")

    return None

def setColIndexing(data, testData):

    print("In development...")

    return None

def resetIndex(data, testData):

    print("In development...")

    return None

def pca(data, model=None):

    if model is None:

        print("PCA is a tool to lower the dimension of high dimensional data. It may not be the best tool for feature extraction, but it gives some insight about the data.\n"
              "PCA는 고차원 데이터를 저차원 데이터로 낮추는 역할을 합니다. 항상 좋은 선택지인 것은 아니지만, 데이터에 대한 다양한 통찰을 주는 흥미로운 기능입니다.")

        n = int(input("Type in the number of column you want to extract (only natural number) / 전체 데이터셋에서 남기고 싶은 열의 개수를 입력하세요 (자연수만 가능): "))

        model = PCA(n_components=n)

        data = model.fit_transform(data)

        print("")

    else:

        data = model.transform(data)



    return data, model
