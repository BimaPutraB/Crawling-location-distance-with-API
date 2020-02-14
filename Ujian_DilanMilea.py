import requests             #Import Package
import emoji

urlProv="http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json"
dataProv = requests.get(urlProv)
otProv= dataProv.json()         #Create Prov List

provD="BANTEN"
provM="JAWA BARAT"

valProv=list(otProv.values())
keyProv=list(otProv.keys())
kodeProvD=keyProv[valProv.index(provD)]     #Search Dilan's Prov Code From its Values

valProv=list(otProv.values())   
keyProv=list(otProv.keys())
kodeProvM=keyProv[valProv.index(provM)]     #Search milea's Prov Code From its Values

urlZip="http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json"
dataZip = requests.get(urlZip)
otZip= dataZip.json()                       #open zip json

kelM=[]
for i in range(len(otZip[kodeProvM])):
    kelM.append(otZip[kodeProvM][i]["urban"])       #Create Urban list from its Province

kelD=[]
for j in range(len(otZip[kodeProvD])):
    kelD.append(otZip[kodeProvD][j]["urban"])       #Create Urban list from its Province


kelrM="CITARUM"
kodePosM= otZip[kodeProvM][kelM.index(kelrM)]["postal_code"]    #search Milea's zipcode from her urbans index

kelrD="SAMPORA"
kodePosD= otZip[kodeProvD][kelD.index(kelrD)]["postal_code"]    #search dilan's zipcode from her urbans index

apiKey="lWORePNXQ3jFsDwZO9ExlTGbrXosoK2EasTNctbOz7LrppdvueDRk9fcK8OnBufw"
kodepos1= kodePosM
kodepos2= kodePosD
url= f"http://www.zipcodeapi.com/rest/{apiKey}/distance.json/{kodepos1}/{kodepos2}/km"

data = requests.get(url)
output = data.json()
jarak=output["distance"]

print(f"Kode Pos lokasi Dilan adalah {kodePosD}")
print(f"Kode Pos lokasi Milea adalah {kodePosM}")
print("Jarak Dilan & Milea adalah {jarak} km")

print(emoji.emojize('Saatnya Milea dan Dilan makan :pizza::pizza::pizza::pizza:'))
