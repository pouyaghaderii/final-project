# تعریف کلاس کاربر
class User:
    # سازنده کلاس کاربر
    def __init__(self, name, password):
        # نام و رمز عبور کاربر را ذخیره می‌کنیم
        self.name = name
        self.password = password
        # یک لیست خالی برای حساب های کاربر ایجاد می‌کنیم
        self.accounts = []

    # یک متد برای اضافه کردن یک حساب به لیست حساب های کاربر
    def add_account(self, account):
        # حساب را به لیست اضافه می‌کنیم
        self.accounts.append(account)

    # یک متد برای نمایش اطلاعات کاربر و حساب هایش
    def show_info(self):
        # نام و تعداد حساب های کاربر را چاپ می‌کنیم
        print(f"User: {self.name}")
        print(f"Number of accounts: {len(self.accounts)}")
        # برای هر حساب در لیست حساب ها، شماره و موجودی آن را چاپ می‌کنیم
        for account in self.accounts:
            print(f"Account number: {account.number}")
            print(f"Account balance: {account.balance}")

# تعریف کلاس حساب
class Account:
    # سازنده کلاس حساب
    def __init__(self, number, balance):
        # شماره و موجودی حساب را ذخیره می‌کنیم
        self.number = number
        self.balance = balance

    # یک متد برای افزودن مبلغ به موجودی حساب
    def deposit(self, amount):
        # مبلغ را به موجودی اضافه می‌کنیم
        self.balance += amount

    # یک متد برای برداشت مبلغ از موجودی حساب
    def withdraw(self, amount):
        # اگر مبلغ کمتر یا مساوی موجودی باشد، آن را از موجودی کم می‌کنیم و True برمی‌گردانیم
        if amount <= self.balance:
            self.balance -= amount
            return True
        # در غیر این صورت، False برمی‌گردانیم
        else:
            return False

# تعریف کلاس admin
class Admin(User):
    # سازنده کلاس admin
    def __init__(self, name, password):
        # سازنده کلاس پدر (User) را با نام و رمز عبور فراخوانی می‌کنیم
        super().__init__(name, password)
        # یک لغت خالی برای نگه داشتن تمام کاربران و حساب های بانک ایجاد می‌کنیم
        self.bank = {}

    # یک متد برای اضافه کردن یک کاربر به لغت بانک
    def add_user(self, user):
        # نام کاربر را به عنوان کلید و لیست حساب هایش را به عنوان مقدار در لغت قرار میدهيم 
        self.bank[user.name] = user.accounts

    # یک متد برای نمایش اطلاعات تمامی کاربران و حساب های بانک
    def show_bank_info(self):
        # برای هر کلید و مقدار در لغت بانک
        for name, accounts in self.bank.items():
            # نام کاربر و تعداد حساب هایش را چاپ می‌کنیم
            print(f"User: {name}")
            print(f"Number of accounts: {len(accounts)}")
            # برای هر حساب در لیست حساب ها، شماره و موجودی آن را چاپ می‌کنیم
            for account in accounts:
                print(f"Account number: {account.number}")
                print(f"Account balance: {account.balance}")
# وارد کردن کتابخانه datetime برای کار با تاریخ
import datetime

# تعریف یک لیست خالی برای نگه داشتن کد ملی های ثبت شده
national_codes = []

# تعریف یک شمارنده برای تولید کد منحصر به فرد برای هر کاربر
user_id = 0
# تغییر سازنده کلاس کاربر
def __init__(self, name, family_name, father_name, birth_date, city, mobile_number, national_code, landline_number=None):
    # اگر کد ملی در لیست کد ملی ها وجود داشت، یک خطا پرتاب می‌کنیم
    if national_code in national_codes:
        raise ValueError("National code already exists")
    # در غیر این صورت، کد ملی را به لیست اضافه می‌کنیم
    else:
        national_codes.append(national_code)
    # نام، نام خانوادگی، نام پدر، تاریخ تولد، شهر، شماره موبایل، شماره ثابت و کد ملی را ذخیره می‌کنیم
    self.name = name
    self.family_name = family_name
    self.father_name = father_name
    self.birth_date = birth_date
    self.city = city
    self.mobile_number = mobile_number
    self.landline_number = landline_number
    self.national_code = national_code
    # یک لیست خالی برای حساب های کاربر ایجاد می‌کنیم
    self.accounts = []
    # یک شماره منحصر به فرد برای هر کاربر تولید می‌کنیم و آن را ذخیره می‌کنیم
    global user_id # برای دسترسی به شمارنده جهانی user_id
    user_id += 1 # شمارنده را یک واحد افزایش میدهيم 
    self.id = user_id # شمارنده را به عنوان شماره کاربر ذخیره میدهيم 

# تغییر متد show_info برای نمایش اطلاعات بیشتر کاربر و حساب هایش
def show_info(self):
    # نام، نام خانوادگی، نام پدر، تاریخ تولد، شهر، شماره موبایل، شماره ثابت، کد ملی و شماره کاربر را چاپ میدهيم 
    print(f"Name: {self.name}")
    print(f"Family name: {self.family_name}")
    print(f"Father name: {self.father_name}")
    print(f"Birth date: {self.birth_date}")
    print(f"City: {self.city}")
    print(f"Mobile number: {self.mobile_number}")
    print(f"Landline number: {self.landline_number}")
    print(f"National code: {self.national_code}")
    print(f"User ID: {self.id}")
    # تعداد حساب های کاربر را چاپ می‌کنیم
    print(f"Number of accounts: {len(self.accounts)}")
    # برای هر حساب در لیست حساب ها، شماره، موجودی و تاریخ افتتاح آن را چاپ می‌کنیم
    for account in self.accounts:
        print(f"Account number: {account.number}")
        print(f"Account balance: {account.balance}")
        print(f"Account opening date: {account.opening_date}")

# تغییر سازنده کلاس حساب
def __init__(self, number, balance):
    # شماره و موجودی حساب را ذخیره می‌کنیم
    self.number = number
    self.balance = balance
    # تاریخ افتتاح حساب را با استفاده از کتابخانه datetime ذخیره می‌کنیم
    self.opening_date = datetime.date.today()

# اضافه کردن یک متد برای نمایش جزئیات واریزها و برداشت های حساب
def show_transactions(self):
    # چاپ شماره و موجودی حساب
    print(f"Account number: {self.number}")
    print(f"Account balance: {self.balance}")
    # چاپ تعداد و جزئیات واریزها و برداشت های حساب
    print(f"Number of deposits: {len(self.deposits)}")
    for deposit in self.deposits:
        print(f"Deposit amount: {deposit.amount}")
        print(f"Deposit date: {deposit.date}")
        print(f"Deposit time: {deposit.time}")
        print(f"Deposit description: {deposit.description}")
    print(f"Number of withdrawals: {len(self.withdrawals)}")
    for withdrawal in self.withdrawals:
        print(f"Withdrawal amount: {withdrawal.amount}")
        print(f"Withdrawal date: {withdrawal.date}")
        print(f"Withdrawal time: {withdrawal.time}")
        print(f"Withdrawal description: {withdrawal.description}")

# تعریف یک کلاس برای نگه داشتن جزئیات یک واریز یا برداشت
class Transaction:
    # سازنده کلاس Transaction
    def __init__(self, amount, description):
        # مقدار و توضیحات واریز یا برداشت را ذخیره میدهيم 
        self.amount = amount
        self.description = description
        # تاریخ و زمان واریز یا برداشت را با استفاده از کتابخانه datetime ذخیره میدهيم 
        self.date = datetime.date.today()
        self.time = datetime.datetime.now().time()

    
    # تغییر متد deposit برای ذخیره جزئیات واریز
    def deposit(self, amount, description):
        # مبلغ را به موجودی اضافه می‌کنیم
        self.balance += amount
        # یک شیء از کلاس Transaction با مقدار و توضیحات واریز ایجاد می‌کنیم
        deposit = Transaction(amount, description)
        # اگر لیست واریزها وجود نداشت، یک لیست خالی ایجاد می‌کنیم
        if not hasattr(self, "deposits"):
            self.deposits = []
        # شیء واریز را به لیست واریزها اضافه می‌کنیم
        self.deposits.append(deposit)
    
    # تغییر متد withdraw برای ذخیره جزئیات برداشت
    def withdraw(self, amount, description):
        # اگر مبلغ کمتر یا مساوی موجودی باشد، آن را از موجودی کم می‌کنیم و True برمی‌گردانیم
        if amount <= self.balance:
            self.balance -= amount
            # یک شیء از کلاس Transaction با مقدار و توضیحات برداشت ایجاد میدهيم 
            withdrawal = Transaction(amount, description)
            # اگر لیست برداشت ها وجود نداشت، یک لیست خالی ايجاد میدهيم 
            if not hasattr(self, "withdrawals"):
                self.withdrawals = []
            # شيء برداشت را به ليست برداشت ها اضافه مي‌کنيم
            self.withdrawals.append(withdrawal)
            return True
        # در غیر این صورت، False برمیدهيم 
        else:
            return False
    
    # اضافه کردن یک متد برای حذف حساب کاربر
    def delete_account(self):
        # حساب را از ليست حساب های کاربر حذف مي‌کنيم 
        self.user.accounts.remove(self)
        # شماره حساب را پرینت مي‌کنيم 
        print(f"Account number {self.number} deleted successfully")
    
    # اضافه کردن چند متد برای تغيير اطلاعات حساب کاربر
    def change_name(self, new_name):
        # نام جديد را ذخيره مي‌کنيم 
        self.user.name = new_name
        # نام جديد را پرینت مي‌کنيم 
        print(f"Name changed to {new_name}")
    
    def change_family_name(self, new_family_name):
        # نام خانوادگي جديد را ذخيره مي‌کنيم 
        self.user.family_name = new_family_name
        # نام خانوادگي جديد را پرینت مي‌کنيم 
        print(f"Family name changed to {new_family_name}")
    
    def change_father_name(self, new_father_name):
        # نام پدر جديد را ذخيره مي‌کنيم 
        self.user.father_name = new_father_name
        # نام پدر جديد را پرینت مي‌کنيم 
        print(f"Father name changed to {new_father_name}")
    
    def change_birth_date(self, new_birth_date):
        # تاريخ تولد جديد را ذخيره مي‌کنيم 
        self.user.birth_date = new_birth_date
        # تاريخ تولد جديد را پرینت مي‌کنيم 
        print(f"Birth date changed to {new_birth_date}")
    
    def change_city(self, new_city):
        # شهر جديد را ذخيره مي‌کنيم 
        self.user.city = new_city
        # شهر جديد را پرینت مي‌کنيم 
        print(f"City changed to {new_city}")
    
    def change_mobile_number(self, new_mobile_number):
        # شماره موبايل جديد را ذخيره مي‌کنيم 
        self.user.mobile_number = new_mobile_number
        # شماره موبايل جديد را پرینت مي‌کنيم 
        print(f"Mobile number changed to {new_mobile_number}")
    
    def change_landline_number(self, new_landline_number):
        # شماره ثابت جديد را ذخيره مي‌کنيم 
        self.user.landline_number = new_landline_number
        # شماره ثابت جديد را پرینت مي‌کنيم 
        print(f"Landline number changed to {new_landline_number}")


# تعریف یک کلاس برای حساب جاری
class CurrentAccount(Account):
    # سازنده کلاس حساب جاری
    def __init__(self, number, balance, user):
        # سازنده کلاس پدر (Account) را با شماره، موجودی و کاربر فراخوانی می‌کنیم
        super().__init__(number, balance, user)
        # یک حداکثر میزان برداشت برای حساب جاری تعیین می‌کنیم
        self.max_withdrawal = 10000000

    # تغییر متد withdraw برای بررسی حداکثر میزان برداشت
    def withdraw(self, amount, description):
        # اگر مبلغ بیشتر از حداکثر میزان برداشت باشد، یک خطا پرتاب می‌کنیم
        if amount > self.max_withdrawal:
            raise ValueError("Amount exceeds the maximum withdrawal limit")
        # در غیر این صورت، متد withdraw کلاس پدر را با مقدار و توضیحات فراخوانی میدهيم 
        else:
            return super().withdraw(amount, description)

# تعريف يک کلاس برای حساب پس انداز
class SavingsAccount(Account):
    # سازنده کلاس حساب پس انداز
    def __init__(self, number, balance, user):
        # سازنده کلاس پدر (Account) را با شماره، موجودی و کاربر فراخوانی میدهيم 
        super().__init__(number, balance, user)
        # یک نرخ سود برای حساب پس انداز تعيين مي‌کنيم 
        self.interest_rate = 0.15

    # اضافه کردن یک متد برای محاسبه سود حساب پس انداز
    def calculate_interest(self):
        # سود را با ضرب موجودي در نرخ سود و تقسيم بر 12 محاسبه مي‌کنيم 
        interest = self.balance * self.interest_rate / 12
        # سود را به صورت دو رقم اعشار چاپ و برمي‌گردانيم 
        print(f"Interest: {interest:.2f}")
        return interest

# تعريف يک کلاس برای حساب قرض الحسنه
class QarzolHasanehAccount(Account):
    # سازنده کلاس حساب قرض الحسنه
    def __init__(self, number, balance, user):
        # سازنده کلاس پدر (Account) را با شماره، موجودي و کاربر فراخواني مي‌کنيم 
        super().__init__(number, balance, user)
        # چک مي‌کنيم که آيا موجودي منفي است يا خير 
        if balance < 0:
            # اگر منفي است، يک خطا پرتاب مي‌کنيم 
            raise ValueError("Balance cannot be negative for QarzolHasaneh account")
    
    # تغيير متد withdraw براي بررسي موجودي منفي
    def withdraw(self, amount, description):
        # اگر مبلغ بيشتر از موجودي باشد، يک خطا پرتاب مي‌کنيم 
        if amount > self.balance:
            raise ValueError("Balance cannot be negative for QarzolHasaneh account")
        # در غير اين صورت، متد withdraw کلاس پدر را با مقدار و توضيحات فراخواني مي‌کنيم 
        else:
            return super().withdraw(amount, description)


# وارد کردن کتابخانه mysql.connector برای اتصال به پایگاه داده mysql
import mysql.connector

# ایجاد یک اتصال به پایگاه داده با استفاده از نام کاربری، رمز عبور و نام پایگاه داده
connection = mysql.connector.connect(user="username", password="password", database="bank")

# ایجاد یک شیء cursor برای اجرای دستورات sql
cursor = connection.cursor()

# تعریف یک تابع برای ایجاد جدول های لازم در پایگاه داده
def create_tables():
    # ایجاد جدول users با ستون های id، name، family_name، father_name، birth_date، city، mobile_number، landline_number و national_code
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, name VARCHAR(255), family_name VARCHAR(255), father_name VARCHAR(255), birth_date DATE, city VARCHAR(255), mobile_number VARCHAR(255), landline_number VARCHAR(255), national_code VARCHAR(255))")

    # ایجاد جدول accounts با ستون های number، balance، opening_date و user_id
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts (number INT PRIMARY KEY, balance DECIMAL(15,2), opening_date DATE, user_id INT, FOREIGN KEY (user_id) REFERENCES users(id))")

    # ایجاد جدول transactions با ستون های id، amount، description، date، time و account_number
    cursor.execute("CREATE TABLE IF NOT EXISTS transactions (id INT PRIMARY KEY AUTO_INCREMENT, amount DECIMAL(15,2), description VARCHAR(255), date DATE, time TIME, account_number INT, FOREIGN KEY (account_number) REFERENCES accounts(number))")

# تعریف یک تابع برای ذخیره اطلاعات یک کاربر در پایگاه داده
def save_user(user):
    # اجرای یک دستور sql برای درج رکورد جدید در جدول users با مقادیر مربوط به شیء کاربر
    cursor.execute("INSERT INTO users (id, name, family_name, father_name, birth_date, city, mobile_number, landline_number, national_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (user.id, user.name, user.family_name, user.father_name, user.birth_date, user.city, user.mobile_number, user.landline_number, user.national_code))
    # تأیید تغییرات در پایگاه داده
    connection.commit()

# تعریف یک تابع برای ذخیره اطلاعات یک حساب در پایگاه داده
def save_account(account):
    # اجرای یک دستور sql برای درج رکورد جدید در جدول accounts با مقادیر مربوط به شیء حساب
    cursor.execute("INSERT INTO accounts (number, balance, opening_date, user_id) VALUES (%s, %s, %s, %s)", (account.number, account.balance, account.opening_date, account.user.id))
    # تأیید تغییرات در پایگاه داده
    connection.commit()

# تعریف یک تابع برای ذخیره اطلاعات یک واریز یا برداشت در پایگاه داده
def save_transaction(transaction):
    # اجرای یک دستور sql برای درج رکورد جدید در جدول transactions با مقادیر مربوط به شیء واریز یا برداشت
    cursor.execute("INSERT INTO transactions (amount, description, date, time, account_number) VALUES (%s, %s, %s, %s, %s)", (transaction.amount, transaction.description, transaction.date, transaction.time, transaction.account.number))
    # تأیید تغییرات در پایگاه داده
    connection.commit()

import sys

# تعریف یک تابع برای گرفتن ورودی از کاربر
def get_input(prompt):
    # چاپ پیام درخواست ورودی
    print(prompt)
    # خواندن ورودی از کاربر
    input = sys.stdin.readline().strip()
    # برگرداندن ورودی
    return input

# تعریف یک تابع برای نمایش منوی اصلی
def show_main_menu():
    # چاپ گزینه های منو
    print("Welcome to the bank system. Please choose an option:")
    print("1. Create a new user")
    print("2. Login as an existing user")
    print("3. Login as admin")
    print("4. Exit")

# تعریف یک تابع برای نمایش منوی کاربر
def show_user_menu(user):
    # چاپ گزینه های منو
    print(f"Hello {user.name}. Please choose an option:")
    print("1. Show user info")
    print("2. Create a new account")
    print("3. Delete an account")
    print("4. Show account info")
    print("5. Deposit to an account")
    print("6. Withdraw from an account")
    print("7. Show transactions of an account")
    print("8. Change user info")
    print("9. Logout")

# تعریف یک تابع برای نمایش منوی admin
def show_admin_menu(admin):
    # چاپ گزینه های منو
    print(f"Hello {admin.name}. Please choose an option:")
    print("1. Show admin info")
    print("2. Show bank info")
    print("3. Logout")


# تعریف یک تابع برای ایجاد یک کاربر جدید
def create_user():
    # گرفتن ورودی های مورد نیاز از کاربر
    name = get_input("Enter your name:")
    family_name = get_input("Enter your family name:")
    father_name = get_input("Enter your father name:")
    birth_date = get_input("Enter your birth date (YYYY-MM-DD):")
    city = get_input("Enter your city:")
    mobile_number = get_input("Enter your mobile number:")
    landline_number = get_input("Enter your landline number (optional):")
    national_code = get_input("Enter your national code:")
    # ساخت یک شیء از کلاس User با ورودی های گرفته شده
    user = User(name, family_name, father_name, birth_date, city, mobile_number, landline_number, national_code)
    # ذخیره اطلاعات کاربر در پایگاه داده
    save_user(user)
    # چاپ پیام موفقیت آمیز
    print(f"User {user.name} created successfully")

# تعریف یک تابع برای ورود به سیستم به عنوان یک کاربر موجود
def login_user():
    # گرفتن ورودی های مورد نیاز از کاربر
    user_id = get_input("Enter your user ID:")
    national_code = get_input("Enter your national code:")
    # اجرای یک دستور sql برای جستجوی رکورد مطابق با شماره کاربر و کد ملی در جدول users
    cursor.execute("SELECT * FROM users WHERE id=%s AND national_code=%s", (user_id, national_code))
    # دریافت نتیجه جستجو
    result = cursor.fetchone()
    # اگر نتیجه خالی نبود، یعنی رکورد مورد نظر پیدا شده است
    if result:
        # ساخت یک شیء از کلاس User با استفاده از مقادیر رکورد پیدا شده
        user = User(result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
        user.id = result[0] # تنظيم شماره کاربر برابر با ستون id رکورد
        # چاپ پيام خوش آمدگويي 
        print(f"Welcome {user.name}")
        # برگرداندن شيء کاربر 
        return user
    # در غیر این صورت، یعنی رکورد مورد نظر پیدا نشده است
    else:
        # چاپ پيام خطا 
        print("Invalid user ID or national code")
        # برگرداندن None 
        return None



# تعريف يک تابع برای ورود به سيستم به عنوان admin
def login_admin():
    # گرفتن ورودي هاي مورد نياز از کاربر 
    name = get_input("Enter your name:")
    password = get_input("Enter your password:")
    # اجرای یک دستور sql برای جستجوی رکورد مطابق با نام و رمز عبور در جدول admins
    cursor.execute("SELECT * FROM admins WHERE name=%s AND password=%s", (name, password))
    # دریافت نتیجه جستجو
    result = cursor.fetchone()
    # اگر نتیجه خالی نبود، یعنی رکورد مورد نظر پیدا شده است
    if result:
        # ساخت یک شیء از کلاس Admin با استفاده از مقادیر رکورد پیدا شده
        admin = Admin(result[1], result[2])
        admin.id = result[0] # تنظيم شماره admin برابر با ستون id رکورد
        # چاپ پيام خوش آمدگويي 
        print(f"Welcome {admin.name}")
        # برگرداندن شيء admin 
        return admin
    # در غیر این صورت، یعنی رکورد مورد نظر پیدا نشده است
    else:
        # چاپ پيام خطا 
        print("Invalid name or password")
        # برگرداندن None 
        return None

# تعریف یک تابع برای ایجاد یک حساب جدید برای یک کاربر
def create_account(user):
    # گرفتن ورودی های مورد نیاز از کاربر
    number = get_input("Enter the account number:")
    balance = get_input("Enter the initial balance:")
    type = get_input("Enter the account type (C for current, S for savings, Q for qarzolhasaneh):")
    # بر اساس نوع حساب، یک شیء از کلاس مربوطه با شماره، موجودی و کاربر ساخته می‌شود
    if type == "C":
        account = CurrentAccount(number, balance, user)
    elif type == "S":
        account = SavingsAccount(number, balance, user)
    elif type == "Q":
        account = QarzolHasanehAccount(number, balance, user)
    else:
        # اگر نوع حساب معتبر نبود، یک خطا پرتاب می‌شود
        raise ValueError("Invalid account type")
    # حساب را به لیست حساب های کاربر اضافه می‌کنیم
    user.accounts.append(account)
    # ذخیره اطلاعات حساب در پایگاه داده
    save_account(account)
    # چاپ پیام موفقیت آمیز
    print(f"Account {account.number} created successfully")


# ادامه کد قبلی

# تعریف یک تابع برای حذف یک حساب برای یک کاربر
def delete_account(user):
    # گرفتن ورودی از کاربر برای شماره حساب مورد نظر
    number = get_input("Enter the account number to delete:")
    # جستجوی حساب با شماره مورد نظر در لیست حساب های کاربر
    account = user.find_account_by_number(number)
    # اگر حساب پیدا شد، متد delete_account را برای آن فراخوانی می‌کنیم
    if account:
        account.delete_account()
    # در غیر این صورت، چاپ پیام خطا
    else:
        print("Account not found")

# تعریف یک تابع برای نمایش اطلاعات یک حساب برای یک کاربر
def show_account_info(user):
    # گرفتن ورودی از کاربر برای شماره حساب مورد نظر
    number = get_input("Enter the account number to show info:")
    # جستجوی حساب با شماره مورد نظر در لیست حساب های کاربر
    account = user.find_account_by_number(number)
    # اگر حساب پیدا شد، متد show_info را برای آن فراخوانی می‌کنیم
    if account:
        account.show_info()
    # در غیر این صورت، چاپ پیام خطا
    else:
        print("Account not found")

# تعريف يک تابع براي واريز به يک حساب براي يک کاربر 
def deposit_to_account(user):
    # گرفتن ورودي از کاربر براي شماره حساب مورد نظر 
    number = get_input("Enter the account number to deposit to:")
    # جستجوي حساب با شماره مورد نظر در ليست حساب هاي کاربر 
    account = user.find_account_by_number(number)
    # اگر حساب پيدا شد، مقدار و توضيحات واريز را از کاربر مي‌گيريم 
    if account:
        amount = get_input("Enter the amount to deposit:")
        description = get_input("Enter the description of deposit:")
        # متد deposit را براي حساب فراخواني مي‌کنيم 
        account.deposit(amount, description)
        # چاپ پيام موفقيت آميز 
        print(f"Deposit successful. New balance: {account.balance}")
    # در غير اين صورت، چاپ پيام خطا 
    else:
        print("Account not found")



# تعريف يک تابع براي برداشت از يک حساب براي يک کاربر 
def withdraw_from_account(user):
    # گرفتن ورودي از کاربر براي شماره حساب مورد نظر 
    number = get_input("Enter the account number to withdraw from:")
    # جستجوي حساب با شماره مورد نظر در ليست حساب هاي کاربر 
    account = user.find_account_by_number(number)
    # اگر حساب پيدا شد، مقدار و توضيحات برداشت را از کاربر مي‌گيريم 
    if account:
        amount = get_input("Enter the amount to withdraw:")
        description = get_input("Enter the description of withdrawal:")
        # متد withdraw را براي حساب فراخواني مي‌کنيم و نتيجه را در يک متغير ذخيره مي‌کنيم 
        result = account.withdraw(amount, description)
        # اگر نتيجه True باشد، يعني برداشت موفقيت آميز بوده است 
        if result:
            # چاپ پيام موفقيت آميز 
            print(f"Withdrawal successful. New balance: {account.balance}")
        # در غير اين صورت، يعني برداشت ناموفق بوده است 
        else:
            # چاپ پيام خطا 
            print("Insufficient balance")
    # در غير اين صورت، چاپ پيام خطا 
    else:
        print("Account not found")

# تعریف یک تابع برای نمایش تراکنش های یک حساب برای یک کاربر
def show_transactions_of_account(user):
    # گرفتن ورودی از کاربر برای شماره حساب مورد نظر
    number = get_input("Enter the account number to show transactions:")
    # جستجوی حساب با شماره مورد نظر در لیست حساب های کاربر
    account = user.find_account_by_number(number)
    # اگر حساب پیدا شد، متد show_transactions را برای آن فراخوانی می‌کنیم
    if account:
        account.show_transactions()
    # در غیر این صورت، چاپ پیام خطا
    else:
        print("Account not found")



# تعریف یک تابع برای تغییر اطلاعات یک کاربر
def change_user_info(user):
    # گرفتن ورودی از کاربر برای شماره حساب مورد نظر
    number = get_input("Enter the account number to change info:")
    # جستجوی حساب با شماره مورد نظر در لیست حساب های کاربر
    account = user.find_account_by_number(number)
    # اگر حساب پیدا شد، گزینه های تغییر اطلاعات را نمایش می‌دهیم
    if account:
        print("Please choose an option to change:")
        print("1. Name")
        print("2. Family name")
        print("3. Father name")
        print("4. Birth date")
        print("5. City")
        print("6. Mobile number")
        print("7. Landline number")
        # گرفتن ورودی از کاربر برای انتخاب گزینه
        option = get_input("Enter your option:")
        # بر اساس گزینه انتخاب شده، عملیات مربوطه را انجام می‌دهیم
        if option == "1":
            # تغییر نام کاربر
            new_name = get_input("Enter your new name:")
            account.change_name(new_name)
        elif option == "2":
            # تغییر نام خانوادگی کاربر
            new_family_name = get_input("Enter your new family name:")
            account.change_family_name(new_family_name)
        elif option == "3":
            # تغییر نام پدر کاربر
            new_father_name = get_input("Enter your new father name:")
            account.change_father_name(new_father_name)
        elif option == "4":
            # تغییر تاریخ تولد کاربر
            new_birth_date = get_input("Enter your new birth date (YYYY-MM-DD):")
            account.change_birth_date(new_birth_date)
        elif option == "5":
            # تغییر شهر کاربر
            new_city = get_input("Enter your new city:")
            account.change_city(new_city)
        elif option == "6":
            # تغییر شماره موبایل کاربر
            new_mobile_number = get_input("Enter your new mobile number:")
            account.change_mobile_number(new_mobile_number)
        elif option == "7":
            # تغییر شماره ثابت کاربر
            new_landline_number = get_input("Enter your new landline number (optional):")
            account.change_landline_number(new_landline_number)
        else:
            # چاپ پیام خطا در صورت انتخاب گزینه نامعتبر
            print("Invalid option")
    # در غیر این صورت، چاپ پیام خطا
    else:
        print("Account not found")

# تعريف يک تابع براي نمايش اطلاعات بانک 
def show_bank_info():
    # اجرای يک دستور sql براي شمارش تعداد کل کاربران در جدول users 
    cursor.execute("SELECT COUNT(*) FROM users")
    # دريافت نتيجه شمارش 
    user_count = cursor.fetchone()[0]
    # چاپ تعداد کل کاربران 
    print(f"Total users: {user_count}")
    # اجرای يک دستور sql براي شمارش تعداد کل حساب ها در جدول accounts 
    cursor.execute("SELECT COUNT(*) FROM accounts")
    # دريافت نتيجه شمارش 
    account_count = cursor.fetchone()[0]
    # چاپ تعداد کل حساب ها 
    print(f"Total accounts: {account_count}")
    # اجرای يک دستور sql براي محاسبه مجموع موجودي کل حساب ها در جدول accounts 
    cursor.execute("SELECT SUM(balance) FROM accounts")
    # دريافت نتيجه محاسبه 
    total_balance = cursor.fetchone()[0]
    # چاپ مجموع موجودي کل حساب ها 
    print(f"Total balance: {total_balance}")

# تعریف یک تابع برای اجرای برنامه
def run():
    # ایجاد جدول های لازم در پایگاه داده
    create_tables()
    # تعریف یک متغیر برای نگه داشتن شیء کاربر یا admin فعال
    active_user = None
    # تعریف یک حلقه بی نهایت برای نمایش منو و انجام عملیات
    while True:
        # اگر کاربر یا admin فعال وجود نداشت، منوی اصلی را نمایش می‌دهیم
        if not active_user:
            show_main_menu()
            # گرفتن ورودی از کاربر برای انتخاب گزینه منو
            option = get_input("Enter your option:")
            # بر اساس گزینه انتخاب شده، عملیات مربوطه را انجام می‌دهیم
            if option == "1":
                # ایجاد یک کاربر جدید
                create_user()
            elif option == "2":
                # ورود به سیستم به عنوان یک کاربر موجود و ذخیره شیء کاربر در متغیر active_user
                active_user = login_user()
            elif option == "3":
                # ورود به سیستم به عنوان admin و ذخیره شیء admin در متغیر active_user
                active_user = login_admin()
            elif option == "4":
                # خروج از برنامه با استفاده از دستور break
                print("Goodbye")
                break
            else:
                # چاپ پیام خطا در صورت انتخاب گزینه نامعتبر
                print("Invalid option")
        # در غیر این صورت، بررسی می‌کنیم که شیء فعال از کدام کلاس است
        else:
            # اگر شيء فعال از کلاس User باشد، منوي کاربر را نمايش مي‌دهيم 
            if isinstance(active_user, User):
                show_user_menu(active_user)
                # گرفتن ورودي از کاربر براي انتخاب گزينه منو 
                option = get_input("Enter your option:")
                # براساس گزينه انتخاب شده، عمليات مربوطه را انجام مي‌دهيم 
                if option == "1":
                    # نمایش اطلاعات کاربر
                    active_user.show_info()
                elif option == "2":
                    # ایجاد یک حساب جدید برای کاربر
                    create_account(active_user)
                elif option == "3":
                    # حذف یک حساب برای کاربر
                    delete_account(active_user)
                elif option == "4":
                    # نمایش اطلاعات یک حساب برای کاربر
                    show_account_info(active_user)
                elif option == "5":
                    # واریز به یک حساب برای کاربر
                    deposit_to_account(active_user)
                elif option == "6":
                    # برداشت از یک حساب برای کاربر
                    withdraw_from_account(active_user)
                elif option == "7":
                    # نمایش تراکنش های یک حساب برای کاربر
                    show_transactions_of_account(active_user)
                elif option == "8":
                    # تغییر اطلاعات کاربر
                    change_user_info(active_user)
                elif option == "9":
                    # خروج از حساب کاربری با تنظیم متغیر active_user برابر با None
                    print(f"Goodbye {active_user.name}")
                    active_user = None
                else:
                    # چاپ پیام خطا در صورت انتخاب گزینه نامعتبر
                    print("Invalid option")
            # اگر شيء فعال از کلاس Admin باشد، منوي admin را نمايش مي‌دهيم 
            elif isinstance(active_user, Admin):
                show_admin_menu(active_user)
                # گرفتن ورودي از کاربر براي انتخاب گزينه منو 
                option = get_input("Enter your option:")
                # براساس گزينه انتخاب شده، عمليات مربوطه را انجام مي‌دهيم 
                if option == "1":
                    # نمایش اطلاعات admin
                    active_user.show_info()
                elif option == "2":
                    # نمایش اطلاعات بانک
                    active_user.show_bank_info()
                elif option == "3":
                    # خروج از حساب admin با تنظیم متغیر active_user برابر با None
                    print(f"Goodbye {active_user.name}")
                    active_user = None
                else:
                    # چاپ پیام خطا در صورت انتخاب گزینه نامعتبر
                    print("Invalid option")
            else:
                # چاپ پیام خطا در صورت نامعلوم بودن نوع شیء فعال
                print("Unknown user type")
                break

# فراخوانی تابع run برای اجرای برنامه
run()
