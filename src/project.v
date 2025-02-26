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
    
    // Priority encoder logic
    reg [7:0] priority_out;
    reg found;
    integer i;
    
    always @(*) begin
        priority_out = 8'hF0; // Default value when no bit is set
        found = 1'b0;
        
        for (i = 15; i >= 0; i = i - 1) begin
            // Check bits from MSB (15) to LSB (0)
            if (combined_in[i] && !found) begin
                priority_out = i[7:0];
                found = 1'b1;
            end
        end
    end
    
    assign uo_out = priority_out;
    assign uio_out = 8'b0;     
    assign uio_oe = 8'b0;      
    
    // Properly handle unused signals
    wire unused = &{ena, clk, rst_n, 1'b0};
endmodule
