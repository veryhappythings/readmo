from __future__ import with_statement
import glob
import os
import web
from vendor import markdown

pages = []
for filename in sorted(glob.glob('pages/*.markdown')):
    with open(filename, 'r') as f:
        data = ''.join(f.readlines())
        pages.append(data)

class page(object):
    def GET(self, page_number=1):
        page_number=int(page_number)
        return render.page(data=markdown.markdown(page_from_number(page_number)),
                           current_page=page_number,
                           paging_numbers=links_for_page_number(page_number),
                           number_of_pages=len(pages))

def page_from_number(page_number):
    if page_number < 1:
        page_number = 1
    if len(pages) > page_number-1:
        return pages[page_number-1]
    raise web.notfound()

def links_for_page_number(page_number, distance=2):
    if page_number > len(pages): return []
    links = []
    low_distance, high_distance = distance, distance
    if page_number <= distance: low_distance = page_number-1
    if page_number + distance >= len(pages): high_distance = len(pages) - page_number
    links += range(page_number - low_distance, page_number+1)
    links += range(page_number + 1, page_number + 1 + high_distance)
    if links[0] != 1: links.insert(0, 1)
    if links[-1] != len(pages): links.append(len(pages))
    return links

def notfound():
    return web.notfound(render.notfound())

urls = (
  '^/$', 'page',
  '^/(\d+)$', 'page',
)

render = web.template.render('templates', base='base')
app = web.application(urls, globals())
app.notfound = notfound
app.cgirun()
