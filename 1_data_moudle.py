# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 1_data_moudle.py
@time: 2019/07/21
"""

import collections

Card = collections.namedtuple('Card', ['rand', 'suit'])  # 定义的这个鬼东西是真的看不懂
print(Card)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]  # 这种写法真的是惊呆了

    def log_info(self):
        print('rands:', self.ranks)
        print('suits', self.suits)
        print('_cards:', self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):  # python 会自动获取这个内置方法，实现迭代
        return self._cards[position]


def main():
    deck = FrenchDeck()
    deck.log_info()


if __name__ == '__main__':
    main()
