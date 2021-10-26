import sys
import os

sys.path.insert(0, os.path.join(os.path.abspath("venv"), "Lib", "site-packages"))
sys.path.insert(0, os.path.join(os.path.abspath("venv"), "Scripts"))
import argparse
import parser_back as pb
from customExceptions import InvalidInputException


def print_news(source, limit=None):
    news = pb.get_items_from_rss(source, limit)
    if news:
        for item in news:
            print(item)
            print("-----------------------------------------------------------------------------------")


def print_json(source, limit=None):
    news = pb.get_jsoned_news(source, limit)
    if news:
        for item in news:
            print(item)
            print("-----------------------------------------------------------------------------------")


def process_args(args):
    if args.version:
        print(pb.version)
        return
    pb.verbose = args.verbose
    if args.source:
        if args.json:
            print_json(args.source, args.limit)
        else:
            print_news(args.source, args.limit)
    else:
        raise InvalidInputException("Wrong input formate: source requred!")


parser = argparse.ArgumentParser(description="Pure Python command-line RSS reader.")
parser.add_argument("source", nargs='?', default=None, help="RSS URL")
parser.add_argument("--version", action='store_const', help="Print version info", const=True, default=False)
parser.add_argument("--verbose", action='store_const', help="Outputs verbose status messages", const=True, default=False)
parser.add_argument("--json", action='store_const', help=" Print result as JSON in stdout", const=True, default=False)
parser.add_argument("--limit", default=None, help="Limit news topics if this parameter provided", type=int)

args = parser.parse_args()
process_args(args)