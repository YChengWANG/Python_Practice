/*
作用：
1.修饰变量，变量不可以被改变；
2.修饰指针，分为指向常量的指针（P to const）和自身是常量的指针（const P）
3.修饰引用，指向常量的引用（ref to const），用于形参类型，即避免了拷贝，又避免了函数对值的修改
4.修饰成员函数，说明该成员函数内不能修改成员变量
*/

class A{
    private:
        const int a;
    public:
        //构造函数，初始化
        A():a(0){};
        A(int x):a(x){};

        //const 用于对重载函数的区分
        int GetValue();         //普通成员函数
        int GetValue() const;   //常成员函数，不得修改任何数据和成员的值
};

void function(){

    // 对象
    A b;                        // 普通对象，可以调用全部成员函数、更新常成员变量
    const A a;                  // 常对象，只能调用常成员函数
    const A *p = &a;            // 指针变量，指向常对象
    const A &q = a;             // 指向常对象的引用


    // 指针
    char greeting[] = "Hello";
    char* p1 = greeting;                // 指针变量，指向字符数组变量
    const char* p2 = greeting;          // 指针变量，指向字符数组常量（const 后面是 char，说明指向的字符（char）不可改变）
    char* const p3 = greeting;          // 自身是常量的指针，指向字符数组变量（const 后面是 p3，说明 p3 指针自身不可改变）
    const char* const p4 = greeting;    // 自身是常量的指针，指向字符数组常量
}

// 函数
void function1(const int Var);           // 传递过来的参数在函数内不可变
void function2(const char* Var);         // 参数指针所指内容为常量
void function3(char* const Var);         // 参数指针为常量
void function4(const int& Var);          // 引用参数在函数内为常量

// 函数返回值
const int function5();      // 返回一个常数
const int* function6();     // 返回一个指向常量的指针变量，使用：const int *p = function6();
int* const function7();     // 返回一个指向变量的常指针，使用：int* const p = function7();