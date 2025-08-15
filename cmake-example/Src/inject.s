.syntax unified
.cpu cortex-m4
.thumb
    .section .text.AsmDumper
      .weak AsmDumper
    .type AsmDumper, %function
AsmDumper:
    push {r0-r4}
    /**
        Load data from address
     */
    ldr r0, =0x08000000
    ldr r1, =0x20000000
    ldr r2, [r1]
    add r0, r2

    ldr r4, =0x08000080
    cmp r0, r4
    bge end

    /* [data] <- memory */
    ldrb r0, [r0]

    /* while -> UARTx->SR */
loop:
    ldr r3, =0x40004400
    ldr r4, [r3, #0]
    and r4, #128
    cmp	r4, #128	
    bne loop

    /* [data] -> UARTx->DR */
    strh r0, [r3, #4]

    /* Increment and store */
    add r2, #1
    str r2, [r1]
end:
    /* Send over UART */
    pop {r0-r4}
    mov r0, #0
    bx lr