from __future__ import print_function
import time
import urllib.error
import urllib.parse
import urllib.request


class GoogleFinance(object):
    cookier = urllib.request.HTTPCookieProcessor()

    def __init__(self):
        # Build the cookie handler
        # self.cookier = urllib.request.HTTPCookieProcessor()
        self.opener = urllib.request.build_opener(GoogleFinance.cookier)
        urllib.request.install_opener(self.opener)

        # Cookie and corresponding crumb
        self._cookie = None
        self._crumb = None

        # Headers to fake a user agent
        self._headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}

    def _get_cookie_crumb(self):
        req = urllib.request.Request('https://finance.yahoo.com/quote/^GSPC', headers=self._headers)
        f = urllib.request.urlopen(req)
        alines = f.read().decode('utf-8')

        global _crumb
        cs = alines.find('CrumbStore')
        cr = alines.find('crumb', cs + 10)
        cl = alines.find(':', cr + 5)
        q1 = alines.find('"', cl + 1)
        q2 = alines.find('"', q1 + 1)
        crumb = alines[q1 + 1:q2]
        _crumb = crumb

        for c in self.cookier.cookiejar:
            if c.domain != '.yahoo.com':
                continue
            if c.name != 'B':
                continue
            self._cookie = c.value

    def load_yahoo_quote(self, ticker, begindate, enddate, info='quote'):
        if self._cookie is None or self._crumb is None:
            self._get_cookie_crumb()

        tb = time.mktime((int(begindate[0:4]), int(begindate[4:6]), int(begindate[6:8]), 4, 0, 0, 0, 0, 0))
        te = time.mktime((int(enddate[0:4]), int(enddate[4:6]), int(enddate[6:8]), 18, 0, 0, 0, 0, 0))

        param = dict()
        param['period1'] = int(tb)
        param['period2'] = int(te)
        param['interval'] = '1d'
        if info == 'quote':
            param['events'] = 'history'
        elif info == 'dividend':
            param['events'] = 'div'
        elif info == 'split':
            param['events'] = 'split'
        param['crumb'] = _crumb
        params = urllib.parse.urlencode(param)
        url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?{}'.format(ticker, params)
        req = urllib.request.Request(url, headers=self._headers)

        f = urllib.request.urlopen(req)
        alines = f.read().decode('utf-8')
        return alines.split('\n')
