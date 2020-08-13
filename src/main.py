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

else:
    print("Incomplete.")

loc = intfunc.message_loc_get()

if loc == 1:
    input_file = intfunc.get_input_file()
    output_file = intfunc.get_output_file()
    chunk_size = (bits//8) - 1
    open(output_file, 'w+').close()
    with open(input_file) as f:
        for piece in dcp.read_in_chunks(f, chunk_size):
            piece = dcp.PT2OS(piece)
            l = len(piece)
            piece = dcp.OS2IP(piece)

            c = rsa.enc(piece)
            piece = rsa.dec(c)

            piece = dcp.I2OSP(piece, l)
            piece = dcp.OS2PT(piece)

            with open(output_file, 'a') as f:
                print(piece, end='', file=f)
else:
    m = str(input("Enter a string: "))
    m = dcp.PT2OS(m)
    l = len(m)
    m = dcp.OS2IP(m)

    c = rsa.enc(m)
    print("Encrypted string is:", m)
    m = rsa.dec(c)

    m = dcp.I2OSP(m, l)
    m = dcp.OS2PT(m)
    print("Decrypted string is: ", m)
