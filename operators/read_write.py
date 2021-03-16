def my_save(name,data):
    with open(name, 'w') as f:
        f.write(str(data))

def my_open(name):
    with open(name, 'r') as f:
        data = f.read()
        dict_name = eval(data)
    return dict_name