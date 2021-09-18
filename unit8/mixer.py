
import pygame
import sys, win32com.client


class MusicControl():
    def __init__(self):
        self.land_sound = pygame.mixer.Sound('pop0.wav')
        self.remove_sound = pygame.mixer.Sound('pop2.wav')

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut("music.mp3.lnk")
        music_file = shortcut.Targetpath
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1,0.0)
        self.music_playing = True
        

    def stop_background_music(self):
        if self.music_playing:
            pygame.mixer.music.stop()
        self.music_playing = False

    def start_background_music(self):
        if not self.music_playing:
            pygame.mixer.music.play(-1,0.0)
        self.music_playing = True

    def play_land_sound(self):
        if self.music_playing:
            self.land_sound.play()

    def play_remove_sound(self):
        if self.music_playing:
            self.remove_sound.play()
