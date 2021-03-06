from python_model.factory.factory_interface.audi_factory import AudiFactory
from python_model.factory.factory_interface.lada_factory import LadaFactory
from python_model.factory.factory_interface.mercedes_factory import MercedesFactory
from python_model.factory.factory_interface.vaz_factory import VazFactory

if __name__ == "__main__":
    audi_car = AudiFactory.create_car()
    lada_car = LadaFactory.create_car()
    merscedes_car = MercedesFactory.create_car()
    vaz_car = VazFactory.create_car()

    print(audi_car.body.name, audi_car.engine, audi_car.interior)
    print(lada_car.body.name, lada_car.engine, lada_car.interior)
    print(merscedes_car.body.name, merscedes_car.engine, merscedes_car.interior)
    print(vaz_car.body.name, vaz_car.engine, vaz_car.interior)

'''
output:
> sedan v5.0 black_skin
> sedan v1.4 raw_black_metal
> sedan v6.0 brown_skin
> sedan v2.5 raw_silver_metall
'''