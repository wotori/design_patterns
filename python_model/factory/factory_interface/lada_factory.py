#!/usr/bin/python
# -*- coding: utf-8 -*-

from python_model.factory.factory_interface.abstract_factory import AbstractFactory
from python_model.factory.factory_interface.enum.bodytype import BodyType
from python_model.factory.factory_interface.cars.lada import Lada


class LadaFactory(AbstractFactory):

    @classmethod
    def create_body(cls):
        return BodyType.sedan

    @classmethod
    def create_engine(cls):
        return 'v1.4'

    @classmethod
    def create_interior(cls):
        return 'raw_black_metal'

    @classmethod
    def create_car(cls):
        body = cls.create_body()
        engine = cls.create_engine()
        interior = cls.create_interior()
        return Lada(body, engine, interior)
