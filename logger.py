class Logger:

    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)

    def display_logs(self):
        print("\n=== TRACE LOG ===")
        for log in self.logs:
            print(log)