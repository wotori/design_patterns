#!/usr/bin/python
# -*- coding: utf-8 -*-

from python_model.factory.factory_interface.abstract_factory import AbstractFactory
from python_model.factory.factory_interface.enum.bodytype import BodyType
from python_model.factory.factory_interface.cars.mercsedes import Mercsedes

class MercedesFactory(AbstractFactory):

    @classmethod
    def create_body(cls):
        return BodyType.sedan

    @classmethod
    def create_engine(cls):
        return 'v6.0'

    @classmethod
    def create_interior(cls):
        return 'brown_skin'

    @classmethod
    def create_car(cls):
        body = cls.create_body()
        engine = cls.create_engine()
        interior = cls.create_interior()
        return Mercsedes(body, engine, interior)
