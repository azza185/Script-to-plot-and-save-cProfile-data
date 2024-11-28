import pprint as pp
import sys
import matplotlib.pyplot as plt
import json

def read_file(filename):
    document = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                line_index = line.index(':')
                line = line[:line_index]
                document.append(line.split())
            except:
                pass
    return document

def order_file(document):
    results = dict()
    totaltime = 0
    for line in document[4::]:
        if len(line) == 6:
            totaltime += float(line[1])
            filename = line[5]
            if filename in results:
                stats = results[filename]
                stats[0] += float(line[0])
                stats[1] += float(line[1])
                stats[2] += float(line[2])
                stats[3] += float(line[3])
                stats[4] += float(line[4])
                results[filename] = stats
            else:
                stat = [float(x) for x in line[:5]]
                results[filename] = stat

    return results, totaltime

def save_data(data,filename,totaltime):
    with open(filename,'w') as f:
        # write the title then data in a nice format
        TotalTime = {"Total Time": totaltime}
        f.write(json.dumps(TotalTime, indent=4))
        f.write(json.dumps(data, indent=4))

def main(filename):
    document = read_file(filename)
    results,totaltime = order_file(document)
    # pp.pprint(results)

    for key, value in results.items():
        print(key)
        print(value)
        print('\n')
    print('Total Time')
    print(totaltime)
    save_data(results,f'./output/{filename.split("/")[-1].strip(".txt")}.json', totaltime)

if __name__ == '__main__':
    print(sys.argv[1])
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('I need a file name')