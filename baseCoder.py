import sys
import argparse
from base64 import base64_encoder, base64_decoder
from base32 import base32_encoder, base32_decoder

if __name__ == "__main__":
    parser = argparse.ArgumentParser("description = Base decoder")

    parser.add_argument("input", type=str, help="provide something to encode/decode")
    parser.add_argument(
        "-32",
        "--base32",
        action="store_true",
        help="base32",
    )
    parser.add_argument(
        "-64",
        "--base64",
        action="store_true",
        help="base64",
    )
    parser.add_argument(
        "-e",
        "--encode",
        action="store_true",
        help="encode",
    )
    parser.add_argument(
        "-d",
        "--decode",
        action="store_true",
        help="decode",
    )
    args = parser.parse_args()

    if (args.encode and args.base64):
        print(base64_encoder(args.input))
    elif (args.decode and args.base64):
        print(base64_decoder(args.input))
    elif (args.encode and args.base32):
        print(base32_encoder(args.input))
    elif (args.decode and args.base32):
        print(base32_decoder(args.input))
    else:
        parser.print_help()
        sys.exit(1)
