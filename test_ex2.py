import sqlite3, unittest, ex2

class TestFuncs(unittest.TestCase):

    def test_insert(self):
        
        self.assertEqual(ex2.insert_utilisateur("bob","Abc123!@#"), True)
        self.assertEqual(ex2.insert_utilisateur("alice","Hhh111-+="), True)
        self.assertEqual(ex2.insert_utilisateur("bo","Abc123!@#"), False)
        self.assertEqual(ex2.insert_utilisateur("bob","Abc123!"), False)
        self.assertEqual(ex2.insert_utilisateur("bob","Abc123!@#"), False)

    def test_logging(self):
        
        self.assertEqual(ex2.logging("bob","Abc123!@#"), True)
        self.assertEqual(ex2.logging("alice","Hhh111-+="), True)
        self.assertEqual(ex2.logging("bobbb","Abc123!@#"), False)
        self.assertEqual(ex2.logging("bob","Abc123!sdad"), False)

    def test_verification(self):
        
        self.assertEqual(ex2.verification(), True)
        ex2.c.execute("insert into utilisateurs values (?, ?, ?, ?, ?, ?)", ("bo", "dawcwa", "ds23fwf2fsiu", "12dhs9ad91g", "19huwdhqwu", "12ucbvrvja"))
        self.assertEqual(ex2.verification(), False)
        ex2.c.execute("delete from utilisateurs where username = 'bo'")

if __name__ == '__main__':
    unittest.main()