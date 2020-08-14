import rsa_primitive as rsa
import math_functions as mf
import data_conversion_primitives as dcp
import interaction_functions as intfunc

state = intfunc.login_or_signup()
if state == 1:
    data = intfunc.signup_core()
    bits = rsa.get_bits()
    pqned = rsa.gen_keys(bits)
    intfunc.signup_pqned(data, pqned)

user = intfunc.login()
file_or_string = intfunc.message_loc_get()

if file_or_string == 1:
    enc_or_dec = intfunc.encrpyt_or_decrypt()
    if enc_or_dec == 1:
        input_file = intfunc.get_input_file()
        output_file = intfunc.get_output_file()
        enc_data = intfunc.get_encrypt_list(user)
        bits = enc_data[0]
        e = enc_data[1]
        n = enc_data[2]
        chunk_size = (bits//8) - 1
        open(output_file, 'w+').close()
        list_of_chunks = []
        with open(input_file) as fin:
            print("All okay. Encrypting...")
            for data in dcp.read_in_chunks(fin, chunk_size):
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
        d = dec_data[1]
        p = dec_data[2]
        q = dec_data[3]
        chunk_size = (bits//8) - 1
        open(output_file, 'w+').close()
        with open(input_file) as fin:
            list_of_chunks = fin.read()
            list_of_chunks = list_of_chunks.strip('][').split(', ')
            print("All okay. Decrypting...")
            for data in list_of_chunks:
                data = rsa.dec(int(data), d, p, q)
                data = dcp.I2OSP(data, chunk_size)
                data = dcp.OS2PT(data)
                with open(output_file, 'a') as f:
                    print(data, end='', file=f)
        print("Decrypted. Output written to", f.name)

elif file_or_string == 2:
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
    print("Decrypted string is: ", m)

else:
    sure = (input("[ACCOUNT DELETION]: Proceed? Irreversible. (y or n): "))
