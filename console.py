import sys


#Do not modify the script.

lid = None

ver = "0.0.4"


questionNumDict = {"main":1}

questionDict = {1: ["어떤 기능을 사용하실 것입니까? \n 데이터 시각화는 dv, 기계학습은 ml를 눌러주세요: ", "What function do you want to use? \n dv for Data Visualization \n ml for Machine Learning: "]
                }

answerDict = {1: ["dv", "ml"]}

def div():

    print("="*10)

def sdiv():

    print("-"*10)







def commandReader(questionListNum, languageID):

    commandCode = questionListNum * 100

    while True:

        command = input(questionDict[questionListNum][languageID])

        if command in answerDict[questionListNum]:

            for n in range(len(answerDict[questionListNum])):

                if command == answerDict[questionListNum][n]:

                    commandCode += n

                    return commandCode


                else:

                    continue

            print(
                "Fatal Error 001. Contact schialab from Github. \n 시스템 오류 001. 카카오톡 채널 cailhelp 혹은"
                "Github schialab에 문의하십시오.")

            sys.exit()





        else:

            print("Wrong input. Try again. \n잘못된 입력입니다. 주어진 선택지 중 하나를 택하여 다시 입력하십시오.")






def commandRun(commandCode, dataWareHouse):

    if commandCode == 100:

        vi.projectRun(lid, dataWareHouse)




    elif commandCode == 101:


        mlf.projectRun(lid, dataWareHouse)







while True:

    command = input("What Language you are most comfortable? e for English \n"
                "어떤 언어의 사용이 가장 편하신가요? 한국어를 선택하실려면 k를 입력해 주세요: ")


    if command == "e":

        lid = 1

        break

    elif command == "k":

        lid = 0

        break


    else:

        print("Wrong input. Try again. \n잘못된 입력입니다. 주어진 선택지 중 하나를 택하여 다시 입력하십시오.")


print("Program initiate. DataToGo VER %s \n프로그램 시동. DataToGo VER %s"%(ver, ver))


import GALOIS as gal
import customModeling as cm
import DataPreprocessing as dp
import MachineLearningFramework as mlf
import Visualizer as vi
import SchiaModels as sm
import GALOIS as g
import StatisticsAnalysis as sa





print("Program files imported. initiation complete. \n프로그램 파일 가져오기 성공. 프로그램 시동 성공.")

mainData = dp.DataWareHouse(dp.fileGathering())



while True:

    data = None

    testData = None


    print("Data Preprocessing Sequence \n 데이터 전처리 과정 실행")


    dp.dataPreprocessingInterface(mainData)






    commandRun(commandReader(1, lid), mainData)


    command2 = input("'exit' to Exit Program. Enter to continue using. / exit를 입력해 프로그램을 종료하십시오. 기존 데이터로 계속 진행하려면 엔터를 누르세요.")


    if command2 == "exit":

        break

