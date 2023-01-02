data = [100,20,30,40,50,60] # 0....10

idx = int( input("Enter an index : ") )
# val = int( input("Enter an value : ") )

# value in list


####### sample 1 ###########
# if val in data:
#     print("Yes.")
# else:
#     print("No!")
#
# ####### sample 2 ##########
#  
# if idx >=0 and idx < len(data):
#     print("Yes.")
# else:
#     print("No!")

######### sample 3 ###########
# index within list range

if idx in range( len(data) ):
    print("Yes.")
else:
    print("No!")
