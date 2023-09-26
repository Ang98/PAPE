import os

def main():
    nombre = os.getenv('USERNAME')
    print(f"hola mundo soy {nombre}")

if __name__=="__main__":
    main()