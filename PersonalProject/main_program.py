# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:49:37 2020

@author: James
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# Import the functions 
from calculations_functions import calc_mean, calc_sdv, calc_min, calc_max, calc_mode, calc_median_skewness, calc_median_skewness, convert_list_to_dictionary, calc_churn_rate, calc_median, calc_mode_skewness

# create an empty dictionary
data_by_gender = {}
data_by_tenure = {}
data_by_internet_service = {}
data_by_churn  = {}


#date format string
format_str = "%d/%m/%Y"

# create empty lists 
gender_list = []
tenure_list = []
phone_services_list = []
internet_service_list = []
contract_list = []
monthly_costs_list = []
total_charges_list = []
churns_list = []

date_list = []
confirmed_case_list = []
total_confirmed_list = []
confirmed_deaths_lists = []
total_deaths_list = []
datetime_list = []

try:
    #open the files
    with open ("Customer_Churn.csv") as file_in, open ("CovidDailyStatisticsProfile.csv") as file_in_c:
        header_values = file_in.readline()
        for line in file_in:
            #split each line up and into variables seperated by a comma
            gender,tenure,phone_service,internet_service,contract,monthly_costs,total_charges,churn = line.split(",")
            #remove the blank spaces '\n'  
            line = line.strip()
            
            #add the values in the dataset to their respective lists
            gender_list.append(gender)
            tenure_list.append(int(tenure))
            phone_services_list.append(phone_service)
            internet_service_list.append(internet_service)
            contract_list.append(contract)
            monthly_costs_list.append(float(monthly_costs))
            total_charges_list.append(total_charges)
            churns_list.append(churn)
            
            if not tenure in data_by_churn:
                data_by_churn[tenure] = churn
            #or else add it to the 
            else:
                data_by_churn[tenure] += churn
                
                #if this is the first month
            if not tenure in data_by_tenure:
                data_by_tenure[tenure] = int(tenure)
            # or else add it to the value
            else:
                data_by_tenure[tenure] += int(tenure)
    
     
        header_values = file_in_c.readline()
        for line in file_in_c:
            #split each line up and into variables seperated by a comma
            date, confirmed_covid_cases, total_confirmed_covid_cases, confirmed_covid_deaths, total_covid_deaths= line.split(",")
            #remove the blank spaces '\n'  
            line = line.strip()
            
            #add the values in the dataset to their respective lists
            date_list.append(date)
            confirmed_case_list.append(int(confirmed_covid_cases))
            total_confirmed_list.append(int(total_confirmed_covid_cases))
            confirmed_deaths_lists.append(int(confirmed_covid_deaths))
            total_deaths_list.append(int(total_covid_deaths))
            
            datetime_list.append(datetime.datetime.strptime(date, format_str))
            
    
    
    while True:
        main_choice = int(input("Choose your analysis: \n 1: Numbered Results \n 2: Visualise Data \n 3: Exit Program"))
        #Main menu with choices
        if main_choice == 3:
            break
        
        elif main_choice == 1:
            while True:
                choice = int(input("Calculate the following: \n 1:Max \n 2:Min \n 3:Mean \n 4:Median \n 5:Mode \n 6:Standard Deviation \n 7:Median Skew \n 8:Mode Skew \n 9:Churn Rate \n 10:Main Menu \n"))
                if choice == 10:
                    break
                
                # Calculate the maximum
                elif choice == 1:
                    max_choice = int(input("calculate the maximum for the folowing (1)Tenure (2)Monthly Charge (3)Main Menu"))
                    if max_choice == 1:    
                        print(f"The maximum tenure is, {calc_min(tenure_list):0.02f} months")          
                    elif max_choice == 2:    
                        print(f"The maximum monthly charge is, {calc_min(monthly_costs_list):0.02f} ")
                    elif max_choice == 3:    
                        break
                    else:
                        print("Please enter a correct value")
                
                # Calculate minimum menu
                elif choice == 2:
                    min_choice = int(input("calculate the minimum for the folowing (1)Tenure (2)Monthly Charge (3)Main Menu"))
                    if min_choice == 1:    
                        print(f"The minimum tenure is, {calc_min(tenure_list):0.02f} months")          
                    elif min_choice == 2:    
                        print(f"The minimum monthly charge is, {calc_min(monthly_costs_list):0.02f} ")
                    elif min_choice == 4:    
                        break
                    else:
                        print("Please enter a correct value")
                        
                # Calculate mean menu
                elif choice == 3:
                    mean_choice = int(input("calculate the mean for the folowing (1)Tenure (2)Monthly Charge (3)Main Menu"))
                    if mean_choice == 1:    
                        print(f"The mean tenure is, {calc_mean(tenure_list):0.02f} months")          
                    elif mean_choice == 2:    
                        print(f"The mean monthly charge  is, {calc_mean(monthly_costs_list):0.02f} ")
                    elif mean_choice == 3:    
                        break
                    else:
                        print("Please enter a correct value")  
                        
                # Calculate median menu
                elif choice == 4:
                    medians_choice = int(input("calculate the mean for the folowing (1)Tenure (2)Monthly Charge (3)Main Menu"))
                    if medians_choice == 1:    
                        print(f"The median tenure is, {calc_median(tenure_list):0.02f} months")          
                    elif medians_choice == 2:    
                        print(f"The median monthly charge  is, {calc_median(monthly_costs_list):0.02f} ")
                    elif medians_choice == 3:    
                        break
                    else:
                        print("Please enter a correct value")  
                        
                 # Calculate mode menu
                elif choice == 5:
                    mode_choice = int(input("calculate the mode for the folowing (1)Tenure (2)Monthly Charge (3)Main Menu"))
                    if mode_choice == 1:    
                        print(f"The median mode is, {calc_mode(tenure_list):0.02f} months")          
                    elif mode_choice == 2:    
                        print(f"The mode monthly charge  is, {calc_mode(monthly_costs_list):0.02f} ")
                    elif mode_choice == 3:    
                        break
                    else:
                        print("Please enter a correct value")
                
                # Calculate standard deviation menu
                elif choice == 6:
                    sdv_choice = int(input("calculate the standard deviation for the folowing (1)Tenure (2)Monthly Charge (3)Main Menu"))
                    if sdv_choice == 1:    
                        print(f"The standard deviation of tenure is, {calc_sdv(tenure_list):0.02f} months")          
                    elif sdv_choice == 2:    
                        print(f"The standard deviation of monthly charge  is, {calc_sdv(monthly_costs_list):0.02f} ")
                    elif sdv_choice == 3:    
                        break
                    else:
                        print("Please enter a correct value") 
                        
                # Calculate median skew menu
                elif choice == 7:
                    median_choice = int(input("calculate the median skew for the folowing (1)Tenure (2)Monthly Charge (3)Main Menu"))
                    if median_choice == 1:    
                        break
                         #print(f"The median skew of tenure is, {calc_median_skewness(tenure_list):0.02f} months")          
                    elif median_choice == 2:
                        break
                         #print(f"The median skew of monthly charge  is, {calc_median_skewness(monthly_costs_list):0.02f} ")
                    elif median_choice == 3:    
                        break
                    else:
                        print("Please enter a correct value")   
                
                # Calculate mode skew menu
                elif choice == 8:
                    mode_choice = int(input("calculate the mode skew for the folowing (1)Tenure (2)Monthly Charge (3)Main Menu"))
                    if mode_choice == 1:    
                        print(f"The mode skew of tenure is, {calc_mode_skewness(tenure_list):0.02f} months")          
                    elif mode_choice == 2:    
                        print(f"The mode skew of monthly charge  is, {calc_mode_skewness(monthly_costs_list):0.02f} ")
                    elif mode_choice == 3:    
                        break
                    else:
                        print("Please enter a correct value")   
                
                #Calculate Churn Rate
                elif choice == 9:
                    while True:
                        churn_choice = int(input("Churn Rate (1)Month (2)Exit"))
                        if churn_choice == 1:
                            try:
                                time_period = input("Please enter your timeframe (0-72)")
                                print(f"The churn rate of month {time_period} is, {calc_churn_rate(time_period,data_by_churn):0.02f} %")   
                            except KeyError as error:
                                print("Handling Out of bounds error", error)
                        elif churn_choice == 2:    
                            break
                        else:
                            print("Please enter a correct value")
                
                else:
                    print("Please enter a correct value")
        
        
        #Matplot visualisation menu
        elif main_choice == 2:
            while True:
                v_choice = int(input(" What visualisation would you like to see (1)Piechart (2)Barchart (3)Dateplot (4)Exit"))
                
                if v_choice == 4:
                    break
                
                elif v_choice == 1:
                    while True:
                        p_choice = int(input("See a piechart breakdown by (1)Gender (2)Internet Service (3) Contract (4)Phone Service (5)Main Menu"))
                        
                        #Tenure Piechart
                        if p_choice == 1:
                            # Create the figure and axes
                            fig, ax = plt.subplots()
                            # Set the title
                            ax.set_title("Gender Piechart Breakdown")
                            #do a pie chart
                            ax.pie(convert_list_to_dictionary(gender_list).values(), labels = convert_list_to_dictionary(gender_list).keys(), autopct = "%.0f%%")
                            # show the plot
                            plt.show()
                            # Save the figure (bbox = "tight" eliminates whitespace padding)
                            fig.savefig("tenure_piechart.png")
                        
                        #Internet Service Piechart
                        elif p_choice == 2:
                            # Create the figure and axes
                            fig, ax = plt.subplots()
                            # Set the title
                            ax.set_title("Internet Service Piechart Breakdown")
                            #do a pie chart
                            ax.pie(convert_list_to_dictionary(internet_service_list).values(), labels = convert_list_to_dictionary(internet_service_list).keys(), autopct = "%.0f%%")
                            # show the plot
                            plt.show()
                            # Save the figure (bbox = "tight" eliminates whitespace padding)
                            fig.savefig("internet_service_piechart.png")
                            
                        #Contract Piechart
                        elif p_choice == 3:
                            # Create the figure and axes
                            fig, ax = plt.subplots()
                            # Set the title
                            ax.set_title("Contract Piechart Breakdown")
                            #do a pie chart
                            ax.pie(convert_list_to_dictionary(contract_list).values(), labels = convert_list_to_dictionary(contract_list).keys(), autopct = "%.0f%%")
                            # show the plot
                            plt.show()
                            # Save the figure (bbox = "tight" eliminates whitespace padding)
                            fig.savefig("contract_piechart.png")
                            
                        #Phone Service Piechart
                        elif p_choice == 4:
                            # Create the figure and axes
                            fig, ax = plt.subplots()
                            # Set the title
                            ax.set_title("Phone Service Piechart Breakdown")
                            #do a pie chart
                            ax.pie(convert_list_to_dictionary(phone_services_list).values(), labels = convert_list_to_dictionary(phone_services_list).keys(), autopct = "%.0f%%")
                            # show the plot
                            plt.show()
                            # Save the figure (bbox = "tight" eliminates whitespace padding)
                            fig.savefig("contract_piechart.png")
                        
                        elif p_choice == 5:
                            break
                        
                        else:
                            print("Invalid Choice")
                                                  
                elif v_choice == 2:
                    bar_choice = int(input(" What barchart for tenure would you like to see (1)Unsorted (2)Sorted by values (3)Sorted by Keys (4)Main Menu"))
                    
                    #unsorted barchart
                    if bar_choice == 1:
                        # create a figure and an axis object
                        fig, ax = plt.subplots()
                        # set the title
                        ax.set_title("Tenure")
                        # set the y positions
                        y_pos = [ i for i in range(len(data_by_tenure))]
                        # set the y tick labels
                        ax.set_yticks(y_pos)
                        ax.set_yticklabels(data_by_tenure.keys())
                        # set the labels on the axes
                        ax.set_ylabel("Month of Tenure")
                        ax.set_xlabel("Total Tenure")
                        # do a horizontal bar chart
                        ax.barh(y_pos,data_by_tenure.values(), align="center")
                        plt.show()
                        # save the bar chart
                        fig.savefig("tenure_barchart.png")
                    
                    #sorted by values
                    elif bar_choice == 2:
                        # create a figure and an axis object
                        fig, ax = plt.subplots()
                        # set the title
                        ax.set_title("Tenure")
                        # set the y positions
                        y_pos = [ i for i in range(len(data_by_tenure))]
                        # set the y tick labels
                        ax.set_yticks(y_pos)
                        ax.set_yticklabels(data_by_tenure.keys())
                        # set the labels on the axes
                        ax.set_ylabel("Month of Tenure")
                        ax.set_xlabel("Total Tenure")
                        # do a horizontal bar chart
                        ax.barh(y_pos,sorted(data_by_tenure.values()), align="center")
                        plt.show()
                        # save the bar chart
                        fig.savefig("tenure_barchart.png")
                        
                    #sorted by keys
                    elif bar_choice == 3:
                        # create a figure and an axis object
                        fig, ax = plt.subplots()
                        # set the title
                        ax.set_title("Tenure Per Month")
                        # set the y positions
                        y_pos = [ i for i in range(len(data_by_tenure))]
                        # set the y tick labels
                        ax.set_yticks(y_pos)
                        ax.set_yticklabels(sorted(data_by_tenure.keys()))
                        # set the labels on the axes
                        ax.set_ylabel("Month of Tenure")
                        ax.set_xlabel("Total Tenure")
                        # do a horizontal bar chart
                        ax.barh(y_pos,data_by_tenure.values(), align="center")
                        plt.show()
                        # save the bar chart
                        fig.savefig("tenure_barchart.png")
                        
                    elif bar_choice == 5:
                        # create a figure and an axis object
                        fig, ax = plt.subplots()
                        # set the title
                        ax.set_title("Tenure Per Month")
                        # set the y positions
                        y_pos = [ i for i in range(len())]
                        # set the y tick labels
                        ax.set_yticks(y_pos)
                        ax.set_yticklabels(sorted(data_by_tenure.keys()))
                        # set the labels on the axes
                        ax.set_ylabel("Month of Tenure")
                        ax.set_xlabel("Total Tenure")
                        # do a horizontal bar chart
                        ax.barh(y_pos,data_by_tenure.values(), align="center")
                        plt.show()
                        # save the bar chart
                        fig.savefig("tenure_barchart.png")
                    else:
                        print("Invalid choice")
                
                    
                elif v_choice == 3:
                    while True:
                        dp_choice = int(input(" What datetime barchart for tenure would you like to see (1)Confirmed Cases (2)Total Confirmed Cases (3)Confirmed Covid Deaths (4)Total Covid Deaths (5)Main Menu"))
                        
                        #quit to main menu
                        if dp_choice == 5:
                            break
                        
                        #confirmed cases dateplot
                        elif dp_choice == 1:
                            # create a figure and an axis object
                            fig, ax = plt.subplots()
                            
                            # format the ticks
                            months = mdates.MonthLocator()  # every month
                            ax.xaxis.set_minor_locator(months)
        
                            # set the labels on the axes
                            ax.set_xlabel("Time")
                            ax.set_ylabel("Number of Confirmed Cases")
                            
                            # set the title
                            ax.set_title("Confirmed cases")
                    
                            # do a date plot: mpl.dates.date2num converts date objects to mathplotlib format
                            
                            ax.plot_date(mpl.dates.date2num(datetime_list), confirmed_case_list, marker = ",", linestyle="-")
                            plt.show()
                            
                            # save the image
                            fig.savefig('confirmed_cases_date_plot.png', bbox_inches='tight')
                            
                        #Total Confirmed Cases dateplot
                        elif dp_choice == 2:
                            # create a figure and an axis object
                            fig, ax = plt.subplots()
                            
                            # format the ticks
                            months = mdates.MonthLocator()  # every month
                            ax.xaxis.set_minor_locator(months)
                            #y_pos = [ i for i in range(len(total_confirmed_list))]
                            #ax.set_yticklabels(total_confirmed_list)
                            
                            # set the labels on the axes
                            ax.set_xlabel("Time")
                            ax.set_ylabel("Number of Confirmed Cases")
                            
                            # set the title
                            ax.set_title("Confirmed cases")
                            
                            # do a date plot: mpl.dates.date2num converts date objects to mathplotlib format
                            
                            ax.plot_date(mpl.dates.date2num(datetime_list), total_confirmed_list, marker = ",", linestyle="-")
                            plt.show()
                            
                            # save the image
                            fig.savefig('total_confirmed_cases_date_plot.png')
                    
                        #Confirmed Covid Deaths dateplot
                        elif dp_choice == 3:
                            # create a figure and an axis object
                            fig, ax = plt.subplots()
                            
                            # format the ticks
                            months = mdates.MonthLocator()  # every month
                            ax.xaxis.set_minor_locator(months)
                            
                            # set the labels on the axes
                            ax.set_xlabel("Time")
                            ax.set_ylabel("Number of Confirmed Covid Deaths")
                            
                            # set the title
                            ax.set_title("Confirmed Covid Deaths")
                            
                            # do a date plot: mpl.dates.date2num converts date objects to mathplotlib format
                            
                            ax.plot_date(mpl.dates.date2num(datetime_list), confirmed_deaths_lists, marker = ",", linestyle="-")
                            plt.show()
                            
                            # save the image
                            fig.savefig('total_confirmed_cases_date_plot.png', bbox_inches='tight')
                            
                        
                        #Total Covid Deaths dateplot
                        elif dp_choice == 4:
                            # create a figure and an axis object
                            fig, ax = plt.subplots()
                            
                            # format the ticks
                            months = mdates.MonthLocator()  # every month
                            ax.xaxis.set_minor_locator(months)
                            
                            # set the labels on the axes
                            ax.set_xlabel("Time")
                            ax.set_ylabel("Number of Covid Deaths")
                            
                            # set the title
                            ax.set_title("Total Covid Deaths")
                            
                            # do a date plot: mpl.dates.date2num converts date objects to mathplotlib format
                            
                            ax.plot_date(mpl.dates.date2num(datetime_list), total_deaths_list, marker = ",", linestyle="-")
                            plt.show()
                            
                            # save the image
                            fig.savefig('total_confirmed_cases_date_plot.png', bbox_inches='tight')
                        
                        
                        
                        else:
                            print("Please enter a correct value")
                
        
        else:
                print("Please enter a correct value")
                
            
                
except FileNotFoundError:
    print("Error Customer_Churn.csv does not exist")  
    
# outputed the results to an external file
try:
    with open("FileOutput.txt", "w") as output:
        output.write(f"The maximum tenure is: {calc_max(tenure_list):0.2f}\n")
        output.write(f"The minimum tenure is: {calc_min(tenure_list):0.2f}\n")
        output.write(f"The mean tenure is: {calc_mean(tenure_list):0.2f} \n")
        output.write(f"The median tenure is: {calc_median(tenure_list):0.2f}\n")
        output.write(f"The mode tenure is: {calc_mode(tenure_list):0.2f}\n")
        output.write(f"The standard deviation is: {calc_sdv(tenure_list):0.2f}\n")
        output.write(f"The median skew is: {calc_median_skewness(tenure_list):0.2f}\n")
        output.write(f"The mode skew is: {calc_mode_skewness(tenure_list):0.2f}\n")
        #output.write(f"The churn of month 7 is: {calc_mode_skewness(str(7),data_by_churn):0.2f}\n")
        
        output.close()
except FileNotFoundError:
    print("Error FileOutput.txt does not exist")
