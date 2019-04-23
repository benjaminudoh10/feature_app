from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcv1_6_oxebQgv00dMezqfxB8zTEQRk4yYgB9truidCJwpCj-' \
    b'ESTGRhIyVpEkLQ-xWfGIN_cHgwmXhVdB5zK3BFVS6cjkQZHNmTDf_zpXFghu8' \
    b'FzIS3nkQpKO3xClkU7kq9DxdgfNcFD9PjMr4GpI8VdjY98zVExArpEOrGhBKc' \
    b'ltHIkbjBoKeTJK-2nQmPbRRdpg1'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
