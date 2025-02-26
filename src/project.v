/*
 * Copyright (c) 2025 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_priority_encoder ( 
    input  wire [7:0] ui_in,    
    output wire [7:0] uo_out,   
    input  wire [7:0] uio_in,   
    output wire [7:0] uio_out,  
    output wire [7:0] uio_oe,   
    input  wire       ena,      
    input  wire       clk,      
    input  wire       rst_n     
);

    
    wire [15:0] combined_in;
    assign combined_in = {ui_in, uio_in};
    // whether it's the first time to find the 1.
    integer term;
    integer i;
    // Priority encoder logic
    reg [7:0] priority_out;
    
    always @(*) begin
        
        // Default to 0, will be overridden by first 1 found
        priority_out = 8'b11110000;
        term = 0;
        for (i = 15; i >= 0; i = i - 1) begin
            // Check bits from MSB (15) to LSB (0)
            if (combined_in[i] && term == 0) begin
                priority_out = i;
                term = 1;
            end
    end

    
    assign uo_out = priority_out;
    assign uio_out = 8'b0;     
    assign uio_oe = 8'b0;      

    
    wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule
