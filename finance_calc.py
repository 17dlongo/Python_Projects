money = 0
#gpy = int(input("What percentage gain is made every year"))*.01
#salery = int(input("Enter your average salery"))
#save = int(input("What percetage do you save every year"))*.01
#rint(save)
salery = 1000000
save = .9
def calc(salery,money,save):
    for gain in range(2,3):
        gpy = gain*.01
        print(gpy)
        money = 0
        mwo = 0
        for i in range(0,50):
            money += save*salery
            mwo += save*salery
            money *= gpy+1
            money = int(money)
            print("Income per year",money*gpy)
            print("year",i,"money with",money,"money without",mwo,"difference",money-mwo)

calc(salery,money,save)
