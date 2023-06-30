"""
This python code will parse all demos in a folder into analyzed folder.

Example:
    D:/demos/pug_de_ancient_2022-11-09_20.dem
    will be parsed and JSON file will be saved to
    D:/demos/analyzed/pug_de_ancient_2022-11-09_20.json

Notes:
    If you have many demos in the folder that are not parsed, this will murder your PC.
    Parsing 240 demos took like 8min with Ryzen 3800X

"""
import os
from awpy import DemoParser
from threading import Thread
import time

demos_folder = "D:/demos/"
analyzed_folder = "D:/demos/analyzed/"
analyze_threads = []

def analyze_demo(demo):
    """ Analyze a demo file.

    Args:
        demo (str): The name of the demo file.

    Returns:
        None
    """
    demo_parser = DemoParser(demofile=demos_folder + demo, demo_id=demo.replace(".dem", ""), parse_rate=128, outpath=analyzed_folder)
    data = demo_parser.parse()

def analyze_demos():
    """ Analyze all demo files in the demos folder.
        Does not analyze already analyzed demos.

    Returns:
        None
    """
    try:
        demos = os.listdir(demos_folder)
        analyzed = os.listdir(analyzed_folder)
        for demo in demos:
            if ".dem" in demo and not demo[:-4] + ".json" in analyzed:
                analyze_thread = Thread(target=analyze_demo, args=(demo,))
                analyze_threads.append(analyze_thread)
        
        for thread in analyze_threads:
            thread.start()
        
        for thread in analyze_threads:
            thread.join()
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
    start_time = time.time()
    analyze_demos()
    print("--- %s seconds ---" % (time.time() - start_time))