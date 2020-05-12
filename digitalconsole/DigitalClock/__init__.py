import time

def StartClock(message="", end=60):
    hour, minute, second = '00', '00', '00'
    for sec in range(0, end+1):
        print(f'{message}{hour}:{minute}:{second}', end='\r')
        time.sleep(0.95)
        second = str(int(second)+1).zfill(2)
        if second == "60":
            second = '00'
            minute = str(int(minute)+1).zfill(2)
            if minute == "60":
                minute = '00'
                hour = str(int(hour)+1).zfill(2)