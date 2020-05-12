import time
# █
class ProgressBar:
    def __init__(self, bar:str="||", fill:str="█", length:int=50, autoFill:bool=True, autoFillSize:int=1, delay:int=1):
        self.bar, self.fill, self.length, self.autoFill, self.autoFillSize, self.delay = bar, fill, length, autoFill, autoFillSize, delay
        self.percent = '000'
    def ShowBar(self):
        self.progressbar, space = '', ''
        for l in range(0, self.length):
            space += " "
            self.progressbar = f"{self.bar[0]}{space}{self.bar[-1]}"
        self.each = (100/self.length)*self.autoFillSize
        if self.autoFill:
            per = 1
            while per <= 101:
                time.sleep(self.delay)
                self.percent = (str(eval(self.percent) + self.each)).zfill(3)
                print(f"{self.progressbar.replace(' ', self.fill, per*self.autoFillSize)} {self.percent.replace('.0', '')} %", end='\r', flush=True)
                if eval(self.percent) == 100:
                    break
                per += 1
        elif not self.autoFill:
            self.percent = (str(eval(self.percent)))
            print(f"{self.progressbar} {self.percent.replace('.0', '')} %", end='\r')
    def NextFill(self, fillLength:int=1):
        self.fillLength = fillLength
        self.each = (100/self.length)*self.fillLength
        self.percent = (str(eval(self.percent) + self.each)).zfill(3)
        self.progressbar = self.progressbar.replace(' ', self.fill, self.fillLength)
        print(f"{self.progressbar} {self.percent.replace('.0', '')}", end='\r')