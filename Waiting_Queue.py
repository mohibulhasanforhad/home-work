#  Hospital Waiting Queue

queue = ['Rin', 'Sam', 'Yuki']

queue.append('Leo')

called_patient = queue.pop(0)

print("Now calling:", called_patient)
print("Remaining queue:", queue)
print("Patients waiting:", len(queue))