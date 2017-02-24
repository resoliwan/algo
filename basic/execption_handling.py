try:
    raise RuntimeError("test")
except:
    print('RuntimeError catched')
