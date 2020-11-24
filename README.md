# Title: Detecting political division on Twitter
# Abstract
While the paper explores the general Twitter graph properties, we propose to study if we can detect political division in the graph. To do so, we propose to build an additional dataset with US politicians' Twitter handles and political alignments, and assign their corresponding nodes in the Twitter graph an appropriate label (e.g. "democrat" or "republican"). We will then run a community detection algorithm on the Twitter graph of followers, and see whether we can detect political clusters and their shapes, and to what extent they may be connected. Since visualizing the full graph may be challenging due to its size, we may have to find alternative methods to study the result. This would allow us to understand a small part of the political landscape, and reflect on how it reflects or affects the real landscape, and how that can be improved (for example, by encouraging more cross-party communication).
# Research questions
1. Is there a political division on US Twitter?
2. How big are the political clusters? Are they the norm, or more of an exception?
3. To what extent do highly-partisan people communicate with the other party? 
# Proposed datasets
"Social graph" dataset from the paper -- This dataset only lets us know who follows who on Twitter. The only data we have is each user's Twitter ID.
"TwitterHandles.csv" from the “Democrat Vs. Republican Tweets” Kaggle dataset. This dataset assigns a political leaning label ("Democrat" or "Republican") to US politicians' Twitter handles.
We will then need to enrich this dataset by using the Twitter API to get the Twitter user ID for each handle.

