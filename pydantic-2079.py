from typing import Union

from pydantic import BaseModel

"""
Issue: https://github.com/samuelcolvin/pydantic/issues/2079
"""

class FooEmpty(BaseModel):
    pass

class BarEmpty(BaseModel):
    pass

class TestEmpty(BaseModel):
    test: Union[FooEmpty, BarEmpty]

class Foo(BaseModel):
    typename: str = "Foo"
    class Config:
        extra = 'forbid'

class Bar(BaseModel):
    typename: str = "Bar"
    class Config:
        extra = 'forbid'

class Test(BaseModel):
    test: Union[Foo, Bar]

print("Should be Foo:", Test(test=Foo()))
print("Should be Bar:", Test(test=Bar()))
print("Should be Bar:", TestEmpty(test=BarEmpty()))
print("Most certainly should be Bar:", type(Test(test=Bar()).test))
print("Should be true:", isinstance(Test(test=Bar()).test, Bar))
print("Should be false:", isinstance(Test(test=Bar()).test, Foo))
