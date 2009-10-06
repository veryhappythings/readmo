from web.template import CompiledTemplate, ForLoop


def base():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (content):
        yield '', join_('<!DOCTYPE\n')
        yield '', join_(' html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n')
        yield '', join_('  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n')
        yield '', join_('<html xmlns="http://www.w3.org/1999/xhtml" lang="en">\n')
        yield '', join_('<head>\n')
        yield '', join_('    <meta http-equiv="content-type" content="text/html; charset=utf-8" />\n')
        yield '', join_('    <title>Readmo</title>\n')
        yield '', join_('    <link rel="stylesheet" href="/static/readmo.css" type="text/css" media="screen" charset="utf-8"/>\n')
        yield '', join_('</head>\n')
        yield '', join_('<body>\n')
        yield '', join_(escape_(content, False), '\n')
        yield '', join_('</body>\n')
        yield '', join_('</html>\n')
    return __template__

base = CompiledTemplate(base(), 'templates/base.html')


def notfound():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__():
        yield '', join_("<div id='content'>\n")
        yield '', join_('<p>Oh no! This page is not here! :(</p>\n')
        yield '', join_('</div>\n')
    return __template__

notfound = CompiledTemplate(notfound(), 'templates/notfound.html')


def page():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (data, number_of_pages, current_page, paging_numbers):
        yield '', join_("<ul id='nav'>\n")
        for i in loop.setup(paging_numbers):
            yield '', join_("<li><a href='/", escape_(i, True), "'>", escape_(i, True), '</a></li>\n')
        yield '', join_('</ul>\n')
        yield '', join_('\n')
        yield '', join_("<div id='content'>\n")
        yield '', join_(escape_(data, True), '\n')
        yield '', join_('</div>\n')
    return __template__

page = CompiledTemplate(page(), 'templates/page.html')
