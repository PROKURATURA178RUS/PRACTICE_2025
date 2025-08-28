from stat import PaymentStatistics

file_path = "personal_transactions.csv"

stats = PaymentStatistics(file_path)

print(stats.load_data())
stats.plot_payment_system_pie()