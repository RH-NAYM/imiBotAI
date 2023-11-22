from data_functions import *
import re
date_pattern = r'\d{1,2}/\d{1,2}/\d{4}'

def calculate(bot):
    text = bot["You"]
    reply = bot["ChatBot"]

    if reply=="hey :-)" or reply=="hello, thanks for visiting" or reply=="hi there, what can I do for you?" or reply=="hi there, how can I help?":
        chatbot = reply

    elif reply=="I am ChatBot. How can I help you?":
        chatbot = reply

    elif reply=="see you later, thanks for visiting" or reply=="have a nice day" or reply=="bye! come back again soon.":
        chatbot = reply

    elif reply=="happy to help!" or reply=="any time!" or reply=="my pleasure":
        chatbot = reply

    elif reply=="why did the hipster burn his mouth? He drank the coffee before it was cool." or reply=="what did the buffalo say when his son left for college? Bison.":
        chatbot = reply

    elif reply=="total_day_worked":
        chatbot = total_day()

    elif reply=="total_employee_worked":
        chatbot = total_employee_worked()

    elif reply=="total_material_used":
        chatbot = total_mat_used()

    elif reply=="total_strike_rate":
        chatbot = total_sr()

    elif reply=="total_shop_covered":
        chatbot = total_shop_covered()

    elif reply=="total_avg_eemployee":
        chatbot = total_avg_employee()

    elif reply=="total_avg_material":
        chatbot = total_avg_mat()

    elif reply=="total_avg_shop":
        chatbot = total_avg_shop()

    elif reply=="total_max_employee":
        chatbot = max_employee()

    elif reply=="total_max_material":
        chatbot = max_mat()

    elif reply=="total_max_strike_rate":
        chatbot = maxSR()

    elif reply=="total_max_shop_covered":
        chatbot = max_shop()

    elif reply=="total_min_employee":
        chatbot = min_employee()

    elif reply=="total_min_material":
        chatbot = min_mat()

    elif reply=="total_min_strike_rate":
        chatbot = minSR()

    elif reply=="total_min_shop_covered":
        chatbot = min_shop()

    elif reply=="single_date_employee":
        match = re.search(date_pattern, text)
        if match:
            day = match.group(0)
        chatbot = single_date_employee(day)

    elif reply=="single_date_material":
        match = re.search(date_pattern, text)
        if match:
            day = match.group(0)
        chatbot = single_date_mat(day)

    elif reply=="single_date_strike_rate":
        match = re.search(date_pattern, text)
        if match:
            day = match.group(0)
        chatbot = single_date_sr(day)
    
    elif reply=="single_date_shop_covered":
        match = re.search(date_pattern, text)
        if match:
            day = match.group(0)
        chatbot = single_date_shop(day)
    
    elif reply=="today_employee":
        chatbot = today_employee()

    elif reply=="today_material":
        chatbot = today_mat()

    elif reply=="today_strike_rate":
        chatbot = today_sr()

    elif reply=="today_shop_covered":
        chatbot = today_shop()

    elif reply=="yesterday_employee":
        chatbot = yesterday_employee()

    elif reply=="yesterday_material":
        chatbot = yesterday_mat()

    elif reply=="yesterday_strike_rate":
        chatbot = yesterday_sr()

    elif reply=="yesterday_shop":
        chatbot = yesterday_shop()

    elif reply=="in_between_two_date_total_employee":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = day2_employee(day1,day2)

    elif reply=="in_between_two_date_total_material":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = day2_mat(day1,day2)

    elif reply=="in_between_two_date_total_strike_rate":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = day2_sr(day1,day2)

    elif reply=="in_between_two_date_total_shop":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = day2_shop(day1,day2)

    elif reply=="in_between_two_date_max_employee":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = max_employee_2_day(day1,day2)

    elif reply=="in_between_two_date_max_material":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = max_material_2_day(day1,day2)

    elif reply=="in_between_two_date_max_strike_rate":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = max_sr_2_day(day1,day2)

    elif reply=="in_between_two_date_max_shop":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = max_shop_2_day(day1,day2)

    elif reply=="in_between_two_date_min_employee":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = min_employee_2_day(day1,day2)

    elif reply=="in_between_two_date_min_material":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = min_material_2_day(day1,day2)

    elif reply=="in_between_two_date_min_strike_rate":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = min_sr_2_day(day1,day2)

    elif reply=="in_between_two_date_min_shop":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = min_shop_2_day(day1,day2)

    elif reply=="in_between_2_day_avg_employee":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = avg_employee_2_day(day1,day2)

    elif reply=="in_between_2_day_avg_material":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = avg_mat_2_day(day1,day2)

    elif reply=="in_between_2_day_avg_strike_rate":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = avg_sr_2_day(day1,day2)

    elif reply=="in_between_2_day_avg_shop":
        matches = re.findall(date_pattern, text)
        day1 = matches[0]
        day2 = matches[1]
        chatbot = avg_shop_2_day(day1,day2)
    else:
        chatbot = warning
    return chatbot





