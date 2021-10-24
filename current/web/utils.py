import time
def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年","月","日")

if __name__ == "__main__":
    print(get_time())