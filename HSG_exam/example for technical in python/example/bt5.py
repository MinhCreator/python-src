class inputs(object):

    def __init__(self) -> None:
        self.str = ""

    def __call__(self) -> str:
        self.str = input().upper()
        
    
    def prints(self) -> None:
        print(self.str)



string = inputs()

string.__call__()

string.prints()