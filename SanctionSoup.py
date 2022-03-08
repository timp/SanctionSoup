from bs4 import BeautifulSoup
#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

print("An attempt to parse " + 
      "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1058962/UK_Sanctions_List.xml" + 
      " from https://www.gov.uk/government/publications/the-uk-sanctions-list") 
print("")

with open('UK_Sanctions_List.xml', 'r', encoding="utf8") as f:

    contents = f.read()
    encoded = contents.encode('utf-8')

    soup = BeautifulSoup(encoded, 'lxml')
    #print(soup.encode('cp1252', errors='ignore'))
    russian_counter = 0
    for d in soup.find_all('designation'):
        code = d.uniqueid.text.encode('cp1252', errors='ignore').decode()
        if code.startswith("RUS"):
            russian_counter = russian_counter + 1
            id = d.uniqueid.text.encode('cp1252', errors='ignore').decode()
            entity_type  = d.individualentityship.text.encode('cp1252', errors='ignore').decode()
            if d.sanctionsimposed is not None:
               sanction = d.sanctionsimposed.text.encode('cp1252', errors='ignore').decode()
            else: 
                sanction= "none"
            if d.datedesignated is not None:
               designated = d.datedesignated.text.encode('cp1252', errors='ignore').decode()
               date_of = designated 
            else: 
                updated = d.lastupdated.text.encode('cp1252', errors='ignore').decode()
                date_of = updated
            print (id, date_of, entity_type,sanction, "  ")
    print("\nTotal: ", russian_counter)