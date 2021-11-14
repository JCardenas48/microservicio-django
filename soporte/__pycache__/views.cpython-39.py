a
    �c�a  �                   @   s�   d dl mZ d dlmZ ddlmZmZ ddlmZm	Z	 G dd� dej
�ZG dd	� d	ej�ZG d
d� dej
�ZG dd� dej�ZdS )�    )�render)�generics�   )�PersonaSoporteSerializer�PQRSerializer)�PersonaSoporte�PQRc                   @   s   e Zd Zej�� ZeZdS )�PersonaSoporteListCreateN�	�__name__�
__module__�__qualname__r   �objects�all�querysetr   �serializer_class� r   r   �"C:\Desarrollo\ms1\soporte\views.pyr	      s   
r	   c                   @   s   e Zd Zej�� ZeZdS )�PersonaSoporteUpdateDeleteNr
   r   r   r   r   r      s   
r   c                   @   s   e Zd Zej�� ZeZdS )�PQRListCreateN�	r   r   r   r   r   r   r   r   r   r   r   r   r   r      s   
r   c                   @   s   e Zd Zej�� ZeZdS )�PQRUpdateDeleteNr   r   r   r   r   r      s   
r   N)�django.shortcutsr   �rest_frameworkr   �serializersr   r   �modelsr   r   �ListCreateAPIViewr	   �RetrieveUpdateDestroyAPIViewr   r   r   r   r   r   r   �<module>   s   