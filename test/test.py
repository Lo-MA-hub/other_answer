# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_priority_encoder(dut):
    """Test the priority encoder functionality."""
    dut._log.info("Starting priority encoder test")

    # Define test cases: (ui_in, uio_in, expected priority output, expected NAND output)
    test_cases = [
        (0b00000000, 0b00000000, 0b11110000, 0b11111111),  # All zeros case
        (0b00000001, 0b00000000, 0b00000000, 0b11111110),  # LSB first '1'
        (0b00010000, 0b00000000, 0b00000100, 0b11101111),  # Single '1' in MSB half
        (0b00000000, 0b10000000, 0b00001000, 0b01111111),  # First '1' in B[7:0]
        (0b11110000, 0b00001111, 0b00001100, 0b00001111),  # Multiple '1's, highest at 12
    ]

    for ui_in, uio_in, expected_priority, expected_nand in test_cases:
        # Set inputs
        dut.ui_in.value = ui_in
        dut.uio_in.value = uio_in

        # Wait briefly to ensure values settle
        await Timer(1, units="ns")

        # Check expected outputs
        assert dut.uo_out.value == expected_priority, \
            f"Priority encoder failed: {bin(ui_in)} {bin(uio_in)} -> {bin(dut.uo_out.value)}, expected {bin(expected_priority)}"
        
        assert dut.uio_out.value == expected_nand, \
            f"Bitwise NAND failed: {bin(ui_in)} & {bin(uio_in)} -> {bin(dut.uio_out.value)}, expected {bin(expected_nand)}"
    
    dut._log.info("Priority encoder test completed successfully")
