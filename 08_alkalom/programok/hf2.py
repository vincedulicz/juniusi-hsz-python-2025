

# II. feladat

class_a_range = (0, 127)
class_b_range = (128, 191)
class_c_range = (192, 223)
class_d_range = (224, 239)
class_e_range = (240, 255)

descriptions = [
    "A osztály: nagy hálózatok",
    "B osztály: közepes hálózatok",
    "C osztály: kisebb hálózatok",
    "D osztály: multicast",
    "E osztály: fenntartott"
]
class_labels = ["A", "B", "C", "D", "E"]

"""

ip_classes = {
 "A": {"range": class_a_range, "description": class_a_description},
"B": {"range": class_b_range, "description": class_b_description},
"C": {"range": class_c_range, "description": class_c_description},
"D": {"range": class_d_range, "description": class_d_description},
"E": {"range": class_e_range, "description": class_e_description
}


"""

def create_ip_classes():
    """ Létrehozzuk az IP osztályokat dict-be """

    return {label: {"range": ip_range, "description": description}
            for label, ip_range, description in zip(
            class_labels,
            [class_a_range, class_b_range, class_c_range, class_d_range, class_e_range],
            descriptions
        )
    }

def find_ip_classes(ip_classes, ip):
    """ Megkeressük az IP címet """

    # 192.168.1.1 -> 4 oktet

    if ip.count('.') != 3:
        return "Érvénytelen IP cím: 4 oktetnek kell lennie"

    try:
        first_octet = int(ip.split(".")[0])

        for label, info in ip_classes.items():
            if info["range"][0] <= first_octet <= info[range][1]:
                return f'{label} osztály - {info["description"]}'
    except ValueError as e:
        return f'Érvénytelen cím, számnak kell lennie: {e}'
    except Exception as e:
        print(f'Valami nagyon elromlott... {e}')
        return "Érvénytelen cím"

def main():
    """ Főprogi """

    ip_classes = create_ip_classes()

    ip_address = input("Adja meg az IP címet pl. 192.168.1.1 : ")

    print(find_ip_classes(ip_classes, ip_address))


