from typing import Annotated
from pydantic import Field
from Workout_API.workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description = 'Nome do centro de Treinamento', examples ='Smart King', max_length = 20)]
    endereco: Annotated[str, Field(description = 'Endereço do centro de treinamento', examples ='Rua Brasil', max_length = 60)]
    proprietario: Annotated[str, Field(description = 'Proprietário do centro de treinamento', examples ='Pedro', max_length = 30)]
