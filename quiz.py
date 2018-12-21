from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = 'gAAAAABcHPY4sA5Jezq-1tbkmuIBy5S9795ejgoytsUt_Tp5sHACA8bnhImLwZnbWXOKSStV0XijZ1tmZ48CMmP937JFTxaVG1Zl0lRp1i1Mwv9Z4C60h_yynoVS3qbK7QgRdkooizTHWC2A_Mp7riUQjSyaJE4-sMmTDGni8syqtlnfIspt9oy1cI8WM4tHgyY48n365AvE'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()