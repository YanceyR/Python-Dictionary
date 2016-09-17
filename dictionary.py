import csv

 
#operations for text file
def save_dict(file_name,dict_rap):
    global f
    f = open(file_name, 'w')
    w = csv.writer(f)
    for key, val in dict_rap.items():
        w.writerow([key] + val)
    f.close()
     
def read_dict(file_name):
    f = open(file_name,'r')
    dict_rap={}
    for value in csv.reader(f):
        for i in range(len(value)):
            if i == 0:
                key = value[i]
                dict_rap[key] = []
            else:
                dict_rap[key].append(value[i])
    f.close()
    return(dict_rap)
    
file_name = 'dict.txt'
urbandict = read_dict(file_name)
#end



#Body of program
def lookup():
    key = input('What word are you looking for {}?: '.format(name)).lower()
    if key in urbandict:
        for i in urbandict[key][i]:
            print(i)
    else:
        alt = input('Sorry, {} is currently not in this dictionary, do you want to add it?, Yes or No: '.format(key)).lower()
        if alt == 'yes':
            add_dict()
        else:
            print('Returning back to Main Menu.')
            urban_dict()

def reverse_lookup(urbandict):
    v = input('What definition are you looking for?: ').lower()
    for key in urbandict:
        if urbandict[key] == [v]:
            print(key)       
    urban_dict()
   
def display(urbandict):
    print()
    for key in urbandict:
       for meaning in urbandict[key]:
           print(key,':', meaning)
    urban_dict()

def add_dict():
    key = input('What word do you want to add to the dictionary?: ').lower()
    if key in urbandict:
        for meaning in urbandict[key]:
           print(key,':', meaning)
        add = input('{} already exists, do you want to add a new definition?, Yes or No: '.format(key)).lower()
        if add == 'yes':
            exdef = input('Type in your new definition: ')
            urbandict.setdefault(key,[]).append(exdef)
            print('Your entry was a success!'.format(name))
            save_dict(file_name, urbandict)
        else:
            print('Returning back to Main Menu.')
            urban_dict()                        
    else:
            mdef = input('Type in your definion for {}: '.format(key))
            urbandict[key] = [mdef]
            print('Your entry was a success {}!'.format(name))
            save_dict(file_name, urbandict)
            urban_dict()
          
def remove_dict(urbandict):
    pref = int(input('[1]Do you want to remove a word or a [2]definition from a word, please enter 1 or 2: '))
    if pref == 1:
        word = input('What word do you want to remove?: ').lower()
        del urbandict[word]
        save_dict(file_name, urbandict)               
        print('The removal process was a success {}!'.format(name))
    elif pref == 2:
        key = input('What word do you want to remove a definition from?: ').lower()
        for index, element in enumerate(urbandict[key]):
            print(index, element)
        num = int(input("Enter number for definion you want to delete: "))
        for i, j in enumerate(urbandict[key]):
            if i == num:
                urbandict[key].remove(j)
                urbandict = {k:v for k,v in urbandict.items() if v != []}
                save_dict(file_name, urbandict)
        print('The removal process was a success {}!'.format(name))
    else:
        print('Sorry, your input was invalid {}'.format(name))
        remove_dict()
    urban_dict()
#end

#Control center for program
name = input('Hello there curious cat, what shall I call you?: ')
print('Nice to meet you {}, what do you want to do?: '.format(name))
def urban_dict():
    print()
    print('A.Search for a term \nB.'
          'Lookup definion for term \nC.'
          'Display all current definitions \nD.'
          'Add a new word or definiton to a current word \ne.'
          'Remove a word or definion to a current word')
    ans = input("Please choose the corresponding letter {}, or enter 'Exit': ".format(name)).lower()
    if ans == 'a':
        lookup()
    elif ans == 'b':
        reverse_lookup(urbandict)
    elif ans == 'c':
        display(urbandict)
    elif ans == 'd':
        add_dict()
    elif ans == 'e':
        remove_dict(urbandict)
    elif ans == 'exit':
        print('Thank you for improving your vocab {}, goodbye!'.format(name))
    else:
        print('Sorry, your input was invalid {}'.format(name))
        urban_dict()
#end


#starting program
urban_dict()
