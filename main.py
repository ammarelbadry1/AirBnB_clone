#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime


def main():
    instance = BaseModel()

    
    print(instance.id)
    print(instance.created_at)
    print(instance.updated_at)


if __name__ == "__main__":
    main()
