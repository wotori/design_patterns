#!/usr/bin/python
# -*- coding: utf-8 -*-

from factory.abstract_factory import AbstractFactory
from factory.enum.bodytype import BodyType
from factory.cars.vaz import Vaz

class VazFactory(AbstractFactory):

    @classmethod
    def create_body(cls):
        return BodyType.sedan

    @classmethod
    def create_engine(cls):
        return 'v2.5'

    @classmethod
    def create_interior(cls):
        return 'raw_silver_metall'

    @classmethod
    def create_car(cls):
        body = cls.create_body()
        engine = cls.create_engine()
        interior = cls.create_interior()
        return Vaz(body, engine, interior)
