import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        f = open(file, 'rb')
        print(f'Time required for {file} = {start_time}')
    except FileNotFoundError as e:
        print(e)
        print(f'Time required for {file} = 0.0')
    else:
        print(f.read())
        f.close()
        return f
    finally:
        print(time.time())


