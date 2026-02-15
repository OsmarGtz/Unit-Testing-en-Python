import unittest
import os
from src.bank_account import BankAccount
from unittest.mock import patch
from src.exceptions import InsufficientFundsError, WithdralTimeRestictionError


class BankAccountTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.account = BankAccount(balance = 2000, log_file = "transaction log.txt")

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
       
    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 2500, "El balance no es igual")

    def test_withdraw(self):
        new_balance = self.account.withdraw(300)
        self.assertEqual(new_balance, 1700, "El balance no es igual")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 2000, "El balance no coincide")

    def test_transaction_log(self):
        self.assertTrue(os.path.exists("transaction log.txt"))

    def test_count_transaction(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

    def test_withdraw_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2100)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 1900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdralTimeRestictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdralTimeRestictionError):
            self.account.withdraw(100)
        
    def test_deposit_multiples_ammounts(self):
        test_cases = [
            {"ammount": 100, "expected" : 2100},
            {"ammount": 3000, "expected" : 5000},
            {"ammount": 4500, "expected" : 6500}
            ]
        
        for case in test_cases:
           with self.subTest(case = case):
               self.account = BankAccount(balance = 2000, log_file="transactions.txt")
               new_balance = self.account.deposit(case["ammount"])
               self.assertEqual(new_balance, case["expected"])