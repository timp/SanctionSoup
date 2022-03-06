from bs4 import BeautifulSoup
#set PYTHONIOENCODING=utf-8
#set PYTHONLEGACYWINDOWSSTDIO=utf-8

with open('UK_Sanctions_List.xml', 'r', encoding="utf8") as f:

    contents = f.read()
    encoded = contents.encode('utf-8')

    soup = BeautifulSoup(encoded, 'lxml')
    print("Going up\n")
    #print(soup.encode('cp1252', errors='ignore'))
    for d in soup.find_all('designation'):
        code = d.uniqueid.text.encode('cp1252', errors='ignore').decode()
        if code.startswith("RUS"):
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
            print (id, date_of, entity_type,sanction)
