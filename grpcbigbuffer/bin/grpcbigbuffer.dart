import 'package:protobuf/protobuf.dart';

void main(List<String> arguments) {
  print('Hello world!', );

  //call AsyncGenerator
  Stream<int> asyncGenerator=createAsyncGenerator(15);
  
  //use AsyncGenerator
  asyncGenerator.listen((int value) {
    print('Value Form Async Generator: $value');
  });

}

//Create AsyncGenerator
Stream<int> createAsyncGenerator(int n) async* {
  int k = 0;
  while (k < n) yield k++;
}