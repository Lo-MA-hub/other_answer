`default_nettype none

module tt_um_priority_encoder (
    input  wire [7:0] ui_in,   
    input  wire [7:0] uio_in,  
    output wire [7:0] uo_out,  
    input  wire       ena,     
    input  wire       clk,     
    input  wire       rst_n,   
    output wire [7:0] uio_out, 
    output wire [7:0] uio_oe   
`ifdef GL_TEST
    ,input wire VPWR,          
    input wire VGND            
`endif
);
 
    wire [15:0] in;
    assign in = {ui_in, uio_in};  // ui_in is A[7:0] (MSB), uio_in is B[7:0] (LSB)
 
    reg [7:0] out;

    // Priority encoder logic
    always @(*) begin
        if (in[15])         out = 8'd15;  
        else if (in[14])    out = 8'd14;
        else if (in[13])    out = 8'd13;
        else if (in[12])    out = 8'd12;
        else if (in[11])    out = 8'd11;
        else if (in[10])    out = 8'd10;
        else if (in[9])     out = 8'd9;
        else if (in[8])     out = 8'd8;
        else if (in[7])     out = 8'd7;
        else if (in[6])     out = 8'd6;
        else if (in[5])     out = 8'd5;
        else if (in[4])     out = 8'd4;
        else if (in[3])     out = 8'd3;
        else if (in[2])     out = 8'd2;
        else if (in[1])     out = 8'd1;
        else if (in[0])     out = 8'd0;
        else                out = 8'b1111_0000;  
    end

  
    assign uo_out = (ena & rst_n) ? out : 8'b0;
 
    assign uio_oe  = 8'b0;   
    assign uio_out = 8'b0;   

endmodule

`default_nettype wire
