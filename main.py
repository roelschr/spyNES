# import usefull packages
import sys

#import spyNES packages
from rom import ROM


def main():
    assert len(sys.argv) > 1, "Not given any parameter."

    fp = open(sys.argv[1],  "rb")
    ROM(fp)

if __name__ == "__main__":
    main()
