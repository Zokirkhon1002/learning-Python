###1
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()} ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar;

# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar[:]) # [:] bu belgi orqali ro'yxatning nusxalab olyapmiz
# print(baholar)
# print(talabalar)



# Uyga vazifa
# Amaliyot

###2
# def boshharf_katta_qil(names):
#     newList =[]
#     for name in names:
#         newList.append(name.title())
#     return print(newList);

# ismlar = ["zokirkhon", "khurshidbek", "sayfullokhon","boburmirzo","muhriddin","rafiqjon","abdulkhamid"]
# boshharf_katta_qil(ismlar)



###1
# def boshharf_katta_qil(names):
#     for index in range(len(names)):
#         names[index] = names[index].title()
#     return print(names)

# ismlar = ["zokirkhon", "khurshidbek", "sayfullokhon","boburmirzo","muhriddin","rafiqjon","abdulkhamid"]
# boshharf_katta_qil(ismlar)



###3
###2
def boshharf_katta_qil(names):
    baholar = {}
    for name in names:
        baho = int(input(f"Talaba {name.title()}ning bahosini kiriting: "))
        baholar[name] = baho
    return print(baholar)



ismlar = ["zokirkhon", "khurshidbek", "sayfullokhon","boburmirzo","muhriddin","rafiqjon","abdulkhamid"]
boshharf_katta_qil(ismlar)
print(ismlar)
