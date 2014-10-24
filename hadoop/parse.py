filename = []
functionA = lambda i:len(str(i))==1 and 'part-0000'+str(i) or (len(str(i))==2 and 'part-000'+str(i) or 'part-00'+str(i))
for i in range(147):
    filename.append(functionA(i))

transformData = {}
for item in ['part-00000', 'part-00001']:
    input = open('./train/transformData/'+item)
    for line in input:
        tmp = line.split('^')[0]
        transformData[tmp] = True
    input.close()
output = open('trainInput', 'w')
for item in filename:
    print item
    input = open('./train/monitorData/'+item)
    for line in input:
        tmp = line.split('^')
        userid = tmp[0]
        adid = tmp[2]+tmp[3]
        if userid in transformData.keys():
            output.write(userid + ' ' + adid + ' 1')
        else:
            output.write(userid + ' ' + adid + ' 0')
    input.close()
output.close()

output = open('validationInput')
for item in filename:
    input = open('./validation/monitorData/' + item)
    for line in input:
        tmp = line.split('^')
        userid = tmp[0]
        adid = tmp[2] + tmp[3]
        output.write(userid + ' ' + adid + ' 1')
    input.close()
output.close()