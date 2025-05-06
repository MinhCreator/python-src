# print("WUBWUBABCWUB".split("WUB"))



class method:
    def remove_viruss(text: str, pattern: str) -> str:

        list_cut = text.split(pattern)
        store = [word for word in list_cut if word != '' ]
        
        return " ".join(store)

string = "WUBWUBIWUBAMWUBNAM" 
string2 = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONS"
        

print(method.remove_viruss(string2,"WUB"))