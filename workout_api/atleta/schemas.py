from pydantic import BaseModel, Field, PositiveFloat
from typing import Annotated


class Atleta(BaseModel):
    nome: Annotated[str, Field(description = 'Nome do atleta', examples ='João', max_length = 50)]
    cpf: Annotated[str, Field(description = 'Cpf do atleta', examples ='12345678900', max_length = 11)]
    idade: Annotated[int, Field(description = 'Idade do atleta', examples ='20')]
    peso: Annotated[PositiveFloat, Field(description = 'Peso do atleta', examples ='90.5')]
    altura: Annotated[PositiveFloat, Field(description = 'Altura do atleta', examples ='1.90')]
    sexo: Annotated[str, Field(description = 'Sexo do atleta', examples ='M', max_length=1)]