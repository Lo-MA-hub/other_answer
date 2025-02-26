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
    
    always @(*) begin
        if (combined_in == 16'b0) begin
            // Special case: all zeros
            priority_out = 8'b11110000;  
        end else begin
            // Default to 0, will be overridden by first 1 found
            priority_out = 8'b0;
            
            // Check bits from MSB (15) to LSB (0)
            if (combined_in[15]) priority_out = 8'd15;
            else if (combined_in[14]) priority_out = 8'd14;
            else if (combined_in[13]) priority_out = 8'd13;
            else if (combined_in[12]) priority_out = 8'd12;
            else if (combined_in[11]) priority_out = 8'd11;
            else if (combined_in[10]) priority_out = 8'd10;
            else if (combined_in[9]) priority_out = 8'd9;
            else if (combined_in[8]) priority_out = 8'd8;
            else if (combined_in[7]) priority_out = 8'd7;
            else if (combined_in[6]) priority_out = 8'd6;
            else if (combined_in[5]) priority_out = 8'd5;
            else if (combined_in[4]) priority_out = 8'd4;
            else if (combined_in[3]) priority_out = 8'd3;
            else if (combined_in[2]) priority_out = 8'd2;
            else if (combined_in[1]) priority_out = 8'd1;
            else if (combined_in[0]) priority_out = 8'd0;
        end
    end

    
    assign uo_out = priority_out;
    assign uio_out = 8'b0;     
    assign uio_oe = 8'b0;      

    
    wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule
