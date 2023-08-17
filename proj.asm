.data
ler_op: .asciiz "\nIndique a operação que pretende realizar: "
op_soma: .asciiz "\nIndique '1' para calcular a soma de dois números."
op_subt: .asciiz "\nIndique '2' para calcular a subtracção de dois números."
op_multiplic: .asciiz "\nIndique '3' para calcular a multiplicação de dois números."
op_divis: .asciiz "\nIndique '4' para calcular a divisão de dois números."
op_fact: .asciiz "\nIndique '5' para calcular o factorial de um número."
op_pot: .asciiz "\nIndique '6' para calcular a potencia de um número."
op_sair: .asciiz "\nIndique '7' para terminar o programa "
ler_int_1: .asciiz "\nIntroduza o primeiro número inteiro: "
ler_int_2: .asciiz "\nIntroduza o segundo número inteiro: "
ler_n_fact: .asciiz "\nIndique o número para calcular o factorial: "
ler_n_q_c: .asciiz "\nIndique um número inteiro: "
ler_b_pote_: .asciiz "\nIndique a base da potencia: "
ler_e_pote_: .asciiz "\nIndique o expoente da potencia: "
resultado_soma: .asciiz "O resultado da soma dos dois números e: "
resultado_sub: .asciiz "O resultado da diferença dos dois números e: "
resultado_mult: .asciiz "O resultado da multiplicação dos dois números e: "
resultado_div: .asciiz "O resultado da divisão é: "
result_fact: .asciiz "\n factorial é: "
result_poten: .asciiz "\n O resultado da potencia é: "
err: .asciiz "\nOpção inválida."
n_linha: .asciiz "\n"
.text
.globl __start
__start:
opcoes:
la $a0, n_linha
li $v0, 4
syscall
la $a0, op_soma
li $v0, 4
syscall
la $a0, op_subt
li $v0, 4
syscall
la $a0, op_multiplic
li $v0, 4
syscall
la $a0, op_divis
li $v0, 4
syscall
la $a0, op_fact
li $v0, 4
syscall
la $a0, op_pot
li $v0, 4
syscall
la $a0, op_sair
li $v0, 4
syscall
la $a0, n_linha
li $v0, 4
syscall
la $a0, ler_op
li $v0, 4
syscall


li $v0, 5
syscall
move $a1, $v0



beq $a1, 1, op_som
beq $a1, 2, op_sub
beq $a1, 3, op_mul
beq $a1, 4, op_div
beq $a1, 5, op_f
beq $a1, 6, op_t
beq $a1, 7, fim_prg
blt $a1, 1, erro

op_som:
addi $sp, $sp, -4
sw $ra, 0($sp)
jal soma

op_sub:
addi $sp, $sp, -4
sw $ra, 0($sp)
jal subtracao
j opcoes

op_mul:
addi $sp, $sp, -4
sw $ra, 0($sp)
jal multiplicacao
j opcoes


op_div:
addi $sp, $sp, -4
sw $ra, 0($sp)
jal divisao
j opcoes

op_f:
addi $sp, $sp, -4
sw $ra, 0($sp)
jal factorial
j opcoes

op_t:
addi $sp, $sp, -4
sw $ra, 0($sp)
jal potencia
j opcoes


soma:
addi $sp, $sp, -8
sw $ra, -4($sp)
la $a0, ler_int_1
li $v0, 4
syscall
li $v0, 5
syscall
move $t0, $v0
la $a0, ler_int_2
li $v0, 4
syscall
li $v0, 5
syscall
move $t1, $v0
la $a0, resultado_soma
li $v0, 4
syscall
add $a0, $t0, $t1
li $v0, 1
syscall
la $a0, n_linha
li $v0, 4
syscall
li $v0, 5
syscall
lw $ra, -4($sp)
addi $sp, $sp, 4
jr $ra

subtracao:
addi $sp, $sp, -8
sw $ra, -4($sp)
la $a0, ler_int_1
li $v0, 4
syscall
li $v0, 5
syscall
move $t1, $v0
la $a0, ler_int_2
li $v0, 4
syscall
li $v0, 5
syscall
move $t2, $v0
la $a0, resultado_sub
li $v0, 4
syscall
sub $a0, $t1, $t2
li $v0, 1
syscall
la $a0, n_linha
li $v0, 4
syscall
li $v0, 5
syscall
lw $ra, -4($sp)
addi $sp, $sp, 4
jr $ra


multiplicacao:
addi $sp, $sp, -8
sw $ra, -4($sp)
la $a0, ler_int_1
li $v0, 4
syscall
li $v0, 5
syscall
move $t1, $v0
la $a0, ler_int_2
li $v0, 4
syscall
li $v0, 5
syscall
move $t2, $v0
la $a0, resultado_mult
li $v0, 4
syscall
mul $a0 $t1, $t2
li $v0, 1
syscall
la $a0, n_linha
li $v0, 4
syscall
li $v0, 5
syscall
lw $ra, -4($sp)
addi $sp, $sp, 4
jr $ra


divisao:
addi $sp, $sp, -8
sw $ra, -4($sp)
la $a0, ler_int_1
li $v0, 4
syscall
li $v0, 5
syscall
move $t1, $v0
la $a0, ler_int_2
li $v0, 4
syscall
li $v0, 5
syscall
move $t2, $v0
la $a0, resultado_div
li $v0, 4
syscall
div $t1, $t2
mflo $a0
li $v0, 1
syscall
la $a0, n_linha
li $v0, 4
syscall
li $v0, 5
syscall
lw $ra, -4($sp)
addi $sp, $sp, 4
jr $ra


factorial:
addi $sp, $sp, -8
sw $ra, -4 ($sp)
la $a0, ler_n_fact
li $v0, 4
syscall
li $v0, 5
syscall
move $a0, $v0
jal FACT
move $s0, $v0
la $a0, result_fact
li $v0, 4
syscall
move $a0, $s0
li $v0, 1
syscall
la $a0, n_linha
li $v0, 4
syscall
lw $ra, 4($sp)
addi $sp, $sp, 8
j opcoes
FACT: 
addi $sp, $sp, -12
sw $ra, 8($sp)
sw $a0, 0($sp)
li $v0, 1
slti $t0, $a0, 2
bne $t0, $0, sai_fact
addi $a0, $a0, -1
jal FACT
lw $t0, 0($sp)
mul $v0, $v0, $t0
sai_fact:
lw $ra, 8($sp)
addi $sp, $sp, 12
jr $ra


potencia:
addi $sp, $sp, -8
sw $ra, -4($sp)
la $a0, ler_b_pote_
li $v0, 4
syscall
li $v0, 5
syscall
move $t1, $v0
la $a0, ler_e_pote_
li $v0, 4
syscall
li $v0, 5
syscall
move $t2, $v0
la $a0, result_poten
li $v0, 4
syscall
move $s0, $zero
li $t0, 1
for: 
beq $t0,$t2,Instr_c
mul $a0,$t0,$t1
move $t3,$a0
addi $t0,$t0,1
j for
sw
Instr_c:
li $v0, 1
syscall
la $a0, n_linha
li $v0, 4
syscall
li $v0, 5
syscall
lw $ra, -4($sp)
addi $sp, $sp, 4
jr $ra

erro:
la $a0, err
li $v0, 4
syscall	
j opcoes

fim_prg:
li $v0, 10
syscall

