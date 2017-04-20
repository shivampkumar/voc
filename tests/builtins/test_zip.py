from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class ZipTests(TranspileTestCase):
    def test_zip(self):
        self.assertCodeExecution("""
            lst=['a','b','c','d','e']
            str="TestString"
            tup=(1,2,5,9,4,8,0,4)
            print(list(zip(lst,str,tup)))
            print(list(zip(lst,tup,"hi there")))
            """)

    def test_zip_expectedFailure(self):
        self.assertCodeExecution("""
            lst=['a','b','c','d','e']
            str="TestString"
            tup=(1,2,5,9,4,8,0,4)
            try:
                print(list(zip(5)))
            except TypeError as err:
                print(err)
            try:
                print(list(zip(lst,str,tup,7.9)))
            except TypeError as err:
                print(err)
            try:
                print(list(zip(True,lst,tup,"hi there")))
            except TypeError as err:
                print(err)
            """)


class BuiltinZipFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["zip"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_None',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple',
    ]
