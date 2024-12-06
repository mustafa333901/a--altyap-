import pandas as pd
from sklearn.model_selection import train_test_split

# --------------------
# 1. Veri Altyapısı
# --------------------
class DataPipeline:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self):
        """Veriyi yükler."""
        return pd.read_csv(self.data_path)

    def clean_data(self, data):
        """Veri temizleme ve ön işleme."""
        data = data.dropna()
        data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        return data

    def split_data(self, data, target_column, test_size=0.2):
        """Veriyi eğitim ve test olarak böler."""
        X = data.drop(columns=[target_column])
        y = data[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=42)
