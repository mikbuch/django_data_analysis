from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Home')
    return render(request, 'home.html')


def about(request):
    print('About')
    return render(request, 'about.html')


def data_analysis(request):
    print('Data analysis')
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        print('\nWhat is `myfile`?')
        print(type(myfile))

        print('\nDirectly accessing `myfile` gives nothing :(')
        print(type(str(myfile.read())))
        print(str(myfile.read()))

        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        print('\nHowever, when using FileSystemStorage...')
        print(type(fs.open(myfile)))
        print(fs.open(myfile))

        print('\nOpen and preview using pandas:')
        df = pd.read_csv(fs.open(myfile))
        print(df)

        print('\nOr with CSV module:')
        with fs.open(myfile) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)

        print('Data analysis')
        r, p = stats.pearsonr(df['Diameter of Parent Seed (0.01 inch)'],
                              df['Diameter of Daughter Seed (0.01 inch)'])
        # Prevent p = 0.0
        if p < 0.001:
            p = 0.001
        r, p = '%.03f' % r, '%.03f' % p

        return render(request, 'data_analysis.html',
                      {'result_present': True,
                       'results': {'r': r, 'p': p},
                       'df': df.to_html()})

    return render(request, 'data_analysis.html')
