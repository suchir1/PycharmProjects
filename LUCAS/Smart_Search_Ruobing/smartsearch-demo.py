
# coding: utf-8

# In[ ]:

#user, 
from SEARCH_BING_MODULE import bingURL
from SEARCH_YAHOO_MODULE import yahooURL
from SVO_SENT_MODULE_spacy import SVOSENT
import time


# In[ ]:

Subject='North Korea'
CAMEO= 'Threaten unconventional attack'
Object=''
sentence=Subject+' '+CAMEO+' '+Object # subject+cameo code


# In[ ]:

bing=bingURL()
t0=time.time()
urls=bing.search_urls(sentence,1)
t1=time.time()
print('time cost:',t1-t0)
print('#urls found:',len(urls))


# In[ ]:

import SCRAPER
articles=SCRAPER.scrape_from_urls(urls)


# In[ ]:

svo_sent = SVOSENT()
import pandas as pd
articles=svo_sent.split_and_clean(articles)
import time
t0=time.time()
results=[]
for i,article in enumerate(articles):
    try:
        result=svo_sent.svo_senti_from_article(article)
        results.append(result)
        print(i+1,'th/',len(articles),'article is done')
        
    except Exception as e: 
        print(i,'th article has error:',e)
#result2=svo_sent.svo_senti_from_article(article,'Robin')
t1=time.time()
results=pd.concat(results, axis=0)
print('time cost',end=':')
print(t1-t0)

#svo_sent.WriteCSV(results,'corpus4_full_dataset')


# In[ ]:

results


# In[ ]:

results.to_csv('test2.csv',index=False)


# In[ ]:

import CAMEO_CONVERT
results['Names']= results['Names'].apply(lambda x : CAMEO_CONVERT.toCAMEO(x))


# In[ ]:

results


# In[ ]:

import numpy as np
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                              'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})


# In[ ]:



# In[ ]:



