import argparse

def main():
    parser = argparse.ArgumentParser(description="Argparse példa")

    parser.add_argument("nev", type=str, help="Add meg a neved")

    parser.add_argument(
        "-n", "--number",
        type=int,
        default=1,
        help="Az ismétlsek száma (default 1)"
    )

    parser.add_argument(
        "operation",
        type=str,
        choices=["add", "subtract", "multiply", "divide"],
        help="Mik a műveletek: add, subtract, multiply, divide"
    )

    parser.add_argument("--source", type=str, help="Forrás fájl neve")

    parser.add_argument("--destination", type=str, help="Cél fájl neve")

    parser.add_argument("--debug", action="store_true", help="Debug mód bekapcsolása")

    args = parser.parse_args()

    if args.debug:
        print("[DEBUG] Debug mód bekapcsolva")
        # ...

    print(f'Helló {args.nev}! Válaszott művelet: {args.operation}')

    if args.source and arg.destination:
        print(f"másol innen: {args.source} ide: {args.destination}")

    for _ in range(args.number):
        print(f'Művelet végrehajtása: {args.operation}')


main()