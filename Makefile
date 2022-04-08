# celaut
python3 -m grpc_tools.protoc -I. --python_out=. celaut.proto --experimental_allow_proto3_optional &&
# onnx
python3 -m grpc_tools.protoc -I. --python_out=. onnx.proto --experimental_allow_proto3_optional &&
# api
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. api.proto --experimental_allow_proto3_optional &&
# gateway
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. gateway.proto --experimental_allow_proto3_optional &&
# solvers_dataset
python3 -m grpc_tools.protoc -I. --python_out=. solvers_dataset.proto --experimental_allow_proto3_optional &&
# buffer
python3 -m grpc_tools.protoc -I. --python_out=. buffer.proto --experimental_allow_proto3_optional &&
# compile
python3 -m grpc_tools.protoc -I. --python_out=. compile.proto --experimental_allow_proto3_optional 