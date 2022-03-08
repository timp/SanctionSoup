curl -L -k -H "Accept-Charset: utf-8;q=0.7,*;q=0.7"   https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1058962/UK_Sanctions_List.xml > UK_Sanctions_List.xml

date >> gets.txt

python SanctionSoup.py > README.md

