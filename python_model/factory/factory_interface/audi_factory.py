#!/usr/bin/python
# -*- coding: utf-8 -*-

from python_model.factory.factory_interface.abstract_factory import AbstractFactory
from python_model.factory.factory_interface.enum.bodytype import BodyType
from python_model.factory.factory_interface.cars.audi import Audi


class AudiFactory(AbstractFactory):

    @classmethod
    def create_body(cls):
        return BodyType.sedan

    @classmethod
    def create_engine(cls):
        return 'v5.0'

    @classmethod
    def create_interior(cls):
        return 'black_skin'

    @classmethod
    def create_car(cls):
        body = cls.create_body()
        engine = cls.create_engine()
        interior = cls.create_interior()
        return Audi(body, engine, interior)
