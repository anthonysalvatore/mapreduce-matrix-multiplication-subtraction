#!/bin/bash    

m=2 # rows in M
n=2 # columns in N

hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-file ./mapper.py \
-mapper "./mapper.py $m $n" \
-file ./reducer.py \
-reducer ./reducer.py \
-input /data \
-output /output

