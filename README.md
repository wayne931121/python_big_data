# python_big_data
這個程式能讓Python處理巨大的陣列，藉由將記憶體轉移到固態硬碟做資料處理，並且一次只讀取部分資料，讓程式不因為電腦記憶體不夠而無法運作。

可將下面這兩個函數換成你自己的資料格式，並且「一行為一筆資料」(這個模組以換行符號作為讀取中斷點標記，所以資料內不能包含換行符號，您可以用其他符號取代)。
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
以我這個檔案的資料結構來說，是將下面這個陣列轉為用檔案儲存，並且直接在檔案內進行處理，而不是記憶體:
```
a = [[["1","1","1"],"121"],[["2","1","1"],"328"],......]
```
## length(name)
回傳陣列長度<br>
name: filename 檔案名稱

## popArray(filename,start,end=-1,temp_filename="37404740011223tmp")
將陣列從第start項到第end項刪除(包括start和end)<br>
start: index (from 0)<br>
end: index (from 0)

## appendArray(name,array)
將指定項目附加到陣列末項
name: filename<br>
array: item

## readArray(name,start,value=1,check=0)
從第start項讀取value個項目出來
name: filename<br>
start: index (from 0)<br>
value: (value>0)<br>
check: 0、1<br>
check為0時，如果start或要讀取的項目超出陣列index會回報錯誤，check為1時則不報錯並回傳None。

### empty_check(r,check=0)
資料結構中不能完全無資料，此函數將檢查是否無完全資料或有結構缺失，並且報錯或回傳。

## create(name)
創建空檔案<br>
name: 檔案名稱

## remove(name)
刪除指定檔案(os.remove(name))<br>
name: 檔案名稱
