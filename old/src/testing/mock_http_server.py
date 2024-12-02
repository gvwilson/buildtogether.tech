INDEX_PAGE = '<html><body><h1>Index Page</h1></body></html>'
USER_PAGE = '<html><body><h1>User Page</h1></body></html>'

def mock_http_server(url):
    if url == '/':
        return INDEX_PAGE
    elif url in ['/user/', '/user/index.html']:
        return USER_PAGE
    else:
        raise UrlError(f'unhandled URL "{url}"')
