import timeit 
import sqlite3 
import matplotlib.pyplot as plt
import networkx as nx
from multiprocessing import Pool 


# Accessing the Structured data using Sqlite 
db_con = sqlite3.connect('Tweets.db') # creating and connecting for our database file 
c = db_con.cursor() # this will be our cursor 
c.execute('SELECT user_screen_name FROM TweetsDataTable ORDER by id_n ASC') 
user = [usr 
        for usr in c.fetchall()]
c.execute('SELECT hashtags FROM TweetsDataTable ORDER by id_n ASC') 
h_tags = [tags 
        for tags in c.fetchall()]
c.execute('SELECT user_mentions_screen_name FROM TweetsDataTable ORDER by id_n ASC') 
user_mentions = [usr_m 
        for usr_m in c.fetchall()]

user_set = set([i[0] for i in user])

def find_weights(user_nodes):
    (i,j) = user_nodes
    #debug = 0
    #sql_version = 0
    #if sql_version:
        #c.execute('SELECT hashtags FROM TweetsDataTable WHERE user_screen_name = ?', (i,)) 
        #hashtags_used_by_user_i = [p.lower() for hashtag in c.fetchall() for p in hashtag[0].split(',')]
      
        #c.execute('SELECT user_mentions_screen_name FROM TweetsDataTable WHERE user_screen_name = ?', (i,)) 
        #user_mentions_used_by_user_i = [u for user_mentions in c.fetchall() for u in user_mentions[0].split(',')]                    
                
        #c.execute('SELECT hashtags FROM TweetsDataTable WHERE user_screen_name = ?', (j,)) 
        #hashtags_used_by_user_j = [p.lower() for hashtag in c.fetchall() for p in hashtag[0].split(',')]
        
        #c.execute('SELECT user_mentions_screen_name FROM TweetsDataTable WHERE user_screen_name = ?', (j,)) 
        #user_mentions_used_by_user_j = [u for user_mentions in c.fetchall() for u in user_mentions[0].split(',')]                   
        
    #else:
    all_tweet_indices_of_user_i = [l for l, k in enumerate(user) if k[0] == i]
    hashtags_used_by_user_i = [p.lower() for a in all_tweet_indices_of_user_i 
                            for p in h_tags[a][0].split(',')]
    user_mentions_used_by_user_i = [u for a in all_tweet_indices_of_user_i
                                for u in user_mentions[a][0].split(',')]
    all_tweet_indices_of_user_j = [l for l, k in enumerate(user) if k[0] == j]
    hashtags_used_by_user_j = [p.lower() for a in all_tweet_indices_of_user_j 
                            for p in h_tags[a][0].split(',')]                             
    user_mentions_used_by_user_j = [u for a in all_tweet_indices_of_user_j
                                for u in user_mentions[a][0].split(',')]
                                    
    common_user_mentions = list(set(user_mentions_used_by_user_i).intersection(user_mentions_used_by_user_j))
    common_hashtags = list(set(hashtags_used_by_user_i).intersection(hashtags_used_by_user_j))
    user_mention_weight = len(common_user_mentions)
    hashtag_weight = (1/3.0)*(len(common_hashtags))
    weight = hashtag_weight + user_mention_weight

    if weight > 0:
        return (i,j,weight)


    #if debug:
     #   print(all_tweet_indices_of_user_i)
    # print(hashtags_used_by_user_i)
    #print(user_mentions_used_by_user_i)
    #print(all_tweet_indices_of_user_j)
    #print(hashtags_used_by_user_j)
    #print(user_mentions_used_by_user_j)
    #print(common_user_mentions)
    #print(common_hashtags)
     #   print(hashtag_weight)
     #   print(user_mention_weight)
     #   print(weight)


nw = nx.Graph()
USER_SET= list(user_set)

user_set = USER_SET[5:10]

start_time = timeit.default_timer()

if __name__ == '__main__':
    p = Pool(processes = 4)
    print('entering multiprocessing')
    interaction_weight = p.map(find_weights, [(user_set[i],user_set[j]) for i in range(len(user_set)) for j in range(i+1, len(user_set))])
        #print([(user_set[0],user_set[1])])
        #interaction_weight = p.map(find_weights, (user_set[0],user_set[1]))
    print('done')
    p.close()
total_duration = timeit.default_timer() - start_time
print(total_duration)
print(interaction_weight)




if 0:
    nw = nx.Graph()
    if __name__ == '__main__':
        p = Pool(processes = 50)
        for i in list(user_set)[0:3]:
            for j in list(user_set)[0:5]:
                #print(i,j)
                if (i,j) in checked:
                    checked.append((j,i)) 
                    continue
                elif i == j:
                    checked.append((j,i)) 
                    continue
                else:
                    #interaction_weight = p.map(find_weights, [(i,j)])
                    interaction_weight = p.map(find_weights, [i for i in interaction_nodes])
                    checked.append((j,i)) 
                    #print(interactions)
                    if interaction_weight[0] > 0:
                        nw.add_edge(i,j,weight = interaction_weight)
    p.close()


    def add_interaction(i,j):
        if (i,j) in checked:
            return  [(j,i), (i,j,0.0)] 
        
        elif i == j:
            return  [(j,i), (i,j,0.0)] 
            
        else:
            total_weight = find_weights(i,j)
            #if total_weight > 0:
                #nw.add_edge(i,j,weight = total_weight)
                #print(w/len(user_set)*100)
        return  [(j,i), (i,j,total_weight)] 
     
        

    if 0:
        interaction_nodes= []
        counter = 0
        for i in range(len(user_set)-1):
                print(counter, (counter/len(user_set))*100)
                counter+= 1
                for j in range(i+1, len(user_set)):
                    interaction_nodes.append((user_set[i],user_set[j]))
