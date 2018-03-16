.code
PUBLIC Collatz
; limit passed in RCX
; return int in RAX
; rcx n
; r8 limit
; r9 maxLength
; r10 length
; r11 sequence
; RAX is startingNumber at end

Collatz PROC
	mov		r8, rcx		; limit = n
	shr		rcx, 1		; n /= 2
	dec		rcx			; n = limit/2-1
	xor		rax, rax	; startingNumber = 0
	xor		r9, r9		; maxLength = 0
OuterLoop:				; for n from limit/2-1 to limit
	inc		rcx
	inc		rcx			; n += 2
	cmp		rcx, r8		; if n < limit
	ja		Finish
	mov		r10, 1		; length = 1
	mov		r11, rcx	; sequence = n
InnerLoop:				; while sequence > 1
	test	r11, 1		; set zero flag if even
	jz		Ev

	lea		r11, [r11*2 + r11 + 1] ; sequence = 3seq + 1
	inc		r10			; length++
Ev:						; always fall thru to ev
	shr		r11, 1		; seq /= 2
	inc		r10			; length++
	cmp		r11, 1		; if seq = 1
	ja		InnerLoop	; continue inner loop

	cmp		r10, r9		; if length > maxLength
	jb		OuterLoop
	mov		rax, rcx	; startingNumber = n
	mov		r9, r10
	jmp		OuterLoop
Finish:
	ret
Collatz ENDP
END