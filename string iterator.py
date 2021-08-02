#adam locke 2021 June
#a script to consider strings and hunt for specific words, then respond based upon the word detected.

#a dictionary of relevant words that the script will hunt for.
target_list = {'deku':'nerd','bakugou':'king', 'todoroki':'edgelord'}
target_string = ''
compare_list=[]

def get_string():
    global target_string
    print("ready for string analyis.")
    target_string = input("Who is your favorite UA student?\n")

def string_analysis():
    global target_string
    global compare_list
    analysis_string=target_string+' '
    print(analysis_string)
    word= []
    wordcount=0
    relevant_count=0
    multichoice=False
    nochoice=False
    comparison=''
    compare_list=[]
    for element in analysis_string:
        word.append(element)
        if element == ' ':
            comparison= comparison.join(word)
            comparison.lower()
            comparison_slice=comparison[:-1]
            compare_list.append(comparison_slice)
            #wordcount = +1
            #print(wordcount)
            word=[]
            #print(comparison)
            comparison=''
    #print(compare_list)


def compare_words():
    global compare_list
    global target_list
    relevant_words=0
    result_list=[]
    multichoice=False
    #nochoice=False
    conclusion=''
    #two problems: none of the keys will ever line up because it's sticking a space on the end of each word, we need to eliminate that space before the dictionary check.  the new for loop is trying to fix that, but i need to remove the item from the list and then append it to another list after editing as it, it seems inefficient.
    for items in compare_list:
        cut_target=items
        cut_result=cut_target[:1]
        result_list.append(cut_result)
    #so now I have a list of cleaned up lower case words for the machine to interpret, now we need to check and see if any of them are in the dictionary with a for loop.
    for items in compare_list:
        if items in target_list and relevant_words==0:
            relevant_words=+1
            conclusion=items
        elif items in target_list and relevant_words>0:
            multichoice=True
        else:
            pass
        '''
        check=
        if check=='irrelevant':
            print("analyzed a word ", items," but it was irrelevant")
            pass
        elif relevant_words==0:
            relevant_words= +1
            conclusion=items
            #print("I see you mentioned ",conclusion," so I suppose you like a hero who is a",target_list[conclusion],"."
        elif relevant_words>1:
            multichoice=True
        else:
            nochoice==True'''
    if conclusion=='':
        #print(relevant_words)
        print("Indecisive?  Or could it be that you don't watch MHA?")
    elif multichoice==True:
        #print(relevant_words)
        print("I don't have any time for people who cannot make up their minds.\nMention only one hero next time.")
    else:
        #print(relevant_words)
        print("I see you mentioned ",conclusion," so I guess you prefer a hero who is a ",target_list[conclusion],".")
            
            
    
    
    '''for items in compare_list:
        if items==target_list[items] and relevant_count==0:
            relevant_count= +1
            wordcount= +1
            conclusion= comparison
            comparison=''
        elif items==target_list[items] and relevant_count>0:
            multichoice=True
            wordcount= +1
            comparison=''
        elif items==target_list[items] and relevant_count==0 and compare_list[items]==compare_list[-1]:
            nochoice=True
            wordcount= +1
            comparison=''
        else:
            wordcount= +1
            pass'''

'''    if multichoice==False and nochoice==False:
        print("I see you mentioned ",conclusion," so I guess you prefer a hero who is a ",target_list[conclusion])
    elif multichoice==True and nochoice==False:
        print('No wishy washy nonsense, only one hero can be chosen.')
    else:
        print("It's okay if you're still thinking of who is your favorite.")
        
    print("String analysis complete, there were ",wordcount," words and ",relevant_count,"relevant words.")'''

get_string()
string_analysis()
compare_words()
