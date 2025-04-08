

class Twisted_Ed:
    def __init__(self, e, d, p=None):
        if p is None:
            raise ValueError("p is mandatory")
        self.e = e
        self.d = d
        self.s = (e - d)/4
        self.t = (e + d)/6

        
    def form_to_W(self):
        a = self.s*self.s - 3*self.t*self.t
        b = 2*self.t*self.t*self.t - self.t*self.s*self.s
        return a, b

    def T_E_coords_to_W(self, u, v):
        x = self.s*(1+v)*pow((1-v)+self.t, -1, self.p)
        y = self.s*(1+v)*pow(((1-v)*u), -1, self.p)
        return x, y

    def W_coords_to_T_E(self, x, y):
        u = (x-self.t)*pow(y, -1, self.p)
        v = (x-self.t-self.s)*pow((x-self.t+self.s), -1, p)
        return u, v


