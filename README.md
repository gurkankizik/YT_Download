# YT Download: Galaksinin En Güvenli Müzik İndiricisi

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
FFmpeg’i ise [şuradan](https://www.gyan.dev/ffmpeg/builds/) indir. Zip dosyasını ayıkla, `bin` klasörü içindeki `ffmpeg.exe` dosyasını örneğin `C:\ffmpeg\bin\ffmpeg.exe` yoluna koy.

## 3. Çalıştırma ve Kullanım
Arayüz yok, Docker yok (Docker Desktop kurup da Docker komutlarını öğrenip bir de konteyner ayağa kaldırmak 7.5 milyar yıl sürebilir), sadece saf Python ve terminal. Kodun olduğu klasörde terminali açıp:
```
python yt_download.py
```
yaz. Sana bir URL soracak. Playlist veya tek video, hiç fark etmez. Yapıştır, ENTER’a bas, arkana yaslan. Eğer playlist ise, şarkılar playlist adında bir klasöre iner. Tek şarkıysa olduğu yere iner.

## 4. Bilgilendirme
Bu script yalnızca hobi ve eğitim amaçlı geliştirilmiştir. Telif hakkı içeren içeriklerin indirilmesi, paylaşılması veya dağıtılması ilgili ülke yasalarına ve platformların kullanım şartlarına aykırı olabilir. Bu scriptin kullanımı sonucu doğabilecek her türlü yasal sorumluluk ve yükümlülük tamamen kullanıcıya aittir. Geliştirici, bu scriptin üçüncü şahıslar tarafından kullanımından doğabilecek herhangi bir doğrudan veya dolaylı zarardan sorumlu tutulamaz. Script ticari amaçla kullanılmamalıdır.