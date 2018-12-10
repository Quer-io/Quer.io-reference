import sys
import os.path
sys.path = [os.path.dirname(__file__) + '/..'] + sys.path
import querio as q
from querio.ml.expression import Feature
from querio.queryobject import QueryObject
import logging

logging.basicConfig(level=logging.DEBUG)

dB = "postgres://queriouser:pass1@localhost:5432/normaldb"
i = q.Interface(dB, 'querio_view')

object1 = QueryObject('height')
object1.add((Feature('profession_name') == 'programmer'))
object1.add(Feature('stars') > 20)

result1 = i.object_query(object1)
print(result1)  # > (avg income = 3000; std deviation income = 2000)

