product = 'bread' # Global variables



def changing_product():

    product = 'Milk'
    print('Local: ', product)
    def showing_enclosed():
        product = 'Cola'
        print('Enclosed scope: ', product)

    showing_enclosed()
    print(product, 'ууdef'
                   '')
changing_product()

print('Global:', product)
