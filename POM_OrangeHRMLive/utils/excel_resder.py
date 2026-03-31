import pandas as pd

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def get_test_rows(self):
        return self.df.to_dict(orient='records')

    def save_result(self, test_id, status):
        # self.df['Test_id'] = self.df['Test_id'].astype(str)
        # test_id = str(test_id)
        print(f"Searching for: {test_id} ({type(test_id)}) in column of type ({self.df['Test_id'].dtype})")

        # Locate the specific Test_id and update the 'Result'
        # Locate the specific Test_id and update the 'Result'
        self.df.loc[self.df['Test_id'] == test_id, 'Result'] = status
        self.df.to_csv(self.file_path, index=False)