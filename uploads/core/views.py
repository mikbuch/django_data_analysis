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
        filename = fs.save(myfile.name, myfile)
        print('\nHowever, when using FileSystemStorage...')
        print('\nReading filename: %s' % filename)
        print(type(fs.open(filename)))
        print(fs.open(filename))

        print('\nOpen and preview using pandas:')
        df = pd.read_csv(fs.open(filename))
        print(df)

        print('\nOr with CSV module:')
        with fs.open(filename, 'rt') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)

        print('Data analysis')
        r_table = df.apply(lambda x: df.apply(lambda y: r_xor_p(x, y,
                                                                r_xor_p='r')))
        p_table = df.apply(lambda x: df.apply(lambda y: r_xor_p(x, y,
                                                                r_xor_p='p')))

        return render(request, 'data_analysis.html',
                      {'result_present': True,
                       'results': {'r_table': r_table.to_html(),
                                   'p_table': p_table.to_html()},
                       'df': df.to_html()})

    return render(request, 'data_analysis.html')


def r_xor_p(x, y, r_xor_p='r'):
    ''' Pearson's r or its p
    Depending of what you would like to get.
    '''
    r, p = stats.pearsonr(x, y)

    if r_xor_p == 'r':
        return r
    else:
        return p
