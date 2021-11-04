import gateway_pb2

# This is part of the transport protocol (slot) data.
StartService_input = {
    1 : gateway_pb2.celaut__pb2.Any.Metadata.HashTag.Hash,
    2 : gateway_pb2.celaut__pb2.Any,
    3: gateway_pb2.HashWithConfig,
    4: gateway_pb2.ServiceWithConfig
}

"""
    // ( celaut.Any.Metadata.HashTag.Hash=H, celaut.Any=S, celaut.Configuration=C; { H v S v H^C v S^C } )

    // S partition [(1, 2.4, 3, 4), (2.1, 2.2, 2.3)]

    // H^C 
    message HashWithConfig { 
        celaut.Any.Metadata.HashTag.Hash hash = 1;
        celaut.Configuration config = 3;  
    }

    // S^C
    message ServiceWithConfig { 
        celaut.Any service = 2;
        celaut.Configuration config = 3;
    }
.proto
"""