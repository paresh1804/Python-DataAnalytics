import matplotlib.pyplot as plt
from datetime import datetime
fig,ax=plt.subplots()
print(fig)
print(ax)

# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# y2=[1,2,3,4,5]
# ax.bar(x,y2)

# plt.show()

ts=int(1613692800.0)

print(datetime.utcfromtimestamp(ts))
