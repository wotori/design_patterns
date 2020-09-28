#!/usr/bin/python
# -*- coding: utf-8 -*-

from factory.abstract_factory import AbstractFactory
from factory.enum.bodytype import BodyType
from factory.cars.mercsedes import Mercsedes

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
