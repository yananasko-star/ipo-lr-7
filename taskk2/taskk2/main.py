import json
with open('dump.json','r',encoding='utf-8')as file #загружаем данные из файла
data=json.load(file)
search_code=input("введите номур квалификации") #пользователь вводит номер квалификации
found=False
#ицем квалификацию
for item in data:
    if item.get('model')=='reference.qualification':
    fielda=item.get('field',{})
    if field=item.get('code')==search.code:
        found=True
        specialty_name=" "
        for spec_item in data:
            if spec_item.get('model')=='reference.specialty': and spec_item.get('pk')==field.get('specialte')
            specialty_name==spec_item.get('field,{}').get('name','')
            break
        print("=============== Найдено ===============")
        print(f"{field['code']}>>Специальность \{specialty_name}",ПТО)
         print(f"{field['code']}>>Квалификация \{field['name']}")

         if not found:
            print("=============== Не найдено ===============")
