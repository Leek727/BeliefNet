weights = ""

with open("weight.csv", "r") as f:
    weights = f.read().strip()

weights = " ".join(weights.split())

commas_added = ""
while len(weights) != 0:
    # get weights
    ind = weights.index("]]")+2
    commas_added += '\n' + weights[0:ind].replace(" ", ",")

    weights = weights[ind:len(weights)]

    # get biases
    ind = weights.index("]")+2
    commas_added += '\n' + weights[0:ind].replace(" ", ",")

    weights = weights[ind:len(weights)]

# this is horrible
commas_added = commas_added.replace("\n,","\n").replace(",\n","\n").replace('[,','[').replace(',]',']').strip().split('\n')

layers = "layers = ["
for i in range(0, len(commas_added), 2):
    layers += f"[{commas_added[i]}, {commas_added[i+1]}], "

layers = layers[0:len(layers)-2] + ']'
print(layers)