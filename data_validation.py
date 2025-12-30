from abc import ABC
import pandas as pd
import numpy as np

class DataValidation(ABC):
    def __init__(self):
        super().__init__()

    @classmethod
    def validate(self, data:pd.DataFrame):
        raise NotImplementedError("validate not implemented.")
    
class TransactionValidation(DataValidation):
    def __init__(self):
        super().__init__()
    
    @classmethod
    def validate(self, data:pd.DataFrame):
        json_safe_data = []

        for _, row in data.iterrows():
            record = {}

            for col in data.columns:
                val = row[col]

                if isinstance(val, (np.floating, float)):
                    if np.isnan(val) or np.isinf(val):
                        val = 0.0
                    val = float(max(min(val, 1e4), -1e4))

                elif isinstance(val, (np.integer, int)):
                    val = int(val)

                elif isinstance(val, pd.Timestamp):
                    val = val.strftime("%Y-%m-%d %H:%M:%S")

                elif val is None:
                    val = ""

                else:
                    val = str(val)

                record[col] = val

            json_safe_data.append(record)

        return json_safe_data