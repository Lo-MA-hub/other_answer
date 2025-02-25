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
 
    for _ in range(10):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        dut.ui_in.value = a
        dut.uio_in.value = b
        await Timer(10, units="ns")
        in_val = (a << 8) | b  # Combine into 16-bit value
        expected = 240  # Default if no '1'
        for i in range(15, -1, -1):
            if in_val & (1 << i):
                expected = i
                break
        assert dut.uo_out.value == expected, f"Random test failed: In={bin(in_val)}, Expected={expected}, Got={dut.uo_out.value}"

    print("All tests passed")
