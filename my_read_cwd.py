import os


def read_cwd():
    return os.getcwd()



if __name__ == "__main__":

    result = read_cwd()
    print(f"resulit is: {result} with type: {type(result)}")