import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

input_dir_base = "../Results/DNS_"

def load_data(file_name):
  with open(file_name, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    return list(spamreader)

def pre_process_data(scenario, n_queries_sent):
  data = [[],[],[],[]] # there are 4 scenarios only
  for n_affected_components in range(4):
    # generate file names
    sent_data_file_name = input_dir_base+scenario+'/time_sheet_dns_client_sent_'\
      +str(n_queries_sent)+'pkts_'+str(n_affected_components)+scenario+'.csv'
    received_data_file_name = input_dir_base+scenario+'/time_sheet_dns_client_received_' \
      +str(n_queries_sent)+'pkts_'+str(n_affected_components)+scenario+'.csv'

    # load data from CSV files
    sent_data = load_data(sent_data_file_name)
    received_data = load_data(received_data_file_name)

    # calculate the latency (RTT)
    values = []
    for i in range(len(sent_data)):
      v = float(received_data[i][1]) - float(sent_data[i][1]) # [1] refers to the timestamp column
      values.append(round(v,6)) 
    data[n_affected_components] = values
  return data

def truncate(f, n):
  '''Truncates/pads a float f to n decimal places without rounding'''
  s = '%.12f' % f
  i, p, d = s.partition('.')
  return float('.'.join([i, (d+'0'*n)[:n]]))

def calc_average(values):
  average = sum(values)/len(values)
  return average

def calc_error(conjunto,average):
  std_deviation = np.std(np.array(conjunto))
  confidence_interval = scipy.stats.norm.interval(0.95, loc=average, scale=std_deviation)
  return confidence_interval[1]-average


def process_data(data):
  j = 0
  for i in data:
    print(j,"Faults:")
    avg = calc_average(i)
    print("Average:",truncate(avg,4))
    print("Error:",truncate(calc_error(i,avg),4))
    print()
    j+=1


def plot():
  pass

#==============================================================================

scenario = None
print("Choose an option:")
print("1 - Failures")
print("2 - Intrusions")
print("Other - Quit")
opt = input()
if opt == "1":
  scenario = "failures"
elif opt == "2":
  scenario = "intrusions"
else:
  sys.exit()

n_queries_sent = input("Please, type the number of DNS queries sent: ")

data = pre_process_data(scenario, int(n_queries_sent))

processed_data = process_data(data)

plot()
