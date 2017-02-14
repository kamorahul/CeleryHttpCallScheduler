Install dependency
       
       pip3 install flask
       pip3 install celery


To start Producer 

    FLASK_APP=sequlizer.py
    flask run
    
To Start Worker
            
     celery -A tasks worker -l info
    
    
Modify the Tasks.py to set the address of mongo for storing logs and rabbit mq to change the broker.

Setting the tasks : 


http://HOST/set?endpoint=ENDPOINT&type=PROTOCOL&action=METHOD&schedule=TIME_IN_SECONDS&qs=QUERY_STRING&post_json=BODY_DATA_IN_JSON

ENDPOINT : http endpoint to call

METHOD : post or get

TIME_IN_SECONDS : the time to invoke the method or pass "now" without quotes to call instantly

QUERY_STRING : if method is get then this parameter will be consider.

BODY_DATA_IN_JSON : if method is post then this parameter will be consider.
