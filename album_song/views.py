from django.shortcuts import render, redirect
import psycopg2

# Create your views here.

def get_db_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres.vjxypfaouaiqkavqanuu",
        password="marmutkelompok9",
        host="aws-0-ap-southeast-1.pooler.supabase.com",
        port="5432",
    )
    return conn

def show_album(request):
    email = request.COOKIES.get('email')

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM label\
                WHERE email = %s", (email,))
    label = cur.fetchmany()
    
    # Mengecek apakah merupakan label
    if len(label) == 1:
        id_label = label[0][0]
        
        cur.execute("SELECT * FROM album\
                    WHERE id_label = %s", (id_label,))
        showed_album = cur.fetchall()
        
        context = {
            'role': 'label',
            'status': 'success',
            'nama': label[0][1],
            'showed_album': showed_album,
        }
        
        conn.commit()
        cur.close()
        conn.close()
        
        return render(request, 'list_album.html', context)
    
    return render(request, 'list_album.html')

def show_song(request):
    album_id = request.GET.get('album_id')
    showed_song = []
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT judul FROM album \
                WHERE id = %s", (album_id,))
    album_name = cur.fetchone()[0]
    
    cur.execute("SELECT id_konten, total_play, total_download FROM song \
                WHERE id_album = %s", (album_id,))
    showed_song = cur.fetchall()
    
    for i in range(len(showed_song)):
        cur.execute("SELECT judul, tanggal_rilis, tahun, durasi FROM konten \
                    WHERE id = %s", (showed_song[i][0],))
        song_details = cur.fetchone()
        song_details = list(song_details)
        song_details[0] = song_details[0].split('-')[0].strip()
        showed_song[i] = showed_song[i] + tuple(song_details)

    context = {
        'status': 'success',
        'showed_song': showed_song,
        'album_name': album_name, 
    }
    
    conn.commit()
    cur.close()
    conn.close()
    return render(request, 'song_album.html', context)

def delete_album(request):
    album_id = request.GET.get('album_id')
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM album WHERE id = %s", (album_id,))

    
    conn.commit()
    cur.close()
    conn.close()
    
    return redirect('album_song:show_album')

def delete_song(request):
    song_id = request.GET.get('song_id')
    
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM song WHERE id_konten = %s", (song_id,))
    
    conn.commit()
    cur.close()
    conn.close()
    
    return redirect('album_song:show_album')

