import zelva

cont = 0

while cont != 1:
    print("")
    
    i = input("1 => SPIRALA\n"
              "2 => TMA NA KONCI TUNELU\n"
              "3 => KRUHY V KRUZICH\n"
              "4 => ZIG-ZAG\n:")

    if i == '1':
        zelva.cisteni()
        zelva.spiral()
        
    elif i == '2':
        zelva.cisteni()
        zelva.tma_konec_tunelu()
    elif i == '3':
        zelva.cisteni()
        zelva.kresli_kruhy_v_kruzich()
    elif i == '4':
        zelva.cisteni()
        zelva.chase()
        
    else:
        print("Neplatná volba! \n")        

    cont = int(input("CONTINUE (0/1) : "))
