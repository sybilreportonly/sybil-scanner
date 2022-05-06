import pandas as pd
def trim(addr):
        return(f"{addr[:6]}...{addr[-4:]}")

def stage1():
    original_file_name = "USDT.csv"
    data = pd.read_csv(original_file_name)

    total_length = len(data['to'])
    res = {'from': list(), 'to': list()}
    for i in range(total_length):
        print(f"stage1_{i/total_length*100}%")
        if(data['from'][i] != data['to'][i]):
            res['from'].append(data['from'][i])
            res['to'].append(data['to'][i])

    df = pd.DataFrame(res)
    df.to_csv('./filter1.csv')

def stage2():
    data = pd.read_csv("filter1.csv")
    total_length = len(data['to'])
    res = {'first': list(), 'mid': list(), 'last': list()}
    for i in range(total_length):
        print(f"stage2_{i/total_length*100}%")
        for j in range(i, total_length):
            if(data['to'][i] == data['from'][j] and data['from'][i] != data['to'][j]):
                print(f"{trim(data['from'][i])} > {trim(data['from'][j])} > {trim(data['to'][j])}")
                res['first'].append(data['from'][i])
                res['mid'].append(data['from'][j])
                res['last'].append(data['to'][j])
                break

    df = pd.DataFrame(res)
    df.to_csv('./links_3.csv')
def stage3():
    data = pd.read_csv("links_3.csv")
    total_length = len(data['first'])
    res = {'first': list(), 'mid1': list(), 'mid2': list(), 'mid3': list(), 'last': list()}
    for i in range(total_length):
        print(f"stage3_{i/total_length*100}%")
        for j in range(i, total_length):
            if(data['last'][i] == data['first'][j] and data['first'][i] != data['last'][j]):
                print(f"{trim(data['first'][i])} > {trim(data['mid'][i])} > {trim(data['last'][i])} >  {trim(data['mid'][j])} > {trim(data['last'][j])}")
                res['first'].append(data['first'][i])
                res['mid1'].append(data['mid'][i])
                res['mid2'].append(data['last'][i])
                res['mid3'].append(data['mid'][j])
                res['last'].append(data['last'][j])
                break


    df = pd.DataFrame(res)
    df.to_csv('./links_5.csv')
def stage4():

    data = pd.read_csv("links_5.csv")

    def trim(addr):
        return(f"{addr[:6]}...{addr[-4:]}")

    total_length = len(data['first'])
    res = {
        'first': list(),
        'mid1': list(),
        'mid2': list(),
        'mid3': list(),
        'mid4': list(),
        'mid5': list(),
        'mid6': list(),
        'mid7': list(),
        'last': list()
        }
    for i in range(total_length):
        print(f"stage4_{i/total_length*100}%")
        for j in range(i, total_length):
            if(data['last'][i] == data['first'][j] and data['first'][i] != data['last'][j]):
                print(f"{trim(data['first'][i])} > ..... > {trim(data['last'][j])}")
                res['first'].append(data['first'][i])
                res['mid1'].append(data['mid1'][i])
                res['mid2'].append(data['mid2'][i])
                res['mid3'].append(data['mid3'][i])
                res['mid4'].append(data['last'][i])
                res['mid5'].append(data['mid1'][j])
                res['mid6'].append(data['mid2'][j])
                res['mid7'].append(data['mid3'][j])
                res['last'].append(data['last'][j])
                break
    df = pd.DataFrame(res)
    df.to_csv('./links_9.csv')
def stage5():
    data = pd.read_csv("links_9.csv")

    total_length = len(data['first'])
    addresses = list()
    for i in range(total_length):
        adds = list(data.iloc[i])[1:]
        dup = len(adds) != len(set(adds))
        if(not dup):
            addresses = addresses + adds
    print(len(list(set(addresses))))
    print("====final====")
    for acc in list(set(addresses)):
        print(acc)
stage1()
stage2()
stage3()
stage4()
stage5()
