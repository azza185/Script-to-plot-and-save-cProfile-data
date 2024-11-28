import pprint as pp
import sys
import matplotlib.pyplot as plt
import json
import os
import numpy as np
import argparse

def read_file(filename: str) -> list:
    '''
    Read the file and return the data in a list

    Args:
        filename (str): The name of the file to be read

    Returns:
        list: A list containing the data from the file
    '''
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


def order_file(document: str) -> tuple:
    '''
    Take the file and order the data into a dictonary based on the filename


    Args:
        document (str): The folder to be read

    Returns:
        tuple: A tuple containing the results and the total time
    '''
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

def plot_results(data: dict, filename: str, totaltime: float) -> None:
    '''
    Plot the results of the profiling

    Args:
        data (dict): A dictionary containing the profiling data
        filename (str): The name of the file
        totaltime (float): The total time of the profiling
    '''
    # Splitting the data
    modules = list(data.keys())
    values = list(data.values())
    ncalls = [value[0] for value in values if type(value) == list]
    tottime = [value[1] for value in values if type(value) == list]
    cumtime = [value[3] for value in values if type(value) == list]

    # Creating the plots
    fig, ax = plt.subplots(3, 1, figsize=(14, 18))

    fig.canvas.manager.set_window_title(f'Average of {filename} runs with average total run time: {totaltime} seconds')

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

def parse_arguments() -> argparse.Namespace:
    '''
    Parse the arguments passed to the script

    Returns:
        argparse.Namespace: The parsed arguments
    '''
    # Create a parser object
    parser = argparse.ArgumentParser(description="Example script with flags")

    # Add flags
    parser.add_argument(
        '--directory', '-d',
        type=str,
        help='Specify the directroy the .txt files are in'
    )
    parser.add_argument(
        '--filePrefix', '-fp',
        type=str,
        help='Your file prefix'
    )

    # Parse and return the arguments
    return parser.parse_args()

def main(directory,filePrefix):
    filename = []
    prefix = filePrefix 
    for file in os.listdir(directory):
        if file.startswith(filePrefix):
            filename.append(file)
    times_dict = {}
    totalTime = []
    i = 0
    for _, file in enumerate(filename):
        document = read_file(os.path.join(directory, file))
        results, totaltime = order_file(document)
        totalTime.append(totaltime)
        times_dict[i] = results
        i += 1
    averaged = {}
    for key, item in times_dict.items():
        for key2, item2 in item.items():
            print(key2)
            print(item2)
            print('\n')
            averaged[key2] = [x + y for x, y in zip(item[key2], item2)]
    
            
    avage_total_time = np.mean(totalTime)
    print('Average Total Time\n')
    print(avage_total_time)
    plot_results(averaged,prefix,avage_total_time)
    
if __name__ == '__main__':
    args = parse_arguments()
    if args.directory and args.filePrefix:
        main(args.directory, args.filePrefix)
    else:
        print("Please provide the directory and file prefix")