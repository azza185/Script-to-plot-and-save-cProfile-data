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

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)

# print(document)

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

def plot_results(data,filename,totaltime):
    # Splitting the data
    modules = list(data.keys())
    values = list(data.values())
    ncalls = [value[0] for value in values if type(value) == list]
    tottime = [value[1] for value in values if type(value) == list]
    cumtime = [value[3] for value in values if type(value) == list]

    # Creating the plots
    fig, ax = plt.subplots(3, 1, figsize=(14, 18))

    fig.canvas.manager.set_window_title(f'Profilling {filename.split("/")[-1]} with total run time: {totaltime} seconds')

    # Plot for ncalls
    ax[0].bar(modules, ncalls, color='blue')
    ax[0].set_title('Number of Calls per Module')
    ax[0].set_ylabel('Number of Calls')
    ax[0].tick_params(axis='x', rotation=45)

    # Plot for tottime
    ax[1].bar(modules, tottime, color='green')
    ax[1].set_title('Total Time per Module')
    ax[1].set_ylabel('Total Time (seconds)')
    ax[1].tick_params(axis='x', rotation=45)

    # Plot for cumtime
    ax[2].bar(modules, cumtime, color='red')
    ax[2].set_title('Cumulative Time per Module')
    ax[2].set_ylabel('Cumulative Time (seconds)')
    ax[2].tick_params(axis='x', rotation=45)

    # Adjust layout to not overlap
    plt.tight_layout()
    plt.show()

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
    # save_data(results,f'./output/{filename.split("/")[-1].strip(".txt")}.json', totaltime)
    plot_results(results,filename,totaltime)
    
if __name__ == '__main__':
    print(sys.argv[1])
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('I need a file name')