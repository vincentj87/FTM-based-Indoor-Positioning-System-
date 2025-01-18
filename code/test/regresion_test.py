import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def plot_scatter():
    fig, ax=plt.subplots(4,3)
    ax[0,0].scatter(laser_anch1,uwb1)
    ax[0,0].title.set_text("UWB Anchor 1")
    ax[0,1].scatter(laser_anch1,ftm1)
    ax[0,1].title.set_text("FTM Range Anchor 1")
    ax[0,2].scatter(laser_anch1,rssi1)
    ax[0,2].title.set_text("RSSI Anchor 1")

    ax[1,0].scatter(laser_anch2,uwb2)
    ax[1,0].title.set_text("UWB Anchor 2")
    ax[1,1].scatter(laser_anch2,ftm2)
    ax[1,1].title.set_text("FTM Range Anchor 2")
    ax[1,2].scatter(laser_anch2,rssi2)
    ax[1,2].title.set_text("RSSI Anchor 2")

    ax[2,0].scatter(laser_anch3,uwb3)
    ax[2,0].title.set_text("UWB Anchor 3")
    ax[2,1].scatter(laser_anch3,ftm3)
    ax[2,1].title.set_text("FTM Range Anchor 3")
    ax[2,2].scatter(laser_anch3,rssi3)
    ax[2,2].title.set_text("RSSI Anchor 3")

    ax[3,0].scatter(laser_anch4,uwb4)
    ax[3,0].title.set_text("UWB Anchor 4")
    ax[3,1].scatter(laser_anch4,ftm4)
    ax[3,1].title.set_text("FTM Range Anchor 4")
    ax[3,2].scatter(laser_anch4,rssi4)
    ax[3,2].title.set_text("RSSI Anchor 4")
    plt.show()


location_data=pd.read_csv("C:/Users/vince/Documents/semester 7/Tugas Akhir/code/test/data/location_data.csv")

laser_anch1=location_data.iloc[0:60,1]
laser_anch2=location_data.iloc[0:60,2]
laser_anch3=location_data.iloc[0:60,3]
laser_anch4=location_data.iloc[0:60,4]

uwb1=location_data.iloc[0:60,5]
uwb2=location_data.iloc[0:60,6]
uwb3=location_data.iloc[0:60,7]
uwb4=location_data.iloc[0:60,8]

ftm1=location_data.iloc[0:60,9]
ftm2=location_data.iloc[0:60,11]
ftm3=location_data.iloc[0:60,13]
ftm4=location_data.iloc[0:60,15]

ftm1_tof=location_data.iloc[0:60,10]
ftm2_tof=location_data.iloc[0:60,12]
ftm3_tof=location_data.iloc[0:60,14]
ftm4_tof=location_data.iloc[0:60,16]

rssi1=location_data.iloc[0:60,17]
rssi2=location_data.iloc[0:60,18]
rssi3=location_data.iloc[0:60,19]
rssi4=location_data.iloc[0:60,20]
    
laser_anch1_train,laser_anch1_test,ftm1_train,ftm1_test=train_test_split(laser_anch1,ftm1,test_size=1/6,random_state=0)

laser_anch1_train=np.array(laser_anch1_train).reshape(-1,1)

laser_anch1_test=np.array(laser_anch1_test).reshape(-1,1)



model1=LinearRegression()

model1.fit(laser_anch1_train,ftm1_train)
m1=model1.coef_
c1=model1.intercept_

ftm1_pred_train =m1*laser_anch1_train+c1
ftm1_pred_test=m1*laser_anch1_test+c1
# print(ftm1_pred_train.flatten())




fig, ax =plt.subplots(1,2)

ax[0].scatter(laser_anch1_train,ftm1_train)
ax[0].plot(laser_anch1_train,ftm1_pred_train,color='red')
ax[0].title.set_text("training")
# ax[0].xlabel("real_distance")
# ax[0].ylabel("ftm distance")

ax[1].scatter(laser_anch1_test,ftm1_test)
ax[1].plot(laser_anch1_test,ftm1_pred_test,color='red')
ax[1].title.set_text("testing")
# ax[1].xlabel("real_distance")
# ax[1].ylabel("ftm distance")

plt.show()

