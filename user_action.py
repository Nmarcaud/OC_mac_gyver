#! /usr/bin/env python3
# coding: utf-8

class User_action:

    @classmethod
    def user_action(cls):
        cls.user_answer = str(input("Direction mac Gyver: "))
        return cls.user_answer

