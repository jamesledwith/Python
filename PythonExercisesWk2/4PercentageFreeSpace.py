#This program checks the percentage of disk space left and prints an apropiate response 


total_space = float(input("Enter total space: "))

amount_used = float(input("Enter amount used: "))

free_space_percent = 100 - (amount_used / total_space * 100);

print(f"The percentage of free space is {free_space_percent:.1f}%") 

if(amount_used > total_space):
    print("Input data is Invalid")
elif(total_space == amount_used):
    print("Warning: System full")
elif(5 <= free_space_percent < 100):
    print("System has sufficient disk space")
elif(0 <= free_space_percent < 5 ):
    print("Warning, low disk space")







