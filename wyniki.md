
### Eksperyment 1
#### Temperatura
* Model podstawowy:
    * train
	    * Mean absolute error: 2.20208238667285
	    * Fraction of predictions with absolute error <= 2: 0.5622659869269985
    * test
	    * Mean absolute error: 2.1953617559497656
	    * Fraction of predictions with absolute error <= 2: 0.5786979912146488
* Dzień roku jako sin, cos
* Kierunek wiatru jako sin, cos
* Obie optymalizacje
### Wiatr
* Model podstawowy
    * train
	    * ROC_AUC: 0.8960369436549291
    * test
	    * ROC_AUC: 0.7553192052905189
* Dzień roku jako sin, cos
* Kierunek wiatru jako sin, cos
* Obie optymalizacje


###Eksperyment 2
#### Temperatura
MSE
* train
	* Mean absolute error: 2.7366398443966724
	* Fraction of predictions with absolute error <= 2: 0.4564493905670376
* test
	* Mean absolute error: 3.2020090362711473
	* Fraction of predictions with absolute error <= 2: 0.36040358079034573

MAE
* train
	* Mean absolute error: 2.7153965778624434
	* Fraction of predictions with absolute error <= 2: 0.47406465288818234
* test
	* Mean absolute error: 3.2426464396045653
	* Fraction of predictions with absolute error <= 2: 0.34996785202037684

#### Wiatr
Cross Entropy
* train
	* ROC_AUC: 0.8568076843225534
* test
	* ROC_AUC: 0.6623236636447205

Focal Loss
* train
	* ROC_AUC: 0.956059191720526
* test
	* ROC_AUC: 0.6340628170325261

###Eksperymet #3
####Temperatura
Model bazowy:
* train
	* Mean absolute error: 2.7366398443966724
	* Fraction of predictions with absolute error <= 2: 0.4564493905670376
* test
	* Mean absolute error: 3.2020090362711473
	* Fraction of predictions with absolute error <= 2: 0.36040358079034573

Model A:
* train
	* Mean absolute error: 7.021524060770603
	* Fraction of predictions with absolute error <= 2: 0.13971383147853733
* test
	* Mean absolute error: 7.634810577571083
	* Fraction of predictions with absolute error <= 2: 0.12953162866610612

Model B:
* train
	* Mean absolute error: 3.1771367505403685
	* Fraction of predictions with absolute error <= 2: 0.3767037625861155
* test
	* Mean absolute error: 3.6946716206128265
	* Fraction of predictions with absolute error <= 2: 0.30426826252534744

Model C:
* train
	* Mean absolute error: 4.862332956343701
	* Fraction of predictions with absolute error <= 2: 0.23249602543720194
* test
	* Mean absolute error: 5.384959335249013
	* Fraction of predictions with absolute error <= 2: 0.19872397250111284


#### Wiatr
Model bazowy:
* train
	* ROC_AUC: 0.8568076843225534
* test
	* ROC_AUC: 0.6623236636447205

Model A:
* train
	* ROC_AUC: 0.8958818590728733
* test
	* ROC_AUC: 0.6315882784791245

Model B:
* train
	* ROC_AUC: 0.8472582955958052
* test
	* ROC_AUC: 0.6839878636916268

Model C:
* train
	* ROC_AUC: 0.887167637953014
* test
	* ROC_AUC: 0.628390203745488

###Eksperymet #4
####Temperatura
ReLU:
* train
	* Mean absolute error: 2.724203995068045
	* Fraction of predictions with absolute error <= 2: 0.459523052464229
* test
	* Mean absolute error: 3.1945998443192
	* Fraction of predictions with absolute error <= 2: 0.36114545724318714

Sigmoid:
* train
	* Mean absolute error: 2.827857809330305
	* Fraction of predictions with absolute error <= 2: 0.45059883412824586
* test
	* Mean absolute error: 3.180940351909937
	* Fraction of predictions with absolute error <= 2: 0.3741035659528167


####Wiatr
ReLU:
* train
	* ROC_AUC: 0.8610908552477988
* test
	* ROC_AUC: 0.6534520096436296

Sigmoid:
* train
	* ROC_AUC: 0.7943021887848039
* test
	* ROC_AUC: 0.6883210103436285
