from SeSP.data.data_handler import data_decoder

with open("savefile.bin", "rb") as f:
    decd: data_decoder = data_decoder(f.read())
    print(decd.read_var_int())
    print(decd.read_string())