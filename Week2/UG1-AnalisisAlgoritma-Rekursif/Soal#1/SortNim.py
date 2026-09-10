def InsertRecursive(sorted_array, current_value, current_length):
    # TODO 1
    if current_length == 0:
        return [current_value]

    # NIM ganjil = Ascending
    if int(NIM_MAHASISWA[-1]) % 2 != 0:
        if sorted_array[current_length - 1] > current_value:
            # TODO 2
            return InsertRecursive(sorted_array, current_value, current_length - 1) + [sorted_array[current_length - 1]]
        else:
            return sorted_array[:current_length] + [current_value]

    # NIM genap = Descending
    else:
        if sorted_array[current_length - 1] < current_value:
            # TODO 2
            return InsertRecursive(sorted_array, current_value, current_length - 1) + [sorted_array[current_length - 1]]
        else:
            return sorted_array[:current_length] + [current_value]


def RecursiveFilterSort(data_array, current_length):
    # TODO 3
    if current_length == 0:
        return []

    hasil = RecursiveFilterSort(data_array, current_length - 1)

    # NIM ganjil = ambil angka ganjil
    if int(NIM_MAHASISWA[-1]) % 2 != 0:
        if data_array[current_length - 1] % 2 != 0:
            return InsertRecursive(
                hasil,
                data_array[current_length - 1],
                len(hasil)
            )
        else:
            return hasil

    # NIM genap = ambil angka genap
    else:
        if data_array[current_length - 1] % 2 == 0:
            return InsertRecursive(
                hasil,
                data_array[current_length - 1],
                len(hasil)
            )
        else:
            return hasil


# Ganti dengan NIM Anda
NIM_MAHASISWA = "71251177"

if NIM_MAHASISWA != "":
    raw_data = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)

    final_result = RecursiveFilterSort(raw_data, data_length)

    # TODO 4
    print("===== FILTER & SORT NIM =====")
    print("NIM Mahasiswa :", NIM_MAHASISWA)

    if int(NIM_MAHASISWA[-1]) % 2 != 0:
        print("Tipe          : GANJIL (Ascending)")
    else:
        print("Tipe          : GENAP (Descending)")

    print("Data Digit Awal :", raw_data)
    print("Hasil Akhir     :", final_result)