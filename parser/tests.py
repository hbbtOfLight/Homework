import unittest
from item import Item


from parser_back import get_xml_items_list
import parser_back as pb

rss_page_text = '<channel><title>Tproger</title>' \
                '<item>' \
                '<title>Почему я бросил работу в крупной IT-компании и перешел на фриланс</title>' \
                '<link>https://tproger.ru/articles/pochemu-ja-brosil-rabotu-v-krupnoj-it-kompanii-i-pereshel-na-frilans/</link>' \
                '<pubDate>Tue, 26 Oct 2021 11:29:58 +0000</pubDate>'\
                '<description><![CDATA[<p>Авторы поговорили со экспертами из ИТ-сферы и узнали, что мотивировало их перейти на фриланс. А также рассказали о плюсах и минусах фриланса.</p>' \
                '<p>— Читать дальше «<a rel="nofollow" href="https://tproger.ru/articles/pochemu-ja-brosil-rabotu-v-krupnoj-it-kompanii-i-pereshel-na-frilans/">Почему я бросил работу в крупной IT-компании и перешел на фриланс</a>»</p>' \
                ']]></description></item>' \
                '<item><title>Пример создания домашнего микрокластера minicube</title><link>https://tproger.ru/articles/primer-sozdanija-domashnego-mikroklastera-minicube/</link>'
'<pubDate>Mon, 25 Oct 2021 15:53:13 +0000</pubDate>' \
'<description><![CDATA[<p>Backend-разработчик рассказал как создать домашний микрокластер minicube на OS Windows без привлечения сторонних виртуальных машин.</p>' \
'<p>— Читать дальше «<a rel="nofollow" href="https://tproger.ru/articles/primer-sozdanija-domashnego-mikroklastera-minicube/">Пример создания домашнего микрокластера minicube</a>»</p>' \
']]></description></item></channel>'


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_unlimited_parsing(self):
        self.assertEqual(2, len((get_xml_items_list(rss_page_text)[1])))

    def test_limited_parsing(self):
        self.assertEqual(1, len((get_xml_items_list(rss_page_text, limit=1)[1])))

    def test_item_creation(self):
        xmled_item = get_xml_items_list(rss_page_text)[1][0]
        self.assertNotEqual(None, pb.create_item(xmled_item))

    def test_page_parse(self):
        self.assertIsInstance(pb.parse_page(rss_page_text)[1][0], Item)

    def test_create_item_exception(self):
        self.assertRaises(AttributeError, pb.create_item, "<link></link>")




