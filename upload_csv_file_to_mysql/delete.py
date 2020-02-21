
from library.class1 import neumath 
import mysql.connector

df=neumath()

input_ = int(input())
df.delete_lead(input_)
