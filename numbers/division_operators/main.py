transactions = 10
total_time_minutes = 60
average_time_for_transaction = 7

# Calculate the number of completed transactions
completed = total_time_minutes // average_time_for_transaction
# Calculate the number of remaining minutes
minutes = total_time_minutes % average_time_for_transaction

# Print these values
print("The number of completed transactions is", completed)
print("The number of remaining minutes is", minutes)