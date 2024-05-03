from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import re
import json as json_module  # import json module as json_module
import html

class UnhandledException(Exception):
    pass

def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,  
) -> List[str]:
    key_mapping = {"title": "Feed", "pubDate": "Published"}  # mapping of old keys to new keys

    channel_info = {}
    for tag in ["title", "link", "lastBuildDate", "pubDate", "language", "category", "managingEditor", "description"]:
        match = re.search(f'<{tag}>(.*?)</{tag}>', xml)
        if match:
            channel_info[tag] = html.unescape(match.group(1))  # use old key for JSON output

    items_info = []
    for match in re.finditer(r'<item>(.*?)</item>', xml, re.DOTALL):
        item = match.group(1)
        item_info = {}
        for tag in ["title", "author", "pubDate", "link", "category", "description"]:
            match = re.search(f'<{tag}>(.*?)</{tag}>', item)
            if match:
                item_info[tag] = html.unescape(match.group(1))  # use old key for JSON output
        items_info.append(item_info)

    if limit is not None:
        items_info = items_info[:limit]

    if json:  # keep the argument name as json
        json_output = channel_info  # directly use channel_info as the root object
        json_output["items"] = items_info  # add items to the root object
        return [json_module.dumps(json_output, indent=2)]  # use json_module instead of json
    else:
        console_output = []
        for key, value in channel_info.items():
            console_output.append(f"{key_mapping.get(key, key).capitalize()}: {value}")  # use new key for console output
        console_output.append("\n")

        for item in items_info:
            for key, value in item.items():
                console_output.append(f"{key_mapping.get(key, key).capitalize()}: {value}")  # use new key for console output
            console_output.append("\n")
        return console_output

def main(argv: Optional[Sequence] = None):
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)

    if args.source:
        xml = requests.get(args.source).text
    else:
        raise ValueError("RSS URL is required")

    try:
        result = rss_parser(xml, args.limit, args.json)
        print("\n".join(result))
        return 0
    except Exception as e:
        raise UnhandledException(e)

if __name__ == "__main__":
    main()
