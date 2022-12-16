import time


def read_file_timed(file):
    """Возвращает содержимое файла и измеряет требуемое время."""
    start_time = time.time()
    try:
        f = open(file, 'rb')
    except FileNotFoundError as e:
        print(e)
        print(f'Time required for {file} = 0.0')
    else:
        print(f.read())
        f.close()
        print(f'Time required for {file} = {time.time() - start_time}')
        return f
    finally:
        print('Finishing...')


video_data = read_file_timed('video.mp4')
