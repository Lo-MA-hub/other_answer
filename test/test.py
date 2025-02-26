 

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
    await ClockCycles(dut.clk, 1)
    dut.rst_n.value = 1

    dut._log.info("Test priority encoder behavior")

    # Test 1: High priority bit detection (bit 13)
    dut.ui_in.value = 0b00101010
    dut.uio_in.value = 0b11110001
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 13, f"Test 1 failed: Expected 13, got {dut.uo_out.value}"

    # Test 2： Test if it works well when the input is 1. 
    dut.ui_in.value = 0b00000000    # A[7:0]
    dut.uio_in.value = 0b00000001   # B[7:0]
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0, f"Test 2 failed: Expected 0, got {dut.uo_out.value}"

    # Test 3: Test if the function behaves well when the input is 0
    dut.ui_in.value = 0b00000000    # A[7:0]
    dut.uio_in.value = 0b00000000   # B[7:0]
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 240, f"Test 3 failed: Expected 240, got {dut.uo_out.value}"

    # Test 4: Test if the function behaves well when the highest 1 is 15th.
    dut.ui_in.value = 0b10000000    
    dut.uio_in.value = 0b00000000   
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 15, f"Test 4 failed: Expected 15, got {dut.uo_out.value}"

    dut._log.info("All tests passed")
