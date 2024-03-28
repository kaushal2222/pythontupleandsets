basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
l=len(basket)
print(l)
sor=sorted(basket)
print(sor)

print("orange" in basket)
print("crabrass"   in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
c=a-b
print(c)
k=a|b
print(k)
s=a&b
print(s)
d=a^b
print(d)

european_flowers = {"sunflowers", "roses", "lavender", "tulips", "goldcrest"}
print(european_flowers)
american_flowers = {"roses", "tulips", "lilies", "daisies"}
print(american_flowers)
american_flowers.add("orchids")
print(american_flowers)
diff=american_flowers.difference(european_flowers)
print(diff)

a=american_flowers.intersection(european_flowers)
print(a)

print(american_flowers.isdisjoint(european_flowers)) #koi pan common item hase to false return karse alag hase to ture return karse
print(american_flowers.issuperset(european_flowers))#current set ni item jo bija setma hoyto true naito false
print(american_flowers.issubset(european_flowers))#bija set ni item currrnt set ma male to true nai to false

print(american_flowers.symmetric_difference(european_flowers)) #same hase ae return nai thay
print(american_flowers.union(european_flowers))#badhi item le common sivay ni common vari aek var le

update=(american_flowers.update(european_flowers))
print(american_flowers)

discard= (american_flowers.discard("roses"))
print(american_flowers)

american_flowers.pop()
print(american_flowers)

american_flowers.clear()
print(american_flowers)
