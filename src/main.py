import rsa_primitive as rsa
import math_functions as mf
import data_conversion_primitives as dcp
import interaction_functions as intfunc
from progress.bar import IncrementalBar
import sys

state = intfunc.login_or_signup()
if state == 1:
    data = intfunc.signup_core()
    bits = rsa.get_bits()
    pqned = rsa.gen_keys(bits)
    print("Keys successfully generated.")
    intfunc.signup_pqned(data, pqned)

user = intfunc.login()

while True:
    operation = intfunc.get_operation()
    if operation == 1:
        enc_or_dec = intfunc.encrpyt_or_decrypt()
        if enc_or_dec == 1:
            recpt = intfunc.get_reciever()
            input_file = intfunc.get_input_file()
            output_file = intfunc.get_output_file()
            enc_data = intfunc.get_encrypt_list(recpt)
            bits = enc_data[0]
            e = enc_data[1]
            n = enc_data[2]
            chunk_size = (bits//8) - 1
            open(output_file, 'w+').close()
            list_of_chunks = []
            fobj = open(input_file, 'r')
            l = sum(1 for _ in (dcp.read_in_chunks(fobj, chunk_size)))
            with open(input_file) as fin:
                print("All okay.")
                for data in IncrementalBar('Encrypting...', max=l).iter(dcp.read_in_chunks(fin, chunk_size)):
                    data = dcp.PT2OS(data, chunk_size)
                    data = dcp.OS2IP(data)
                    data = rsa.enc(data, e, n)
                    list_of_chunks.append(int(data))
            with open(output_file, 'a') as fout:
                print(list_of_chunks, end='', file=fout)
            print("Encrypted. Output written to", fout.name)

        else:
            input_file = intfunc.get_input_file()
            output_file = intfunc.get_output_file()
            dec_data = intfunc.get_decrypt_list(user)
            bits = dec_data[0]
            p = dec_data[1]
            q = dec_data[2]
            d_p = dec_data[3]
            d_q = dec_data[4]
            q_inv = dec_data[5]
            chunk_size = (bits//8) - 1
            open(output_file, 'w+').close()
            with open(input_file) as fin:
                list_of_chunks = fin.read()
            list_of_chunks = list_of_chunks.strip('][').split(', ')
            print("All okay.")
            f =  open(output_file, 'a')
            bar = IncrementalBar('Decrypting...', max=len(list_of_chunks))
            for data in list_of_chunks:
                data = rsa.dec(int(data), p, q, d_p, d_q, q_inv)
                data = dcp.I2OSP(data, chunk_size)
                data = dcp.OS2PT(data)
                print(data, end='', file=f)
                bar.next()
            f.close()
            dcp.kill_nulls(output_file)
            bar.finish()
            print("Decrypted. Output written to", f.name)

    elif operation == 2:
        enc_data = intfunc.get_encrypt_list(user)
        bits = enc_data[0]
        e = enc_data[1]
        n = enc_data[2]
        chunk_size = (bits//8) - 1
        dec_data = intfunc.get_decrypt_list(user)
        bits = dec_data[0]
        d = dec_data[1]
        p = dec_data[2]
        q = dec_data[3]

        m = str(input("Enter a string: "))
        m = dcp.PT2OS(m, chunk_size)
        m = dcp.OS2IP(m)

        c = rsa.enc(m, e, n)
        print("Encrypted string is:", m)
        m = rsa.dec(c, d, p, q)

        m = dcp.I2OSP(m, chunk_size)
        m = dcp.OS2PT(m)
        print("Decrypted string is:", m)

    elif operation == 3:
        path = intfunc.get_path()
        sys.path.append(path)
        print(sys.path[-1], "successfully appended to sys.path.")


    elif operation == 4:
        while True:
            try:
                sure = str(input("[ACCOUNT DELETION]: Proceed? Irreversible. (y or n): "))
                if sure not in ('y', 'n'):
                    print("[ACCOUNT DELETION]: Please answer y or n.")
                else:
                    if sure == "y":
                        intfunc.del_user()
                        print("All okay. Account successfully deleted.")
                        exit()
                    else:
                        break
            except (TypeError, ValueError):
                print("[ACCOUNT DELETION]: Please answer y or n.")

    else:
        exit()
