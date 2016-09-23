import socket
from django.conf import settings
from rest_framework.metadata import BaseMetadata

class Meta():
    def __init__(self, limit=0, page=0, record_count=0, total_records=0, time=0):
        self.version = settings.VERSION
        self.server = socket.gethostname()
        self.limit = limit
        self.page = page
        self.record_count = record_count
        self.total_records = total_records
        self.time = time


class MetaError():
    def __init__(self, developer_message, user_message, error_code):
        self.developer_message = developer_message
        self.user_message = user_message
        self.error_code = error_code
        self.more_info = settings.MORE_INFO

class MetaBatch():
    def __init__(self, id, status, object):
        self.id = id
        self.status = status
        self.object = object

class MetaBatchStatus():
    def __init__(self, id, description):
        self.id = id
        self.description = description

class Metadata(BaseMetadata):
    """
    Don't include field and other information for `OPTIONS` requests.
    Just return the name and description.
    """
    def determine_metadata(self, request, view, meta, obj):

        return  {
                   'meta': {
                       'version': meta.version,
                       'server': meta.server,
                       'limit': meta.limit,
                       'page': meta.page,
                       'recordCount': meta.record_count,
                       'totalRecords': meta.total_records,
                       'time': meta.time
                    },
                    'records': obj
                }

    def determine_metadata_error(self, request, view, list_errors):

        metaErrors = []

        for m in list_errors:
            metaErrors.append({
                       "developerMessage": m.developer_message,
                       "userMessage": m.user_message,
                       "errorCode": m.error_code,
                       "moreInfo": m.more_info
                    })

        return metaErrors
