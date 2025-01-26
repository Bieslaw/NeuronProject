
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

###Eksperymet #3
####Temperatura
Model bazowy:
* train
	* Mean absolute error: 2.224468288295613
	* Fraction of predictions with absolute error <= 2: 0.5564064053476614
* test
	* Mean absolute error: 2.190860158016228
	* Fraction of predictions with absolute error <= 2: 0.5778095849168353

Model A:
* train
	* Mean absolute error: 3.885937565076981
	* Fraction of predictions with absolute error <= 2: 0.2896579442810907
* test
	* Mean absolute error: 4.373468597912471
	* Fraction of predictions with absolute error <= 2: 0.23947485316618133

Model B:
* train
	* Mean absolute error: 2.8950658878883457
	* Fraction of predictions with absolute error <= 2: 0.44014553762189834
* test
	* Mean absolute error: 2.8562665584401485
	* Fraction of predictions with absolute error <= 2: 0.44760870638171857

Model C:
* train
	* Mean absolute error: 3.420493176038504
	* Fraction of predictions with absolute error <= 2: 0.36335751909123604
* test
	* Mean absolute error: 3.231835450897093
	* Fraction of predictions with absolute error <= 2: 0.40027639307043084


#### Wiatr
Model bazowy:
* train
	* ROC_AUC: 0.8946494058812555
* test
	* ROC_AUC: 0.7575780489670345

Model A:
* train
	* ROC_AUC: 0.9235322304553445
* test
	* ROC_AUC: 0.7359713849721106

Model B:
* train
	* ROC_AUC: 0.8920216206609455
* test
	* ROC_AUC: 0.7655038960096339

Model C:
* train
	* ROC_AUC: 0.9165502355096555
* test
	* ROC_AUC: 0.7293944054175762


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
