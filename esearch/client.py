# -*- coding: utf-8 -*-
'''
Elasticsearch Python client:
https://elasticsearch-py.readthedocs.io/en/master/
'''

import elasticsearch

def es_draft():
    # https://elasticsearch-py.readthedocs.io/en/7.0.1/api.html#elasticsearch
    es = elasticsearch.Elasticsearch([
        {'host':'localhost', 'port':'9200'}
    ])


    # https://elasticsearch-py.readthedocs.io/en/7.0.1/api.html#cat
    response = es.cat.health(v=True, format='json')
    print(response[0])

if __name__ == '__main__':
    es_draft()