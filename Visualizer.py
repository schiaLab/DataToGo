import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager,rc

from pandas.api.types import is_numeric_dtype
def div():

    print("="*10)


def sdiv():

    print("-"*10)


functionNumDict = {"ovd":1, "tvd":2, "ovl":3, "nvl":3 , "tvs":4, "avp":5, "avn":6, }

instructionDict = {
    1: ["이 도표는 여러분의 데이터셋의 한 가지 특성(열)의 분포를 알아봅니다. \n 예를 들면, 운동기록에서 각 요일에 얼마나 운동을 했는지 센 다음, 그것을 막대그래프로 보여줍니다. 그러면 어느 요일에 가장 많이 운동을 했는지 등을 알 수 있지요.\n 필요할 경우 다른 특성을 기준으로 데이터를 나눈 후, 각각의 데이터에 대한 분포 그래프를 겹쳐서 볼 수도 있습니다.",
        "This figure helps you to look over the distribution of a feature, or a column.\n For example, from your exercise data, you can see the distribution in the aspect of data of the week. Then, you might know which day you exercise most.\n You can categorize the data with another column "
        "and draw multiple graphs in one figure."],
2:["이 도표는 여러분의 데이터셋의 두 가지 특성(열)의 분포를 알아봅니다. \n 예를 들면, 휴양지의 기온하고 휴양지의 교통량을 각각 x축, y축으로 놓으면 더운 여름과 추운 겨울날, 즉 성수기 때 교툥량이 많이 분포할 수도 있을 것입니다.\n 필요할 경우 다른 특성을 기준으로 데이터를 나눈 후, 각각의 데이터에 대한 분포 그래프를 겹쳐서 볼 수도 있습니다. \n "
   "이 도표는 얼마나 많이 분포해 있는가를 2차원으로 확인해야 하기에, 밀집도를 나타나는 등고선이나 색깔을 통해 얼마나 밀집되어 있는지를 확인할 수 있습니다.",
   "This figure helps you to look over the distribution of two features, or a column. \n For example, by putting temperature as X axis and Traffic as Y axis in some vacation spot, you might find that people get into a traffic jam in those areas when it's too cold or too warm.\n You can categorize the data with another column "
        "and draw multiple graphs in one figure. \n Because the figure should show you how much dense is the spot, it might use contours or colors to represent the density."] ,
    3:["이 도표는 시간이나 특정 순서에 따라 값이 어떻게 변화하는지 알아봅니다. \n 예를 들면, 매주 소비금액 데이터를 시간별로 나열하면, 시간에 따라 소비금액이 늘어나는지, 반복되는 주기 등 눈여겨볼만한 패턴은 없는지 등 다양한 점들을 생각해 볼 수 있습니다. \n 여러 개의 열의 데이터를 한 번에 겹쳐서 볼 수도 있습니다.",
       "This figure helps you to understand data in the aspect of time or sequence. \nFor example, if you have a data of your spending record, by putting them in order of time,\n you might see trends like steadily growth of spending, or stunted spending amount right before your allowance or pay day.\n You can overlap many columns into one figure."],
    4: [
        "이 도표는 두 변수 간의 관계를 점들로 나타냅니다. \n 예를 들어, 키를 세로 좌표, 몸무게를 가로 좌표로 한 다음 각 사람마다 점을 찍으면, 대략적으로 키가 커지면 몸무게도 대략적으로 커지는 관계를 볼 수도 있습니다. \n 이 도표에서는 자동으로 두 변수 간의 선형 관계를 직선으로 그려줍니다.",
        "This figure help you to get a idea of two variable's relationship. \nFor example, if you put in the data of the hight and weight of people,\n you might see that when a person is tall, generally that person is heavier than other shorter people\n The figure autometically shows a linear relationship between two variable."],
    5: [
        "이 도표는 데이터 내의 가능한 모든 쌍의 열 간 피어슨 상관계수를 색깔로 보여줍니다. \n 예를 들어, 마트에서 각 소비자가 산 양파와 카레, 냉면 육수와 냉면 사리의 개수의 데이터를 가지고 있으면, 이 도표는 가능한 모든 쌍의 경우에서 데이터의 상관관계를 보여줍니다. \n 이 사례에선 카레에 양파를 넣으므로 카레와 양파 간의 상관계수는 높아 밝은 색일 것이고, 반면 카레와 냉면육수는 보통 같이 사지 않으므로 색깔이 짙을 것입니다.",
        "This figure shows Pearson correlation codefficient for every possible combination of pairs of columns by color. \nFor example, if you have a data of customer buying groceries, you might see brigther color for milk and cereals, because most people by them together."],
    6: [
        "이 도표는 기존 데이터셋에 있는 숫자값을 색깔로 나타냅니다. \n 예를 들어, 학생 성적 데이터가 있다면, 이 도표에서는 수학을 못하고 과학을 잘하는 철수의 수학 성적이 과학 성적보다 짙은 색깔로 나타날 것입니다. \n 데이터를 더욱 쉽게 이해하기 위해, 기존 데이터셋에 행 이름이 있는 것을 추천합니다.",
        "This figure help you to see the value of data as color. \n For example, if you have a data of scores for each student at midterm, science nerd sam's science score will show brighter than other student's science score. \n It will be more useful if there is row index for your dataset, not just numbers."]

}

questionDict = {
    1: [["분포를 알고 싶은 특성(열)의 이름이 무엇입니까?: ", "그래프의 이름을 무엇으로 지정하고 싶습니까?: ", "또 다른 열을 기준으로 데이터를 분류하여 다른 색깔의 그래프를 여러 겹 그릴 수 있습니다. 필요하면 열의 이름을 입력하고, 필요없으면 enter를 눌러주세요: "],
        ["What is the name of the feature(column)?: ", "What is the name of the figure?: ", "You can add more graphs according to another column with different colors.\n If needed, enter the name of the column. If not, just press enter: "]],
    2: [["분포를 알고 싶은 한 특성(열)의 이름이 무엇입니까?(x축): ", "분포를 알고 싶은 나머지 특성(열)의 이름이 무엇입니까?(y축): ",
         "그래프의 이름을 무엇으로 지정하고 싶습니까?: ", "또 다른 열을 기준으로 데이터를 분류하여 다른 색깔의 그래프를 여러 겹 그릴 수 있습니다. 필요하면 열의 이름을 입력하고, 필요없으면 enter를 눌러주세요: ", "계단처럼 분리되어 있는 밀집도 표현을 원하시면 normal, 부드럽게 색깔이 연결된 밀집도 표현을 원하시면 smooth를 입력해 주세요: " ,
         "등고선이 필요하면 False, 색깔이 필요하면 True를 입력해 주세요: "],
        ["What is the name of one of the features(column)?(for x axis): ", "What is the name of the other feature(column)?(for y axis): ", "What is the name of the figure?: ",
         "You can add more graphs according to another column with different colors. \n If needed, enter the name of the column. If not, just press enter: ", "To represent density in a stair(contour-like) format, type normal.\n"
                                                                                                                                                           "To represent density in continuous-color format, type smooth: ",
         "For contour, type False. For color, type True: "
         ]],

    3: [["그래프의 제목을 무엇으로 하고 싶습니까?: "],["What is the name of the figure?: "]],

4: [["관계성을 알고 싶은 한 특성(열)의 이름이 무엇입니까?(x축): ", "관계성을 알고 싶은 나머지 특성(열)의 이름이 무엇입니까?(y축): ",
         "그래프의 이름을 무엇으로 지정하고 싶습니까?: ", "또 다른 열을 기준으로 데이터를 분류하여 다른 색깔의 그래프를 여러 겹 그릴 수 있습니다. 필요하면 열의 이름을 입력하고, 필요없으면 enter를 눌러주세요: "],
        ["What is the name of one of the features(column)?(for x axis): ", "What is the name of the other feature(column)?(for y axis): ", "What is the name of the figure?: ",
         "You can add more graphs according to another column with different colors. \n If needed, enter the name of the column. If not, just press enter: "
         ]],
5: [["그래프의 제목을 무엇으로 하고 싶습니까?: "],["What is the name of the figure?: "]],
6: [["그래프의 제목을 무엇으로 하고 싶습니까?: "],["What is the name of the figure?: "]]
}


def preparation():


    sns.set()

    font_path = 'assets/NanumBarunGothic.ttf'

    font_name = font_manager.FontProperties(fname=font_path).get_name()

    rc('font',family=font_name)





def oneVarDistribution(xName, data, title, catName = ""):


    if is_numeric_dtype(data.loc[:, xName]):

        if catName == "":

            preparation()


            sns.displot(data=data, x=xName)
            plt.title(title)
            plt.show()


        else:

            preparation()


            sns.displot(data=data, x=xName, hue=catName)
            plt.title(title)
            plt.show()

    else:


        if catName == "":

            preparation()

            sns.countplot(data=data, x=xName)
            plt.title(title)
            plt.show()



        else:

            preparation()

            sns.countplot(data=data, x=xName, hue=catName)
            plt.title(title)
            plt.show()




def twoVarDisribution(xName, yName, data, title, catName = "", type="normal", fill=False):

    if catName == "" and type == "normal":

        preparation()


        sns.kdeplot(
            data=data, x=xName, y=yName,
            fill=fill)
        plt.title(title)
        plt.show()




    elif catName != "" and type == "normal":

        preparation()

        sns.kdeplot(
            data=data, x=xName, y=yName, hue=catName,
            fill=fill)
        plt.title(title)
        plt.show()

    elif catName != "" and type == "smooth":

        preparation()


        sns.kdeplot(data=data, x=xName, y=yName, fill=True, thresh=0, levels=100, cmap="mako")
        plt.title(title)
        plt.show()



    else:

        print("Two or more smooth plot for each category is not supported.\n두 가지 이상의 카테고리에 대한 서로 다른 smooth plot을 겹치는 것은 불가능합니다.")



def timeSeries(data, title):

    columns = []

    while True:

        column = input("Column name for the figure (enter for stop): \n추가하고 싶은 열 이름 (종료할려면 엔터): ")

        if column == "":

            break

        else:

            columns.append(column)


    #cul = input("Cumulate the result? \n누적된 값의 그래프를 그리고자 합니까?")

    columnList = []

    for column in columns:

        columnList.append(data.loc[:, column])



    preparation()

    fig, ax = plt.subplots()

    for n in range(len(columnList)):

        ax.plot(columnList[n], label=columns[n])

    ax.legend()

    plt.title(title)

    plt.show()

def twoScatterPlot(data, xName, yName, title, catName=""):


    if catName == "":

        preparation()

        sns.lmplot(x=xName, y=yName, data=data)
        plt.title(title)
        plt.show()

    else:

        preparation()

        sns.regplot(x=xName, y=yName, data=data, hue=catName)
        plt.title(title)
        plt.show()

def pearsonHeatmap(data, title):

    data2 = data.corr(method='pearson')

    preparation()

    sns.heatmap(data2)
    plt.title(title)
    plt.show()

def heatmap(data, title):

    preparation()

    sns.heatmap(data)
    plt.title(title)
    plt.show()


def functionNumGenerator(lid):

    if lid == 0:

        print("데이터 시각화 부문에 오신 걸 환영합니다. 데이터를 시각화하는 방법은 참 다양하여 아쉽게도 모든 방법을 여기에 담진 못했습니다.\n 그러나, "
              "기초적인 분포도, 시계열 그래프, 산점도 등과 같은 데이터 시각화 방법들은 구현되어 있습니다. 자세한 설명은 교육영상을 참조해주시기 바랍니다. \n"
              " 3개의 특성간의 분포를 나타내는 등의 일반적이지 않은 방법은 지원하지 않으니 주의해 주시기 바랍니다.")

        var = input("분석할 특성(열)의 개수가 몇 개입니까? (1개:o / 2개:t /n개:n /전부:a (3개: 미개발. 지원예정)): ")

        while True:

            if var == "a":

                type = input("분석하고 특징이 무엇입니까? (피어슨 상관계수: p/ 열과 행에 따른 값의 크기(데이터가 모두 숫자여야만 가능): n): ")

                break

            elif var == "n":

                type = input("분석하고 싶은 2차원 차트 형태가 무엇입니까? (시계열:l): ")

                break

            elif var == "t":

                type = input("분석하고 싶은 2차원 차트 형태가 무엇입니까? (분포:d / 2차원 산점도:s): ")

                break

            elif var == "o":

                type = input("분석하고 싶은 2차원 차트 형태가 무엇입니까? (분포:d / 시계열:l): ")

                break

            else:

                print("잘못된 입력")

                continue



        return functionNumDict[var+"v"+type]


    else:

        print("Welcome to Data visualization section. Visualizing data is a quite extensive field. So unfortunately, I couldn't make every method possible.\n"
              "However I developed some basic tools like distribution plot, time series graph, and scatter plot. More methods will be added by upgrades.")

        var = input("How many features do you need for analysis? (one: o / two: t / all: a (three: working on it!)): ")

        while True:

            if var == "a":

                type = input("What attribute you want to know? (Pearson Correlation Coefficient: p/ normal value size (dataset should be all numbers): n): ")

                break

            elif var == "n":

                type = input("What type of figure do you need? (time series: l): ")

                break

            elif var == "t":

                type = input("What type of figure do you need? (distribution: d / scatter: s): ")

                break

            elif var == "o":

                type = input("What type of figure do you need? (distribution: d / time series: l): ")

                break

            else:

                print("Wrong Input")

                continue





        return functionNumDict[var + "v" + type]


def graphicalFunctionNumGenerator(lid):

    #In Development...

    if lid == 0:

        print("데이터 시각화 부문에 오신 걸 환영합니다. 데이터를 시각화하는 방법은 참 다양하여 아쉽게도 모든 방법을 여기에 담진 못했습니다.\n 그러나, "
              "기초적인 분포도, 시계열 그래프, 산점도 등과 같은 데이터 시각화 방법들은 구현되어 있습니다. 자세한 설명은 교육영상을 참조해주시기 바랍니다. \n"
              " 3개의 특성간의 분포를 나타내는 등의 일반적이지 않은 방법은 지원하지 않으니 주의해 주시기 바랍니다.")

        code = input("원하는 도표의 도표 제목을 입력해 주세요: ")

        return code


    else:

        print("Welcome to Data visualization section. Visualizing data is a quite extensive field. So unfortunately, I couldn't make every method possible.\n"
              "However I developed some basic tools like distribution plot, time series graph, and scatter plot. More methods will be added by upgrades.")

        code = input("Enter the title of the figure you want: ")

        return code






def instruction(functionNum, lid):

    print(instructionDict[functionNum][lid])


def questionCall(functionNum, lid):

    paraList = []

    for question in questionDict[functionNum][lid]:

        print("-"*10)

        paraList.append(input(question))

    return paraList




def autoRun(functionNum, data, paraList):

    if functionNum == 1:


        oneVarDistribution(xName=paraList[0], data=data, title=paraList[1], catName=paraList[2])


    elif functionNum == 2:

        twoVarDisribution(xName=paraList[0], yName=paraList[1], data=data, title=paraList[2], catName=paraList[3], type=paraList[4], fill=bool(paraList[5]))


    elif functionNum == 3:

        timeSeries(data=data, title=paraList[0])

    elif functionNum == 4:

        twoScatterPlot(data=data, xName=paraList[0], yName=paraList[1], title=paraList[2], catName=paraList[3])

    elif functionNum == 5:

        pearsonHeatmap(data=data, title=paraList[0])

    elif functionNum == 6:

        heatmap(data=data, title=paraList[0])

def projectRun(lid, dataWareHouse):


    div()

    print("List of tags / 태그 리스트")
    print(dataWareHouse.dataDict.keys())


    tag = input("Which data tag will you choose? (Enter to exit) / 선택하고자 하는 데이터의 태그를 입력하십시오 (엔터로 종료): ")

    data = dataWareHouse.dataDict[tag]





    print("selected data / 선택된 데이터: ")
    print(data.head())

    while True:

        try:

            functionNum = functionNumGenerator(lid)

            break
        except:

            print("잘못된 입력")

            continue



    instruction(functionNum, lid)

    print(data.columns)

    paraList = questionCall(functionNum, lid)

    autoRun(functionNum, data, paraList)

def backDoorOneVarPlot(data):

    preparation()

    plt.plot(data)

    plt.show()