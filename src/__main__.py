from .console import ProcessCommunicationEventHandler

if __name__ == '__main__':
    handler = ProcessCommunicationEventHandler()
    handler.run_forever()