Install dependency
       
       pip3 install flask
       pip3 install celery


To start Producer 

    FLASK_APP=sequlizer.py
    flask run
    
To Start Worker
            
     celery -A tasks worker -l info
    
    
Modify the Tasks.py to set the address of mongo for storing logs and rebbit mq to change the broker.
