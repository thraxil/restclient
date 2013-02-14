# Copyright 2007, Columbia Center For New Media Teaching And Learning (CCNMTL)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the CCNMTL nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY CCNMTL ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <copyright holder> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

""" Basic Test Suite for restclient

Requires nose and HTTPretty to run
"""

from restclient import GET, POST
from httpretty import HTTPretty, httprettified

test_url = "http://example.com/"
default_body = "Simple response"


@httprettified
def test_get():
    HTTPretty.register_uri(
        HTTPretty.GET,
        test_url,
        body=default_body,
        content_type="text/html"
    )
    r = GET(test_url)
    assert r == default_body
    assert HTTPretty.last_request.method == "GET"


@httprettified
def test_post():
    HTTPretty.register_uri(
        HTTPretty.POST,
        test_url,
        body=default_body,
        content_type="text/html"
    )
    r = POST(
        test_url,
        params={'value': 'store this'},
        accept=["text/plain", "text/html"],
        async=False)
    assert r == default_body
    assert HTTPretty.last_request.method == "POST"
    assert HTTPretty.last_request.headers['accept'] == "text/plain,text/html"


if __name__ == "__main__":
    import nose
    nose.main()
