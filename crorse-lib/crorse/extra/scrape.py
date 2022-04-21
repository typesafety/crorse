"""(WIP) Scrapes and outputs to stdout."""

import multiprocessing
import sys

from bs4 import BeautifulSoup

from crorse.scrape_api import CanvasScrapeAPI


def worker(queue):        
    while True:
        c = 0
        i = queue.get()
        try: 
            res = CanvasScrapeAPI.get_chalmers(i)
            if not res.url.startswith('https://chalmers.instructure.com'):
                continue 
            res = BeautifulSoup(res.text,'html.parser').find('h2')
            
            print((i, res.string), flush=True)
            c += 1
            if c > 20: 
                sleep(60)
                c = 0
        except Exception as e:
            pass
            

def main():
    # TODO: Take parameters to decide processes, domain etc.
    processes = 4
    lst = range(20000,30000)
    queue = multiprocessing.Queue()
    for i in lst:
        queue.put(i)
    ps = []
    for _ in range(processes):
        p = multiprocessing.Process(target=worker, args=(queue,))
        ps.append(p)
        p.start()
    for p in ps:
        p.join()


if __name__ == '__main__':
    sys.setrecursionlimit(25000)
    main()
