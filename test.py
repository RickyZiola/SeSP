from SeSP.data.data_handler import data_encoder


encd: data_encoder = data_encoder()
encd.write_var_int(12345678910)
encd.write_string("save")

with open("savefile.bin", "wb") as file:
    file.write(encd.payload)