# Stubs for email.parser (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import email.feedparser

FeedParser = email.feedparser.FeedParser
BytesFeedParser = email.feedparser.BytesFeedParser

class Parser:
    policy = ...  # type: Any
    def __init__(self, _class=None, *, policy=...): pass
    def parse(self, fp, headersonly=False): pass
    def parsestr(self, text, headersonly=False): pass

class HeaderParser(Parser):
    def parse(self, fp, headersonly=True): pass
    def parsestr(self, text, headersonly=True): pass

class BytesParser:
    parser = ...  # type: Any
    def __init__(self, *args, **kw): pass
    def parse(self, fp, headersonly=False): pass
    def parsebytes(self, text, headersonly=False): pass

class BytesHeaderParser(BytesParser):
    def parse(self, fp, headersonly=True): pass
    def parsebytes(self, text, headersonly=True): pass