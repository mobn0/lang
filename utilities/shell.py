import utilities.basic as basic

class Shell():
    
    def __init__(self):
        self.main()
        
    def main(self):
        while True:
            text = input("basic > ")
            result, error = basic.run("<stdin>", text)
            
            if error: print(error.a_string())
            else: print(result)