#!/usr/bin/env python3


def is_called():
    def is_returned():
        print("Hello")
    print("is_called")
    return is_returned

new =  is_called()

new()

