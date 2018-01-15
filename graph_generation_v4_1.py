import timeit 
import sqlite3 
import matplotlib.pyplot as plt
import networkx as nx
from multiprocessing import Pool, Lock 


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
user_set  = sorted(user_set)
#user_set = list(user_set)
chunk_size = 1000




def find_weights(user_nodes):
    (i,j) = user_nodes
    
    all_tweet_indices_of_user_i = [l for l, k in enumerate(user) if k[0] == i]
    hashtags_used_by_user_i = [p.lower() for a in all_tweet_indices_of_user_i 
                            for p in h_tags[a][0].split(',')]
    #user_mentions_used_by_user_i = [u for a in all_tweet_indices_of_user_i
                                #for u in user_mentions[a][0].split(',')]
    all_tweet_indices_of_user_j = [l for l, k in enumerate(user) if k[0] == j]
    hashtags_used_by_user_j = [p.lower() for a in all_tweet_indices_of_user_j 
                            for p in h_tags[a][0].split(',')]                             
    #user_mentions_used_by_user_j = [u for a in all_tweet_indices_of_user_j
                                #for u in user_mentions[a][0].split(',')]
                                    
    #common_user_mentions = list(set(user_mentions_used_by_user_i).intersection(user_mentions_used_by_user_j))
    common_hashtags = list(set(hashtags_used_by_user_i).intersection(hashtags_used_by_user_j))
    #user_mention_weight = len(common_user_mentions)
    hashtag_weight = len(common_hashtags)
    #weight = hashtag_weight + user_mention_weight
    weight = hashtag_weight
    if weight > 0:
        return (i,j,weight)

length_user_set = len(user_set)


def main():
    for q in range(22, len(user_set)):
        print(q, '/',length_user_set)
        for r in range(q, len(user_set), chunk_size):
            try:
                user_sub_set = user_set[r:r+chunk_size-1]
            except IndexError:
                user_sub_set = user_set[r:len(user_set)]
            except Exception as E:
                print(str(E))
            #start_time = timeit.default_timer()
            p = Pool(processes = 30)
            #print('entering multiprocessing')
            interaction_weight = p.map(find_weights, [(user_set[q],r) for r in user_sub_set])
            p.close()
            print(r,' : done')
            node_interactions = [i for i in interaction_weight if i is not None]
            with open('node_interactions.txt','a') as f:
                f.write(str(node_interactions))
            #total_duration = timeit.default_timer() - start_time
            #print(total_duration)

if __name__ == '__main__':
    main()

