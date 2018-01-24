# -*- coding:utf-8 -*-
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_song(self):
        for i in self.lyrics:
            print(i)

small_red_hat = Song(["采蘑菇的小姑娘",
                      "背着书包上学堂",
                      "咿呀咿呀咿呀哟..."
                    ])

small_red_hat.sing_song()