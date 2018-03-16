.code
PUBLIC Collatz
; limit passed in RCX
; return int in RAX
; rcx n
; r8 limit
; r9 maxLength
; r10 length
; r11 sequence
; rbx bitpacked wheel, 16 4-bit values
; RAX is startingNumber at end

Collatz PROC
	mov		r8, rcx		; limit = n
	shr		rcx, 1		; n /= 2
	xor		rdx, rdx	; clear for n mod 96
	mov		rax, rcx	; dividend is n
	mov		rbx, 96		; tmp divisor = 96
	div		rbx			; now rdx = n mod 96
	sub		rcx, rdx	; n -= n mod 96
						; n now aligned mod 96
	inc		rcx			; n++
	xor		rax, rax	; startingNumber = 0
	xor		r9, r9		; maxLength = 0
	mov		rbx, 7800981004390409766 ; wheel

OuterLoop:				; for n from limit/2-1 to limit
	mov		rdx, rbx	; tmp = wheel
	and		rdx, 15		; isolate 4 lsb
	add		rcx, rdx	; rcx += wheel[i]
	ror		rbx, 4		; turn wheel
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
	jb		OuterLoop	; if not, loop
	mov		rax, rcx	; startingNumber = n
	mov		r9, r10		; maxLength = length
	jmp		OuterLoop
Finish:
	ret
Collatz ENDP
END