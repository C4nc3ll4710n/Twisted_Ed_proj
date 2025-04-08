

class Projective_Coords:
    def __init__(self, x, y, lambd = 1, p=None):
        if p is None:
            raise ValueError("p is mandatory")
        self.p = p
        self.X = (x * lambd) % p
        self.Y = (y * lambd) % p
        self.Z = lambd % p

    def projective_to_affine(X, Y, Z, p):
        inv_Z = pow(Z, -1, p)
        x = (X * inv_Z) % p
        y = (Y * inv_Z) % p
        return (x, y)

        


