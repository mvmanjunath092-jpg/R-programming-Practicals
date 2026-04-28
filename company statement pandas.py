import matplotlib.pyplot as plt
import pandas as pd

data={'company':['Zoho','Microsoft','Google','Apple','Amazon','Deloitte'],
      'Grace point':[730,660,745,600,500,450]
      }
df=pd.DataFrame(data)
print(df)
plt.bar(df['company'],df['Grace point'],color=['yellow','blue','red','black','brown','green'])
plt.xlabel('Company')
plt.ylabel('Grace point')
plt.title('Company - Grace point 2025')
plt.show()