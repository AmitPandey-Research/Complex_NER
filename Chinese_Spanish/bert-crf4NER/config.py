class Config(object):	
  apr_dir = '../model/'
  data_dir = '../corpus/'
  model_name = 'model_0.pt'
  epoch = 1
  bert_model = 'bert-base-uncased'
  lr = 5e-5
  eps = 1e-8
  batch_size = 10
  mode = 'prediction' # for prediction mode = "prediction"
  training_data = 'en_train.conll'
  val_data = 'trainbio.txt'
  test_data = 'en_dev.conll'
  test_out = 'test_prediction.csv'
  raw_prediction_output = 'raw_prediction.csv'
  hidden_dropout_prob = 0.5