import pandas as pd
import os


def change(data,file):
    # sname = ['start_station_name', 'end_station_name', 'start_station_description', 'end_station_description']
    for (item,i) in zip(data['start_station_name'],range(len(data['start_station_name']))):
        if pd.isna(item):
            continue
        else:
            v1 = item.replace("æ", "ae")
            v2 = v1.replace("ø", "oe")
            v3 = v2.replace("å", "aa")
            v4 = v3.replace("Ø","Oe")
            # print(i,item,'->',v4)
            data.at[i,'start_station_name']=v4

    for (item,i) in zip(data['end_station_name'],range(len(data['end_station_name']))):
        if pd.isna(item):
            continue
        else:
            v1 = item.replace("æ", "ae")
            v2 = v1.replace("ø", "oe")
            v3 = v2.replace("å", "aa")
            v4 = v3.replace("Ø","Oe")
            # print(i,item,'->',v4)
            data.at[i,'end_station_name']=v4


    for (item, i) in zip(data['start_station_description'], range(len(data['start_station_description']))):
        if pd.isna(item):
            continue
        else:
            v1 = item.replace("æ", "ae")
            v2 = v1.replace("ø", "oe")
            v3 = v2.replace("å", "aa")
            v4 = v3.replace("Ø", "Oe")
            # print(i, item, '->', v4)
            data.at[i, 'start_station_description'] = v4

    for (item, i) in zip(data['end_station_description'], range(len(data['end_station_description']))):
        if pd.isna(item):
            continue
        else:
            v1 = item.replace("æ", "ae")
            v2 = v1.replace("ø", "oe")
            v3 = v2.replace("å", "aa")
            v4 = v3.replace("Ø", "Oe")
            # print(i, item, '->', v4)
            data.at[i, 'end_station_description'] = v4

    data.to_csv("./processed_csv/"+file,index=None)
    # print("./processed_csv/"+file)
    print(file+" save_success")

if __name__ == '__main__':
    base="/Users/feiyangtang/Desktop/OsloBikeAnalysis/origin_csv/"
    files=os.listdir("/Users/feiyangtang/Desktop/OsloBikeAnalysis/origin_csv")
    for file in files:
        #print(base+file)
        data = pd.read_csv(base+file)
        change(data,file)
# print(data['start_station_name'][0])
# end_station_name
#end_station_description
#start_station_description