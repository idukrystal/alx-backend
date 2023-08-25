#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('2-hypermedia_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")


def a(b):
    for c in b.items():
        print(c)
    print("____________")

print(server.dataset())
a(server.get_hyper(1, 2))
print("---")
a(server.get_hyper(2, 2))
print("---")
a(server.get_hyper(100, 3))
print("---")
a(server.get_hyper(3000, 100))
