

# inside the game loop, to do the event process loop
# to process all events/commands happened in one frame time
for event in pygame.event.get():

    if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_F4 and event.mod&pygame.KMOD_ALT:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        else:
            pass
    elif event.type == pygame.ACTIVEEVENT:
        if event.state==pygame.APPACTIVE:
            if event.gain: # program de-iconized
                pass
            else:    # program iconized (minimized)
                pass
        elif event.state==pygame.APPINPUTFOCUS:
            if event.gain: # program get focus (window at front layer)
                pass
            else:    # program lost focus (window at back layer)
                pass            
        elif event.state==pygame.APPFOCUSMOUSE:
            if event.gain: # mouse in program window
                pass
            else:    # mouse out of program window
                pass
    elif event.type == pygame.KEYDOWN:
        pass
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pass
    elif event.type == pygame.MOUSEBUTTONUP:
        pass
    elif event.type == pygame.MOUSEMOTION:
        pass
