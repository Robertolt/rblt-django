from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 694576600},
        'instalacao-windows': {'titulo': 'Instalando Windows', 'vimeo_id': 695012786},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
