import math

def clean_mean(sample, cutoff):
    
    def stand_dev(array):
        
        mean = sum(array) / len(array)
        sum_of_differences = sum((i - mean)**2 for i in array)
        variance = sum_of_differences / len(array) 
        return math.sqrt(variance)
    
    standard_deviation = stand_dev(sample)
    mean = sum(sample) / len(sample)
    cal_cutoff = standard_deviation * cutoff
    
    new_sample = [i for i in sample if mean - cal_cutoff <= i <= mean + cal_cutoff]
    

    if len(new_sample) == len(sample):
        result = round(sum(new_sample) / len(new_sample), 2)
        return result
    else:
        return clean_mean(new_sample, cutoff)