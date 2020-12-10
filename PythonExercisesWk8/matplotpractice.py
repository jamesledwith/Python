# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 22:01:26 2020

@author: James
"""
import matplotlib.pyplot as plt
import math

# create an empty dictionary
data_by_gender = {}

# create empty lists 
gender_list = []
gender_list_male = []
gender_list_female = []
tenure_list = []
phone_services_list = []
internet_service_list = []
contract_list = []
monthly_costs_list = []
total_charges_list = []
churns_list = []


#open the file
with open ("Customer_Churn.csv") as file_in:
    header_values = file_in.readline()
    for line in file_in:
        #split each line up and into variables seperated by a comma
        gender,tenure,phone_service,internet_service,contract,monthly_costs,total_charges,churn = line.split(",")
        #remove the blank spaces '\n'  
        line = line.strip()
        
        tenure = int(tenure)
        gender = str(gender)
        
        # add the values in the dataset to their respective lists
        gender_list.append(gender)
        tenure_list.append(tenure)
        phone_services_list.append(phone_service)
        internet_service_list.append(internet_service)
        contract_list.append(contract)
        monthly_costs_list.append(monthly_costs)
        total_charges_list.append(total_charges)
        churns_list.append(churn)
        for word in gender_list:
            if gender == "male":
                gender_list_male.append(word)
            else:
                gender_list_female.append(word)
                
      
                             
        # Create the figure and axes
        fig, ax = plt.subplots()
        
        # Set the title
        ax.set_title("Male and Female")
        
        # set the axis labels
        ax.set_xlabel("Gender")
        ax.set_ylabel("Total Amount")
    
        # set the ticks on the x-axis
        ax.set_xticks(range(0,101,10))
    
        # create a list for the grade boundaries
        grades = [0,40,50,60,70,100]       
        
        # draw a histogram
        ax.hist(gender_list_female, ec="black")    
        
        # show the plot
        plt.show()
        
        # Save the figure (bbox = "tight" eliminates whitespace padding)
        fig.savefig("marks_histogram.png", bbox_inches="tight")


# =============================================================================
#             # if this is the first occurence of this state
#             if gender == "Female":
#                 data_by_gender[gender] += gender
#             else:
#                 data_by_gender[gender] += gender
#                 
# =============================================================================
# =============================================================================
#             
#             if not gender in data_by_gender:
#                 data_by_gender[gender] = gender
#             # otherwise add to the existing value
#             else:
#                 data_by_gender[gender] += gender
#             
#             dictionary_length = len(data_by_gender)
#             print(dictionary_length)
# =============================================================================
# =============================================================================
#             
#             # create a figure and an axis object
#             fig, ax = plt.subplots()
#             
#             # set the title
#             ax.set_title("Gender Piechart")
#             
#             # do a pie chart
#             ax.pie(data_by_gender.values(), labels = data_by_gender.keys(),autopct="%.0f%%")
#             plt.show()
#             
#             # save the file
#             fig.savefig('gender_pie_chart.png', bbox_inches='tight')
# =============================================================================
            
            
# =============================================================================
#         tenure_list.sort()
#         # create the figure and axes
#         fig, ax = plt.subplots()
#         
#         # set the title
#         ax.set_title("Tenure list")
#         
#         # set the axis labels
#         ax.set_xlabel("Number of people")
#         ax.set_ylabel("Number of months")
#         
#         #ax.pie()
#         #plot the values
#         ax.plot(tenure_list)
#         
#         #show the plot
#         plt.show()
#         
#         #save the plot and eleminate as much whitespace as possible
#         fig.savefig("firstPlot.png", bbox_inches="tight")
# =============================================================================
     
        
     
        
     
        
     
        
     
        
     
        
     
        
     
# =============================================================================
#         
#         # min, max and sum
#         tenure_max = max(tenure_list)
#         tenure_min = min(tenure_list)
#         tenure_mean = sum(tenure_list) / len(tenure_list)
#     
#         #median of tenure
#         tenure_list.sort()
#         mid_index = int(len(tenure_list)/2)   
#         if len(tenure_list) % 2 == 1:
#             median = tenure_list[mid_index]
#         else:
#             median = tenure_list(tenure_list[mid_index -1 ] + tenure_list[mid_index + 1])/2
#     
#         #mode of tenure   
#         cnt = [] 
#         #count the frequency of each number in the list
#         for num in tenure_list:
#             cnt.append(tenure_list.count(num))
#         #make a distinct list of values
#         unique_count = []  
#         for num in cnt:
#             if num not in unique_count:
#                 unique_count.append(num)  
#         #find the highest frequency number in the list
#         mode = unique_count.index(max(unique_count))
#    
#         #standard deviation of tenure
#         #calculate variance for standard deviation
#         var = sum(pow(num - tenure_mean, 2) for num in tenure_list) / len(tenure_list)
#         standard_deviation = math.sqrt(var)
#          
#         #calculate (median skewness)
#         median_skewness = 3 * (tenure_mean - median) / standard_deviation
#         
#         #calculate (mode skewness)
#         mode_skewness = (tenure_mean - mode) / standard_deviation
#          
#         while True:
#             #Menu with choices
#             choice = int(input("Calculate the following: \n 1:Max \n 2:Min \n 3:Mean \n 4:Median \n 5:Mode \n 6:Standard Deviation \n 7:Median Skew \n 8:Mode Skew \n 9:Quit \n"))
#             if choice == 9:
#                 break
#             elif choice == 1:
#                 print(f"The maximum tenure is {tenure_max} months")
#             elif choice == 2:
#                 print(f"The minimum tenure is {tenure_min} months")
#             elif choice == 3:
#                 print(f"The mean tenure is {tenure_mean:0.2f} months")
#             elif choice == 4:
#                 print(f"The median of tenure is {median} months")
#             elif choice == 5:
#                 print(f"The mode of tenure is {mode}")
#             elif choice == 6:
#                 print(f"The standard deviation of tenure is {standard_deviation:0.2f}")
#             elif choice == 7:
#                 print(f"The median skew of tenure is {median_skewness:0.2f}") 
#             elif choice == 8:
#                 print(f"The mode skew of tenure is {mode_skewness:0.2f}")
#             else:
#                 print("Please enter a correct value")
#       
# except FileNotFoundError:
#     print("Error Customer_Churn.csv does not exist")  
#     
# # outputed the results to an external file
# try:
#     with open("FileOutput.txt", "w") as output:
#         output.write("The maximum tenure is: " + str(tenure_max) + "\n")
#         output.write("The minimum tenure is: " + str(tenure_min) + "\n")
#         output.write(f"The mean tenure is: {tenure_mean:0.2f} \n")
#         output.write("The median tenure is: " + str(median) + "\n")
#         output.write("The mode tenure is: " + str(mode) + "\n")
#         output.write("The standard deviation is: " + str(standard_deviation) + "\n")
#         output.write("The median skew is: " + str(median_skewness) + "\n")
#         output.write("The mode skew is: " + str(mode_skewness) + "\n")
# except FileNotFoundError:
#     print("Error FileOutput.txt does not exist")
# =============================================================================