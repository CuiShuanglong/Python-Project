# coding:utf-8
import urllib.request


class HtmlDownloadr(object):

    def download(self, url):
        if url is None:
            return None
        response=urllib.request.urlopen(url)

        if response.status !=200:
            return None
        return response.read()