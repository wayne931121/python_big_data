import os

def create(name):
    with open(name,"w",encoding="utf-8") as f:
        pass

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

def encodeArrayStructure(singleArrayData):
    #[["1","2","3"],"1"] to "1,2,3_1\n"
    return ",".join(singleArrayData[0])+"_"+singleArrayData[1]+"\n"

def decodeArrayStructure(line):
    # "1,2,3_1\n" to [["1","2","3"],"1"]
    line = line.strip()
    line = line.split("_")
    line[0] = line[0].split(",")
    return line

if __name__=="__main__":
    name = "123444.txt"
    remove(name)
    create(name)
    appendArray(name,[["a","t"],"LLKKKAABBCCFFGG0"])
    appendArray(name,[["a","t"],"LLKKKAABBCCFFGG1"])
    appendArray(name,[["a","t"],"LLKKKAABBCCFFGG2"])
    popArray(name,0)
    print(readArray(name,0))