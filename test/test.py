import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_priority_encoder(dut): 
     
    dut.rst_n.value = 0
    dut.ena.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await Timer(1, units="ns")
    dut.rst_n.value = 1
    dut.ena.value = 1
    await Timer(1, units="ns")
 
    dut.ui_in.value = 0b00101010   
    dut.uio_in.value = 0b11110001  
    await Timer(1, units="ns")
    assert dut.uo_out.value == 13, f"wrong answer: {dut.uo_out.value}, true answer is 13"
 
    dut.ui_in.value = 0b10101010   
    dut.uio_in.value = 0b11110001  
    await Timer(1, units="ns")
    assert dut.uo_out.value == 13, f"wrong answer: {dut.uo_out.value}, true answer is 15"
 
    dut.ui_in.value = 0b00000000
    dut.uio_in.value = 0b00000000
    await Timer(1, units="ns")
    assert dut.uo_out.value == 240, f"wrong answer: {dut.uo_out.value},  true nswer is 240"
 
    dut.ui_in.value = 0b00000000
    dut.uio_in.value = 0b00000001
    await Timer(1, units="ns")
    assert dut.uo_out.value == 0, f"wrong answer: {dut.uo_out.value}, true answer is 0"

     dut.ui_in.value = 0b00000001
    dut.uio_in.value = 0b00000001
    await Timer(1, units="ns")
    assert dut.uo_out.value == 8, f"wrong answer: {dut.uo_out.value}, true answer is 8"

    print("All tests passed")
