# Balanced Parenthesis and Valid Sentence checker

## Balanced Parenthesis
Given an input string consisting of ‘(‘ and ‘)’, a script using PLY so that the input
contains matching parenthesis. Also prints the token list.\
Example : Input : () () (()) ((())) (()())\
Output : Valid Matching. Note: The spaces are to be ignored.\
Input : (())))()()))((((()\
Output : Invalid Matching. Note: The spaces are to be ignored.

## Valid Sentence checker

Given an input string consisting of words in the English alphabet, a Python code using PLY so
that the input is correct as per the Grammatical Rules.\
In addition\
Example : Input : the cat is sleeping.\
Output : Valid Statement.\
Article Noun Verb Verb\
Input : the is the beauty.\
Output : Invalid Statement.

### Tokens used :-
- ARTICLE 
- NOUN 
- VERB 
- VERBEX 
- VERBCB 

### Token matching rules as regex
t_ARTICLE = r'(' + '|'.join(articles) + r')'\
t_NOUN = r'(' + '|'.join(nouns) + r')'\
t_VERB = r'(' + '|'.join(verbs) + r')'\
(#VERBEX is same as verbca as mention in the pdf)\
t_VERBEX = r'is|am|was|were|are'\
t_VERBCB = r'(sleeping|talking|crying|laughing|feeding|eating|bathing|grumbling|loitering|watching)'\

Brown corpus nltk package is used for for the terminals - noun, articles, verbc\

The grammar rules are specified below ->\

	sentence -> noun verb_phrase | noun verbc\
	noun -> article | NOUN\
	verbc -> VERBEX VERBCB\
	article -> ARTICLE | epsilon\
	verb_phrase -> VERB | VERBEX VERB | NOUN verb_phrase | NOUN verbc  \
