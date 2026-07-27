def check_lead (budget):
    if budget is  None:
     return "invalid lead"
    elif budget  >= 5000:
       return "VIP Lead"
    elif budget  >=500:
       return "high value lead"
    else:
       return "low value lead"

print(check_lead(6000))
print(check_lead(400))
print(check_lead(None))
      

    
       
    