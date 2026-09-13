import multiprocessing


def consumer(queue):
    while True:
        msg = queue.get()

        if msg == 'DONE':
            break


def producer(count, queue):
    for i in range(count):
        queue.put(i)

    queue.put('DONE')


queue = multiprocessing.Queue()

consumer_process = multiprocessing.Process(
    target=consumer,
    args=[queue]
)

consumer_process.daemon = True
consumer_process.start()

count = 10**4

producer(count, queue)

consumer_process.join()

print("Sent {0} numbers to Queue...".format(count))
