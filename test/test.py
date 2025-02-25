"""
Code author: Max Ma
Purpose: Testing if the priority encoder works 
"""
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_priority_encoder(dut):
    dut._log.info("Start")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    dut._log.info("Test priority encoder behavior")
    dut.ui_in.value = 0b00101010    # A[7:0]
    dut.uio_in.value = 0b11110001   # B[7:0]
    await Timer(10, units="ns")
    assert dut.uo_out.value == 13, f"Test 1 failed: Expected 13, got {dut.uo_out.value}"
    # test if the the answer is correct when it's the 1st term
    dut.ui_in.value = 0b00000000    # A[7:0]
    dut.uio_in.value = 0b00000001   # B[7:0]
    await Timer(10, units="ns")
    assert dut.uo_out.value == 0, f"Test 2 failed: Expected 0, got {dut.uo_out.value}"
    # test if the the answer is correct when 1's does not exist.
    dut.ui_in.value = 0b00000000    # A[7:0]
    dut.uio_in.value = 0b00000000   # B[7:0]
    await Timer(10, units="ns")
    assert dut.uo_out.value == 240, f"Test 3 failed: Expected 240, got {dut.uo_out.value}"

     # test if the the answer is correct when it's the 15th
    dut.ui_in.value = 0b10000000    
    dut.uio_in.value = 0b00000000   
    await Timer(10, units="ns")
    assert dut.uo_out.value == 15, f"Test 4 failed: Expected 15, got {dut.uo_out.value}"
    # test if the the answer is correct when it's the 2nd
    dut.ui_in.value = 0b00000000    
    dut.uio_in.value = 0b00000011   
    await Timer(10, units="ns")
    assert dut.uo_out.value == 1, f"Test 5 failed: Expected 1, got {dut.uo_out.value}"
