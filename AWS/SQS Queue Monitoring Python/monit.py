from boto.ec2.cloudwatch import CloudWatchConnection
from boto.sqs.connection import SQSConnection
import boto
import sys
from datetime import datetime, timedelta
import locale
from time import sleep

def monit():

	if(len(sys.argv) > 1):
		queue_name = sys.argv[1]
	else:
		print("Please specify a queue name as an argument!")
		sys.exit(1)


	# Connect to CloudWatch and SQS
	cw = CloudWatchConnection(aws_access_key_id = '',
			aws_secret_access_key = '')

	sqs = SQSConnection(aws_access_key_id = '',
			aws_secret_access_key = '')

	# Grab our metrics

	metrics = ['ApproximateNumberOfMessagesVisible', 'NumberOfMessagesReceived', 'NumberOfMessagesSent']

	metric_objects = {}
	for metric in metrics:
		obj = cw.list_metrics(dimensions = dict(QueueName = queue_name),
			metric_name = metric,
			namespace = 'AWS/SQS')

		if(len(obj) <= 0):
			print("No metric found for %s - %s" % (queue_name, metric))
		else:
			metric_objects[metric] = obj[0]

	if(len(metric_objects) <= 0):
		print("No metrics found.")
		sys.exit(1)

	period_printed = True

	timer = 0

	q = sqs.get_queue(queue_name)

	while(True):
		
		if(timer == 0 or ((timer % 300) == 0)):
			time_printed = True
			for m in metric_objects:
				# We'll request a 60s period but it looks like SQS only supports 300s
				
				data = metric_objects[m].query((datetime.now() - timedelta(hours=1)), datetime.now(), 'Sum', 'Count', period = 60)
				
				# These come out of order for some reason
				data.sort(key=lambda r: r['Timestamp'])
				period = data[-1]['Timestamp'] - data[-2]['Timestamp']
				detected_interval = period.seconds
				if(period_printed):
					print("Detected interval of %s seconds." % detected_interval)
					period_printed = False
				data = data[-1]
				if(time_printed):
					print(data['Timestamp'])
					time_printed = False
				
				if(m == 'ApproximateNumberOfMessagesVisible'):
					sys.stdout.write("%s %s\n" % (m, data['Sum']))
				else:
					sys.stdout.write("%s %s\n" % (m, locale.format_string("%.*f", (2, (data['Sum'] / detected_interval)), True)))
				
				sys.stdout.flush()
#		input("Press Enter to check again...")	
				
		
#		if(timer == 0 or ((timer % 5) == 0)):
#			print("Message Count: %s" % q.count())
				
#		sleep(5)
#		timer = timer + 5


if __name__ == '__main__':
    monit()

