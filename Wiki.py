import wikipedia
import main
def wiki(a):
    if a == 'wikipedia':
       main.Goverbal('Please ask your question ....')
       main.Input()

    else:
        main.Goverbal('traversing through the wide collections of wikipedia...')
        a = a.replace("wikipedia", "")
        result= wikipedia.search(a)
        print(result)
        b=int(input("Enter the number corresponding to your desired search result, starting from 0 -"))

        results = wikipedia.summary(result[b] , sentences = 2, auto_suggest=False, redirect=True)
        main.Goverbal("According to Wiki")
        print(results)
        main.Goverbal(results)
