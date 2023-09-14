import numpy as np

def raw_data_peak(raw_list, time):

    list_value, list_time = [],[]
    time = float(time)

    def has_same_sign(num1, num2):
        return (num1 >= 0 and num2 >= 0) or (num1 < 0 and num2 < 0)
    
    def getLists(al_list):
      splitted = []
      splitted_peak = []
      nums = [al_list[0]]
      for i in range(1, len(al_list)):
        if(has_same_sign(al_list[i], al_list[i-1]) == True):
          nums.append(al_list[i])
        else:
          max_num = max(nums)
          splitted_peak.append(max_num)
          splitted.append(nums)
          nums = [al_list[i]]
      return splitted_peak,splitted
    
              
    def get_time_stamp(array_1, array_2, t ):
       time_array = []
       counter = 0

       for i in range(0, len(array_2)):
        selected_array_length = len(array_2[i])
       
        current_peak_index = array_2[i].index(array_1[i])
        
        if i != 0:
            counter = counter + len(array_2[i-1])
        
        if i == 0:
            time_array.append("{:.3f}".format(current_peak_index* t ))
        else:
            time_array.append("{:.3f}".format((current_peak_index + counter) * t))

       return time_array
    
    def splitPosNeg(list_value):
      pos, neg = [], []
      for l in list_value:
        if(l > 0):
          pos.append(l)
        else:
          neg.append(l)
      return max(pos), min(neg)
    
    list_value, splitted_values = getLists(raw_list)
    list_time = get_time_stamp(list_value, splitted_values, time)

    pos,neg = splitPosNeg(list_value)
    print("pos",pos)
    print("neg",neg)
    
    

    return list_value,list_time, pos, neg