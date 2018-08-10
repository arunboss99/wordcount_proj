from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
	#return render(request, 'home.html', {'hithere':'This is me'})
	return render(request, 'home.html')
	

def count(request):
	fulltexts = request.GET['fulltext']
	#print (fulltexts)
	wordlist = fulltexts.split()
	worddictionary = {}
	for word in wordlist:
		if word in worddictionary:
			#increment
			worddictionary[word] += 1
		else:
			#add to dict
			worddictionary[word] = 1
	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'count.html', {'fulltext':fulltexts, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
	return render(request,'about.html')
