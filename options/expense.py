import random
import webbrowser
import os
from time import sleep
import webbrowser

variable = ["Wine Tasting", 'Food', 'Skydiving', 'Symphony', 'Movie drive-in']
random_choice = random.choice(variable)

#placing in every location, along with the website for expense variable
def choices():
    #After random places is variable, it will go along with the if/elif system to correspond with its own function. 
    print("After carefully selectings, we choose: " + random_choice)
    if random_choice == 'Wine Tasting':
        # Function for Wine tasting, random will choose a key from Wine_choice and will depending what it is will open the webside automatically
        def Wine_Tasting():
            print('There are five basic steps in tasting wine: color, swirl, smell, taste, and savor.\n These are also known as the "five S" steps: see, swirl, sniff, sip, savor.\n Your job is to look for clarity, integration, expressiveness, complexity, and connectedness.\n')
            Wine_choice = {"Sable Gate Winery": 'https://sablegatewinery.com/about/', 'Nice Winery':'https://www.nicewines.com/Visit-Us/Tastings', 'Decant Urban Winery': 'https://decantwinery.com','Ermarose Winery': 'https://ermarosewinery.com','Wild Stallion Vineyards': 'https://www.wildstallionvineyards.com'}
            sleep(10)
            entry = random.choice(list(Wine_choice))
            print('Your location for today\'s adventure will be: ' + entry)
            print('A new page will open! Give me a sec for i can tranfer you over')
            sleep(10)

            while True:
                if entry == 'Sable Gate Winery':
                    webbrowser.open('https://sablegatewinery.com/about')
                    break
                elif entry == 'Nice Winery':
                    webbrowser.open('https://www.nicewines.com')
                    break
                elif entry == 'Decant Urban Winery':
                    webbrowser.open('https://decantwinery.com')
                    break
                elif entry == 'Ermarose Winery':
                    webbrowser.open('https://ermarosewinery.com')
                    break
                elif entry == 'Wild Stallion Vineyards':
                    webbrowser.open('https://www.wildstallionvineyards.com')
                    break
        Wine_Tasting()
    elif random_choice == 'Food':
        #function for food, this will place in a random answer from type of food and will go along with the if/elif to go with coressponding function
        def Food():
            os.system('clear')
            print('We have: Steak, Sushi, Italian')
            list = ['Steak','Sushi','Italian']
            Choice_food = random.choice(list)
            print("For today\'s choice we have picked: " + Choice_food)
            sleep(10)
            def Sushi():
                print("Sushi is a popular Japanese dish made from seasoned rice with fish, egg, or vegetables.")
                Sushi_choice = ['Uchi', 'Hidden Omasake','MF Sushi','Kuu','Roka Akor']
                entry = random.choice(Sushi_choice)
                print('Your location for today\'s adventure will be: ' + entry)
                print('A new page will open! Give me a sec for i can transfer you over')
                sleep(10)
                while True:
                    if entry == 'Uchi':
                        webbrowser.open('https://www.uchihouston.com')
                        break
                    elif entry == 'Hidden Omasake':
                        webbrowser.open('https://hiddenomakase.com')
                        break
                    elif entry == 'MF Sushi':
                        webbrowser.open('https://www.opentable.com/r/mf-sushi-houston')
                        break
                    elif entry == 'Kuu':
                        webbrowser.open('https://kuurestaurant.com')
                        break
                    elif entry == 'Roka Akor':
                        webbrowser.open('https://www.rokaakor.com')
                        break

            def Steak():
                print("Steak is a food that can be described as tender, flavorful, juicy, and cooked to perfection")
                Steak_choice = ['Vic & Anthony\'s Steakhouse', 'B & B Butchers & Restaurant','Mastro\'s Steakhouse','Tony\'s','The Capital Grille']
                entry = random.choice(Steak_choice)
                print('Your location for today\'s adventure will be: ' + entry + '!\n' )
                print('A new page will open! Give me a sec for i can transfer you over')
                sleep(10)
                while True:
                    if entry == 'Vic & Anthony\'s Steakhouse':
                        webbrowser.open('vicandanthonys.com')
                        break
                    elif entry == 'B & B Butchers & Restaurant':
                        webbrowser.open('bbbutchers.com')
                        break
                    elif entry == 'Mastro\'s Steakhouse':
                        webbrowser.open('https://www.mastrosrestaurants.com')
                        break
                    elif entry == 'Tony\'s':
                        webbrowser.open('https://www.tonyshouston.com')
                        break
                    elif entry == 'The Capital Grille':
                        webbrowser.open(' https://www.thecapitalgrille.com/locations/tx/houston/houston-the-galleria/8007')
                        break

            def Italian():
                print("Squisito! If you want to pay someone the highest compliment for their cooking, an excellent alternative to buono is the word squisito meaning exquisite or delicious.\n")
                Sushi_choice = ['Sorrento Ristorante', 'Da Marco Italian Restaurant','La Griglia','Amore']
                entry = random.choice(Sushi_choice)
                print('Your location for today\'s adventure will be: ' + entry + '!\n' )
                print('A new page will open! Give me a sec for i can transfer you over')
                sleep(10)
                while True:
                    if entry == 'Sorrento Ristorante':
                        webbrowser.open('https://www.sorrentohouston.com')
                        break
                    elif entry == 'Da Marco Italian Restaurant':
                        webbrowser.open('https://www.damarcohouston.com')
                        break
                    elif entry == 'La Griglia':
                        webbrowser.open('https://www.lagrigliarestaurant.com')
                        break
                    elif entry == 'Amore':
                        webbrowser.open('https://www.amorehouston.com')
                        break
#based om the option given it will go toward the elif and print that function
            if Choice_food == 'Sushi':
                Sushi()
            elif Choice_food == 'Steak':
                Steak()
            elif Choice_food == 'Italian':
                Italian()
        Food()
    elif random_choice == 'Skydiving':
        #skydiving function
        def Skydiving():
            print("Tired of something casual? Take it up to skies! \n")
            print('A new page will open! Give me a sec for i can transfer you over')
            sleep(10)
            webbrowser.open('https://www.skydivehouston.com')
        Skydiving()

    elif random_choice == 'Symphony':
        def Symphony():
            print("a large group of musicians who play together on a variety of string, wind and percussion instruments.\n Find your sound, your melody, your rhythm, bring it to thy self!")
            print('A new page will open! Give me a sec for i can transfer you over')
            sleep(10)
            webbrowser.open('https://houstonsymphony.org')  
        Symphony()

    elif random_choice == 'Movie drive-in':
        def Movie_drive_in():
            print("Moviegoers are meant to drive into the theater and park their cars in front of a large screen that displays the movie.")
            Movie_choice = ['Moonstruck', 'Showboat','Mastro\'s Steakhouse','Rooftop Cinema Club','BlueMoon Cinemas']
            entry = random.choice(Movie_choice)
            print('Your location for today\'s adventure will be: ' + entry + '!\n' )
            print('A new page will open! Give me a sec for i can transfer you over')
            sleep(10)
            while True:
                    if entry == 'Moonstruck':
                        webbrowser.open('https://www.moonstruckdrivein.com')
                        break
                    elif entry == 'Showboat':
                        webbrowser.open('https://www.showboathouston.com')
                        break
                    elif entry == 'Rooftop Cinema Club':
                        webbrowser.open('https://rooftopcinemaclub.com/houston/')
                        break
                    elif entry == 'BlueMoon Cinemas':
                        webbrowser.open('https://bmcinemas.com/index.html')
                        break
        Movie_drive_in()
choices()