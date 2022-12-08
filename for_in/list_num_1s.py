from os import system



system("cls")


# list / array / vector
data = [ -10, 0, 5, 10, -15, 20, 0]
#

# 1. len
print( f"the data has {len(data)} values" )

# 2. set zeros in the second half
# half_idx = round(len(data) / 2)
# print(half_idx)

# for i in range(half_idx,len(data)):
#     data[i] = 0
max_dat = max(data)
min_dat = min(data)

half_idx = int(len(data) / 2)
print(half_idx)

#+ HW : do the same but for the left half
for i in range(0,half_idx):
    data[i] = 0

print(data)
    
print("Max data from array ",max_dat)    
print("Minim data from array ",min_dat)    

# # 3. swaping
# # HW : input indexes of values from keyboard
# free = data[1]
# data[1] = data[4]
# data[4] = free
#change_first = int(input("Change data value"))
data_ = [1, 2, 3, 4, 5, 6, 7, 8]
#### first change value index
free_first = data_[1]
data_[1] = data_[5]
data_[5] = free_first
#### second change value idex
free_second = data_[2]
data_[2] = data_[6]
data_[6] = free_second

for i in data_:
    i
        
print(data_)



# # media datas
# mv = 0
# for i in range(len(data)):
#     mv += data[i]

# mv /= len(data) 
# # onother ex short:
# mv = sum(data) / len(data) 
# # + HW : find the max/min values and print  

# # Found index in list
# val = 10
# found_idx = -1
# for i in range(len(data)):
#     if val == data[i]:
#         found_idx = i
#         break
# """
# found_idx = data.index(val)  # found fast
# """    
# print(f"value {val} found on {found_idx}")    

# print(data)
# print(mv)