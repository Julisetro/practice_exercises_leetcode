"""Solución al problema de leet code titulado: Greatest common divisor of strings"""
from math import gcd

class Solution:
    """Clase de la solucón"""
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Rvisamos si la concatenación de los strings son iguales o no
        # si no es igual, significa que no se pueden dividir en partes iguales entre si 
        # por lo que retornamos ""
        if str1 + str2 != str2 + str1:
            return ""
        #Si lo anterior es falso, devuelve la subcadena de 0 a gcd de size(str1), size(str2)
        return str1[:gcd(len(str1), len(str2))]