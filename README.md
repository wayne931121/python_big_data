# python_big_data
這個程式能讓Python處理巨大的陣列，藉由將記憶體轉移到固態硬碟做資料處理，並且一次只讀取部分資料，讓程式不因為電腦記憶體不夠而無法運作。

請將下面這兩個函數換成你自己的資料格式，並且一行為一筆資料
```
def encodeArrayStructure(singleArrayData):
    #[["1","2","3"],"1"] to "1,2,3_1\n"
    return ",".join(singleArrayData[0])+"_"+singleArrayData[1]+"\n"

def decodeArrayStructure(line):
    # "1,2,3_1\n" to [["1","2","3"],"1"]
    line = line.strip()
    line = line.split("_")
    line[0] = line[0].split(",")
    return line
```
