import multiprocessing
import requests

def downloadFile(url, name):
    print(f"downloading started {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"downloading finished {name}")

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"
    processes = []

    for i in range(10):
        p = multiprocessing.Process(target=downloadFile, args=(url, i))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
