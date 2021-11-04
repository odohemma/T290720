import pywikibot

# Connect to english wiki
en_wiki = pywikibot.Site('en', 'wikipedia')

# Then connect to wikidata
en_wiki_repo = en_wiki.data_repository()


def edit_article(page_to_be_edited):
    text = page_to_be_edited.get()
    # Append hello at the end of the page
    text = text + '\n' + 'Hello'
    print ("'Hello' has been appended to the page." + '\n')
    page_to_be_edited.text = text
    try:
        page_to_be_edited.save("The edited copy has been saved.")
        return True
    except:
        print ('\n' + "The edit(s) cannot be saved.")
        return False
    

def print_wikidata(wikidata_item, p_number):
   q_number = wikidata_item.title()
   print(q_number)
   item_dict = wikidata_item.get()
   try:    
       for claim in item_dict['claims'][p_number]:
           value = claim.getTarget()
           item_dict = value.get()
           print(p_number + ' value: ' + value.title())
           print(p_number + ' label: ' + item_dict['labels']['en'])      
   except: 
       print("Problem with the page, this did not work.")       
   return False


page_to_be_edited = pywikibot.Page(en_wiki_repo, 'User:Odohemma/Outreachy_1')


# Print of page to be edited
print(page_to_be_edited.text)


# editarticle function
edit_article(page_to_be_edited)


# Print wikidata items below
print('\n' + "The items below are wikidata items:" + '\n')

page = pywikibot.ItemPage(en_wiki_repo, 'Q4115189')
print_wikidata(page,'P31')
print ('\n')
page = pywikibot.ItemPage(en_wiki_repo, 'Q211658')
print_wikidata(page,'P289')