import os
import pandas as pd
import requests
import time
import us

from tqdm import tqdm

url = 'https://api.data.gov/ed/collegescorecard/v1/schools'

class CollegeScorecard:

    def __init__(self, api_key = None):
        self.api_key = api_key
        self.session_url = f'{url}?api_key={api_key}'
        self.fields = list()
        self.parameters = list()

    def add_fields(self, fields: list = None):
        """
        A method for adding fields to the instance.
        """
        [self.fields.append(field) for field in fields if field not in self.fields]

    def add_parameters(self, params: list = None):
        """
        A method for adding filter parameters to the instance.
        """
        [self.parameters.append(param) for param in params if param not in self.parameters]

    def get_data(self, params: list=None, fields: list=None):
        if params is None:
            params = self.parameters
        if fields is None:
            fields = self.fields
        df = pd.DataFrame()
        self.session_url = f'{self.session_url}&{'&'.join(params)}&fields={','.join(fields)}&per_page=100'
        response = requests.get(self.session_url)
        total = response.json()['metadata']['total']
        pages = total//100+1
        print(f'{total} institutions found...')
        for page in tqdm(range(0, pages), position=0, leave=False):
            results_url = f'{self.session_url}&page={page}'
            results = requests.get(results_url)
            results_df = pd.DataFrame(results.json()['results'])
            df = pd.concat([df,results_df], ignore_index=True)
            time.sleep(.5)
        return df

    def show_fields(self):
        """A method for verifying the fields that have already been added to the class instance."""
        try:
            isinstance(self.fields, list)
        except TypeError as e:
            print(f"The class attribute 'fields' is not a list: {e}")
        if len(self.fields) == 0:
            print('No fields entered')
        else:
            return self.fields

    def reset_instance(self):
        self.__init__()

    # def get_data(self, state: str):
    #     query_url = f{self.session_url}