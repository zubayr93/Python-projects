total_hr= int(input("total hours worked: "))
reg_pay = int(input("pay per hour: "))
if total_hr > 40:
    extra_hrs = total_hr - 40
    extra_hr_pay = extra_hrs * (reg_pay * 1.5)
    total_work_pay = ((total_hr - extra_hrs) * reg_pay) + extra_hr_pay  
    print (total_work_pay)
else:
    norm_hr_pay = total_hr * reg_pay
    print (norm_hr_pay)
    
