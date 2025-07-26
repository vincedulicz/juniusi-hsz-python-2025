import json
from typing import List, Dict, Union

def load_json(filename: str) -> Union[Dict, List]:
    """ JSON fájl betöltése dict-be"""

    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Error file: {filename} not found.')
        return {}
    except json.JSONDecodeError:
        print(f'Error: Failed to decode JSON from {filename}')
        return {}

def save_json(data: Union[Dict, List], filename: str) -> None:
    """ Adatok mentése JSON-be """

    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f'Data save to {filename}')
    except IOError as e:
        print(f'Error: Unable to save file {filename}, {e}')

def filter_invalid_matches(matches: List[Dict]) -> List[Dict]:
    """ Hibás meccsek kiszűrése, ahol hiányzik a 'ht' kulcs, hibásként fájlba menti """

    valid_matches = []
    invalid_matches = []

    for match in matches:
        try:
            if 'ht' not in match["score"]:
                raise KeyError(f'Missing "ht" in match: {match}')
            valid_matches.append(match)
        except KeyError:
            invalid_matches.append(match)

    if invalid_matches:
        save_json({"invalid_matches": invalid_matches}, "hibas.json")
        print(f'{len(invalid_matches)} invalid matches save to "hibas.json"')

    return valid_matches

def home_losing_at_halftime_but_wins(matches: List[Dict]) -> List[Dict]:
    """
    Azokat a meccseket adja vissza,
    ahol a hazai csapat féliődben vesztésre állt,
    de a végén megnyerte a meccset
    """

    results = []
    for match in matches:
        try:
            ht_home, ht_away = match["score"]["ht"]
            ft_home, ft_away = match["score"]["ft"]
            if ht_home < ht_away and ft_home > ft_away:
                results.append(match)
        except KeyError as e:
            print(f'Error processing match: {match}. Missing key: {e}')

    return results

def home_losing_at_halftime_but_draws(matches: List[Dict]) -> List[Dict]:
    """
    Azokat a meccseket adja vissza ahol,
    a hazai csapat félidőben vesztésre állt,
    de a végén X lett.
    """

    results = []
    for match in matches:
        try:
            ht_home, ht_away = match["score"]["ht"]
            ft_home, ft_away = match["score"]["ft"]
            if ht_home < ht_away and ft_home == ft_away:
                results.append(match)
        except KeyError as e:
            print(f"Error processing match: {match}. Missing key {e}")

    return results

def home_concedes_more_than_three_goals(matches: List[Dict]) -> List[Dict]:
    """
    Vissza adjuk azokat a meccseket ahol a
    hazai csapat 3-nál több gólt kapott.
    """

    results = []
    for match in matches:
        try:
            _, ft_away = match["score"]["ft"]
            if ft_away > 3:
                results.append(match)
        except KeyError as e:
            print(f'Error processing match: {match}. Missing key: {e}')
    return results

def home_score_more_than_three_goals(matches: List[Dict]) -> List[Dict]:
    """
    Vissza adja azokat a meccseket, ahol
    a hazai csapat 3-nál többet rúgott
    :param matches:
    :return:
    """
    results = []
    for match in matches:
        try:
            ft_home, _ = match["score"]["ft"]
            if ft_home > 3:
                results.append(match)
        except KeyError as e:
            print(f'Erros processing...')
    return results

def filter_by_matchday(matches: List[Dict], matchday: str) -> List[Dict]:
    """ Meccsek szűrése forduló (matchday) alapján """

    try:
        results = [
            match for match in matches if match["round"].lower() == f'matchday {matchday}'.lower()
        ]
        return results
    except KeyError as e:
        print(f'Error filtering by matchday: {e}')
        return []

def filter_by_date(matches: List[Dict], date: str) -> List[Dict]:
    """
    Meccsek szűrése dátum alapján pl 2020-05-06
    :param matches:
    :param date:
    :return:
    """
    try:
        results = [
            match for match in matches if match["date"] == date
        ]
        return results
    except KeyError as e:
        print(f'Error filtering by date: {e}')
        return []

def print_resutls(title: str, matches: List[Dict]) -> None:
    print(title)

    if matches:
        for match in matches:
            print(
                f'{match["round"]}: {match["team1"]} vs {match["team2"]}'
                f'Date: {match["date"]}, HT: {match["score"].get("ht", "N/A")}, FT: {match["score"].get("ft", "N/A")}'
            )
            print("-" * 50)

def main() -> None:
    """
    A program fő ciklusa:
    -adat betöltés
    -invalid filtering
    -menüben user által filter
    -elemezni...
    :return:
    """

    filename = "adatok/data.json"
    data = load_json(filename)
    matches = data.get("matches", [])

    matches = filter_invalid_matches(matches)

    while True:
        options = [
            "1. Search by Matchday",
            "2. Search by Date",
            "3. Analyze all matches"
        ]

        print(f'Options: {[option for option in options]}')

        choice = input("Choose an option (1/2/3/q): ")

        if choice == "1":
            matchday = input("Enter matchday (1-9): ")
            filtered_matches = filter_by_matchday(matches, matchday)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            filtered_matches = filter_by_date(matches, date)
        elif choice.lower() in ["end", "q", "quit"]:
            break
        else:
            filtered_matches = matches

        halftime_loss_to_win = home_losing_at_halftime_but_wins(filtered_matches)
        halftime_loss_to_draw = home_losing_at_halftime_but_draws(filtered_matches)
        home_concede_3_or_more = home_concedes_more_than_three_goals(filtered_matches)
        home_score_3_or_more = home_score_more_than_three_goals(filtered_matches)

        print_resutls("1) Hazai félidőben vereségre áll, de fordít", halftime_loss_to_win)
        print_resutls("2) Hazai féliődben vereségre áll, de X lesz", halftime_loss_to_draw)
        print_resutls("3) Hazai 3 gólnál többet kap", home_concede_3_or_more)
        print_resutls("4) Hazai 3 gólnál többet rúg", home_score_3_or_more)


main()