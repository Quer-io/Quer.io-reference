import sys
import os.path
sys.path = [os.path.dirname(__file__) + '/..'] + sys.path
import querio as q
from querio.ml.expression import Feature
from querio.queryobject import QueryObject

dB = "postgres://queriouser:pass1@localhost:5432/normaldb"
i = q.Interface(dB, "person")
object1 = QueryObject("height")
object1.add((Feature('age') > 30) & (Feature('income') > 10000))
result1 = i.object_query(object1)

print(result1) 

