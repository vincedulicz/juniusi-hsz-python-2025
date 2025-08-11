import calendar
import random


class UserGeneratorConfig:
    COUNTRY_CHOICES = ["HU", "EU", "USA", "SP"]
    BIRTH_YEAR_RANGE = (1920, 1980)
    BIRTH_MONTH_RANGE = (1, 12)
    VALID_UNTIL_DAYS = (0, 365)


class UserGenerator:
    def __init__(self, names, config=UserGeneratorConfig):
        self._names = names
        self._config = config

    def _user_id(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def _born_date(self):
        year = random.randint(self._config.BIRTH_YEAR_RANGE[0], self._config.BIRTH_YEAR_RANGE[1])
        month = random.randint(self._config.BIRTH_MONTH_RANGE[0], self._config.BIRTH_MONTH_RANGE[1])
        days_in_month = calendar.monthrange(year, month)[1]
        day = random.randint(1, days_in_month)

        return f"{year:04d}.{month:02d}.{day:02d}"

    def _age(self, born_date):
        birth_year = int(born_date.split(".")[0])
        current_year = datetime.now().year
        return current_year - birth_year

    def _country(self):
        return random.choice(self._config.COUNTRY_CHOICES)

    def _worker(self):
        return random.choice([True, False])

    def _valid_until(self):
        return datetime.now() + timedelta(days=random.randint(*self._config.VALID_UNTIL_DAYS))

    def random_user(self):
        user_id = f'user-{self._user_id()}'
        born_date = self._born_date()
        age = self._age(born_date)

        return {
            user_id: {
                "valid_until": self._valid_until().strftime("%Y-%m-%d"),
                "born-date": born_date,
                "name": random.choice(self._names),
                "age": age,
                "country": self._country(),
                "worker": self._worker(),
                "other": []
            }
        }