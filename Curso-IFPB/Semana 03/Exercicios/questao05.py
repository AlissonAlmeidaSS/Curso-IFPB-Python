corinthians = 0
palmeiras = 0
qtde = 0
var = "a"
while var != "F" and var !="f" :
    print("Digite C para Corinthians ou P Palmeiras e F para encerrar")
    var = input("Digite qual time Torce: ")
    if var == "C" or var == "c":
        corinthians = corinthians+1
    if var == "p" or var == "P":
        palmeiras = palmeiras+1
    qtde = qtde+1
    
        

print("O total de entrevistados = ", qtde)
print("A quantidade de torcedores do Palmeiras = ", palmeiras," A porcertagem dos torcedores e = ", round((palmeiras * 100)/qtde,2),"%")
print("A quantidade de torcedores do Corinthians = ", corinthians," A porcertagem dos torcedores e = ", round((corinthians * 100)/qtde,2),"%")
