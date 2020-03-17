class EPD_Stub:
    def reset(self):
        pass

    def send_command(self, command):
        pass

    def send_data(self, data):
        pass

    def ReadBusy(self):
        pass

    def init(self):
        return 0

    def getbuffer(self, image):
        return []

    def display(self, imageblack, imagered):
        pass

    def Clear(self):
        pass

    def sleep(self):
        pass
