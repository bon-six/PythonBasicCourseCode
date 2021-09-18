import pygame
import sys

pygame.init()

WINDOWS_SIZE=(800,600)
FPS=40

screen = pygame.display.set_mode(WINDOWS_SIZE,0,32)
pygame.display.set_caption('program title')

clock = pygame.time.Clock()

# test code to print all event types that supported by pygame
e_types = {
    pygame.QUIT : 'QUIT',
    pygame.ACTIVEEVENT : 'ACTIVEEVENT'     ,
    pygame.KEYDOWN   :'KEYDOWN'       ,
    pygame.KEYUP       :'KEYUP'     ,
    pygame.MOUSEMOTION :'MOUSEMOTION'     ,
    pygame.MOUSEBUTTONUP  :'MOUSEBUTTONUP'  ,
    pygame.MOUSEBUTTONDOWN:'MOUSEBUTTONDOWN' ,
    pygame.JOYAXISMOTION  :'JOYAXISMOTION',
    pygame.JOYBALLMOTION :'JOYBALLMOTION',
    pygame.JOYHATMOTION    :'JOYHATMOTION'  ,
    pygame.JOYBUTTONUP    :'JOYBUTTONUP'  ,
    pygame.JOYBUTTONDOWN :'JOYBUTTONDOWN'  ,
    pygame.VIDEORESIZE    :'VIDEORESIZE'   ,
    pygame.VIDEOEXPOSE    :'VIDEOEXPOSE'  ,
    pygame.USEREVENT      :'USEREVENT' ,
    pygame.AUDIODEVICEADDED  :'AUDIODEVICEADDED' ,
    pygame.AUDIODEVICEREMOVED :'AUDIODEVICEREMOVED',
    pygame.FINGERMOTION     :'FINGERMOTION' ,
    pygame.FINGERDOWN    :'FINGERDOWN'   ,
    pygame.FINGERUP       :'FINGERUP' ,
    pygame.MOUSEWHEEL    :'MOUSEWHEEL' ,
    pygame.MULTIGESTURE :'MULTIGESTURE' ,
    pygame.TEXTEDITING  :'TEXTEDITING',
    pygame.TEXTINPUT   :'TEXTINPUT',
    #pygame.WINDOWEVENT:'WINDOWEVENT',
    pygame.WINDOWSHOWN: 'WINDOWSHOWN',
    pygame.WINDOWHIDDEN: 'WINDOWHIDDEN',
    pygame.WINDOWEXPOSED:'WINDOWEXPOSED',
    pygame.WINDOWMOVED:'WINDOWMOVED',
    pygame.WINDOWRESIZED:'WINDOWRESIZED',
    pygame.WINDOWSIZECHANGED:'WINDOWSIZECHANGED',
    pygame.WINDOWMINIMIZED:'WINDOWMINIMIZED',
    pygame.WINDOWMAXIMIZED:'WINDOWMAXIMIZED',
    pygame.WINDOWRESTORED:'WINDOWRESTORED',
    pygame.WINDOWENTER:'WINDOWENTER',
    pygame.WINDOWLEAVE:'WINDOWLEAVE',
    pygame.WINDOWFOCUSGAINED:'WINDOWFOCUSGAINED',
    pygame.WINDOWFOCUSLOST:'WINDOWFOCUSLOST',
    pygame.WINDOWCLOSE:'WINDOWCLOSE',
    pygame.WINDOWTAKEFOCUS:'WINDOWTAKEFOCUS',
    pygame.WINDOWHITTEST:'WINDOWHITTEST',
    pygame.DROPBEGIN:'DROPBEGIN',
    pygame.DROPCOMPLETE:'DROPCOMPLETE',
    pygame.DROPFILE :'DROPFILE',
    pygame.DROPTEXT:'DROPTEXT',
    pygame.MIDIIN:'MIDIIN',
    pygame.MIDIOUT:'MIDIOUT',
    pygame.CONTROLLERDEVICEADDED :'CONTROLLERDEVICEADDED'   ,
    pygame.JOYDEVICEADDED          :'JOYDEVICEADDED' ,
    pygame.CONTROLLERDEVICEREMOVED :'CONTROLLERDEVICEREMOVED',
    pygame.JOYDEVICEREMOVED       :'JOYDEVICEREMOVED',
    pygame.CONTROLLERDEVICEREMAPPED:'CONTROLLERDEVICEREMAPPED',
}

game_on = True

while game_on: # game loop. one round is one Frame.

    # inside the game loop, to do the event process loop
    # to process all events/commands happened in one frame time
    for event in pygame.event.get():
        # test code to print all events.
        print('type', event.type, e_types[event.type])
        print('content', event.__dict__)
        
        if event.type==pygame.QUIT:
            # before QUIT, there always one WINDOWCLOSE event. can respond to that event instead to exit the program.
            game_on = False
            break

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_F4 and event.mod&pygame.KMOD_ALT:
                # actually cannot get this KEYDOWN and KEYUP, but will be a WINDOWCLOSE and QUIT,
                # tested in windows platform pygame
                game_on = False
                break
            elif event.key == pygame.K_ESCAPE:
                # use `ESC` to exit game is a common way of many games
                game_on = False
                break
            else:
                # check and process other key events
                pass
        elif event.type == pygame.ACTIVEEVENT:
            if event.state==pygame.APPACTIVE:
                if event.gain: # program de-iconized
                    # always WINDOWRESTORED event follow. can process that event instead.
                    pass
                else:    # program iconized (minimized)
                    # always WINDOWMINIMIZED event follow. can process that event instead.
                    pass
            elif event.state==pygame.APPINPUTFOCUS:
                if event.gain: # program get focus (window at front layer)
                    # always WINDOWFOCUSGAINED event follow. can process that event instead.
                    pass
                else:    # program lost focus (window at back layer)
                    # always WINDOWFOCUSLOST event follow. can process that event instead.
                    # after WINDOWFOCUSLOST, always follow one TEXTEDITING event.
                    pass            
            elif event.state==pygame.APPFOCUSMOUSE:
                if event.gain: # mouse in program window
                    # always WINDOWENTER event follows. can process that event instead.
                    pass
                else:    # mouse out of program window
                    # always WINDOWLEAVE event follows. can process that event instead.
                    pass
        elif event.type == pygame.KEYDOWN:
            # if press key and hold, then release, will be
            #    1. one KEYDOWN event,
            #    2. then follow a series of TEXTINPUT event,
            #    3. then finally one KEYUP event.
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.MOUSEMOTION:
            pass

    if game_on == False:  # receive command to exit game
        break

    screen.fill('black')
    # game continue. do all sprite process.

    # draw the result into the screen
    pygame.display.update()

    clock.tick(FPS)

# exit game
pygame.quit()
sys.exit()
