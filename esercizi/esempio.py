filenames = ["1.Row Data.text", "2.Reports.text", "3.Presentation.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

    rate = 0.95
    dollar_amount = float(input('How many dollars you have got?:'))
    euros = dollar_amount * rate
    print('the amount of euros is:')
    print(euros)

    ranking = ['John', 'Sen', 'Lisa']
    rank = int(input('enter a rank number:'))
    name = ranking[rank]
    print(name)

    ranking = ['John', 'Sen', 'Lisa']

    person_name = input('inserire il nome:')
    rank = ranking.index(person_name) + 1
    print(rank)
