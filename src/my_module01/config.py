from dotenv import load_dotenv
from pydantic import BaseModel, Field, ConfigDict

load_dotenv(override=True)


class ExtraBaseModel(BaseModel):
    model_config = ConfigDict(extra="allow")


class MyClassConfigPM(ExtraBaseModel):
    """Pydantic model for the configuration of the module.

    Attributes:
        min_length (int  ): Minimum length of the list.
        max_length (int  ): Maximum length of the list.
        min_value  (float): Minimum value for the module.
        max_value  (float): Maximum value for the module.
        threshold  (float): Threshold value for the module.
    """

    min_length: int = Field(default=2, ge=1, le=1000)
    max_length: int = Field(default=100, ge=1, le=1000)
    min_value: float = Field(default=0.0, ge=0.0, le=1.0)
    max_value: float = Field(default=1.0, ge=0.0, le=1.0)
    threshold: float = Field(default=0.5, ge=0.0, le=1.0)


__all__ = ["MyClassConfigPM"]
