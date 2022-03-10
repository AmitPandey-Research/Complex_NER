class Config(object):	
  apr_dir = '../model/'
  data_dir = '../corpus/'
  model_name = 'model_4.pt'
  epoch = 5
  bert_model = 'dccuchile/bert-base-spanish-wwm-cased'
  lr = 5e-5
  eps = 1e-8
  batch_size = 10
  mode = 'prediction' # for prediction mode = "prediction"
  training_data = 'es_train.conll'
  val_data = 'es_train.conll'
  test_data = 'es_dev.conll'
  test_out = 'test_prediction.csv'
  raw_prediction_output = 'raw_prediction.csv'
  hidden_dropout_prob = 0.5