// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.
(LOOP)
    @KBD
    D=M
    @BLACKEN
    D;JNE 
    @color
    M=0    
    @RENDER
    0;JMP
(BLACKEN)
    @color
    M=-1    
(RENDER)
    @SCREEN
    D=A
    @address
    M=D    
(SCREEN_LOOP)
    @color
    D=M   
    @address
    A=M      
    M=D      
    @address
    M=M+1   
    D=M
    @KBD
    D=D-A  
    @SCREEN_LOOP
    D;JLT    
    @LOOP
    0;JMP  
