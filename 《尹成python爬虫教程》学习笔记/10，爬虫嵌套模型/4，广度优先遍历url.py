from queue import Queue


def download_page(url):
    pass


def get_page_data(pagedata):
    pass


def get_page_urls(pagedata):
    pass


def BSF(url):
    queue = Queue() # 队列
    queue.put(url)
    while not queue.empty():
        url = queue.get(url)
        pagedata = download_page(url)
        data_list = get_page_data(pagedata)
        if len(data_list) != 0:
            for data in data_list:
                print(data)
        url_list = get_page_urls(pagedata)
        if len(url_list) != 0:
            for myurl in url_list:
                queue.put(myurl)

