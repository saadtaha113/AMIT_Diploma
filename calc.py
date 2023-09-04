def inputs_user():
    '''' this functio is for taking from user two inputs and operation type 
    context = {
        "first_user_input",
        "seconed_user_input"
        "opertion_type"
        }
    '''
    first_input = int(input('plz enter the big  no='))
    seconed_input = int(input('plz enter the small no='))
    operation_type= input('select the type of the operation "add" "sub" "multi" "div" =')
    context = {
        "first_user_input":first_input,
        "seconed_user_input":seconed_input,
        "opertion_type":operation_type
        }
    return context
# #  3 from operation ttypes and finsh to fish 
# def add(a,b):
#     return a+b
data_from_user = inputs_user()
while data_from_user['opertion_type'] != "finsh":
    print(data_from_user['opertion_type'])
    if data_from_user['opertion_type'] =='add':
        print(data_from_user['first_user_input']+data_from_user['seconed_user_input'])
    elif data_from_user['opertion_type'] =='sub':
        print(data_from_user['first_user_input']-data_from_user['seconed_user_input'])
    elif data_from_user['opertion_type'] =='multi':
        print(data_from_user['first_user_input']*data_from_user['seconed_user_input'])
    elif data_from_user['opertion_type'] =='div':
        print(data_from_user['first_user_input']/data_from_user['seconed_user_input'])
        
    data_from_user = inputs_user()

    

