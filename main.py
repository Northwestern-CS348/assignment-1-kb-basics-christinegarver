import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase

class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)

        # Assert facts from statements_kb2.txt
        file2 = 'statements_kb2.txt'
        data2 = read.read_tokenize(file2)
        for item2 in data2:
            if isinstance(item2, Fact):
                self.KB.kb_assert(item2)



    # Tests Provided
    def test1(self):
        ask1 = read.parse_input("fact: (color bigbox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        #self.assertEqual(answer.list_of_bindings[0][1][0], ask1)

    def test2(self):
        ask1 = read.parse_input("fact: (color littlebox red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)

    def test3(self):
        ask1 = read.parse_input("fact: (color ?X red)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox")
        self.assertEqual(str(answer[1]), "?X : pyramid3")
        self.assertEqual(str(answer[2]), "?X : pyramid4")


    def test4(self):
        ask1 = read.parse_input("fact: (color bigbox ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?Y : red")

    def test5(self):
        ask1 = read.parse_input("fact: (color ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox, ?Y : red")
        self.assertEqual(str(answer[1]), "?X : littlebox, ?Y : blue")
        self.assertEqual(str(answer[2]), "?X : pyramid1, ?Y : blue")
        self.assertEqual(str(answer[3]), "?X : pyramid2, ?Y : green")
        self.assertEqual(str(answer[4]), "?X : pyramid3, ?Y : red")
        self.assertEqual(str(answer[5]), "?X : pyramid4, ?Y : red")

    # Own tests

    # test to make sure assert only stores Facts
    """def test6(self):
        result = self.KB.kb_assert(Fact("fact: (color cube ?X)"))
        self.assertTrue(result)

    def test7(self):
        result = self.KB.kb_assert("rule: ((inst ?x ?y) (isa ?y ?z)) -> (inst ?x ?z)")
        self.assertFalse(result)

    def test8(self):
        result = self.KB.kb_assert(Fact("fact: ()"))
        self.assertFalse(result)"""

    # asserting elements from statements_kb2.txt
    def test8(self):
        ask1 = read.parse_input("fact: (isa ?X Wizard)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Sorceress")

    # asking for a rule returns false
    def test9(self):
        ask1 = read.parse_input("rule: ((inst ?x ?y) (isa ?y ?z)) -> (inst ?x ?z)")
        print(' Asking if', ask1)
        answer=self.KB.kb_ask(ask1)
        self.assertFalse(answer)

    # asking for a fact that does not exist in KB should return false
    def test10(self):
        ask1 = read.parse_input("fact: (color cube yello)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)

    # asking with no object
    def test11(self):
        ask1 = read.parse_input("fact: (color ?X blue)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : littlebox")
        self.assertEqual(str(answer[1]), "?X : pyramid1")

    # missing object and adjective from both statement files
    def test12(self):
        ask1 = read.parse_input("fact: (inst ?X ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : bigbox, ?Y : box")
        self.assertEqual(str(answer[1]), "?X : littlebox, ?Y : box")
        self.assertEqual(str(answer[2]), "?X : pyramid1, ?Y : pyramid")
        self.assertEqual(str(answer[3]), "?X : pyramid2, ?Y : pyramid")
        self.assertEqual(str(answer[4]), "?X : pyramid3, ?Y : pyramid")
        self.assertEqual(str(answer[5]), "?X : pyramid4, ?Y : pyramid")
        self.assertEqual(str(answer[6]), "?X : cube1, ?Y : cube")
        self.assertEqual(str(answer[7]), "?X : cube2, ?Y : cube")
        self.assertEqual(str(answer[8]), "?X : cube3, ?Y : cube")
        self.assertEqual(str(answer[9]), "?X : cube4, ?Y : cube")
        self.assertEqual(str(answer[10]), "?X : sphere1, ?Y : sphere")
        self.assertEqual(str(answer[11]), "?X : Sarorah, ?Y : Sorceress")
        self.assertEqual(str(answer[12]), "?X : Nosliw, ?Y : Dragon")


    # asserting a rule should not assert anything into KB
    def test13(self):
        item1 = Fact("rule: ((inst ?x ?y) (isa ?y ?z)) -> (inst ?x ?z)")
        self.KB.kb_assert(item1)
        ask1 = read.parse_input("rule: ((inst ?x ?y) (isa ?y ?z)) -> (inst ?x ?z)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertFalse(answer)






if __name__ == '__main__':
    unittest.main()
