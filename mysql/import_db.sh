DUMP_FILE=mysqlsampledatabase.sql
HOST=mydb1.ctiembqzvsd8.us-east-1.rds.amazonaws.com
USER=root

mysql -u $USE -H$HOST -p  < $DUMP_FILE 
