  
def read_file(filename):
    def generator(filename):
        with open(filename, 'rb') as entry:

            for chunk in iter(lambda: entry.read(1024 * 1024), b''):

                yield chunk

    import celaut_pb2, time
    start = time.time()
    buffer = b''.join([b for b in generator(filename)])
    print(len(buffer))
    # return buffer
    any  = celaut_pb2.Any()
    any.ParseFromString(buffer)
    print(time.time() - start)

import threading

x = threading.Thread(target=read_file, args=('__registry__/16426da109eed68c89bf32bcbcab208649f01d608116f1dda15e12d55fc95456', ))
y = threading.Thread(target=read_file, args=('__registry__/47744b30d73d12235f80be88e6e665d5f2d4784f9ca90a12bc9e002633fd9b3e', ))
z = threading.Thread(target=read_file, args=('__registry__/60610f898fc859ca133cb971e9fd757fbf40513e60eee0a0f937994781922cdd', ))
t = threading.Thread(target=read_file, args=('__registry__/60610f898fc859ca133cb971e9fd757fbf40513e60eee0a0f937994781922cdd', ))

x.start()
y.start()
z.start()
t.start()

x.join()
y.join()
z.join()
t.join()