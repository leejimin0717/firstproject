from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def result(request):
    input_text = request.GET['text1']

    word_list = input_text.split()

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'text1': input_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})