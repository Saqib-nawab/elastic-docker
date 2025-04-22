from elasticsearch import Elasticsearch
import hashlib

class ElasticSearchPipeline:
    def __init__(self):
        self.es = Elasticsearch(["http://localhost:9200"])
        self.index = "quotes_index"

    def process_item(self, item, spider):
        doc_id = hashlib.sha1(item['text'].encode('utf-8')).hexdigest()
        doc = {
            'text': item['text'],
            'author': item['author'],
            'tags': item['tags']
        }
        self.es.index(index=self.index, id=doc_id, body=doc)
        return item
