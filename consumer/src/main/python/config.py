#Redis Server Configurations
REDIS_HOST="127.0.0.1"

#RabbitMQ Server Configurations
RABBITMQ_HOST="localhost"
RABBITMQ_TASK_QUEUE_NAME="imds_task_queue"
RABBITMQ_PREFETCH_COUNT=1

#Network File System Configurations
NFS_REMOTE_PATH="127.0.0.1:/srv/nfs4/imds"
NFS_LOCAL_PATH="/mnt/nfs/imds"

#YARA Options
YARA_RULES_PATH="/opt/imds/consumer/yara.rules
