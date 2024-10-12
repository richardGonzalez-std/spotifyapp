import spotipy
from spotipy import SpotifyOAuth
from spotipy import SpotifyException
import tkinter as tk
from tkinter import ttk
from contextlib import suppress
from tkinter import messagebox
#Autenticación SPOTIFY
spAuth = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="b1acffa58207408795fbe41f12d6f445",
    client_secret="00802d891c8946c69372d1cacf5aa90c",
    redirect_uri="http://localhost:8080",
    scope="user-modify-playback-state user-read-playback-state"
)) 

def get_current_device():
    try:
        devices = spAuth.devices()["devices"]
        if devices:
            print(f"connected to {devices[0]["name"]}")
            return devices[0]["id"]  # Devuelve el ID del primer dispositivo activo
        else:
            messagebox.showwarning("Advertencia", "No se encontró ningún dispositivo activo.")
            return None
    except SpotifyException as e:
        messagebox.showerror("Error", f"Error al obtener dispositivos: {e}")
        return None

def play_song():
    device_id = get_current_device()

    
    if device_id is None:
        return
    
    try:
        print(f"currently playing {spAuth.currently_playing}")
        spAuth.start_playback(device_id=device_id)
        update_status("Reproduciendo")
    except SpotifyException as e:
        messagebox.showerror("Error", f"Error al reproducir la canción: {e}")

def pause_song():
    device_id = get_current_device()
    
    if device_id is None:
        return
    
    try:
        spAuth.pause_playback(device_id=device_id)
        update_status("Pausado")
    except SpotifyException as e:
        messagebox.showerror("Error", f"Error al pausar la canción: {e}")

def next_song():
    device_id = get_current_device()
    
    if device_id is None:
        return
    
    try:
        spAuth.next_track(device_id=device_id)
        update_status("Siguiente canción")
    except SpotifyException as e:
        if e.http_status == 404:
            messagebox.showwarning("Advertencia", "Dispositivo no encontrado. Intentando reconectar...")
            # Intentar reconectar el dispositivo y repetir la acción
            device_id = get_current_device()
            if device_id:
                try:
                    spAuth.next_track(device_id=device_id)
                    update_status("Siguiente canción después de reconectar")
                except SpotifyException as e2:
                    messagebox.showerror("Error", f"No se pudo ejecutar el comando después de reconectar: {e2}")
        else:
            messagebox.showerror("Error", f"Error al cambiar a la siguiente canción: {e}")

def previous_song():
    device_id = get_current_device()
    
    if device_id is None:
        return
    
    try:
        spAuth.previous_track(device_id=device_id)
        update_status("Canción anterior")
    except SpotifyException as e:
        if e.http_status == 404:
            messagebox.showwarning("Advertencia", "Dispositivo no encontrado. Intentando reconectar...")
            # Intentar reconectar el dispositivo y repetir la acción
            device_id = get_current_device()
            if device_id:
                try:
                    spAuth.previous_track(device_id=device_id)
                    update_status("Canción anterior después de reconectar")
                except SpotifyException as e2:
                    messagebox.showerror("Error", f"No se pudo ejecutar el comando después de reconectar: {e2}")
        else:
            messagebox.showerror("Error", f"Error al cambiar a la canción anterior: {e}")

def toggle_playback():
    playback_info = spAuth.current_playback()
    
    if playback_info is None:
        messagebox.showwarning("Advertencia", "No hay reproducción activa o no se pudo obtener el estado de reproducción.")
        return
    
    try:
        if playback_info["is_playing"]:
            pause_song()
        else:
            play_song()
    except SpotifyException as e:
        messagebox.showerror("Error", f"Error al cambiar el estado de reproducción: {e}")

def update_status(message):
    status_label.config(text=message)



# Crear la interfaz con Tkinter
root = tk.Tk()
root.title(f"Controlador de {spAuth.devices()["devices"][0]["name"]}")
root.geometry("500x500")
root.configure(bg="#191414")
style = ttk.Style()
style.configure("Spotify.TButton",
                background="#1DB954",  # Color verde de Spotify
                foreground="black",     # Color de texto blanco
                font=("Helvetica", 12, "bold"),  # Fuente y estilo
                padding=10)            # Espaciado

style.map("Spotify.TButton",
          background=[('active', '#1ED760'), ('pressed', '#1AA34A')]) 
# Crear los botones
image_playlist = ttk.Frame(spotipy.Spotify.playlist_cover_image(self=spotipy.Spotify,playlist_id=spotipy.Spotify._get_id))
"""play_pause_button = ttk.Button(root, text="Reproducir/Pausar", command=toggle_playback, width=20, style="Spotify.TButton")
play_pause_button.pack(pady=10)

next_button = ttk.Button(root,text="Siguiente Canción",command=next_song,width=20, style="Spotify.TButton")
next_button.pack(pady=10)

previous_button = ttk.Button(root, text="Canción Anterior", command=previous_song, width=20, style="Spotify.TButton")
previous_button.pack(pady=10)
exit_button = ttk.Button(root, text="Salir", command=root.quit, width=20, style="Spotify.TButton")
exit_button.pack(pady=10)
# Crear una etiqueta para mostrar el estado

# Ejecutar la interfaz"""
status_label = tk.Label(root, text=f"Estado:conectado a {get_current_device()}", fg="blue")
status_label.pack(pady=20)  

root.mainloop()

