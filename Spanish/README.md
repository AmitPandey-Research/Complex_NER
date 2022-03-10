Models for Name Entity Recognition in pytorch</br>

**Setting up the initial requirements** <br>
pip install -r requirements.txt<br>

**For traninig a model**: <br>
Keep the training data file in the corpus directory<br>
cd Spanish_NER <br>
python BERT_Linear(or)BERT_CRF(or)BERT_BiLSTM_CRF.py --mode train <br>

**For testing the model**: <br>
Keep the test/dev data file in the corpus directory<br>
cd Spanish_NER <br>
python BERT_Linear(or)BERT_CRF(or)BERT_BiLSTM_CRF.py --mode test <br>
