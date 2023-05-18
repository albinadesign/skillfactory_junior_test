from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        wordcount = request.POST['wordcount']
        if filename != '':

            with open(filename) as file:
                text = file.read()
            text = text.replace("\n", " ")
            text = text.replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("—", "").replace(
                ":", "")
            text = text.lower()
            words = text.split()
            listwordcount = list()
            for word in words:
                if word == wordcount:
                    listwordcount.append(word)
            amount = len(listwordcount)
            i = True

            return render(request, 'upload.html',
                          {'amount': amount, 'wordcount': wordcount, 'i': i, 'on': 'active'})

        else:
            return render(request, 'upload.html', {'on': 'active'})

    return render(request, 'upload.html')

