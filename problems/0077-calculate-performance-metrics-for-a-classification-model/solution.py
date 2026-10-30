import numpy as np
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	# Implement your code here
	actual=np.asarray(actual)
	predicted=np.asarray(predicted)
	tp=np.sum((actual==1) & (predicted==1))
	tn=np.sum((actual==0) & (predicted==0))
	fp=np.sum((actual==0) & (predicted==1))
	fn=np.sum((actual==1) & (predicted==0))
	confusion_matrix=[[tp.item(),fn.item()],[fp.item(),tn.item()]]
	accuracy=(tp+tn)/(tp+fp+fn+tn)
	specificity=tn/(tn+fp)
	negativePredictive=tn/(tn+fn)
	f1=(2*tp)/(2*tp + fp + fn)
	return confusion_matrix,np.round(accuracy, 3).item(), np.round(f1, 3).item(), np.round(specificity, 3).item(), np.round(negativePredictive, 3).item()
