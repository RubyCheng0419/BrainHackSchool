import useful_functions as UF

from argparse import ArgumentParser, Namespace
parser = ArgumentParser()
parser.add_argument("--message", action='store',
                    help="Path to raw data txt file, i.e. msg_file.txt.", type=str)
parser.add_argument("--key", help="key", type=str)
parser.add_argument("--mode",
                    help="takes either enc or dec as its value", default = "enc",
                    type=str)

echo: Namespace = parser.parse_args()

if __name__ == "__main__":
    if echo.mode == "enc":
        encrypt = "True"
        summary = echo.message.replace(".txt", "_encrypted.txt")
        # print(msg_file)
    elif echo.mode == "dec":
        encrypt = "False"
        summary = echo.message.replace(".txt", "_decrypted.txt")
        # print(msg_file)

    with open(summary, 'w') as f:
        print(summary)
        handle = open(echo.message)
        # print(handle)
        # print(echo.message)
        for line in handle:
            line = line.rstrip()
            ans = UF.process_message(line, echo.key,encrypt)
            print(ans)
            f.write("%s\n" % ans)
            
