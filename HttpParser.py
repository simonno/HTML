from datetime import datetime


class HttpMassageParser:

    def __init__(self, http_version, number_type, content_type, connection, data):

        self._http_version = http_version
        self._connection = connection
        self._number_type = number_type
        self._content_type = content_type
        self._data = data
        self._data_length = len(data)
        self._html_datetime_format = '%a, %m %b %Y %H:%M:%S'

    def get_massage(self):
        if self._number_type == 404:
            self._data = '<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n<meta charset="UTF-8">' \
                   '\r\n<title>Title</title>\r\n</head>\r\n<body>\r\n<h1>Not found</h1>' \
                   '\r\n</body>\r\n</html>'

        elif self._number_type == 304:
            self._data = ''

        massage = 'HTTP/' + str(self._http_version) + ' ' + self.__get_number_type_str() + '\r\n'
        massage += 'Date: ' + self.__get_date() + ' GMT\r\n'
        massage += 'Content-Length: ' + str(self._data_length) + '\r\n'
        massage += 'Content-Type: ' + self._content_type + '\r\n'
        if self._number_type == 200:
            massage += 'Last-Modified: ' + self.__get_date() + ' GMT\r\n'
        massage += 'Connection: ' + self._connection + '\r\n\r\n' + self._data
        return massage

    def __get_date(self):
        return datetime.today().strftime(self._html_datetime_format)

    def __get_number_type_str(self):
        return {
            200: '200 OK',
            301: '301 Moved Permanently',
            304: '304 Not Modified',
            400: '400 Bad Request',
            404: '404 Not Found',
            505: '505 HTTP Version Not Supported',

        }.get(self._number_type, 404)
