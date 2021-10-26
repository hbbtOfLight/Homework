import json
from serializer import serialize, define_path
from _datetime import datetime, date
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from jsonSerializer import itemEncoder

# from datetime import date


import item

version = "version: 1.1"
verbose = False


def print_log(message):
    if verbose:
        print(message)


def get_from_url(address):
    try:
        session = HTMLSession()
        return session.get(address)
    except requests.exceptions.RequestException as e:
        print_log(f"Request exception! {e}")
        raise
    except Exception as e:
        print_log(f"Unknown exception establishing connection {e}")
        raise


def get_xml_items_list(rss_page_text, limit=None):
    try:
        soup = BeautifulSoup(rss_page_text, "xml")
        return soup.find("title"), soup.find_all("item", limit=limit)
    except Exception as e:
        print_log(f"Exception while looking for items! {e}")
        raise


def create_item(it):
    try:
        it_xml = BeautifulSoup(str(it), "xml")
        descr_lxml = BeautifulSoup(it_xml.find("description").text, "lxml")
        return item.Item(it_xml.find("title").text,
                         it_xml.find("pubDate").text,
                         it_xml.find("link").text, descr_lxml.text)
    except AttributeError as e:
        print_log(f"Something's wrong with xml! Attribute error {e}")
        raise
    except Exception as e:
        print_log(f"Unexpected exception{e}")
        raise


def mistake_counter(mistakes=0):
    while True:
        mistakes += 1
        yield mistakes


def parse_page(rss_page_text, limit=None):
    source, items = None, None
    try:
        source, items = get_xml_items_list(rss_page_text, limit)
    except Exception as e:
        print_log(f"Failed to get xml items!{e}")
        raise
    print_log("Got xml items")
    news_list = []
    mistake_num = mistake_counter()
    for it in items:
        try:
            news_list.append(create_item(it))
        except Exception:
            print_log(f"Failed to add element! Mistake count {next(mistake_num)}")
        else:
            print_log(f"Successfully processed element. Total elements parsed: {len(news_list)}")
    print_log(f"Parsed {len(news_list)} elements, mistakes number = {next(mistake_num) - 1}")

    return source, news_list


def get_items_from_rss(address, limit=None):
    rss_page = None
    try:
        rss_page = get_from_url(address)
    except Exception:
        print_log("Oops! Failed to get rss!")
        return None
    else:
        print_log("Got rss. Trying to parse it")
    try:
        source, news_list = parse_page(rss_page.text, limit)
        print_log("Got news list")
        serialize({source.text: news_list})
        print_log("Serialized this list")
        return news_list
    except Exception as e:
        print(f"Something went wrong: got {e}")
    return None


def get_jsoned_news(address, limit=None):
    try:
        list_to_json = get_items_from_rss(address, limit)
        print_log("Got items. Trying to convert to json")
        return [json.dumps(obj, cls=itemEncoder, sort_keys=False, ensure_ascii=False, indent=4) for obj in list_to_json]
    except Exception as e:
        print(f"Failed to get data in json formate. Occured {e}")


def get_items_from_json(cur_date: datetime.date = date(1970, 1, 1)):
    response_dict = dict()
    with open(define_path(), 'r') as file:
        data_dict = json.load(file)
        for title, items in data_dict.items():
            for it in items:
                it_cls = item.Item.from_json(it)
                if it_cls.date.date() >= cur_date:
                    if title in response_dict:
                        response_dict[title].append(it)
                    else:
                        response_dict[title] = [it]
    return data_dict

