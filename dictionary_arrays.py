def add_element(key,list_element,sample):
    dic = {}
    dic[key] = list_element;
    sample.append(dic);



sample_dictionary =     [{"france" :["paris1","paris2"]},{"france" :["Bezing1","bezing2"]}]
print(sample_dictionary)
#add_element("Russia",["Masco1","Masco2"],sample_dictionary)
#print(sample_dictionary)
sample_dictionary.insert(1,{"Russia":["Masco1","Masco2"]})
print(sample_dictionary)