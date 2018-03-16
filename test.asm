.code
PUBLIC Collatz
; limit passed in RCX
; return int in RAX
; rcx n
; r8 limit
; r9 sequenceLength
; r10 length
; r11 sequence
; RAX is startingNumber at end

Collatz PROC
	mov		rax, rcx
	mov		rbx, 1
	cmp		rax, rbx
	jb		Testlbl
	inc		rax
Testlbl:
	ret
Collatz ENDP
END