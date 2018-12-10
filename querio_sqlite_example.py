import sys
import os.path
sys.path = [os.path.dirname(__file__) + '/..'] + sys.path
import querio as q
from querio.ml.expression import Feature
from querio.queryobject import QueryObject
import logging

logging.basicConfig(level=logging.DEBUG)

dB = "sqlite:///queriosqlite.db"

i = q.Interface(dB, "person")

object1 = QueryObject("height")
object1.add((Feature('age') > 30) & (Feature('income') > 6000))

result1 = i.object_query(object1)

print(result1) 

