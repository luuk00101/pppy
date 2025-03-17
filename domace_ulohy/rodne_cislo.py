class RodneCislo:
    # Initialize class
    def __init__(self, birth_number):
        birth_number_editted = birth_number.replace("/", "")

        if not RodneCislo.__validate_birth_number(birth_number_editted):
            raise ValueError("Invalid birth number")

        self.__birth_number = birth_number
        self.__set_day_of_birth(birth_number)
        self.__set_month_of_birth(birth_number)
        self.__set_year_of_birth(birth_number)
        self.__set_gender(birth_number)

    # Implement the equals  method
    def __eq__(self, other):
        if not isinstance(other, RodneCislo):
            return NotImplemented

        return self.__birth_number == other.__birth_number

    # Implement the lesser than method
    def __lt__(self, other):
        if not isinstance(other, RodneCislo):
            return NotImplemented

        return (
            self.__year_of_birth > other.__year_of_birth
            or self.__month_of_birth > other.__month_of_birth
            or self.__day_of_birth > other.__day_of_birth
        )

    # Implement the lesser than or equal method
    def __le__(self, other):
        if not isinstance(other, RodneCislo):
            return NotImplemented

        return self < other or (
            self.__year_of_birth == other.__year_of_birth
            and self.__month_of_birth == other.__month_of_birth
            and self.__day_of_birth == other.__day_of_birth
        )

    # Implement the greater than method
    def __gt__(self, other):
        if not isinstance(other, RodneCislo):
            return NotImplemented

        return (
            self.__year_of_birth < other.__year_of_birth
            or self.__month_of_birth < other.__month_of_birth
            or self.__day_of_birth < other.__day_of_birth
        )

    # Implement the greater than or equal method
    def __ge__(self, other):
        if not isinstance(other, RodneCislo):
            return NotImplemented

        return self > other or (
            self.__year_of_birth == other.__year_of_birth
            and self.__month_of_birth == other.__month_of_birth
            and self.__day_of_birth == other.__day_of_birth
        )

    # Implement the string method
    def __str__(self):
        return self.__birth_number

    # Implement the representation method
    def __repr__(self):
        return f"RodneCislo('{self.__birth_number}')"  # had to use the single quotes

    # Validate birth number
    def __validate_birth_number(birth_number):
        if len(birth_number) != 9 and len(birth_number) != 10:
            return False

        if not birth_number.isdigit():
            return False

        if (
            int(birth_number[2:4]) > 62
            or (int(birth_number[2:4]) < 51 and int(birth_number[2:4]) > 12)
            or int(birth_number[2:4]) < 1
            or int(birth_number[4:6]) > 31
            or int(birth_number[4:6]) < 1
        ):
            return False

        if int(birth_number) % 11 != 0:
            return False

        return True

    # Set day of birth
    def __set_day_of_birth(self, birth_number):
        self.__day_of_birth = int(birth_number[4:6])

    # Set month of birth
    def __set_month_of_birth(self, birth_number):
        month = int(birth_number[2:4])

        if month > 50:
            self.__month_of_birth = month - 50
        else:
            self.__month_of_birth = int(birth_number[2:4])

    # Set year of birth
    def __set_year_of_birth(self, birth_number):
        year = int(birth_number[:2])

        if year > 54:
            self.__year_of_birth = 1900 + year
        else:
            self.__year_of_birth = 2000 + year

    # Set gender
    def __set_gender(self, birth_number):
        if int(birth_number[2:4]) > 50:
            self.__gender = "female"
        else:
            self.__gender = "male"

    # Get age in years
    def get_age_in_years(self):
        import datetime

        # This is the current date
        current_date = datetime.datetime.now().year
        if datetime.datetime.now().month < self.__month_of_birth or (
            datetime.datetime.now().month == self.__month_of_birth
            and datetime.datetime.now().day < self.__day_of_birth
        ):
            return current_date - self.__year_of_birth - 1

        return current_date - self.__year_of_birth

    # Get age in days
    def get_age_in_days(self):
        import datetime

        # This is the current date
        current_date = datetime.datetime.now()
        # This is the date of birth converted to datetime
        birth_date = datetime.datetime(
            self.__year_of_birth, self.__month_of_birth, self.__day_of_birth
        )
        return (current_date - birth_date).days

    def get_next_birth_number(self):
        end = int(self.__birth_number[-4:])

        while end < 9999:
            end += 1
            # -5 to leave out the slash
            if int(f"{self.__birth_number[:-5]}{end}") % 11 == 0:
                return f"{self.__birth_number[:-4]}{end}"

        raise ValueError("No next birth number")
