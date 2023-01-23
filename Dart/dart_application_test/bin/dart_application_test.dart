// import 'package:dart_application_test/dart_application_test.dart' as dart_application_test;
// var string = "문자열";
// var num = 1;
// var fnum = 1.5;
// var list = ["apple", "banana"];
// var user = {
//   // map
//   "id": 1,
//   "username": "ss"
// };

String string = "문자열";
int num = 1;
double fnum = 1.5;
List<String> lst = ["apple", "banana"];
Map<String, dynamic> map = {"id": 1, "username": "junku"};

void main(List<String> arguments) {
  // print(string);
  // print(num);
  // print(fnum);
  // print(lst);
  // print(lst[0]);
  // print("${map["id"]}");
  print(first(add));
}

Function add = ({int n1 = 1, var n2 = 2}) {
  print("함수의 명칭은 add입니다.");
  return n1 + n2;
};

Function first = (Function f) {
  var answer = f();
  return answer;
};
