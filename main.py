from sensor.logger import logging
from sensor.exception import SensorException

def test():
    try:
        logging.info("starting logging test")
        result = 3/0
        print(result)
        logging.info("stopping logging test")
    except Exception as e:
        logging.debug('debug logging test')
        raise e

if __name__ == "__main__":
    try:
        test()
    except Exception as e:
        print(e)