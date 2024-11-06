from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
from secrets import token_hex
from repository import UserRepository, ProductRepository
from schemas import *

router = APIRouter(prefix="/ozito")

#////////  User
@router.get("/select_all_users")
async def select_all_users():
    users = await UserRepository.select_all()
    return {"data" : users}

@router.post("/create_user")
async def create_user(user : Annotated[SUserAdd, Depends()]):
    created_user = await UserRepository.add_user(user)
    return {"ok" : True, "task_id" : created_user}

@router.get("/check_user")
async def check_user(login : str):
    user = await UserRepository.check_user(login)
    if user:
        return {"message" : "Данный пользователь существует.", "data" : user}
    else:
        return {"message" : "Данный пользователь не существует."}
    
@router.put("/update_user")
async def update_user(id : int, user : Annotated[SUserAdd, Depends()]):
    result = await UserRepository.update_user(id, user)
    return result
    
#////////  Products
@router.get("/select_all_products")
async def select_all_products(category : str = "All"):
    users = await ProductRepository.select_all(category=category)
    return {"data" : users}

@router.post("/create_product")
async def create_product(product : Annotated[SProductAdd, Depends()]):
    created_product = await ProductRepository.add_product(product)
    return {"ok" : True, "task_id" : created_product}
@router.put("/update_product")
async def update_product(id : int, product : Annotated[SProductAdd, Depends()]):
    result = await ProductRepository.update_product(id, product)
    return result

@router.delete("/delete_product")
async def delete_product(id : int):
    result = await ProductRepository.delete_product(id)
    return result

@router.get("/get_image")
async def get_image(file_name : str):
    image_path = Path("" + file_name)
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)