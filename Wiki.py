import wikipedia
import main
def wiki(a):
    if a == 'wikipedia':
       main.Goverbal('Please ask your question ....')
       main.Input()
       
    else:
        main.Goverbal('traversing through the wide collections of wikipedia...')
        a = a.replace("wikipedia", "")
        results = wikipedia.summary(a, sentences=2)
        main.Goverbal("According to Wiki")
        print(results)
        main.Goverbal(results)