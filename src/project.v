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

    wire [15:0] in = {ui_in, uio_in};  // 合并两个8位输入为16位信号
    reg [7:0] out;

    always @(*) begin
        out = 8'b1111_0000; // 默认值
        for (integer i = 15; i >= 0; i = i - 1) begin
            if (in[i]) begin
                out = i;
                break;
            end
        end
    end

    assign uo_out = (ena & rst_n) ? out : 8'b0;
    assign uio_oe  = 8'b0;
    assign uio_out = 8'b0;

endmodule

`default_nettype wire
