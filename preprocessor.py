import torch
from transformers import BertTokenizerFast


class Preprocessor():
    def __init__(self):
        self.tokenizer = BertTokenizerFast.from_pretrained('./models')

    """
    Function tokenize_data
    Params: input_text -> sentence that could be true or fake 
    """
    def tokenize_data(self, text):
        sent_id = self.tokenizer.batch_encode_plus(
            text, padding=True, return_token_type_ids=False)
        return sent_id

    """
    Function create_tensors
    Params: input_text -> sentence that could be true or fake 
    """
    def create_tensors(self, tokenized_input):
        test_seq = torch.tensor(tokenized_input['input_ids'])
        test_mask = torch.tensor(tokenized_input['attention_mask'])
        return test_seq, test_mask