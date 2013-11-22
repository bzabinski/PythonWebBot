import curlfunctions
import parser
import vars
from mongoDB import database
from mongoDB import collection


myDB = database()
myDB.connectToDB(vars.DATABASE_NAME)
col_id2name = myDB.connectToCollection(vars.ID2NAME_COL)
col_wiki = myDB.connectToCollection(vars.WIKI_COL)
wiki_page = curlfunctions.get_http(vars.WIKI_URL)
parser.parse_wiki(wiki_page)
#parser.parse_ebay()
#print(wiki_page)