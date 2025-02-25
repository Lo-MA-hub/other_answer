import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_priority_encoder(dut): 
     
    dut.rst_n.value = 0
    dut.ena.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await Timer(10, units="ns")
    dut.rst_n.value = 1
    dut.ena.value = 1
    await Timer(10, units="ns")
 
    dut.ui_in.value = 0b00101010   
    dut.uio_in.value = 0b11110001  
    await Timer(10, units="ns")
    assert dut.uo_out.value == 13, f"Test 1 failed: Expected 13, got {dut.uo_out.value}"
 
    dut.ui_in.value = 0b00000000
    dut.uio_in.value = 0b00000001
    await Timer(10, units="ns")
    assert dut.uo_out.value == 0, f"Test 2 failed: Expected 0, got {dut.uo_out.value}"
 
    dut.ui_in.value = 0b00000000
    dut.uio_in.value = 0b00000000
    await Timer(10, units="ns")
    assert dut.uo_out.value == 240, f"Test 3 failed: Expected 240, got {dut.uo_out.value}"

    # Additional 
    dut.ui_in.value = 0b10000000    
    dut.uio_in.value = 0b00000000   
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 15, f"Test 4 failed: Expected 15, got {dut.uo_out.value}"

    print("All tests passed")
