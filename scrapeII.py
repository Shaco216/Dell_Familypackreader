from bs4 import BeautifulSoup
import requests

#Latitudes = ['5500', '5400', '5300', '5300 2-1', '5580', '5590', '5591', '7280', '7300', '7390', '7390 2-1']
linklist= []
Short_Versions = []
zuordnungMod2Driv = {
    '5500' : 'win10_latitudee11whl',
    '5400' : 'win10_latitudee11whl',
    '5300' : 'win10_latitudee11whl',
    '5300 2-1' : 'win10_latitudee11whl',
    '5300 2in1' : 'win10_latitudee11whl',
    '5580' : 'win10_latitudee9',
    '7280' : 'win10_latitudee9',
    '5590' : 'win10_latitudee10',
    '7390' : 'win10_latitudee10',
    '7390 2-1' : 'win10_latitudee10',
    '7390 2in1' : 'win10_latitudee10',
    '5591' : 'win10_latitudee10cfl',
    '7300' : 'win10_latitudee11whl2'
    }

zuordnungDriv2Mod = {
    'win10_latitudee11whl' : ['5500', '5400', '5300', '5300 2-1'],
    'win10_latitudee9' : ['5580', '7280'],
    'win10_latitudee10' : ['5590', '7390', '7390 2-1'],
    'win10_latitudee10cfl' : '5591',
    'win10_latitudee11whl2' : '7300'
}


def get_linklist():

    page = requests.get('https://www.dell.com/support/kbdoc/de-de/000180534/dell-familie-treiberpakete')
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.findAll('a'):
        linklist.append(link)
    return linklist

def sort_relevant_information(linklist):
    Latitudes = ["5500", "5400", "5300", "5300 2-1", "5580", "5590", "5591", "7280", "7300", "7390", "7390 2-1"]

    for computer in Latitudes:
        Modell = str(computer)

        Substring = zuordnungMod2Driv.get(Modell) #getting the value of the key inside the dict
        #print(Substring)
        #print(linklist)
        FilteredLinks = [link for link in linklist if Substring in str(link)]
        Versions = []
        #print(Modell)
        Driver = zuordnungMod2Driv.get(Modell)
        print("\n"+Driver)
        if Driver != 'win10_latitudee10':
            count = 1
            for item in FilteredLinks:
                #print('testfor')
                if count < 2:
                    #print('test')
                    Versions.append(item)
                    count = count + 1
        else: #wenn der Driver = win10_latitudee10 überspringt er erst einige einträge um zum richtigen zu kommen
            count = 1
            for item in FilteredLinks:
                #print('testfor')
                if count > 9 and count < 11:
                    #print('test')
                    Versions.append(item)
                count = count + 1

        #print(FilteredLinks)
        Short_Versions = []
        for item in Versions:
            temp = str(item)
            temp = temp.replace('target="_blank">', 'Version= ')
            temp = temp.replace('>', '')
            temp = temp.replace('<', '')
            temp = temp.replace('a href=', '')
            temp = temp.replace('(', 'Date= ')
            temp = temp.replace(')/a', '')
            Short_Versions.append(temp)
        #print(Versions)
        if Modell != "5300 2-1" and Modell != "7390 2-1":
            Short_Versions.insert(0, "Modell: " + Modell + "\t\t")
        else:
            Short_Versions.insert(0, "Modell: " + Modell + "\t")
        print(Short_Versions)
        convert_list_into_txt(Short_Versions)
    return Short_Versions
def convert_list_into_txt(Short_Versions):
    with open('Dell_Familypacks_Driver_Compare.txt', 'a') as writer: #ursprünglich w für write ( a ist adden/appendieren)
        writer.writelines(Short_Versions)
        writer.writelines('\n')
        writer.writelines('\n')
get_linklist()
sort_relevant_information(linklist)


