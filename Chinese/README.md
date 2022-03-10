Models for Name Entity Recognition in pytorch

Setting up the initial requirements
pip install -r requirements.txt

For traninig a model:
Keep the training data file in the corpus directory
cd Chinese_NER
python BERT_Linear(or)BERT_CRF(or)BERT_BiLSTM_CRF.py --mode train

For testing the model:
Keep the test/dev data file in the corpus directory
cd Chinese_NER
python BERT_Linear(or)BERT_CRF(or)BERT_BiLSTM_CRF.py --mode test

