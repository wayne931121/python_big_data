import os

def create(name,string=""):
    with open(name,"w",encoding="utf-8") as f:
        if string: f.write(string)

def remove(name):
    os.remove(name)

def empty_check(r,check=0):
    if r=="":
        if check:
            return -1
        else:
            raise AssertionError("Index out of file range or File is empty or File has empty row.")
    return 1

def readArray(name,start,value=1,check=0):
    if start<0: raise ValueError("Index Must >=0.")
    res = []
    with open(name,"r",encoding="utf-8") as f:
        i=0
        while i<start:
            r = f.readline()
            if empty_check(r,check)==-1: return None
            i += 1
        for i in range(value):
            r = f.readline()
            if empty_check(r,check)==-1: return None
            res.append(decodeArrayStructure(r))
    return res

def appendArray(name,array):
    with open(name,"a",encoding="utf-8") as f:
        f.write(encodeArrayStructure(array))

def popArray(filename,start,end=-1,temp_filename="37404740011223tmp"):
    if end==-1: end=start
    with open(filename,"r",encoding="utf-8") as file:
        with open(temp_filename,"w",encoding="utf-8") as file1:
            i = 0
            while 1:
                data = file.readline()
                if data=="": break
                if i<start or i>end: file1.write(data)
                i+=1
    os.remove(filename)
    os.rename(temp_filename,filename)

def length(name):
    with open(name,"r",encoding="utf-8") as f:
        i=0
        while 1:
            if f.readline()=="":
                break
            i+=1
    return i

def read(name):
    with open(name,"r",encoding="utf-8") as f:
        content = f.read()
    return content

def write(name,string):
    with open(name,"w",encoding="utf-8") as f:
        f.write(string)
    return 1

def encodeArrayStructure(singleArrayData):
    #[["1","2","3"],"1"] to "1,2,3_1\n"
    return ",".join(singleArrayData[0])+"_"+singleArrayData[1]+"\n"

def decodeArrayStructure(line):
    # "1,2,3_1\n" to [["1","2","3"],"1"]
    line = line.strip()
    line = line.split("_")
    line[0] = line[0].split(",")
    return line

def read_until(file, symbol):
    #-> ... data symbol data symbol ... <- Repeat: data symbol. Symbol seperate data.
    data = ""
    while 1:
        temp = file.read(1)
        data += temp
        #debug log: not temp=="symbol", is temp==symbol.
        if temp=="" or temp==symbol:
            break
    return data

def readArray_(name,start,value=1,check=0,seperate="\n",decode=decodeArrayStructure):
    #print(bytes(seperate,encoding="utf-8"))
    if start<0: raise ValueError("Index Must >=0.")
    res = []
    with open(name,"r",encoding="utf-8") as f:
        i=0
        while i<start:
            r = read_until(f,seperate)
            if empty_check(r,check)==-1: return None
            i += 1
        for i in range(value):
            r = read_until(f,seperate)
            if empty_check(r,check)==-1: return None
            res.append(decode(r))
    return res

def appendArray_(name,array,encode=encodeArrayStructure):
    with open(name,"a",encoding="utf-8") as f:
        f.write(encode(array))

def popArray_(filename,start,end=-1,temp_filename="37404740011223tmp",seperate="\n"):
    if end==-1: end=start
    with open(filename,"r",encoding="utf-8") as file:
        with open(temp_filename,"w",encoding="utf-8") as file1:
            i = 0
            while 1:
                data = read_until(file,seperate)
                if data=="": break
                if i<start or i>end: file1.write(data)
                i+=1
    os.remove(filename)
    os.rename(temp_filename,filename)

def length_(name,seperate="\n"):
    with open(name,"r",encoding="utf-8") as f:
        i=0
        while 1:
            if read_until(f,seperate)=="":
                break
            i+=1
    return i

if __name__=="__main__":
    def encodeArrayStructure_(singleArrayData):
        #[["1","2","3"],"1"] to "1,2,3_1$seperate$"
        seperate="\b"
        return ",".join(singleArrayData[0])+"_"+singleArrayData[1]+seperate
    
    def decodeArrayStructure_(line):
        # "1,2,3_1$seperate$" to [["1","2","3"],"1"]
        line = line[:-1]
        line = line.split("_")
        line[0] = line[0].split(",")
        return line
    name = "123444.txt"
    create(name)
    appendArray_(name,[["K1KL","O1","●"],"POIUY"],encode=encodeArrayStructure_)
    appendArray_(name,[["K1KL","O1","●"],"POIUY1"],encode=encodeArrayStructure_)
    appendArray_(name,[["K1KL","O1","●"],"POIUY2"],encode=encodeArrayStructure_)
    appendArray_(name,[["K1KL","O1","●"],"POIUY3"],encode=encodeArrayStructure_)
    appendArray_(name,[["K1KL","O1","●"],"POIUY4"],encode=encodeArrayStructure_)
    appendArray_(name,[["K1KL","O1","●"],"POIUY5"],encode=encodeArrayStructure_)
    popArray_(name,1,end=1,seperate="\b")
    print(length_(name,"\b"))
    print(readArray_(name,start=1,value=1,seperate="\b",decode=decodeArrayStructure_)[0])
