import math
import datetime
import pandas as pd


simpleInterest = lambda a,r: a*r/100
print(f"interest {simpleInterest(100000,2):,.2f}")
sum_amount =int(input("Lumpsum_amount :"))
rate_month= float(input("rate of interest per month :"))
i=1
months = int(input("years :"))*12
sip_amount=int(input("SIP amount per month :"))
stepup =int(input("stepup % every year :"))
years = {}
month = []
sip_list = [] #sip amount monthly
total_invest = [] # total investment monthly 
interest_list =[] # interest calculated monthly 
total_invested_list=[]
total_list = [] # total of sip and interest 
total_invested=sum_amount
while(i<=months):
    sum_amount = sum_amount + sip_amount
    total_invest.append(round(sum_amount))
    sum_amount = sum_amount + simpleInterest(sum_amount,rate_month)
    total_list.append(round(sum_amount)) 
    strin="month "+str(i )
    years[strin]=f"{math.floor(i/12)}y{i%12}m"
    month.append(f"{math.floor(i/12)}y{i%12}m")
    total_invested = total_invested+sip_amount
    total_invested_list.append(total_invested)
    
   # print(f"{math.floor(i/12)}y{i%12}m= {sum_amount:,.2f} \n sip {sip_amount:.0f} Inv:{total_invested}")
    i=i+1
    if  i/12>0 and i%12==1:
        sip_amount=round(sip_amount*(1+0.01*stepup))
        sip_list.append(sip_amount)
    
    
   # print(years)
#print(total_list)

data = {"years":  month,    "Total": total_list, "Invested": total_invested_list}
df = pd.DataFrame(data)
#formatted_df = df.style.format('{:,}')

#print(formatted_df.to_string(index=False))

#print(df.to_string(index=False))
print(df.to_string(justify='right', index=False))
