 

from typing import Optional

import torch

# General
hidden_size: int = 512
dec_hidden_size: Optional[int] = 512
embed_size: int = 512
pointer = True

# Data
max_vocab_size = 20000
embed_file: Optional[str] = None  # use pre-trained embeddings
source = 'big_samples'    # use value: train or  big_samples 
data_path: str = '/content/project_2/model/files/{}.txt'.format(source)
val_data_path: Optional[str] = '/content/project_2/model/files/dev.txt'
test_data_path: Optional[str] = '/content/project_2/model/files/test.txt'
stop_word_file = '/content/project_2/model/files/HIT_stop_words.txt'
max_src_len: int = 300  # exclusive of special tokens such as EOS
max_tgt_len: int = 100  # exclusive of special tokens such as EOS
truncate_src: bool = True
truncate_tgt: bool = True
min_dec_steps: int = 30
max_dec_steps: int = 500
enc_rnn_dropout: float = 0.5
enc_attn: bool = True
dec_attn: bool = True
dec_in_dropout = 0
dec_rnn_dropout = 0
dec_out_dropout = 0


# Training
trunc_norm_init_std = 1e-4
eps = 1e-31
learning_rate = 0.001
lr_decay = 0.0
initial_accumulator_value = 0.1
epochs = 8
batch_size = 32
coverage = True
fine_tune = False
scheduled_sampling = False
weight_tying = False
max_grad_norm = 2.0
is_cuda = True
DEVICE = torch.device("cuda" if is_cuda else "cpu")
LAMBDA = 1

print('coverage:',coverage)
print('Finetune:',fine_tune)
if pointer:
    if coverage:
        if fine_tune:
            model_name = 'ft_pgn'
        else:
            model_name = 'cov_pgn'
    elif scheduled_sampling:
        model_name = 'ss_pgn'
    elif weight_tying:
        model_name = 'wt_pgn'
    else:
        if source == 'big_samples':
            model_name = 'pgn_big_samples'
        
else:
    model_name = 'baseline'

encoder_save_name = '/content/project_2/model/saved_model/' + model_name + '/encoder.pt'
decoder_save_name = '/content/project_2/model/saved_model/' + model_name + '/decoder.pt'
attention_save_name = '/content/project_2/model/saved_model/' + model_name + '/attention.pt'
reduce_state_save_name = '/content/project_2/model/saved_model/' + model_name + '/reduce_state.pt'
losses_path = '/content/project_2/model/saved_model/' + model_name + '/val_losses.pkl'
log_path = '/content/project_2/model/runs/' + model_name


# Beam search
beam_size: int = 3
alpha = 0.2
beta = 0.2
gamma = 2000
