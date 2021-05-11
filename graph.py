import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('baseball.csv',index_col='team',encoding='euc-kr')
#print(df)
font_name=mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font',family=font_name)
ax=df.plot(kind='bar',figsize=(12,4),legend=True, fontsize=12)
ax.set_xlabel('구단',fontsize=12)
ax.set_ylabel('win/lose/draw',fontsize=12)
ax.legend(['win','lose','draw'], fontsize=12)
plt.show()
