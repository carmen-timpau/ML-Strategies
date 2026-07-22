**Results Summary:**

I. 70:15:15 train/validation/test:
Validation Accuracy: 1.0000
Test Accuracy: 0.9630


II. 60:20:20 train/validation/test:
Validation Accuracy: 0.9444
Test Accuracy: 0.9444


III. 70:30 train/test:
Test Accuracy: 0.9630


IV. 60:40 train/test:
Test Accuracy: 0.9583


**Discussion:**

 - 60:20:20 split vs 70:15:15:

Splitting the data into 60:20:20 train/validation/test sets yields the same accuracies (0.9444, high and satisfactory) when evaluating the 
validation and test sets, which shows that the model has a great ability to consistently generalise well when working with previously unseen data, 
which is an ideal trait for an ML model.

Even if when going from a 60:20:20 to a 70:15:15 ratio for the training/validation/test sets the validation accuracy improves from 0.9444 to 1.0000 
and the test accuracy improves from 0.9444 to 0.9630, this is not exactly what the goal of hyperparameter tuning is. Achieving very high accuracies 
is great, but it loses its importance when the model lacks performance consistency (good generalisation). The model should ideally be able to generalise 
properly and consistently to unseen data sets and this is what will truly support its reliability as a model.

The discrepancy between the 60:20:20 and 70:15:15 splits comes from the amount of data which was fed into model training. When using a 70:15:15 split, 
the model is trained on slightly more data than during a 60:20:20 split. This might cause a slight overfitting on training data, which can be reflected 
by a perfect accuracy (by chance) when evaluating the model on that specific validation set, but lower accuracy when using another unseen data set (the 
test set). This translates to poor generalisation, as the model accuracy is obviously dependent on the specific data set that is fed into it, which we 
want to avoid.


 - Omitting the validation set altogether:

Furthermore, if we go on to omit the validation set altogether, the test accuracies we obtain (0.9583 for 60:40 train/test & 0.9630 for 70:30 train/test)
are good, but because we don’t have a validation set, we cannot compare this value with any others, thus this is an unreliable result to base any important 
decisions on and therefore this is not a recommended strategy for data splitting when building your ML model.
