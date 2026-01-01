// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

(RESTART)
    @SCREEN
    D=A
    @address
    M=D        
(KBD_CHECK)
    @KBD
    D=M
    @BLACK
    D;JNE  
    @color
    M=0      
    @DRAW
    0;JMP
(BLACK)
    @color
    M=-1     
(DRAW)
    @color
    D=M
    @address
    A=M       
    M=D       
    @address
    M=M+1     
    D=M
    @KBD
    D=A-D      
    @DRAW
    D;JGT      
    @RESTART
    0;JMP     
