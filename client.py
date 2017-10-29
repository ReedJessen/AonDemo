import requests
import json
import pandas as pd


class IPStreetClient:
    def __init__(self):
        self.api_key = 'TGk3p1B0olaHdkGSbJSyDaMpDBPHiya688V8HOCT'
        self.page_size = 250

    def get_semantic_search(self, raw_text, filter={}):
        """accepts a raw text field and optional query filter dict, returns a semantic search response object"""
        filter.update({'page_size': self.page_size})
        endpoint = 'https://api.ipstreet.com/sandbox_v2.2/claim_only'
        headers = {'x-api-key': self.api_key, 'content-type': 'application/json'}
        payload = json.dumps({'raw_text': raw_text,
                              'q': filter})
        r = requests.post(endpoint, headers=headers, data=payload)

        response = r.json()
        print(response)
        self.semantic_results_df = pd.DataFrame(response['Assets'])

        return self.semantic_results_df

    def get_patents_by_application_numbers(self, application_numbers, page_number):
        """accepts a single patent number, returns a concatenated string of title, abstract, claims"""
        endpoint = 'https://api.ipstreet.com/v3/patent_data'
        headers = {'x-api-key': self.api_key}
        payload = json.dumps(
            {'q': {'application_number': application_numbers, 'page': page_number, 'page_size': self.page_size}})
        r = requests.post(endpoint, headers=headers, data=payload)
        response = r.json()
        print(response)
        return response

    def get_claim_scope_by_publication_numbers(self, publication_numbers):
        """accepts a single patent number, returns a concatenated string of title, abstract, claims"""
        endpoint = 'https://api.ipstreet.com/v3/patent_claim_scope_score'
        headers = {'x-api-key': 'CowP0hsIke3SYXHdFCauR9WxwYJSzOK6dL9Fr1k5'}
        payload = json.dumps({'q': {'publication_number': publication_numbers}})
        r = requests.post(endpoint, headers=headers, data=payload)
        response = r.json()
        # print(response)
        return response

    def get_bibliographic_from_semantic_results(self, semantic_results_df):
        application_numbers_list = semantic_results_df['application_number'].tolist()
        response = self.get_patents_by_application_numbers(application_numbers_list, 1)
        self.bibiographic_results_df = pd.DataFrame(response['assets'])
        return self.bibiographic_results_df

    def get_claim_scope_scores_from_semantic_results(self, semantic_results_df):
        publication_numbers_list = semantic_results_df['publication_number'].tolist()
        publication_numbers_list = [i for i in publication_numbers_list if i != '']
        response = self.get_claim_scope_by_publication_numbers(publication_numbers_list)
        self.claim_scope_results_df = pd.DataFrame(response['assets'])
        # print(self.claim_scope_results_df)
        return self.claim_scope_results_df

    def merge_semantic_bibliographic_claim_scope(self):
        semantic_results_prepped = self.semantic_results_df[['application_number', 'index_position', 'relevence_score']]
        claim_scope_results_prepped = self.claim_scope_results_df[['application_number','claim_scope_scores']]
        claim_scope_results_prepped['application_number'] = claim_scope_results_prepped['application_number'].str.replace('US','')
        claim_scope_results_prepped['application_number'] = claim_scope_results_prepped['application_number'].str.replace('-', '')
        # print(claim_scope_results_prepped)
        self.merged_semantic_bibiographic = pd.merge(self.bibiographic_results_df, semantic_results_prepped, how='left',
                                     left_on='application_number', right_on='application_number')
        self.merged_final = pd.merge(self.merged_semantic_bibiographic, claim_scope_results_prepped, how='left',
                                     left_on='application_number', right_on='application_number')

        return self.merged_final
