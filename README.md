# YT Download: Galaksinin En Güvenli Müzik İndiricisi

> "Eğer Youtube'daki bir playlisti veya videoyu mp3 olarak indirmek istiyorsan, yanına bir havlu al ve bu scripti çalıştır!"  
> — Otostopçunun Galaksi Rehberi

## 1. Giriş
Mert Demir ve Sezen Aksu'nun yeni albümleri çıktı ama Spotify Premium’um yok, YouTube reklamlarından bıktım, mp3 indirme siteleri ise güvensiz (dışarıda içine ne koydukları belli değil) İşte tam bu noktada, Python ile galaksinin en güvenli müzik indiricisiyle karşındayım.

## 2. Gereksinimler
- Python (Zaten GitHub'da README okuyorsan muhtemelen yüklüdür)
- `yt_dlp`
- FFmpeg

Kurulum için terminale şunu yaz:
```
pip install yt-dlp
```
FFmpeg’i ise [şuradan](https://www.gyan.dev/ffmpeg/builds/) indir, zipten çıkar, yolunu scriptte belirt. (Google Amca'ya veya Yapay Zeka Teyze’ye de sorabilirsin)

## 3. Çalıştırma ve Kullanım
Arayüz yok, Docker yok (Docker Desktop kurup da Docker komutlarını öğrenip konteyner ayağa kaldırmak 7.5 milyar yıl sürebilir), sadece saf Python ve terminal. Kodun olduğu klasörde terminali açıp:
```
python yt_download.py
```
yaz. Sana bir URL soracak. Playlist veya tek video, hiç fark etmez. Yapıştır, ENTER’a bas, arkana yaslan. Eğer playlist ise, şarkılar playlist adında bir klasöre iner. Tek şarkıysa olduğu yere iner.

## 4. Bilgilendirme
Bu script tamamen hobi ve eğitim amaçlıdır. Dünyanın herhangi bir köşesinde, herhangi bir yasal sorumluluk sana aittir. Para kazanmak için yazılmamıştır.

> "Hayatın, evrenin ve her şeyin cevabı 42 ise, bu script de müzik indirmenin cevabı olabilir"
İyi eğlenceler ve unutma DON'T PANIC!