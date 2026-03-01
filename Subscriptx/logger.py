class Logger:
    @staticmethod
    def log(message):
        with open("logs.txt", "a") as f:
            f.write(message + "\n")
        print(f"LOG: {message}")