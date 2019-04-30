# coding: utf8

import urllib2
from urlparse import urljoin



class MpegTS:

    def __init__(self, keep=False, verbose=False, m3Url=None, tsUrls=None, headers=None):
        self.keep = keep;
        self.verbose = verbose;
        self.m3Url = m3Url;
        self.tsUrls = tsUrls;
        self.headers = headers;

    def _getContents(self, url):
        opener = urllib2.build_opener();
        opener.addheaders = self.headers;
        response = opener.open(url)
        self._verbo("requested : {}".format(response.geturl()));
        self._verbo("status code: {}".format(response.getcode()));
        self._verbo("meta info: {}".format(response.info()));
        return response.read()
    
    
    def _loadTsUrls(self):
        self._verbo("loading m3Url: {}".format(self.m3Url));
        contents = self._getContents(self.m3Url);
        self.tsNames = [s for s in contents.split() if s[0]!="#" and s!=""]
        self.tsUrls = [urljoin(self.m3Url, u) for u in self.tsNames ]
        self._verbo("TS Playlist links: {}".format("\n".join(self.tsUrls)));
    
    
    def _verbo(self,stri):
        if self.verbose:
            print(stri)
    
    def _keep(self, file_name, contents):
        if self.keep:
            with open("stash/{}".format(file_name),"wb") as f:
                f.write(contents)
    
    def _retrieve(self):
        self._verbo('start retrieving...')
        count = 0
        for tslink, tsname in zip(self.tsUrls, self.tsNames):
            self._verbo('retrieving {}(part {})...'.format(tsname,count))
            ts = self._getContents(tslink);
            self._keep(tsname,ts);
            with open(self.m3Url.split("/")[-1].split(".")[0], 'ab') as f:
                f.write(ts)
            count += 1
            self._verbo('{}(part {}) retrieved'.format(tsname,count))
    
        print 'file: ' + self.m3Url.split("/")[-1].split(".")[0]
