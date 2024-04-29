import ply.lex as lex
import ply.yacc as yacc
import nltk
from nltk.corpus import brown

# Fetching words from Brown corpus
nltk.download('brown')  
words = brown.words()
tagged_words = brown.tagged_words()

# Collect words for each POS tag

#words of POS type AT stored in a terminal articles
articles = set()
#append the (lower case) articles which are not in articles set untill the length is 3 from the tag.
for word, tag in tagged_words:
    if tag == 'AT' and word.lower() not in articles:
        articles.add(word.lower())
        if len(articles) == 3:
            break

#words of POS type 'NN', 'NNS', 'NP', 'NPS' stored in a terminal nouns
nouns = set()
#append the (lower case) words which are not in nouns set untill the length is 10 from the tag.
for word, tag in tagged_words:
    if tag in ('NN', 'NNS', 'NP', 'NPS') and word.lower() not in nouns:
        nouns.add(word.lower())
        if len(nouns) == 10:
            break

#words of POS type 'VB'stored in a terminal verbs
verbs = set()
#append the (lower case) verbs which are not in verbs set untill the length is 10 from the tag.
for word, tag in tagged_words:
    if tag == 'VB' and word.lower() not in verbs:
        verbs.add(word.lower())
        if len(verbs) == 10:
            break


# tokens used
tokens = (
    'ARTICLE',
    'NOUN',
    'VERB',
    'VERBEX',
    'VERBCB',
)

#print(articles)
#print(nouns)
#print(verbs)

# Token matching rules as regex
t_ARTICLE = r'(' + '|'.join(articles) + r')'
t_NOUN = r'(' + '|'.join(nouns) + r')'
t_VERB = r'(' + '|'.join(verbs) + r')'
t_VERBEX = r'is|am|was|were|are'
t_VERBCB = r'(sleeping|talking|crying|laughing|feeding|eating|bathing|grumbling|loitering|watching)'

# Ignored spaces
t_ignore = ' '

# Error handler for illegal characters
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Grammar rules defining
def p_sentence(p):
    """
    sentence : noun verb_phrase
    | noun verbc

    """
    print("Valid statement")


#define noun
def p_noun(p):
    """
    noun : article
                | NOUN
    """
    pass
    
#define verbc    
def p_verbc(p):
	"""
	verbc : VERBEX VERBCB
	
	"""
	pass
	

#define article
def p_article(p):
    '''
    article : ARTICLE
    | empty
    '''
    pass
    
    
#define verb_phrase
def p_verb_phrase(p):
    """
    verb_phrase : VERB
                | VERBEX VERB
                | NOUN verb_phrase
                | NOUN verbc         
               
    """
    
#define error
def p_error(p):
   print("Invalid statement")
   #pass


#define empty
def p_empty(p):
    '''
    empty :
    '''
    p[0] = ""

# Build the parser
parser = yacc.yacc()


# define the grammar checker
def check_grammar(sentence):
    # Input validation
    words = sentence.split()
    #input sentences of size at least 2 words and a maximum of 8 words are accepted else rejected
    if len(words) < 2 or len(words) > 8:
        print("Invalid statement")
        return

    parser.parse(sentence, lexer=lexer)
   
#taking user input
sentence = input("Enter a sentence: ")
check_grammar(sentence)

