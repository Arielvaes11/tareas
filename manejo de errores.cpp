#include <iostream>
using namespace std;

int main()
{
    // Declaramos las variables
    int numero;
    int resultado;

    // Pedimos al usuario que ingrese un numero
    cout << "Ingrese un numero: ";
    cin >> numero;

    try
    {
        // Verificamos que el numero sea mayor que cero
        if (numero <= 0)
        {
            throw "El numero debe ser mayor que cero";
        }
        // Calculamos el resultado
        resultado = numero * numero;
        cout << "El resultado es: " << resultado << endl;
    }
    catch (const char* msg)
    {
        // Si hay una excepcion imprimimos el mensaje
        cerr << msg << endl;
    }

    return 0;
}
