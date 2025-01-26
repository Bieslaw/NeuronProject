
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
	* Mean absolute error: 2.224468288295613
	* Fraction of predictions with absolute error <= 2: 0.5564064053476614
* test
	* Mean absolute error: 2.190860158016228
	* Fraction of predictions with absolute error <= 2: 0.5778095849168353


MAE
* train
	* Mean absolute error: 2.1749646674385086
	* Fraction of predictions with absolute error <= 2: 0.5805004971125167
* test
	* Mean absolute error: 2.1710920349148526
	* Fraction of predictions with absolute error <= 2: 0.5876314100982183

#### Wiatr
Cross Entropy
* train
	* ROC_AUC: 0.8946494058812555
* test
	* ROC_AUC: 0.7575780489670345


Focal Loss
* train
	* ROC_AUC: 0.9678768633465775
* test
	* ROC_AUC: 0.7364716928598911




