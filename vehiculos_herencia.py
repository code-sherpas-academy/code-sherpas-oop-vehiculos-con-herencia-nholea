class Vehiculo():
    def __init__(self):
        pass

class Motor():
    def __init__(self,parMotor):
        self.parMotor = parMotor

class MotorElectrico(Motor):
    def __init__(self, parMotor, poten_elect):
        super().__init__(parMotor)
        self.poten_elect = poten_elect

class MotorCombustion(Motor):
    def __init__(self, parMotor, cilindrada):
        super().__init__(parMotor)
        self.cilindrada = cilindrada


class VehiculosMotor(Vehiculo):
    def __init__(self,motor):
        self.motor = motor

class Coche(VehiculosMotor):
    def __init__(self, motor):
        super().__init__(motor)

class Motocicleta(VehiculosMotor):
    def __init__(self, motor):
        super().__init__(motor)

class Camion(VehiculosMotor):
    def __init__(self, motor):
        super().__init__(motor)


class VehiculosNoMotor(Vehiculo):
    def __init__(self):
        pass

class Bicicleta(VehiculosNoMotor):
    def __init__(self):
        super().__init__()

class MonoCiclo(VehiculosNoMotor):
    def __init__(self):
        super().__init__()


class Triciclo(VehiculosNoMotor):
    def __init__(self):
        super().__init__()


motor1 = VehiculosMotor(MotorElectrico(1, True))
print(motor1.motor.poten_elect)