import pandas as pd
import matplotlib.pyplot as plt


class PaymentStatistics:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        return self.df.head()

    def plot_payment_system_pie(self):
        if self.df is None:
            raise ValueError

        payment_stats = self.df.groupby("Account Name")["Amount"].sum()

        plt.figure(figsize=(8, 6))
        plt.pie(
            payment_stats,
            labels=payment_stats.index,
            autopct="%.1f%%",
            startangle=90
        )
        plt.title("Затраты по типу платежной системы")
        plt.show()