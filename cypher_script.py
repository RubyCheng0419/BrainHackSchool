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

def main(echo):
    if echo.mode == "enc":
        encrypt = True
        summary = echo.message.replace(".txt", "_encrypted.txt")
    elif echo.mode == "dec":
        encrypt = False
        summary = echo.message.replace(".txt", "_decrypted.txt")
    with open(summary, 'w') as f:
        print(summary)
        with open(echo.message) as handle:
            for line in handle:
                line = line.rstrip()
                ans = UF.process_message(line, echo.key, encrypt)
                print(ans)
                f.write("%s\n" % ans)

if __name__ == "__main__":
    main (echo)