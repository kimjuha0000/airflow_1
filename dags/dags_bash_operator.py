from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *", # 분, 시, 일, 월, 요일
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"), # 언제부터 돌지
    catchup=False, # True일 경우 datetime부터 현재시간까지 모두 돌림
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag: 
     bash_t1 = BashOperator(
        task_id="bash_t1", # 객체명과 taskid는 일치하도록
        bash_command="echo whomai",
    )
     
     bash_t2 = BashOperator(
        task_id="bash_t2", # 객체명과 taskid는 일치하도록
        bash_command="echo $HOSTNAME",
    )
     
     bash_t1 >> bash_t2