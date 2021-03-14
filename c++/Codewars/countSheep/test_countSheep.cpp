using namespace std;

Describe(count_sheep_method){
    It(array_one){
        vector<bool> array1 = {true, true, true, false,
                               true, true, true, true,
                               true, false, true, false,
                               true, false, false, true,
                               true, true, true, true,
                               false, false, true, true};
Assert::That(count_sheep(array1), Equals(17));
}
}
;