import math

def Function(x):

    lbs = 16
    tons = 2000
    oz_in_ton = (2000 * 16)

    total_tons = 0
    total_lbs = 0

    total_tons = (x/oz_in_ton)
    total_tons = int(total_tons)

    x = x-(oz_in_ton * total_tons) 

    total_lbs = x/lbs
    total_lbs = int(total_lbs)

    x = x-(total_lbs*lbs)
    print('Tons: {}\nPounds: {}\nOunces {}'.format(total_tons, total_lbs, x))

#Function(32035)


#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places
def Func(A,B,C):
    A_Miles = 15.62
    B_Miles = 41.85
    C_Miles = 32.67

    total_miles_traveled = (A * A_Miles) + (B * B_Miles) + (C * C_Miles)
    
    total_miles_traveled = float("{0:.2f}".format(total_miles_traveled))

    print('Distance: {} miles'.format(total_miles_traveled))

def Func(A,B,C):
    A_Miles = 15.62
    B_Miles = 41.85
    C_Miles = 32.67

    total_miles_traveled = (A * A_Miles) + (B * B_Miles) + (C * C_Miles)
    
    total_miles_traveled = float("{0:.2f}".format(total_miles_traveled))

    print('Distance: {} miles'.format(total_miles_traveled))

#Func(1,2,3)


def area(x,y,z):

    A = 0

    A = ((x + y) / 2) * z

    A = float("{0:.1f}".format(A))

    print("Trapezoid area: {} square meters".format(A))

#area(3,4,5)

def sum(a,b,c,d,e):

    sum = a + b + c + d + e
    fSum = float("{0:.1f}".format(sum))
    stringSum = str(a) + str(b) + str(c) + str(d) + str(e)

    print("Integer: {}\nFloat: {}\nString: {} ".format(sum,fSum,stringSum))

#sum(1,3,6,2,7)

def pigToHuman(x):

    years = x * 5

    print("{} is {} in human Years".format(x,years))

#pigToHuman(8)

def factorialValue(x):
   
   fact = math.factorial(x)
   Boolean = False

   if fact > 100:
       Boolean = True
       

   print("{}\n{}".format(fact,Boolean))

#factorialValue(1)

def insertDash(x):
    x = str(x)
    newString = x[:3] + "-" + x[3:]
    
    newString =  newString[:6] + "-" + newString[6:]

    print(newString)

#insertDash(154175430)
    
#8
def waterState(x): 
    if x < 33:
        print("Frozen")
        print("Watch out for ice!")
    elif (x > 33) and (x < 80):
        print("Cold")
    elif (x > 80) and (x < 115):
        print("Warm")
    elif(x > 115) and (x < 211):
        print("Hot")
    else: 
        print("Boiling")

    if x == 212:
        print("Caution: Hot!")

#waterState(32)

#9        
def frameworks(x):
    frameworksList = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
    try:
        print(frameworksList[x])
    except:
        print("Error")

#frameworks(10)
#10
               
def stockPrice(x, *args):

    stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}
    total = 0

    for i in range(x):
        tick = args[i]
        total = total + stocks[tick] 

    print("Total Price: ${}" .format(total))

#stockPrice(3,'SOFI','AMZN','LVLU')

#11

def list(x):
    predef_list = [4, -27, 15, 33, -10]

    predef_list = sorted(predef_list)

    if x > predef_list[len(predef_list) -1]:
        print("Greater than max? {}".format(True))
    else:
        print("Greater than max? {}".format(False))

#list(100)
            
#12


def finalPrice(y,x):

    purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

    totalPrice = purchase[y] * x
    

    if x >= 10 and x <= 20:
        totalPrice = totalPrice - ((totalPrice * 5) /100)
    elif x > 20:
        totalPrice = totalPrice - ((totalPrice * 10) /100)

    totalPrice = float("{0:.2f}".format(totalPrice))

    print("{} ${}".format(y, totalPrice))

#finalPrice('cookies', 144)
    
#3
    
def dataType(x):

    various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

    data_type = type(various_data_types[x]).__name__

    print("Element {}: {}".format(x , data_type))
    
#dataType(4)

#12


def makeSentence(path):
    newString = "string"
    try:

        text =  open(path, 'r')
        i = 0

        for x in text:
            x = x.strip()
            x = x + " "
            if i < 1:
                newString = x
                i = 5
            else:
                newString = newString + x 

        text.close()

        #print(newString)

        f = open(path, "a")

        f.write("\n{}".format(newString))

        f.close()

        file = open(path, 'r')
        
        
        for i in file:
            print(i)
        

    except FileNotFoundError:

        print("Error: File {} not found.".format(path))
        
    
#makeSentence('C:/Users/madde/OneDrive/Desktop/wgu stuff/file.txt')


import csv

def read_csv_to_dicts(file_path):
    data = {'dict1': {}, 'dict2': {}}
    
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        
        headers = rows[0]
        values1 = rows[1]
        values2 = rows[2]
        
        for header, value1, value2 in zip(headers, values1, values2):
            data['dict1'][header] = value1
            data['dict2'][header] = value2
    
    return data

file_path = 'input1.csv'
result = read_csv_to_dicts('input2.csv')
print(result)