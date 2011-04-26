#!/usr/bin/env python

from nntplib import NNTP


class NewsGrep:
    def __init__(self,server,username,password):
        self.server = NNTP(server, 119,username,password)
    def __del__(self):
        pass

    def __str__(self):
        pass

    def list(self):
        resp, groups = self.server.list()
        for group, last, first, flag in groups:
            print group

    def ls(self,group_name):
        resp, count, first, last, name = self.server.group(group_name)
        print 'Group', name, 'has', count, 'articles, range', first, 'to', last

        resp, subs = self.server.xhdr('subject', first + '-' + last)
        for id, sub in subs[-10:]:
            print id, sub

if __name__ == '__main__':
    p = NewsGrep('news.just4today.net','cghax','vm7yj')
    #p.list()
    p.ls('comp.lang.python')
