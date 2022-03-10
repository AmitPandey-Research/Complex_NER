# BERT_CRF
BERT_CRF model for Name Entity Recognition in pytorch</br>

**Setting up the initial requirements** <br>
pip install -r requirements.txt<br>

**For traninig a model**: <br>
Keep the training data file in the corpus directory<br>
cd bert-crf4NER <br>
python bert_crf.py --mode train <br>

**For testing the model**: <br>
Keep the test/dev data file in the corpus directory<br>
cd bert-crf4NER <br>
python bert_crf.py --mode test <br>

