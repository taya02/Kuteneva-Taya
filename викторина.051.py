def f():
r=0
f=0
print (f'Ввод ответа с большой буквы')
que = [ "Наименьшая частица химического элемента, носитель его свойств? ",
        "Молярная масса Na(до целых) ",
        "Как называются растворимые основания? ",
        "Купоросное масло - это ... кислота ",
        "Самый легкий химический элемент? "]
ans = [ "Атом", "23", "Щелочи","Серная","Водород"]
for i in range (len(que)):
    a = input(que[i])
    if a == ans[i]:
        print ("Ответ верный, умничка :3")
    else:
        print("Ответ не такой, подумай ещё")
        f+=1
print(f"Неправильных ответов {f}")
f()

