from .console import ProcessCommunicationEventHandler
import argparse


def main():
    parser = argparse.ArgumentParser(description="Forward child output to supervisord's stdout")
    parser.add_argument('-f', '--format', nargs='?')
    args = parser.parse_args()

    handler = ProcessCommunicationEventHandler(log_format=args.format)
    handler.run_forever()


if __name__ == '__main__':
    main()