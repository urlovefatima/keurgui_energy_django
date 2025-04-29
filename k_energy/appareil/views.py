from django.shortcuts import render
from .models import Appareil, Piece
from .forms import AppareilForm, PieceForm

# Create your views here.

def appareilsView(request):
    appareils = Appareil.objects.all()
    temp_name = 'appareils.html'
    context = {'appareils': appareils}
    return render(request, temp_name, context)

def piecesView(request):
    pieces = Piece.objects.all()
    appareils = Appareil.objects.all()
    temp_name = 'pieces.html'
    context = {'pieces': pieces, 'appareils': appareils}
    return render(request, temp_name, context)


def ajout_piece(request):
    temp_name = 'add_piece.html'
    if request.method == 'POST':
        form = PieceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PieceForm()
    return render(request, temp_name)


def ajout_appareil(request):
    if request.method == 'POST':
        form = AppareilForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AppareilForm()
    return render(request, 'ajouter_appareil.html', {'form': form})